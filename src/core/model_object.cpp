/******************************************************************************
 *   Copyright (C) 2013-2014 by Alexander Rykovanov                        *
 *   rykovanov.as@gmail.com                                                   *
 *                                                                            *
 *   This library is free software; you can redistribute it and/or modify     *
 *   it under the terms of the GNU Lesser General Public License as           *
 *   published by the Free Software Foundation; version 3 of the License.     *
 *                                                                            *
 *   This library is distributed in the hope that it will be useful,          *
 *   but WITHOUT ANY WARRANTY; without even the implied warranty of           *
 *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the            *
 *   GNU Lesser General Public License for more details.                      *
 *                                                                            *
 *   You should have received a copy of the GNU Lesser General Public License *
 *   along with this library; if not, write to the                            *
 *   Free Software Foundation, Inc.,                                          *
 *   59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.                *
 ******************************************************************************/

#include "model_impl.h"

#include <opc/ua/model.h>
#include <opc/ua/protocol/binary/stream.h>

namespace OpcUa
{
  namespace Model
  {

    Object::Object(NodeId objectId, Services::SharedPtr services)
      : Node(services)
    {
      Id = objectId;
      ReadParameters attrs;
      attrs.AttributesToRead.push_back(MakeReadValueId(objectId, AttributeID::DisplayName));
      attrs.AttributesToRead.push_back(MakeReadValueId(objectId, AttributeID::BrowseName));
      std::vector<DataValue> values = services->Attributes()->Read(attrs);
      DisplayName = values[0].Value.As<LocalizedText>();
      BrowseName = values[1].Value.As<QualifiedName>();
    }

    Object::Object(Object&& object)
      : Node(std::move(object.OpcUaServices))
    {
      Id = std::move(object.Id);
      DisplayName = std::move(object.DisplayName);
      BrowseName = std::move(object.BrowseName);
    }

    Object::Object(const Object& object)
      : Node(object.OpcUaServices)
    {
      Id = object.Id;
      DisplayName = object.DisplayName;
      BrowseName = object.BrowseName;
    }

    Object::Object(Services::SharedPtr services)
      : Node(services)
    {
    }

    ObjectType Object::GetType() const
    {
      return ObjectType(ObjectId::Null, GetServices());
    }

    std::vector<Variable> Object::GetVariables() const
    {
      return Browse<Variable>(GetID(), NodeClass::Variable, GetServices());
    }

    Variable Object::GetVariable(const QualifiedName& name) const
    {
      OpcUa::RelativePathElement element;
      element.ReferenceTypeId = OpcUa::ObjectId::HierarchicalReferences;
      element.IncludeSubtypes = true;
      element.TargetName = name;

      OpcUa::RelativePath path;
      path.Elements.push_back(element);
      return GetVariable(path);
    }

    Variable Object::GetVariable(const RelativePath& relativePath) const
    {
      OpcUa::BrowsePath browsePath;
      browsePath.StartingNode = GetID();
      browsePath.RelativePath = relativePath;
      OpcUa::TranslateBrowsePathsToNodeIdsParameters params;
      params.BrowsePaths.push_back(browsePath);
      const std::vector<OpcUa::BrowsePathResult>& result = GetServices()->Views()->TranslateBrowsePathsToNodeIds(params);
      if (result.size() != 1)
        throw std::runtime_error("object_model| Server returned more than one browse paths on TranslateBrowsePathsToNodeIds request.");

      const OpcUa::BrowsePathResult& resultPath = result.back();
      OpcUa::CheckStatusCode(resultPath.Status);
      if (resultPath.Targets.size() != 1)
        throw std::runtime_error("object_model| Server returned too many target elements on TranslateBrowsePathsToNodeIds request.");

      return Variable(resultPath.Targets.back().TargetId, GetServices());
    }


    std::vector<Object> Object::GetObjects() const
    {
      return Browse<Object>(GetID(), NodeClass::Object, GetServices());
    }

    Object Object::GetObject(const QualifiedName& name) const
    {
      return Object(ObjectId::Null, GetServices());
    }

    Object Object::GetObject(const RelativePath& name) const
    {
      return Object(ObjectId::Null, GetServices());
    }

    Object Object::CreateObject(const ObjectType& type, const QualifiedName& browseName)
    {
      return CreateObject(NodeId(), type, browseName);
    }

    Object Object::CreateObject(const NodeId& newNodeId, const ObjectType& nodeType, const QualifiedName& browseName)
    {
      return CreateObject(newNodeId, GetID(), nodeType.GetID(), browseName, browseName.Name);
    }

    Object Object::CreateObject(const ObjectType& type, const QualifiedName& browseName, const std::string& displayName)
    {
      return CreateObject(NodeId(), GetID(), type.GetID(), browseName, displayName);
    }

    Object Object::CreateObject(const NodeId& newNodeId, const NodeId& parentNode, const NodeId& typeID, const QualifiedName& browseName, const std::string& displayName)
    {
      Object object(GetServices());
      object.Id = InstantiateType(newNodeId, parentNode, typeID, NodeClass::Object, browseName, displayName);
      object.BrowseName = browseName;
      object.DisplayName = LocalizedText(displayName);
      return object;

    }

    NodeId Object::InstantiateType(const NodeId& newNodeId, const NodeId& parentNode, const NodeId& typeID, NodeClass nodeClass, const QualifiedName& browseName, const std::string& displayName)
    {
      // Creating new node for object
      AddNodesItem newNodeRequest;
      newNodeRequest.BrowseName = browseName;
      newNodeRequest.RequestedNewNodeId = newNodeId;
      newNodeRequest.NodeClass = nodeClass;
      newNodeRequest.ParentNodeId = parentNode;
      newNodeRequest.ReferenceTypeId = nodeClass == NodeClass::Object ? ObjectId::HasComponent : ObjectId::HasProperty;
      newNodeRequest.TypeDefinition = typeID;
      ObjectAttributes attrs;
      attrs.Description = LocalizedText(displayName);
      attrs.DisplayName = LocalizedText(displayName);
      newNodeRequest.NodeAttributes = attrs;

      NodeManagementServices::SharedPtr nodes = GetServices()->NodeManagement();
      std::vector<AddNodesResult> newObjectNode = nodes->AddNodes({newNodeRequest});
      if (newObjectNode.size() != 1)
      {
        throw std::runtime_error("opcua_model| Server returned wrong number new nodes results.");
      }

      OpcUa::CheckStatusCode(newObjectNode[0].Status);

      std::map<NodeId, std::vector<ReferenceDescription>> nextRefs;
      nextRefs.insert({newObjectNode[0].AddedNodeId, BrowseObjectsAndVariables(typeID)});
      while(!nextRefs.empty())
      {
        std::map<NodeId, std::vector<ReferenceDescription>> newRefs;
        for (auto idRefs : nextRefs)
        {
          std::map<NodeId, std::vector<ReferenceDescription>> tmpRefs = CopyObjectsAndVariables(idRefs.first, idRefs.second);
          newRefs.insert(tmpRefs.begin(), tmpRefs.end());
        }
        nextRefs = std::move(newRefs);
      }
      return newObjectNode[0].AddedNodeId;
    }

    std::vector<ReferenceDescription> Object::BrowseObjectsAndVariables(const NodeId& id)
    {
      // ID of the new node.
      BrowseDescription desc;
      desc.BrowseDirection = BrowseDirection::Forward;
      desc.IncludeSubtypes = true;
      desc.NodeClassMask =   NodeClass::Object | NodeClass::Variable | NodeClass::Method;
      desc.ReferenceTypeId = ObjectId::HierarchicalReferences;
      desc.NodeId = id;
      desc.ResultMask = BrowseResultMask::NodeClass | BrowseResultMask::TypeDefinition | BrowseResultMask::BrowseName | BrowseResultMask::DisplayName;

      // browse sub objects and variables.
      BrowseParameters query;
      query.NodesToBrowse.push_back(desc);
      ViewServices::SharedPtr views = GetServices()->Views();
      return views->Browse(query)[0].References; //FIME: this method should return BrowseResults
    }

    std::map<NodeId, std::vector<ReferenceDescription>> Object::CopyObjectsAndVariables(const NodeId& targetNode, const std::vector<ReferenceDescription>& refs)
    {
      std::map<NodeId, std::vector<ReferenceDescription>> nextCopyData;
      for (const ReferenceDescription& ref : refs)
      {
        std::vector<AddNodesResult> result;
        std::vector<AddNodesItem> newNodeRequest;
        switch (ref.NodeClass)
        {
          case NodeClass::Object:
          {
            if (ref.TypeDefinition != ObjectId::Null)
            {
              InstantiateType(NodeId(), targetNode, ref.TypeDefinition, NodeClass::Object, ref.BrowseName, ref.DisplayName.Text);
            }
            else
            {
              newNodeRequest = {CreateObjectCopy(targetNode, ref)};
            }
            break;
          }
          case NodeClass::Variable:
          {
            newNodeRequest = {CreateVariableCopy(targetNode, ref)};
            break;
          }
          default:
          {
            continue;
          }
        }
        if (newNodeRequest.empty())
        {
          continue;
        }
        result = GetServices()->NodeManagement()->AddNodes(newNodeRequest);
        std::vector<ReferenceDescription> newRefs = BrowseObjectsAndVariables(ref.NodeId);
        nextCopyData.insert({result[0].AddedNodeId, newRefs});
      }
      return nextCopyData;
    }

    Variable Object::CreateVariable(const QualifiedName& browseName, const Variant& value)
    {
      return CreateVariable(NodeId(), browseName, value);
    }

    Variable Object::CreateVariable(const NodeId& newVariableID, const QualifiedName& browseName, const Variant& value)
    {
      // Creating new node for object
      AddNodesItem newNodeRequest;
      newNodeRequest.BrowseName = browseName;
      newNodeRequest.RequestedNewNodeId = newVariableID;
      newNodeRequest.NodeClass = NodeClass::Variable;
      newNodeRequest.ParentNodeId = GetID();
      newNodeRequest.ReferenceTypeId = ObjectId::HasProperty;
      newNodeRequest.TypeDefinition = NodeId();
      VariableAttributes attrs;
      attrs.Description = LocalizedText(browseName.Name);
      attrs.DisplayName = LocalizedText(browseName.Name);
      attrs.Value = value;
      attrs.DataType = OpcUa::VariantTypeToDataType(value.Type());
      newNodeRequest.NodeAttributes = attrs;

      NodeManagementServices::SharedPtr nodes = GetServices()->NodeManagement();
      std::vector<AddNodesResult> newNode = nodes->AddNodes({newNodeRequest});
      if (newNode.size() != 1)
      {
        throw std::runtime_error("opcua_model| Server returned wrong number new nodes results.");
      }

      OpcUa::CheckStatusCode(newNode[0].Status);
      Variable newVariable(GetServices());
      newVariable.Id = newNode[0].AddedNodeId;
      newVariable.BrowseName = browseName;
      newVariable.DisplayName = attrs.Description;
      newVariable.DataType = value.Type();
      newVariable.TypeId = newNodeRequest.TypeDefinition;
      return newVariable;
    }

    Variable Object::CreateVariable(const QualifiedName& browseName, const VariableType& type)
    {
      return Variable(GetServices());
    }

    Variable Object::CreateVariable(const NodeId& newVariableID, const QualifiedName& browseName, const VariableType& type)
    {
      return Variable(GetServices());
    }

    AddNodesItem Object::CreateVariableCopy(const NodeId& parentID, const ReferenceDescription& ref)
    {
      const NodeId& nodeID = ref.NodeId;

      ReadParameters readParams;
      readParams.AttributesToRead.push_back(MakeReadValueId(nodeID, AttributeID::DisplayName));
      readParams.AttributesToRead.push_back(MakeReadValueId(nodeID, AttributeID::Description));
      readParams.AttributesToRead.push_back(MakeReadValueId(nodeID, AttributeID::Value));
      readParams.AttributesToRead.push_back(MakeReadValueId(nodeID, AttributeID::DataType));
      readParams.AttributesToRead.push_back(MakeReadValueId(nodeID, AttributeID::ValueRank));
      readParams.AttributesToRead.push_back(MakeReadValueId(nodeID, AttributeID::ArrayDimensions));
      readParams.AttributesToRead.push_back(MakeReadValueId(nodeID, AttributeID::AccessLevel));
      readParams.AttributesToRead.push_back(MakeReadValueId(nodeID, AttributeID::UserAccessLevel));
      readParams.AttributesToRead.push_back(MakeReadValueId(nodeID, AttributeID::MinimumSamplingInterval));
      readParams.AttributesToRead.push_back(MakeReadValueId(nodeID, AttributeID::Historizing));
      readParams.AttributesToRead.push_back(MakeReadValueId(nodeID, AttributeID::WriteMask));
      readParams.AttributesToRead.push_back(MakeReadValueId(nodeID, AttributeID::UserWriteMask));
      readParams.AttributesToRead.push_back(MakeReadValueId(nodeID, AttributeID::BrowseName));
      std::vector<DataValue> values = GetServices()->Attributes()->Read(readParams);

      VariableAttributes attrs;
      attrs.DisplayName = values[0].Value.As<LocalizedText>();
      attrs.Description = values[1].Value.As<LocalizedText>();
      attrs.Value = values[2].Value;
      attrs.DataType = values[3].Value.As<NodeId>();
      attrs.ValueRank = values[4].Value.As<int32_t>();
      attrs.ArrayDimensions = values[5].Value.As<std::vector<uint32_t>>();
      attrs.AccessLevel = static_cast<VariableAccessLevel>(values[6].Value.As<uint8_t>());
      attrs.UserAccessLevel = static_cast<VariableAccessLevel>(values[7].Value.As<uint8_t>());
      attrs.MinimumSamplingInterval = values[8].Value.As<Duration>();
      attrs.Historizing = values[9].Value.As<bool>();
      attrs.WriteMask = values[10].Value.As<uint32_t>();
      attrs.UserWriteMask = values[11].Value.As<uint32_t>();

      AddNodesItem newNode;
      newNode.BrowseName = values[12].Value.As<QualifiedName>();
      newNode.NodeClass = NodeClass::Variable;
      newNode.ParentNodeId = parentID;
      newNode.ReferenceTypeId = ref.ReferenceTypeId;
      newNode.TypeDefinition = ref.TypeDefinition;
      newNode.NodeAttributes = attrs;
      return newNode;
    }

    AddNodesItem Object::CreateObjectCopy(const NodeId& parentID, const ReferenceDescription& ref)
    {
      const NodeId& nodeID = ref.TargetNodeId;

      ReadParameters readParams;
      readParams.AttributesToRead.push_back({nodeID, AttributeID::DisplayName});
      readParams.AttributesToRead.push_back({nodeID, AttributeID::Description});
      readParams.AttributesToRead.push_back({nodeID, AttributeID::WriteMask});
      readParams.AttributesToRead.push_back({nodeID, AttributeID::UserWriteMask});
      readParams.AttributesToRead.push_back({nodeID, AttributeID::BrowseName});
      std::vector<DataValue> values = GetServices()->Attributes()->Read(readParams);

      ObjectAttributes attrs;
      attrs.DisplayName = values[0].Value.As<LocalizedText>();
      attrs.Description = values[1].Value.As<LocalizedText>();
      attrs.WriteMask = values[2].Value.As<uint32_t>();
      attrs.UserWriteMask = values[3].Value.As<uint32_t>();

      AddNodesItem newNode;
      newNode.BrowseName = values[4].Value.As<QualifiedName>();
      newNode.NodeClass = NodeClass::Object;
      newNode.ParentNodeId = parentID;
      newNode.ReferenceTypeId = ref.ReferenceTypeId;
      newNode.TypeDefinition = ref.TargetNodeTypeDefinition;
      newNode.Attributes = attrs;
      return newNode;
    }

  } // namespace Model
} // namespace OpcUa
