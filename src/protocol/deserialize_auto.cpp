
/// @author Olivier Roulet-Dubonnet 
/// @email olivier@sintef.no 
/// @brief Opc Ua Binary. 
/// @license GNU LGPL
///
/// Distributed under the GNU LGPL License
/// (See accompanying file LICENSE or copy at
/// http://www.gnu.org/licenses/lgpl.html)
///

#include "binary_serialization.h"
#include <opc/ua/protocol/protocol_auto.h>

#include <opc/ua/protocol/binary/stream.h>

namespace OpcUa
{   
    namespace Binary
    {

    template<>
    void DataDeserializer::Deserialize<XmlElement>(XmlElement& data)
    {
        *this >> data.Length;
        DeserializeContainer(*this, data.Value);
    }


    template<>
    void DataDeserializer::Deserialize<DiagnosticInfo>(DiagnosticInfo& data)
    {
        *this >> data.Encoding;
        if (data.Encoding) & (1>>(0)) *this >> data.SymbolicId;
        if (data.Encoding) & (1>>(1)) *this >> data.NamespaceURI;
        if (data.Encoding) & (1>>(2)) *this >> data.LocalizedText;
        if (data.Encoding) & (1>>(4)) *this >> data.AdditionalInfo;
        if (data.Encoding) & (1>>(5)) *this >> data.InnerStatusCode;
        if (data.Encoding) & (1>>(6)) *this >> data.InnerDiagnosticInfo;
    }


    template<>
    void DataDeserializer::Deserialize<ExtensionObject>(ExtensionObject& data)
    {
        *this >> data.Encoding;
        if (data.Encoding) & (1>>(0)) *this >> data.TypeId;
        *this >> data.BodyLength;
        DeserializeContainer(*this, data.Body);
    }


    template<>
    void DataDeserializer::Deserialize<Argument>(Argument& data)
    {
        *this >> data.Name;
        *this >> data.DataType;
        *this >> data.ValueRank;
        DeserializeContainer(*this, data.ArrayDimensions);
        *this >> data.Description;
    }


    template<>
    void DataDeserializer::Deserialize<EnumValueType>(EnumValueType& data)
    {
        *this >> data.Value;
        *this >> data.DisplayName;
        *this >> data.Description;
    }


    template<>
    void DataDeserializer::Deserialize<TimeZoneDataType>(TimeZoneDataType& data)
    {
        *this >> data.Offset;
        *this >> data.DaylightSavingInOffset;
    }


    template<>
    void DataDeserializer::Deserialize<ApplicationDescription>(ApplicationDescription& data)
    {
        *this >> data.ApplicationUri;
        *this >> data.ProductUri;
        *this >> data.ApplicationName;
        *this >> data.ApplicationType;
        *this >> data.GatewayServerUri;
        *this >> data.DiscoveryProfileUri;
        DeserializeContainer(*this, data.DiscoveryUrls);
    }


    template<>
    void DataDeserializer::Deserialize<RequestHeader>(RequestHeader& data)
    {
        *this >> data.AuthenticationToken;
        *this >> data.Timestamp;
        *this >> data.RequestHandle;
        *this >> data.ReturnDiagnostics;
        *this >> data.AuditEntryId;
        *this >> data.TimeoutHint;
        *this >> data.AdditionalHeader;
    }


    template<>
    void DataDeserializer::Deserialize<ResponseHeader>(ResponseHeader& data)
    {
        *this >> data.Timestamp;
        *this >> data.RequestHandle;
        *this >> data.ServiceResult;
        *this >> data.ServiceDiagnostics;
        DeserializeContainer(*this, data.StringTable);
        *this >> data.AdditionalHeader;
    }


    template<>
    void DataDeserializer::Deserialize<ServiceFault>(ServiceFault& data)
    {
        *this >> data.ResponseHeader;
    }


    template<>
    void DataDeserializer::Deserialize<FindServersParameters>(FindServersParameters& data)
    {
        *this >> data.EndpointUrl;
        DeserializeContainer(*this, data.LocaleIds);
        DeserializeContainer(*this, data.ServerUris);
    }


    template<>
    void DataDeserializer::Deserialize<FindServersRequest>(FindServersRequest& data)
    {
        *this >> data.TypeId;
        *this >> data.RequestHeader;
        *this >> data.Parameters;
    }


    template<>
    void DataDeserializer::Deserialize<FindServersData>(FindServersData& data)
    {
        DeserializeContainer(*this, data.Servers);
    }


    template<>
    void DataDeserializer::Deserialize<FindServersResponse>(FindServersResponse& data)
    {
        *this >> data.TypeId;
        *this >> data.ResponseHeader;
        *this >> data.Parameters;
    }


    template<>
    void DataDeserializer::Deserialize<UserTokenPolicy>(UserTokenPolicy& data)
    {
        *this >> data.PolicyId;
        *this >> data.TokenType;
        *this >> data.IssuedTokenType;
        *this >> data.IssuerEndpointUrl;
        *this >> data.SecurityPolicyUri;
    }


    template<>
    void DataDeserializer::Deserialize<EndpointDescription>(EndpointDescription& data)
    {
        *this >> data.EndpointUrl;
        *this >> data.Server;
        *this >> data.ServerCertificate;
        *this >> data.SecurityMode;
        *this >> data.SecurityPolicyUri;
        DeserializeContainer(*this, data.UserIdentityTokens);
        *this >> data.TransportProfileUri;
        *this >> data.SecurityLevel;
    }


    template<>
    void DataDeserializer::Deserialize<GetEndpointsParameters>(GetEndpointsParameters& data)
    {
        *this >> data.EndpointUrl;
        DeserializeContainer(*this, data.LocaleIds);
        DeserializeContainer(*this, data.ProfileUris);
    }


    template<>
    void DataDeserializer::Deserialize<GetEndpointsRequest>(GetEndpointsRequest& data)
    {
        *this >> data.TypeId;
        *this >> data.RequestHeader;
        *this >> data.Parameters;
    }


    template<>
    void DataDeserializer::Deserialize<GetEndpointsResponse>(GetEndpointsResponse& data)
    {
        *this >> data.ResponseHeader;
        DeserializeContainer(*this, data.Endpoints);
    }


    template<>
    void DataDeserializer::Deserialize<RegisteredServer>(RegisteredServer& data)
    {
        *this >> data.ServerUri;
        *this >> data.ProductUri;
        DeserializeContainer(*this, data.ServerNames);
        *this >> data.ServerType;
        *this >> data.GatewayServerUri;
        DeserializeContainer(*this, data.DiscoveryUrls);
        *this >> data.SemaphoreFilePath;
        *this >> data.IsOnline;
    }


    template<>
    void DataDeserializer::Deserialize<RegisterServerParameters>(RegisterServerParameters& data)
    {
        *this >> data.Server;
    }


    template<>
    void DataDeserializer::Deserialize<RegisterServerRequest>(RegisterServerRequest& data)
    {
        *this >> data.TypeId;
        *this >> data.RequestHeader;
        *this >> data.Parameters;
    }


    template<>
    void DataDeserializer::Deserialize<RegisterServerData>(RegisterServerData& data)
    {
    }


    template<>
    void DataDeserializer::Deserialize<RegisterServerResponse>(RegisterServerResponse& data)
    {
        *this >> data.TypeId;
        *this >> data.ResponseHeader;
        *this >> data.Parameters;
    }


    template<>
    void DataDeserializer::Deserialize<ChannelSecurityToken>(ChannelSecurityToken& data)
    {
        *this >> data.ChannelId;
        *this >> data.TokenId;
        *this >> data.CreatedAt;
        *this >> data.RevisedLifetime;
    }


    template<>
    void DataDeserializer::Deserialize<OpenSecureChannelParameters>(OpenSecureChannelParameters& data)
    {
        *this >> data.ClientProtocolVersion;
        *this >> data.RequestType;
        *this >> data.SecurityMode;
        *this >> data.ClientNonce;
        *this >> data.RequestedLifetime;
    }


    template<>
    void DataDeserializer::Deserialize<OpenSecureChannelRequest>(OpenSecureChannelRequest& data)
    {
        *this >> data.TypeId;
        *this >> data.RequestHeader;
        *this >> data.Parameters;
    }


    template<>
    void DataDeserializer::Deserialize<OpenSecureChannelData>(OpenSecureChannelData& data)
    {
        *this >> data.ServerProtocolVersion;
        *this >> data.SecurityToken;
        *this >> data.ServerNonce;
    }


    template<>
    void DataDeserializer::Deserialize<OpenSecureChannelResponse>(OpenSecureChannelResponse& data)
    {
        *this >> data.TypeId;
        *this >> data.ResponseHeader;
        *this >> data.Parameters;
    }


    template<>
    void DataDeserializer::Deserialize<CloseSecureChannelParameters>(CloseSecureChannelParameters& data)
    {
    }


    template<>
    void DataDeserializer::Deserialize<CloseSecureChannelRequest>(CloseSecureChannelRequest& data)
    {
        *this >> data.TypeId;
        *this >> data.RequestHeader;
        *this >> data.Parameters;
    }


    template<>
    void DataDeserializer::Deserialize<CloseSecureChannelData>(CloseSecureChannelData& data)
    {
    }


    template<>
    void DataDeserializer::Deserialize<CloseSecureChannelResponse>(CloseSecureChannelResponse& data)
    {
        *this >> data.TypeId;
        *this >> data.ResponseHeader;
        *this >> data.Parameters;
    }


    template<>
    void DataDeserializer::Deserialize<SignedSoftwareCertificate>(SignedSoftwareCertificate& data)
    {
        *this >> data.CertificateData;
        *this >> data.Signature;
    }


    template<>
    void DataDeserializer::Deserialize<SignatureData>(SignatureData& data)
    {
        *this >> data.Algorithm;
        *this >> data.Signature;
    }


    template<>
    void DataDeserializer::Deserialize<CreateSessionParameters>(CreateSessionParameters& data)
    {
        *this >> data.ClientDescription;
        *this >> data.ServerUri;
        *this >> data.EndpointUrl;
        *this >> data.SessionName;
        *this >> data.ClientNonce;
        *this >> data.ClientCertificate;
        *this >> data.RequestedSessionTimeout;
        *this >> data.MaxResponseMessageSize;
    }


    template<>
    void DataDeserializer::Deserialize<CreateSessionRequest>(CreateSessionRequest& data)
    {
        *this >> data.TypeId;
        *this >> data.RequestHeader;
        *this >> data.Parameters;
    }


    template<>
    void DataDeserializer::Deserialize<CreateSessionData>(CreateSessionData& data)
    {
        *this >> data.SessionId;
        *this >> data.AuthenticationToken;
        *this >> data.RevisedSessionTimeout;
        *this >> data.ServerNonce;
        *this >> data.ServerCertificate;
        DeserializeContainer(*this, data.ServerEndpoints);
        DeserializeContainer(*this, data.ServerSoftwareCertificates);
        *this >> data.ServerSignature;
        *this >> data.MaxRequestMessageSize;
    }


    template<>
    void DataDeserializer::Deserialize<CreateSessionResponse>(CreateSessionResponse& data)
    {
        *this >> data.TypeId;
        *this >> data.ResponseHeader;
        *this >> data.Parameters;
    }


    template<>
    void DataDeserializer::Deserialize<UserIdentityToken>(UserIdentityToken& data)
    {
        *this >> data.PolicyId;
    }


    template<>
    void DataDeserializer::Deserialize<AnonymousIdentityToken>(AnonymousIdentityToken& data)
    {
        *this >> data.PolicyId;
    }


    template<>
    void DataDeserializer::Deserialize<UserNameIdentityToken>(UserNameIdentityToken& data)
    {
        *this >> data.PolicyId;
        *this >> data.UserName;
        *this >> data.Password;
        *this >> data.EncryptionAlgorithm;
    }


    template<>
    void DataDeserializer::Deserialize<X509IdentityToken>(X509IdentityToken& data)
    {
        *this >> data.PolicyId;
        *this >> data.CertificateData;
    }


    template<>
    void DataDeserializer::Deserialize<IssuedIdentityToken>(IssuedIdentityToken& data)
    {
        *this >> data.PolicyId;
        *this >> data.TokenData;
        *this >> data.EncryptionAlgorithm;
    }


    template<>
    void DataDeserializer::Deserialize<ActivateSessionParameters>(ActivateSessionParameters& data)
    {
        *this >> data.ClientSignature;
        DeserializeContainer(*this, data.ClientSoftwareCertificates);
        DeserializeContainer(*this, data.LocaleIds);
        *this >> data.UserIdentityToken;
        *this >> data.UserTokenSignature;
    }


    template<>
    void DataDeserializer::Deserialize<ActivateSessionRequest>(ActivateSessionRequest& data)
    {
        *this >> data.TypeId;
        *this >> data.RequestHeader;
        *this >> data.Parameters;
    }


    template<>
    void DataDeserializer::Deserialize<ActivateSessionData>(ActivateSessionData& data)
    {
        *this >> data.ServerNonce;
        DeserializeContainer(*this, data.Results);
        DeserializeContainer(*this, data.DiagnosticInfos);
    }


    template<>
    void DataDeserializer::Deserialize<ActivateSessionResponse>(ActivateSessionResponse& data)
    {
        *this >> data.TypeId;
        *this >> data.ResponseHeader;
        *this >> data.Parameters;
    }


    template<>
    void DataDeserializer::Deserialize<CloseSessionParameters>(CloseSessionParameters& data)
    {
        *this >> data.DeleteSubscriptions;
    }


    template<>
    void DataDeserializer::Deserialize<CloseSessionRequest>(CloseSessionRequest& data)
    {
        *this >> data.TypeId;
        *this >> data.RequestHeader;
        *this >> data.Parameters;
    }


    template<>
    void DataDeserializer::Deserialize<CloseSessionData>(CloseSessionData& data)
    {
    }


    template<>
    void DataDeserializer::Deserialize<CloseSessionResponse>(CloseSessionResponse& data)
    {
        *this >> data.TypeId;
        *this >> data.ResponseHeader;
        *this >> data.Parameters;
    }


    template<>
    void DataDeserializer::Deserialize<CancelParameters>(CancelParameters& data)
    {
        *this >> data.RequestHandle;
    }


    template<>
    void DataDeserializer::Deserialize<CancelRequest>(CancelRequest& data)
    {
        *this >> data.TypeId;
        *this >> data.RequestHeader;
        *this >> data.Parameters;
    }


    template<>
    void DataDeserializer::Deserialize<CancelData>(CancelData& data)
    {
        *this >> data.CancelCount;
    }


    template<>
    void DataDeserializer::Deserialize<CancelResponse>(CancelResponse& data)
    {
        *this >> data.TypeId;
        *this >> data.ResponseHeader;
        *this >> data.Parameters;
    }


    template<>
    void DataDeserializer::Deserialize<NodeAttributes>(NodeAttributes& data)
    {
        *this >> data.SpecifiedAttributes;
        *this >> data.DisplayName;
        *this >> data.Description;
        *this >> data.WriteMask;
        *this >> data.UserWriteMask;
    }


    template<>
    void DataDeserializer::Deserialize<ObjectAttributes>(ObjectAttributes& data)
    {
        *this >> data.SpecifiedAttributes;
        *this >> data.DisplayName;
        *this >> data.Description;
        *this >> data.WriteMask;
        *this >> data.UserWriteMask;
        *this >> data.EventNotifier;
    }


    template<>
    void DataDeserializer::Deserialize<VariableAttributes>(VariableAttributes& data)
    {
        *this >> data.SpecifiedAttributes;
        *this >> data.DisplayName;
        *this >> data.Description;
        *this >> data.WriteMask;
        *this >> data.UserWriteMask;
        *this >> data.Value;
        *this >> data.DataType;
        *this >> data.ValueRank;
        DeserializeContainer(*this, data.ArrayDimensions);
        *this >> data.AccessLevel;
        *this >> data.UserAccessLevel;
        *this >> data.MinimumSamplingInterval;
        *this >> data.Historizing;
    }


    template<>
    void DataDeserializer::Deserialize<MethodAttributes>(MethodAttributes& data)
    {
        *this >> data.SpecifiedAttributes;
        *this >> data.DisplayName;
        *this >> data.Description;
        *this >> data.WriteMask;
        *this >> data.UserWriteMask;
        *this >> data.Executable;
        *this >> data.UserExecutable;
    }


    template<>
    void DataDeserializer::Deserialize<ObjectTypeAttributes>(ObjectTypeAttributes& data)
    {
        *this >> data.SpecifiedAttributes;
        *this >> data.DisplayName;
        *this >> data.Description;
        *this >> data.WriteMask;
        *this >> data.UserWriteMask;
        *this >> data.IsAbstract;
    }


    template<>
    void DataDeserializer::Deserialize<VariableTypeAttributes>(VariableTypeAttributes& data)
    {
        *this >> data.SpecifiedAttributes;
        *this >> data.DisplayName;
        *this >> data.Description;
        *this >> data.WriteMask;
        *this >> data.UserWriteMask;
        *this >> data.Value;
        *this >> data.DataType;
        *this >> data.ValueRank;
        DeserializeContainer(*this, data.ArrayDimensions);
        *this >> data.IsAbstract;
    }


    template<>
    void DataDeserializer::Deserialize<ReferenceTypeAttributes>(ReferenceTypeAttributes& data)
    {
        *this >> data.SpecifiedAttributes;
        *this >> data.DisplayName;
        *this >> data.Description;
        *this >> data.WriteMask;
        *this >> data.UserWriteMask;
        *this >> data.IsAbstract;
        *this >> data.Symmetric;
        *this >> data.InverseName;
    }


    template<>
    void DataDeserializer::Deserialize<DataTypeAttributes>(DataTypeAttributes& data)
    {
        *this >> data.SpecifiedAttributes;
        *this >> data.DisplayName;
        *this >> data.Description;
        *this >> data.WriteMask;
        *this >> data.UserWriteMask;
        *this >> data.IsAbstract;
    }


    template<>
    void DataDeserializer::Deserialize<ViewAttributes>(ViewAttributes& data)
    {
        *this >> data.SpecifiedAttributes;
        *this >> data.DisplayName;
        *this >> data.Description;
        *this >> data.WriteMask;
        *this >> data.UserWriteMask;
        *this >> data.ContainsNoLoops;
        *this >> data.EventNotifier;
    }


    template<>
    void DataDeserializer::Deserialize<AddNodesItem>(AddNodesItem& data)
    {
        *this >> data.ParentNodeId;
        *this >> data.ReferenceTypeId;
        *this >> data.RequestedNewNodeId;
        *this >> data.BrowseName;
        *this >> data.NodeClass;
        *this >> data.NodeAttributes;
        *this >> data.TypeDefinition;
    }


    template<>
    void DataDeserializer::Deserialize<AddNodesResult>(AddNodesResult& data)
    {
        *this >> data.StatusCode;
        *this >> data.AddedNodeId;
    }


    template<>
    void DataDeserializer::Deserialize<AddNodesParameters>(AddNodesParameters& data)
    {
        DeserializeContainer(*this, data.NodesToAdd);
    }


    template<>
    void DataDeserializer::Deserialize<AddNodesRequest>(AddNodesRequest& data)
    {
        *this >> data.TypeId;
        *this >> data.RequestHeader;
        *this >> data.Parameters;
    }


    template<>
    void DataDeserializer::Deserialize<AddNodesData>(AddNodesData& data)
    {
        DeserializeContainer(*this, data.Results);
        DeserializeContainer(*this, data.DiagnosticInfos);
    }


    template<>
    void DataDeserializer::Deserialize<AddNodesResponse>(AddNodesResponse& data)
    {
        *this >> data.TypeId;
        *this >> data.ResponseHeader;
        *this >> data.Parameters;
    }


    template<>
    void DataDeserializer::Deserialize<AddReferencesItem>(AddReferencesItem& data)
    {
        *this >> data.SourceNodeId;
        *this >> data.ReferenceTypeId;
        *this >> data.IsForward;
        *this >> data.TargetServerUri;
        *this >> data.TargetNodeId;
        *this >> data.TargetNodeClass;
    }


    template<>
    void DataDeserializer::Deserialize<AddReferencesParameters>(AddReferencesParameters& data)
    {
        DeserializeContainer(*this, data.ReferencesToAdd);
    }


    template<>
    void DataDeserializer::Deserialize<AddReferencesRequest>(AddReferencesRequest& data)
    {
        *this >> data.TypeId;
        *this >> data.RequestHeader;
        *this >> data.Parameters;
    }


    template<>
    void DataDeserializer::Deserialize<AddReferencesData>(AddReferencesData& data)
    {
        DeserializeContainer(*this, data.Results);
        DeserializeContainer(*this, data.DiagnosticInfos);
    }


    template<>
    void DataDeserializer::Deserialize<AddReferencesResponse>(AddReferencesResponse& data)
    {
        *this >> data.TypeId;
        *this >> data.ResponseHeader;
        *this >> data.Parameters;
    }


    template<>
    void DataDeserializer::Deserialize<DeleteNodesItem>(DeleteNodesItem& data)
    {
        *this >> data.NodeId;
        *this >> data.DeleteTargetReferences;
    }


    template<>
    void DataDeserializer::Deserialize<DeleteNodesParameters>(DeleteNodesParameters& data)
    {
        DeserializeContainer(*this, data.NodesToDelete);
    }


    template<>
    void DataDeserializer::Deserialize<DeleteNodesRequest>(DeleteNodesRequest& data)
    {
        *this >> data.TypeId;
        *this >> data.RequestHeader;
        *this >> data.Parameters;
    }


    template<>
    void DataDeserializer::Deserialize<DeleteNodesData>(DeleteNodesData& data)
    {
        DeserializeContainer(*this, data.Results);
        DeserializeContainer(*this, data.DiagnosticInfos);
    }


    template<>
    void DataDeserializer::Deserialize<DeleteNodesResponse>(DeleteNodesResponse& data)
    {
        *this >> data.TypeId;
        *this >> data.ResponseHeader;
        *this >> data.Parameters;
    }


    template<>
    void DataDeserializer::Deserialize<DeleteReferencesItem>(DeleteReferencesItem& data)
    {
        *this >> data.SourceNodeId;
        *this >> data.ReferenceTypeId;
        *this >> data.IsForward;
        *this >> data.TargetNodeId;
        *this >> data.DeleteBidirectional;
    }


    template<>
    void DataDeserializer::Deserialize<DeleteReferencesParameters>(DeleteReferencesParameters& data)
    {
        DeserializeContainer(*this, data.ReferencesToDelete);
    }


    template<>
    void DataDeserializer::Deserialize<DeleteReferencesRequest>(DeleteReferencesRequest& data)
    {
        *this >> data.TypeId;
        *this >> data.RequestHeader;
        *this >> data.Parameters;
    }


    template<>
    void DataDeserializer::Deserialize<DeleteReferencesData>(DeleteReferencesData& data)
    {
        DeserializeContainer(*this, data.Results);
        DeserializeContainer(*this, data.DiagnosticInfos);
    }


    template<>
    void DataDeserializer::Deserialize<DeleteReferencesResponse>(DeleteReferencesResponse& data)
    {
        *this >> data.TypeId;
        *this >> data.ResponseHeader;
        *this >> data.Parameters;
    }


    template<>
    void DataDeserializer::Deserialize<ViewDescription>(ViewDescription& data)
    {
        *this >> data.ViewId;
        *this >> data.Timestamp;
        *this >> data.ViewVersion;
    }


    template<>
    void DataDeserializer::Deserialize<BrowseDescription>(BrowseDescription& data)
    {
        *this >> data.NodeId;
        *this >> data.BrowseDirection;
        *this >> data.ReferenceTypeId;
        *this >> data.IncludeSubtypes;
        *this >> data.NodeClassMask;
        *this >> data.ResultMask;
    }


    template<>
    void DataDeserializer::Deserialize<ReferenceDescription>(ReferenceDescription& data)
    {
        *this >> data.ReferenceTypeId;
        *this >> data.IsForward;
        *this >> data.NodeId;
        *this >> data.BrowseName;
        *this >> data.DisplayName;
        *this >> data.NodeClass;
        *this >> data.TypeDefinition;
    }


    template<>
    void DataDeserializer::Deserialize<BrowseResult>(BrowseResult& data)
    {
        *this >> data.StatusCode;
        *this >> data.ContinuationPoint;
        DeserializeContainer(*this, data.References);
    }


    template<>
    void DataDeserializer::Deserialize<BrowseParameters>(BrowseParameters& data)
    {
        *this >> data.View;
        *this >> data.RequestedMaxReferencesPerNode;
        DeserializeContainer(*this, data.NodesToBrowse);
    }


    template<>
    void DataDeserializer::Deserialize<BrowseRequest>(BrowseRequest& data)
    {
        *this >> data.TypeId;
        *this >> data.RequestHeader;
        *this >> data.Parameters;
    }


    template<>
    void DataDeserializer::Deserialize<BrowseData>(BrowseData& data)
    {
        DeserializeContainer(*this, data.Results);
        DeserializeContainer(*this, data.DiagnosticInfos);
    }


    template<>
    void DataDeserializer::Deserialize<BrowseResponse>(BrowseResponse& data)
    {
        *this >> data.TypeId;
        *this >> data.ResponseHeader;
        *this >> data.Parameters;
    }


    template<>
    void DataDeserializer::Deserialize<BrowseNextParameters>(BrowseNextParameters& data)
    {
        *this >> data.ReleaseContinuationPoints;
        DeserializeContainer(*this, data.ContinuationPoints);
    }


    template<>
    void DataDeserializer::Deserialize<BrowseNextRequest>(BrowseNextRequest& data)
    {
        *this >> data.TypeId;
        *this >> data.RequestHeader;
        *this >> data.Parameters;
    }


    template<>
    void DataDeserializer::Deserialize<BrowseNextData>(BrowseNextData& data)
    {
        DeserializeContainer(*this, data.Results);
        DeserializeContainer(*this, data.DiagnosticInfos);
    }


    template<>
    void DataDeserializer::Deserialize<BrowseNextResponse>(BrowseNextResponse& data)
    {
        *this >> data.TypeId;
        *this >> data.ResponseHeader;
        *this >> data.Parameters;
    }


    template<>
    void DataDeserializer::Deserialize<RelativePathElement>(RelativePathElement& data)
    {
        *this >> data.ReferenceTypeId;
        *this >> data.IsInverse;
        *this >> data.IncludeSubtypes;
        *this >> data.TargetName;
    }


    template<>
    void DataDeserializer::Deserialize<RelativePath>(RelativePath& data)
    {
        DeserializeContainer(*this, data.Elements);
    }


    template<>
    void DataDeserializer::Deserialize<BrowsePath>(BrowsePath& data)
    {
        *this >> data.StartingNode;
        *this >> data.RelativePath;
    }


    template<>
    void DataDeserializer::Deserialize<BrowsePathTarget>(BrowsePathTarget& data)
    {
        *this >> data.TargetId;
        *this >> data.RemainingPathIndex;
    }


    template<>
    void DataDeserializer::Deserialize<BrowsePathResult>(BrowsePathResult& data)
    {
        *this >> data.StatusCode;
        DeserializeContainer(*this, data.Targets);
    }


    template<>
    void DataDeserializer::Deserialize<TranslateBrowsePathsToNodeIdsParameters>(TranslateBrowsePathsToNodeIdsParameters& data)
    {
        DeserializeContainer(*this, data.BrowsePaths);
    }


    template<>
    void DataDeserializer::Deserialize<TranslateBrowsePathsToNodeIdsRequest>(TranslateBrowsePathsToNodeIdsRequest& data)
    {
        *this >> data.TypeId;
        *this >> data.RequestHeader;
        *this >> data.Parameters;
    }


    template<>
    void DataDeserializer::Deserialize<TranslateBrowsePathsToNodeIdsData>(TranslateBrowsePathsToNodeIdsData& data)
    {
        DeserializeContainer(*this, data.Results);
        DeserializeContainer(*this, data.DiagnosticInfos);
    }


    template<>
    void DataDeserializer::Deserialize<TranslateBrowsePathsToNodeIdsResponse>(TranslateBrowsePathsToNodeIdsResponse& data)
    {
        *this >> data.TypeId;
        *this >> data.ResponseHeader;
        *this >> data.Parameters;
    }


    template<>
    void DataDeserializer::Deserialize<RegisterNodesParameters>(RegisterNodesParameters& data)
    {
        DeserializeContainer(*this, data.NodesToRegister);
    }


    template<>
    void DataDeserializer::Deserialize<RegisterNodesRequest>(RegisterNodesRequest& data)
    {
        *this >> data.TypeId;
        *this >> data.RequestHeader;
        *this >> data.Parameters;
    }


    template<>
    void DataDeserializer::Deserialize<RegisterNodesData>(RegisterNodesData& data)
    {
        DeserializeContainer(*this, data.RegisteredNodeIds);
    }


    template<>
    void DataDeserializer::Deserialize<RegisterNodesResponse>(RegisterNodesResponse& data)
    {
        *this >> data.TypeId;
        *this >> data.ResponseHeader;
        *this >> data.Parameters;
    }


    template<>
    void DataDeserializer::Deserialize<UnregisterNodesParameters>(UnregisterNodesParameters& data)
    {
        DeserializeContainer(*this, data.NodesToUnregister);
    }


    template<>
    void DataDeserializer::Deserialize<UnregisterNodesRequest>(UnregisterNodesRequest& data)
    {
        *this >> data.TypeId;
        *this >> data.RequestHeader;
        *this >> data.Parameters;
    }


    template<>
    void DataDeserializer::Deserialize<UnregisterNodesData>(UnregisterNodesData& data)
    {
    }


    template<>
    void DataDeserializer::Deserialize<UnregisterNodesResponse>(UnregisterNodesResponse& data)
    {
        *this >> data.TypeId;
        *this >> data.ResponseHeader;
        *this >> data.Parameters;
    }


    template<>
    void DataDeserializer::Deserialize<EndpointConfiguration>(EndpointConfiguration& data)
    {
        *this >> data.OperationTimeout;
        *this >> data.UseBinaryEncoding;
        *this >> data.MaxStringLength;
        *this >> data.MaxByteStringLength;
        *this >> data.MaxArrayLength;
        *this >> data.MaxMessageSize;
        *this >> data.MaxBufferSize;
        *this >> data.ChannelLifetime;
        *this >> data.SecurityTokenLifetime;
    }


    template<>
    void DataDeserializer::Deserialize<SupportedProfile>(SupportedProfile& data)
    {
        *this >> data.OrganizationUri;
        *this >> data.ProfileId;
        *this >> data.ComplianceTool;
        *this >> data.ComplianceDate;
        *this >> data.ComplianceLevel;
        DeserializeContainer(*this, data.UnsupportedUnitIds);
    }


    template<>
    void DataDeserializer::Deserialize<SoftwareCertificate>(SoftwareCertificate& data)
    {
        *this >> data.ProductName;
        *this >> data.ProductUri;
        *this >> data.VendorName;
        *this >> data.VendorProductCertificate;
        *this >> data.SoftwareVersion;
        *this >> data.BuildNumber;
        *this >> data.BuildDate;
        *this >> data.IssuedBy;
        *this >> data.IssueDate;
        DeserializeContainer(*this, data.SupportedProfiles);
    }


    template<>
    void DataDeserializer::Deserialize<QueryDataDescription>(QueryDataDescription& data)
    {
        *this >> data.RelativePath;
        *this >> data.AttributeId;
        *this >> data.IndexRange;
    }


    template<>
    void DataDeserializer::Deserialize<NodeTypeDescription>(NodeTypeDescription& data)
    {
        *this >> data.TypeDefinitionNode;
        *this >> data.IncludeSubTypes;
        DeserializeContainer(*this, data.DataToReturn);
    }


    template<>
    void DataDeserializer::Deserialize<QueryDataSet>(QueryDataSet& data)
    {
        *this >> data.NodeId;
        *this >> data.TypeDefinitionNode;
        DeserializeContainer(*this, data.Values);
    }


    template<>
    void DataDeserializer::Deserialize<NodeReference>(NodeReference& data)
    {
        *this >> data.NodeId;
        *this >> data.ReferenceTypeId;
        *this >> data.IsForward;
        DeserializeContainer(*this, data.ReferencedNodeIds);
    }


    template<>
    void DataDeserializer::Deserialize<ContentFilterElement>(ContentFilterElement& data)
    {
        *this >> data.FilterOperator;
        DeserializeContainer(*this, data.FilterOperands);
    }


    template<>
    void DataDeserializer::Deserialize<ContentFilter>(ContentFilter& data)
    {
        DeserializeContainer(*this, data.Elements);
    }


    template<>
    void DataDeserializer::Deserialize<FilterOperand>(FilterOperand& data)
    {
    }


    template<>
    void DataDeserializer::Deserialize<ElementOperand>(ElementOperand& data)
    {
        *this >> data.Index;
    }


    template<>
    void DataDeserializer::Deserialize<LiteralOperand>(LiteralOperand& data)
    {
        *this >> data.Value;
    }


    template<>
    void DataDeserializer::Deserialize<AttributeOperand>(AttributeOperand& data)
    {
        *this >> data.NodeId;
        *this >> data.Alias;
        *this >> data.BrowsePath;
        *this >> data.AttributeId;
        *this >> data.IndexRange;
    }


    template<>
    void DataDeserializer::Deserialize<SimpleAttributeOperand>(SimpleAttributeOperand& data)
    {
        *this >> data.TypeDefinitionId;
        DeserializeContainer(*this, data.BrowsePath);
        *this >> data.AttributeId;
        *this >> data.IndexRange;
    }


    template<>
    void DataDeserializer::Deserialize<ContentFilterElementResult>(ContentFilterElementResult& data)
    {
        *this >> data.StatusCode;
        DeserializeContainer(*this, data.OperandStatusCodes);
        DeserializeContainer(*this, data.OperandDiagnosticInfos);
    }


    template<>
    void DataDeserializer::Deserialize<ContentFilterResult>(ContentFilterResult& data)
    {
        DeserializeContainer(*this, data.ElementResults);
        DeserializeContainer(*this, data.ElementDiagnosticInfos);
    }


    template<>
    void DataDeserializer::Deserialize<ParsingResult>(ParsingResult& data)
    {
        *this >> data.StatusCode;
        DeserializeContainer(*this, data.DataStatusCodes);
        DeserializeContainer(*this, data.DataDiagnosticInfos);
    }


    template<>
    void DataDeserializer::Deserialize<QueryFirstParameters>(QueryFirstParameters& data)
    {
        *this >> data.View;
        DeserializeContainer(*this, data.NodeTypes);
        *this >> data.Filter;
        *this >> data.MaxDataSetsToReturn;
        *this >> data.MaxReferencesToReturn;
    }


    template<>
    void DataDeserializer::Deserialize<QueryFirstRequest>(QueryFirstRequest& data)
    {
        *this >> data.TypeId;
        *this >> data.RequestHeader;
        *this >> data.Parameters;
    }


    template<>
    void DataDeserializer::Deserialize<QueryFirstData>(QueryFirstData& data)
    {
        DeserializeContainer(*this, data.QueryDataSets);
        *this >> data.ContinuationPoint;
        DeserializeContainer(*this, data.ParsingResults);
        DeserializeContainer(*this, data.DiagnosticInfos);
        *this >> data.FilterResult;
    }


    template<>
    void DataDeserializer::Deserialize<QueryFirstResponse>(QueryFirstResponse& data)
    {
        *this >> data.TypeId;
        *this >> data.ResponseHeader;
        *this >> data.Parameters;
    }


    template<>
    void DataDeserializer::Deserialize<QueryNextParameters>(QueryNextParameters& data)
    {
        *this >> data.ReleaseContinuationPoint;
        *this >> data.ContinuationPoint;
    }


    template<>
    void DataDeserializer::Deserialize<QueryNextRequest>(QueryNextRequest& data)
    {
        *this >> data.TypeId;
        *this >> data.RequestHeader;
        *this >> data.Parameters;
    }


    template<>
    void DataDeserializer::Deserialize<QueryNextData>(QueryNextData& data)
    {
        DeserializeContainer(*this, data.QueryDataSets);
        *this >> data.RevisedContinuationPoint;
    }


    template<>
    void DataDeserializer::Deserialize<QueryNextResponse>(QueryNextResponse& data)
    {
        *this >> data.TypeId;
        *this >> data.ResponseHeader;
        *this >> data.Parameters;
    }


    template<>
    void DataDeserializer::Deserialize<ReadValueId>(ReadValueId& data)
    {
        *this >> data.NodeId;
        *this >> data.AttributeId;
        *this >> data.IndexRange;
        *this >> data.DataEncoding;
    }


    template<>
    void DataDeserializer::Deserialize<ReadParameters>(ReadParameters& data)
    {
        *this >> data.MaxAge;
        *this >> data.TimestampsToReturn;
        DeserializeContainer(*this, data.NodesToRead);
    }


    template<>
    void DataDeserializer::Deserialize<ReadRequest>(ReadRequest& data)
    {
        *this >> data.TypeId;
        *this >> data.RequestHeader;
        *this >> data.Parameters;
    }


    template<>
    void DataDeserializer::Deserialize<ReadData>(ReadData& data)
    {
        DeserializeContainer(*this, data.Results);
        DeserializeContainer(*this, data.DiagnosticInfos);
    }


    template<>
    void DataDeserializer::Deserialize<ReadResponse>(ReadResponse& data)
    {
        *this >> data.TypeId;
        *this >> data.ResponseHeader;
        *this >> data.Parameters;
    }


    template<>
    void DataDeserializer::Deserialize<HistoryReadValueId>(HistoryReadValueId& data)
    {
        *this >> data.NodeId;
        *this >> data.IndexRange;
        *this >> data.DataEncoding;
        *this >> data.ContinuationPoint;
    }


    template<>
    void DataDeserializer::Deserialize<HistoryReadResult>(HistoryReadResult& data)
    {
        *this >> data.StatusCode;
        *this >> data.ContinuationPoint;
        *this >> data.HistoryData;
    }


    template<>
    void DataDeserializer::Deserialize<HistoryReadDetails>(HistoryReadDetails& data)
    {
    }


    template<>
    void DataDeserializer::Deserialize<ReadEventDetails>(ReadEventDetails& data)
    {
        *this >> data.NumValuesPerNode;
        *this >> data.StartTime;
        *this >> data.EndTime;
        *this >> data.Filter;
    }


    template<>
    void DataDeserializer::Deserialize<ReadRawModifiedDetails>(ReadRawModifiedDetails& data)
    {
        *this >> data.IsReadModified;
        *this >> data.StartTime;
        *this >> data.EndTime;
        *this >> data.NumValuesPerNode;
        *this >> data.ReturnBounds;
    }


    template<>
    void DataDeserializer::Deserialize<ReadProcessedDetails>(ReadProcessedDetails& data)
    {
        *this >> data.StartTime;
        *this >> data.EndTime;
        *this >> data.ProcessingInterval;
        DeserializeContainer(*this, data.AggregateType);
        *this >> data.AggregateConfiguration;
    }


    template<>
    void DataDeserializer::Deserialize<ReadAtTimeDetails>(ReadAtTimeDetails& data)
    {
        DeserializeContainer(*this, data.ReqTimes);
        *this >> data.UseSimpleBounds;
    }


    template<>
    void DataDeserializer::Deserialize<HistoryData>(HistoryData& data)
    {
        DeserializeContainer(*this, data.DataValues);
    }


    template<>
    void DataDeserializer::Deserialize<ModificationInfo>(ModificationInfo& data)
    {
        *this >> data.ModificationTime;
        *this >> data.UpdateType;
        *this >> data.UserName;
    }


    template<>
    void DataDeserializer::Deserialize<HistoryModifiedData>(HistoryModifiedData& data)
    {
        DeserializeContainer(*this, data.DataValues);
        DeserializeContainer(*this, data.ModificationInfos);
    }


    template<>
    void DataDeserializer::Deserialize<HistoryEvent>(HistoryEvent& data)
    {
        DeserializeContainer(*this, data.Events);
    }


    template<>
    void DataDeserializer::Deserialize<HistoryReadParameters>(HistoryReadParameters& data)
    {
        *this >> data.HistoryReadDetails;
        *this >> data.TimestampsToReturn;
        *this >> data.ReleaseContinuationPoints;
        DeserializeContainer(*this, data.NodesToRead);
    }


    template<>
    void DataDeserializer::Deserialize<HistoryReadRequest>(HistoryReadRequest& data)
    {
        *this >> data.TypeId;
        *this >> data.RequestHeader;
        *this >> data.Parameters;
    }


    template<>
    void DataDeserializer::Deserialize<HistoryReadData>(HistoryReadData& data)
    {
        DeserializeContainer(*this, data.Results);
        DeserializeContainer(*this, data.DiagnosticInfos);
    }


    template<>
    void DataDeserializer::Deserialize<HistoryReadResponse>(HistoryReadResponse& data)
    {
        *this >> data.TypeId;
        *this >> data.ResponseHeader;
        *this >> data.Parameters;
    }


    template<>
    void DataDeserializer::Deserialize<WriteValue>(WriteValue& data)
    {
        *this >> data.NodeId;
        *this >> data.AttributeId;
        *this >> data.IndexRange;
        *this >> data.Value;
    }


    template<>
    void DataDeserializer::Deserialize<WriteParameters>(WriteParameters& data)
    {
        DeserializeContainer(*this, data.NodesToWrite);
    }


    template<>
    void DataDeserializer::Deserialize<WriteRequest>(WriteRequest& data)
    {
        *this >> data.TypeId;
        *this >> data.RequestHeader;
        *this >> data.Parameters;
    }


    template<>
    void DataDeserializer::Deserialize<WriteData>(WriteData& data)
    {
        DeserializeContainer(*this, data.Results);
        DeserializeContainer(*this, data.DiagnosticInfos);
    }


    template<>
    void DataDeserializer::Deserialize<WriteResponse>(WriteResponse& data)
    {
        *this >> data.TypeId;
        *this >> data.ResponseHeader;
        *this >> data.Parameters;
    }


    template<>
    void DataDeserializer::Deserialize<HistoryUpdateDetails>(HistoryUpdateDetails& data)
    {
        *this >> data.NodeId;
    }


    template<>
    void DataDeserializer::Deserialize<UpdateDataDetails>(UpdateDataDetails& data)
    {
        *this >> data.NodeId;
        *this >> data.PerformInsertReplace;
        DeserializeContainer(*this, data.UpdateValues);
    }


    template<>
    void DataDeserializer::Deserialize<UpdateStructureDataDetails>(UpdateStructureDataDetails& data)
    {
        *this >> data.NodeId;
        *this >> data.PerformInsertReplace;
        DeserializeContainer(*this, data.UpdateValues);
    }


    template<>
    void DataDeserializer::Deserialize<UpdateEventDetails>(UpdateEventDetails& data)
    {
        *this >> data.NodeId;
        *this >> data.PerformInsertReplace;
        *this >> data.Filter;
        DeserializeContainer(*this, data.EventData);
    }


    template<>
    void DataDeserializer::Deserialize<DeleteRawModifiedDetails>(DeleteRawModifiedDetails& data)
    {
        *this >> data.NodeId;
        *this >> data.IsDeleteModified;
        *this >> data.StartTime;
        *this >> data.EndTime;
    }


    template<>
    void DataDeserializer::Deserialize<DeleteAtTimeDetails>(DeleteAtTimeDetails& data)
    {
        *this >> data.NodeId;
        DeserializeContainer(*this, data.ReqTimes);
    }


    template<>
    void DataDeserializer::Deserialize<DeleteEventDetails>(DeleteEventDetails& data)
    {
        *this >> data.NodeId;
        DeserializeContainer(*this, data.EventIds);
    }


    template<>
    void DataDeserializer::Deserialize<HistoryUpdateResult>(HistoryUpdateResult& data)
    {
        *this >> data.StatusCode;
        DeserializeContainer(*this, data.OperationResults);
        DeserializeContainer(*this, data.DiagnosticInfos);
    }


    template<>
    void DataDeserializer::Deserialize<HistoryUpdateEventResult>(HistoryUpdateEventResult& data)
    {
        *this >> data.StatusCode;
        *this >> data.EventFilterResult;
    }


    template<>
    void DataDeserializer::Deserialize<HistoryUpdateParameters>(HistoryUpdateParameters& data)
    {
        DeserializeContainer(*this, data.HistoryUpdateDetails);
    }


    template<>
    void DataDeserializer::Deserialize<HistoryUpdateRequest>(HistoryUpdateRequest& data)
    {
        *this >> data.TypeId;
        *this >> data.RequestHeader;
        *this >> data.Parameters;
    }


    template<>
    void DataDeserializer::Deserialize<HistoryUpdateData>(HistoryUpdateData& data)
    {
        DeserializeContainer(*this, data.Results);
        DeserializeContainer(*this, data.DiagnosticInfos);
    }


    template<>
    void DataDeserializer::Deserialize<HistoryUpdateResponse>(HistoryUpdateResponse& data)
    {
        *this >> data.TypeId;
        *this >> data.ResponseHeader;
        *this >> data.Parameters;
    }


    template<>
    void DataDeserializer::Deserialize<CallMethodParameters>(CallMethodParameters& data)
    {
        *this >> data.MethodId;
        DeserializeContainer(*this, data.InputArguments);
    }


    template<>
    void DataDeserializer::Deserialize<CallMethodRequest>(CallMethodRequest& data)
    {
        *this >> data.TypeId;
        *this >> data.ObjectId;
        *this >> data.Parameters;
    }


    template<>
    void DataDeserializer::Deserialize<CallMethodResult>(CallMethodResult& data)
    {
        *this >> data.StatusCode;
        DeserializeContainer(*this, data.InputArgumentResults);
        DeserializeContainer(*this, data.InputArgumentDiagnosticInfos);
        DeserializeContainer(*this, data.OutputArguments);
    }


    template<>
    void DataDeserializer::Deserialize<CallParameters>(CallParameters& data)
    {
        DeserializeContainer(*this, data.MethodsToCall);
    }


    template<>
    void DataDeserializer::Deserialize<CallRequest>(CallRequest& data)
    {
        *this >> data.TypeId;
        *this >> data.RequestHeader;
        *this >> data.Parameters;
    }


    template<>
    void DataDeserializer::Deserialize<CallData>(CallData& data)
    {
        DeserializeContainer(*this, data.Results);
        DeserializeContainer(*this, data.DiagnosticInfos);
    }


    template<>
    void DataDeserializer::Deserialize<CallResponse>(CallResponse& data)
    {
        *this >> data.TypeId;
        *this >> data.ResponseHeader;
        *this >> data.Parameters;
    }


    template<>
    void DataDeserializer::Deserialize<MonitoringFilter>(MonitoringFilter& data)
    {
    }


    template<>
    void DataDeserializer::Deserialize<DataChangeFilter>(DataChangeFilter& data)
    {
        *this >> data.Trigger;
        *this >> data.DeadbandType;
        *this >> data.DeadbandValue;
    }


    template<>
    void DataDeserializer::Deserialize<EventFilter>(EventFilter& data)
    {
        DeserializeContainer(*this, data.SelectClauses);
        *this >> data.WhereClause;
    }


    template<>
    void DataDeserializer::Deserialize<AggregateConfiguration>(AggregateConfiguration& data)
    {
        *this >> data.UseServerCapabilitiesDefaults;
        *this >> data.TreatUncertainAsBad;
        *this >> data.PercentDataBad;
        *this >> data.PercentDataGood;
        *this >> data.UseSlopedExtrapolation;
    }


    template<>
    void DataDeserializer::Deserialize<AggregateFilter>(AggregateFilter& data)
    {
        *this >> data.StartTime;
        *this >> data.AggregateType;
        *this >> data.ProcessingInterval;
        *this >> data.AggregateConfiguration;
    }


    template<>
    void DataDeserializer::Deserialize<MonitoringFilterResult>(MonitoringFilterResult& data)
    {
    }


    template<>
    void DataDeserializer::Deserialize<EventFilterResult>(EventFilterResult& data)
    {
        DeserializeContainer(*this, data.SelectClauseResults);
        DeserializeContainer(*this, data.SelectClauseDiagnosticInfos);
        *this >> data.WhereClauseResult;
    }


    template<>
    void DataDeserializer::Deserialize<AggregateFilterResult>(AggregateFilterResult& data)
    {
        *this >> data.RevisedStartTime;
        *this >> data.RevisedProcessingInterval;
        *this >> data.RevisedAggregateConfiguration;
    }


    template<>
    void DataDeserializer::Deserialize<MonitoringParameters>(MonitoringParameters& data)
    {
        *this >> data.ClientHandle;
        *this >> data.SamplingInterval;
        *this >> data.Filter;
        *this >> data.QueueSize;
        *this >> data.DiscardOldest;
    }


    template<>
    void DataDeserializer::Deserialize<MonitoredItemCreateParameters>(MonitoredItemCreateParameters& data)
    {
        *this >> data.MonitoringMode;
        *this >> data.RequestedParameters;
    }


    template<>
    void DataDeserializer::Deserialize<MonitoredItemCreateRequest>(MonitoredItemCreateRequest& data)
    {
        *this >> data.TypeId;
        *this >> data.ItemToMonitor;
        *this >> data.Parameters;
    }


    template<>
    void DataDeserializer::Deserialize<MonitoredItemCreateResult>(MonitoredItemCreateResult& data)
    {
        *this >> data.StatusCode;
        *this >> data.MonitoredItemId;
        *this >> data.RevisedSamplingInterval;
        *this >> data.RevisedQueueSize;
        *this >> data.FilterResult;
    }


    template<>
    void DataDeserializer::Deserialize<CreateMonitoredItemsParameters>(CreateMonitoredItemsParameters& data)
    {
        *this >> data.SubscriptionId;
        *this >> data.TimestampsToReturn;
        DeserializeContainer(*this, data.ItemsToCreate);
    }


    template<>
    void DataDeserializer::Deserialize<CreateMonitoredItemsRequest>(CreateMonitoredItemsRequest& data)
    {
        *this >> data.TypeId;
        *this >> data.RequestHeader;
        *this >> data.Parameters;
    }


    template<>
    void DataDeserializer::Deserialize<CreateMonitoredItemsData>(CreateMonitoredItemsData& data)
    {
        DeserializeContainer(*this, data.Results);
        DeserializeContainer(*this, data.DiagnosticInfos);
    }


    template<>
    void DataDeserializer::Deserialize<CreateMonitoredItemsResponse>(CreateMonitoredItemsResponse& data)
    {
        *this >> data.TypeId;
        *this >> data.ResponseHeader;
        *this >> data.Parameters;
    }


    template<>
    void DataDeserializer::Deserialize<MonitoredItemModifyParameters>(MonitoredItemModifyParameters& data)
    {
        *this >> data.RequestedParameters;
    }


    template<>
    void DataDeserializer::Deserialize<MonitoredItemModifyRequest>(MonitoredItemModifyRequest& data)
    {
        *this >> data.TypeId;
        *this >> data.MonitoredItemId;
        *this >> data.Parameters;
    }


    template<>
    void DataDeserializer::Deserialize<MonitoredItemModifyResult>(MonitoredItemModifyResult& data)
    {
        *this >> data.StatusCode;
        *this >> data.RevisedSamplingInterval;
        *this >> data.RevisedQueueSize;
        *this >> data.FilterResult;
    }


    template<>
    void DataDeserializer::Deserialize<ModifyMonitoredItemsParameters>(ModifyMonitoredItemsParameters& data)
    {
        *this >> data.SubscriptionId;
        *this >> data.TimestampsToReturn;
        DeserializeContainer(*this, data.ItemsToModify);
    }


    template<>
    void DataDeserializer::Deserialize<ModifyMonitoredItemsRequest>(ModifyMonitoredItemsRequest& data)
    {
        *this >> data.TypeId;
        *this >> data.RequestHeader;
        *this >> data.Parameters;
    }


    template<>
    void DataDeserializer::Deserialize<ModifyMonitoredItemsData>(ModifyMonitoredItemsData& data)
    {
        DeserializeContainer(*this, data.Results);
        DeserializeContainer(*this, data.DiagnosticInfos);
    }


    template<>
    void DataDeserializer::Deserialize<ModifyMonitoredItemsResponse>(ModifyMonitoredItemsResponse& data)
    {
        *this >> data.TypeId;
        *this >> data.ResponseHeader;
        *this >> data.Parameters;
    }


    template<>
    void DataDeserializer::Deserialize<SetMonitoringModeParameters>(SetMonitoringModeParameters& data)
    {
        *this >> data.SubscriptionId;
        *this >> data.MonitoringMode;
        DeserializeContainer(*this, data.MonitoredItemIds);
    }


    template<>
    void DataDeserializer::Deserialize<SetMonitoringModeRequest>(SetMonitoringModeRequest& data)
    {
        *this >> data.TypeId;
        *this >> data.RequestHeader;
        *this >> data.Parameters;
    }


    template<>
    void DataDeserializer::Deserialize<SetMonitoringModeData>(SetMonitoringModeData& data)
    {
        DeserializeContainer(*this, data.Results);
        DeserializeContainer(*this, data.DiagnosticInfos);
    }


    template<>
    void DataDeserializer::Deserialize<SetMonitoringModeResponse>(SetMonitoringModeResponse& data)
    {
        *this >> data.TypeId;
        *this >> data.ResponseHeader;
        *this >> data.Parameters;
    }


    template<>
    void DataDeserializer::Deserialize<SetTriggeringParameters>(SetTriggeringParameters& data)
    {
        *this >> data.SubscriptionId;
        *this >> data.TriggeringItemId;
        DeserializeContainer(*this, data.LinksToAdd);
        DeserializeContainer(*this, data.LinksToRemove);
    }


    template<>
    void DataDeserializer::Deserialize<SetTriggeringRequest>(SetTriggeringRequest& data)
    {
        *this >> data.TypeId;
        *this >> data.RequestHeader;
        *this >> data.Parameters;
    }


    template<>
    void DataDeserializer::Deserialize<SetTriggeringData>(SetTriggeringData& data)
    {
        DeserializeContainer(*this, data.AddResults);
        DeserializeContainer(*this, data.AddDiagnosticInfos);
        DeserializeContainer(*this, data.RemoveResults);
        DeserializeContainer(*this, data.RemoveDiagnosticInfos);
    }


    template<>
    void DataDeserializer::Deserialize<SetTriggeringResponse>(SetTriggeringResponse& data)
    {
        *this >> data.TypeId;
        *this >> data.ResponseHeader;
        *this >> data.Parameters;
    }


    template<>
    void DataDeserializer::Deserialize<DeleteMonitoredItemsParameters>(DeleteMonitoredItemsParameters& data)
    {
        *this >> data.SubscriptionId;
        DeserializeContainer(*this, data.MonitoredItemIds);
    }


    template<>
    void DataDeserializer::Deserialize<DeleteMonitoredItemsRequest>(DeleteMonitoredItemsRequest& data)
    {
        *this >> data.TypeId;
        *this >> data.RequestHeader;
        *this >> data.Parameters;
    }


    template<>
    void DataDeserializer::Deserialize<DeleteMonitoredItemsData>(DeleteMonitoredItemsData& data)
    {
        DeserializeContainer(*this, data.Results);
        DeserializeContainer(*this, data.DiagnosticInfos);
    }


    template<>
    void DataDeserializer::Deserialize<DeleteMonitoredItemsResponse>(DeleteMonitoredItemsResponse& data)
    {
        *this >> data.TypeId;
        *this >> data.ResponseHeader;
        *this >> data.Parameters;
    }


    template<>
    void DataDeserializer::Deserialize<CreateSubscriptionParameters>(CreateSubscriptionParameters& data)
    {
        *this >> data.RequestedPublishingInterval;
        *this >> data.RequestedLifetimeCount;
        *this >> data.RequestedMaxKeepAliveCount;
        *this >> data.MaxNotificationsPerPublish;
        *this >> data.PublishingEnabled;
        *this >> data.Priority;
    }


    template<>
    void DataDeserializer::Deserialize<CreateSubscriptionRequest>(CreateSubscriptionRequest& data)
    {
        *this >> data.TypeId;
        *this >> data.RequestHeader;
        *this >> data.Parameters;
    }


    template<>
    void DataDeserializer::Deserialize<CreateSubscriptionData>(CreateSubscriptionData& data)
    {
        *this >> data.SubscriptionId;
        *this >> data.RevisedPublishingInterval;
        *this >> data.RevisedLifetimeCount;
        *this >> data.RevisedMaxKeepAliveCount;
    }


    template<>
    void DataDeserializer::Deserialize<CreateSubscriptionResponse>(CreateSubscriptionResponse& data)
    {
        *this >> data.TypeId;
        *this >> data.ResponseHeader;
        *this >> data.Parameters;
    }


    template<>
    void DataDeserializer::Deserialize<ModifySubscriptionParameters>(ModifySubscriptionParameters& data)
    {
        *this >> data.SubscriptionId;
        *this >> data.RequestedPublishingInterval;
        *this >> data.RequestedLifetimeCount;
        *this >> data.RequestedMaxKeepAliveCount;
        *this >> data.MaxNotificationsPerPublish;
        *this >> data.Priority;
    }


    template<>
    void DataDeserializer::Deserialize<ModifySubscriptionRequest>(ModifySubscriptionRequest& data)
    {
        *this >> data.TypeId;
        *this >> data.RequestHeader;
        *this >> data.Parameters;
    }


    template<>
    void DataDeserializer::Deserialize<ModifySubscriptionData>(ModifySubscriptionData& data)
    {
        *this >> data.RevisedPublishingInterval;
        *this >> data.RevisedLifetimeCount;
        *this >> data.RevisedMaxKeepAliveCount;
    }


    template<>
    void DataDeserializer::Deserialize<ModifySubscriptionResponse>(ModifySubscriptionResponse& data)
    {
        *this >> data.TypeId;
        *this >> data.ResponseHeader;
        *this >> data.Parameters;
    }


    template<>
    void DataDeserializer::Deserialize<SetPublishingModeParameters>(SetPublishingModeParameters& data)
    {
        *this >> data.PublishingEnabled;
        DeserializeContainer(*this, data.SubscriptionIds);
    }


    template<>
    void DataDeserializer::Deserialize<SetPublishingModeRequest>(SetPublishingModeRequest& data)
    {
        *this >> data.TypeId;
        *this >> data.RequestHeader;
        *this >> data.Parameters;
    }


    template<>
    void DataDeserializer::Deserialize<SetPublishingModeData>(SetPublishingModeData& data)
    {
        DeserializeContainer(*this, data.Results);
        DeserializeContainer(*this, data.DiagnosticInfos);
    }


    template<>
    void DataDeserializer::Deserialize<SetPublishingModeResponse>(SetPublishingModeResponse& data)
    {
        *this >> data.TypeId;
        *this >> data.ResponseHeader;
        *this >> data.Parameters;
    }


    template<>
    void DataDeserializer::Deserialize<NotificationMessage>(NotificationMessage& data)
    {
        *this >> data.SequenceNumber;
        *this >> data.PublishTime;
        DeserializeContainer(*this, data.NotificationData);
    }


    template<>
    void DataDeserializer::Deserialize<NotificationData>(NotificationData& data)
    {
    }


    template<>
    void DataDeserializer::Deserialize<DataChangeNotification>(DataChangeNotification& data)
    {
        DeserializeContainer(*this, data.MonitoredItems);
        DeserializeContainer(*this, data.DiagnosticInfos);
    }


    template<>
    void DataDeserializer::Deserialize<MonitoredItemNotification>(MonitoredItemNotification& data)
    {
        *this >> data.ClientHandle;
        *this >> data.Value;
    }


    template<>
    void DataDeserializer::Deserialize<EventNotificationList>(EventNotificationList& data)
    {
        DeserializeContainer(*this, data.Events);
    }


    template<>
    void DataDeserializer::Deserialize<EventFieldList>(EventFieldList& data)
    {
        *this >> data.ClientHandle;
        DeserializeContainer(*this, data.EventFields);
    }


    template<>
    void DataDeserializer::Deserialize<HistoryEventFieldList>(HistoryEventFieldList& data)
    {
        DeserializeContainer(*this, data.EventFields);
    }


    template<>
    void DataDeserializer::Deserialize<StatusChangeNotification>(StatusChangeNotification& data)
    {
        *this >> data.Status;
        *this >> data.DiagnosticInfo;
    }


    template<>
    void DataDeserializer::Deserialize<SubscriptionAcknowledgement>(SubscriptionAcknowledgement& data)
    {
        *this >> data.SubscriptionId;
        *this >> data.SequenceNumber;
    }


    template<>
    void DataDeserializer::Deserialize<PublishParameters>(PublishParameters& data)
    {
        DeserializeContainer(*this, data.SubscriptionAcknowledgements);
    }


    template<>
    void DataDeserializer::Deserialize<PublishRequest>(PublishRequest& data)
    {
        *this >> data.TypeId;
        *this >> data.RequestHeader;
        *this >> data.Parameters;
    }


    template<>
    void DataDeserializer::Deserialize<PublishData>(PublishData& data)
    {
        *this >> data.SubscriptionId;
        DeserializeContainer(*this, data.AvailableSequenceNumbers);
        *this >> data.MoreNotifications;
        *this >> data.NotificationMessage;
        DeserializeContainer(*this, data.Results);
        DeserializeContainer(*this, data.DiagnosticInfos);
    }


    template<>
    void DataDeserializer::Deserialize<PublishResponse>(PublishResponse& data)
    {
        *this >> data.TypeId;
        *this >> data.ResponseHeader;
        *this >> data.Parameters;
    }


    template<>
    void DataDeserializer::Deserialize<RepublishParameters>(RepublishParameters& data)
    {
        *this >> data.SubscriptionId;
        *this >> data.RetransmitSequenceNumber;
    }


    template<>
    void DataDeserializer::Deserialize<RepublishRequest>(RepublishRequest& data)
    {
        *this >> data.TypeId;
        *this >> data.RequestHeader;
        *this >> data.Parameters;
    }


    template<>
    void DataDeserializer::Deserialize<RepublishData>(RepublishData& data)
    {
        *this >> data.NotificationMessage;
    }


    template<>
    void DataDeserializer::Deserialize<RepublishResponse>(RepublishResponse& data)
    {
        *this >> data.TypeId;
        *this >> data.ResponseHeader;
        *this >> data.Parameters;
    }


    template<>
    void DataDeserializer::Deserialize<TransferResult>(TransferResult& data)
    {
        *this >> data.StatusCode;
        DeserializeContainer(*this, data.AvailableSequenceNumbers);
    }


    template<>
    void DataDeserializer::Deserialize<TransferSubscriptionsParameters>(TransferSubscriptionsParameters& data)
    {
        DeserializeContainer(*this, data.SubscriptionIds);
        *this >> data.SendInitialValues;
    }


    template<>
    void DataDeserializer::Deserialize<TransferSubscriptionsRequest>(TransferSubscriptionsRequest& data)
    {
        *this >> data.TypeId;
        *this >> data.RequestHeader;
        *this >> data.Parameters;
    }


    template<>
    void DataDeserializer::Deserialize<TransferSubscriptionsData>(TransferSubscriptionsData& data)
    {
        DeserializeContainer(*this, data.Results);
        DeserializeContainer(*this, data.DiagnosticInfos);
    }


    template<>
    void DataDeserializer::Deserialize<TransferSubscriptionsResponse>(TransferSubscriptionsResponse& data)
    {
        *this >> data.TypeId;
        *this >> data.ResponseHeader;
        *this >> data.Parameters;
    }


    template<>
    void DataDeserializer::Deserialize<DeleteSubscriptionsParameters>(DeleteSubscriptionsParameters& data)
    {
        DeserializeContainer(*this, data.SubscriptionIds);
    }


    template<>
    void DataDeserializer::Deserialize<DeleteSubscriptionsRequest>(DeleteSubscriptionsRequest& data)
    {
        *this >> data.TypeId;
        *this >> data.RequestHeader;
        *this >> data.Parameters;
    }


    template<>
    void DataDeserializer::Deserialize<DeleteSubscriptionsData>(DeleteSubscriptionsData& data)
    {
        DeserializeContainer(*this, data.Results);
        DeserializeContainer(*this, data.DiagnosticInfos);
    }


    template<>
    void DataDeserializer::Deserialize<DeleteSubscriptionsResponse>(DeleteSubscriptionsResponse& data)
    {
        *this >> data.TypeId;
        *this >> data.ResponseHeader;
        *this >> data.Parameters;
    }


    template<>
    void DataDeserializer::Deserialize<ScalarTestType>(ScalarTestType& data)
    {
        *this >> data.Boolean;
        *this >> data.SByte;
        *this >> data.Byte;
        *this >> data.Int16;
        *this >> data.UInt16;
        *this >> data.Int32;
        *this >> data.UInt32;
        *this >> data.Int64;
        *this >> data.UInt64;
        *this >> data.Float;
        *this >> data.Double;
        *this >> data.String;
        *this >> data.DateTime;
        *this >> data.Guid;
        *this >> data.ByteString;
        *this >> data.XmlElement;
        *this >> data.NodeId;
        *this >> data.ExpandedNodeId;
        *this >> data.StatusCode;
        *this >> data.DiagnosticInfo;
        *this >> data.QualifiedName;
        *this >> data.LocalizedText;
        *this >> data.ExtensionObject;
        *this >> data.DataValue;
        *this >> data.EnumeratedValue;
    }


    template<>
    void DataDeserializer::Deserialize<ArrayTestType>(ArrayTestType& data)
    {
        DeserializeContainer(*this, data.Booleans);
        DeserializeContainer(*this, data.SBytes);
        DeserializeContainer(*this, data.Int16s);
        DeserializeContainer(*this, data.UInt16s);
        DeserializeContainer(*this, data.Int32s);
        DeserializeContainer(*this, data.UInt32s);
        DeserializeContainer(*this, data.Int64s);
        DeserializeContainer(*this, data.UInt64s);
        DeserializeContainer(*this, data.Floats);
        DeserializeContainer(*this, data.Doubles);
        DeserializeContainer(*this, data.Strings);
        DeserializeContainer(*this, data.DateTimes);
        DeserializeContainer(*this, data.Guids);
        DeserializeContainer(*this, data.ByteStrings);
        DeserializeContainer(*this, data.XmlElements);
        DeserializeContainer(*this, data.NodeIds);
        DeserializeContainer(*this, data.ExpandedNodeIds);
        DeserializeContainer(*this, data.StatusCodes);
        DeserializeContainer(*this, data.DiagnosticInfos);
        DeserializeContainer(*this, data.QualifiedNames);
        DeserializeContainer(*this, data.LocalizedTexts);
        DeserializeContainer(*this, data.ExtensionObjects);
        DeserializeContainer(*this, data.DataValues);
        DeserializeContainer(*this, data.Variants);
        DeserializeContainer(*this, data.EnumeratedValues);
    }


    template<>
    void DataDeserializer::Deserialize<CompositeTestType>(CompositeTestType& data)
    {
        *this >> data.Field1;
        *this >> data.Field2;
    }


    template<>
    void DataDeserializer::Deserialize<TestStackParameters>(TestStackParameters& data)
    {
        *this >> data.TestId;
        *this >> data.Iteration;
        *this >> data.Input;
    }


    template<>
    void DataDeserializer::Deserialize<TestStackRequest>(TestStackRequest& data)
    {
        *this >> data.TypeId;
        *this >> data.RequestHeader;
        *this >> data.Parameters;
    }


    template<>
    void DataDeserializer::Deserialize<TestStackData>(TestStackData& data)
    {
        *this >> data.Output;
    }


    template<>
    void DataDeserializer::Deserialize<TestStackResponse>(TestStackResponse& data)
    {
        *this >> data.TypeId;
        *this >> data.ResponseHeader;
        *this >> data.Parameters;
    }


    template<>
    void DataDeserializer::Deserialize<TestStackExParameters>(TestStackExParameters& data)
    {
        *this >> data.TestId;
        *this >> data.Iteration;
        *this >> data.Input;
    }


    template<>
    void DataDeserializer::Deserialize<TestStackExRequest>(TestStackExRequest& data)
    {
        *this >> data.TypeId;
        *this >> data.RequestHeader;
        *this >> data.Parameters;
    }


    template<>
    void DataDeserializer::Deserialize<TestStackExData>(TestStackExData& data)
    {
        *this >> data.Output;
    }


    template<>
    void DataDeserializer::Deserialize<TestStackExResponse>(TestStackExResponse& data)
    {
        *this >> data.TypeId;
        *this >> data.ResponseHeader;
        *this >> data.Parameters;
    }


    template<>
    void DataDeserializer::Deserialize<BuildInfo>(BuildInfo& data)
    {
        *this >> data.ProductUri;
        *this >> data.ManufacturerName;
        *this >> data.ProductName;
        *this >> data.SoftwareVersion;
        *this >> data.BuildNumber;
        *this >> data.BuildDate;
    }


    template<>
    void DataDeserializer::Deserialize<RedundantServerDataType>(RedundantServerDataType& data)
    {
        *this >> data.ServerId;
        *this >> data.ServiceLevel;
        *this >> data.ServerState;
    }


    template<>
    void DataDeserializer::Deserialize<EndpointUrlListDataType>(EndpointUrlListDataType& data)
    {
        DeserializeContainer(*this, data.EndpointUrlList);
    }


    template<>
    void DataDeserializer::Deserialize<NetworkGroupDataType>(NetworkGroupDataType& data)
    {
        *this >> data.ServerUri;
        DeserializeContainer(*this, data.NetworkPaths);
    }


    template<>
    void DataDeserializer::Deserialize<SamplingIntervalDiagnosticsDataType>(SamplingIntervalDiagnosticsDataType& data)
    {
        *this >> data.SamplingInterval;
        *this >> data.MonitoredItemCount;
        *this >> data.MaxMonitoredItemCount;
        *this >> data.DisabledMonitoredItemCount;
    }


    template<>
    void DataDeserializer::Deserialize<ServerDiagnosticsSummaryDataType>(ServerDiagnosticsSummaryDataType& data)
    {
        *this >> data.ServerViewCount;
        *this >> data.CurrentSessionCount;
        *this >> data.CumulatedSessionCount;
        *this >> data.SecurityRejectedSessionCount;
        *this >> data.RejectedSessionCount;
        *this >> data.SessionTimeoutCount;
        *this >> data.SessionAbortCount;
        *this >> data.CurrentSubscriptionCount;
        *this >> data.CumulatedSubscriptionCount;
        *this >> data.PublishingIntervalCount;
        *this >> data.SecurityRejectedRequestsCount;
        *this >> data.RejectedRequestsCount;
    }


    template<>
    void DataDeserializer::Deserialize<ServerStatusDataType>(ServerStatusDataType& data)
    {
        *this >> data.StartTime;
        *this >> data.CurrentTime;
        *this >> data.State;
        *this >> data.BuildInfo;
        *this >> data.SecondsTillShutdown;
        *this >> data.ShutdownReason;
    }


    template<>
    void DataDeserializer::Deserialize<SessionDiagnosticsDataType>(SessionDiagnosticsDataType& data)
    {
        *this >> data.SessionId;
        *this >> data.SessionName;
        *this >> data.ClientDescription;
        *this >> data.ServerUri;
        *this >> data.EndpointUrl;
        DeserializeContainer(*this, data.LocaleIds);
        *this >> data.ActualSessionTimeout;
        *this >> data.MaxResponseMessageSize;
        *this >> data.ClientConnectionTime;
        *this >> data.ClientLastContactTime;
        *this >> data.CurrentSubscriptionsCount;
        *this >> data.CurrentMonitoredItemsCount;
        *this >> data.CurrentPublishRequestsInQueue;
        *this >> data.TotalRequestCount;
        *this >> data.UnauthorizedRequestCount;
        *this >> data.ReadCount;
        *this >> data.HistoryReadCount;
        *this >> data.WriteCount;
        *this >> data.HistoryUpdateCount;
        *this >> data.CallCount;
        *this >> data.CreateMonitoredItemsCount;
        *this >> data.ModifyMonitoredItemsCount;
        *this >> data.SetMonitoringModeCount;
        *this >> data.SetTriggeringCount;
        *this >> data.DeleteMonitoredItemsCount;
        *this >> data.CreateSubscriptionCount;
        *this >> data.ModifySubscriptionCount;
        *this >> data.SetPublishingModeCount;
        *this >> data.PublishCount;
        *this >> data.RepublishCount;
        *this >> data.TransferSubscriptionsCount;
        *this >> data.DeleteSubscriptionsCount;
        *this >> data.AddNodesCount;
        *this >> data.AddReferencesCount;
        *this >> data.DeleteNodesCount;
        *this >> data.DeleteReferencesCount;
        *this >> data.BrowseCount;
        *this >> data.BrowseNextCount;
        *this >> data.TranslateBrowsePathsToNodeIdsCount;
        *this >> data.QueryFirstCount;
        *this >> data.QueryNextCount;
        *this >> data.RegisterNodesCount;
        *this >> data.UnregisterNodesCount;
    }


    template<>
    void DataDeserializer::Deserialize<SessionSecurityDiagnosticsDataType>(SessionSecurityDiagnosticsDataType& data)
    {
        *this >> data.SessionId;
        *this >> data.ClientUserIdOfSession;
        DeserializeContainer(*this, data.ClientUserIdHistory);
        *this >> data.AuthenticationMechanism;
        *this >> data.Encoding;
        *this >> data.TransportProtocol;
        *this >> data.SecurityMode;
        *this >> data.SecurityPolicyUri;
        *this >> data.ClientCertificate;
    }


    template<>
    void DataDeserializer::Deserialize<ServiceCounterDataType>(ServiceCounterDataType& data)
    {
        *this >> data.TotalCount;
        *this >> data.ErrorCount;
    }


    template<>
    void DataDeserializer::Deserialize<StatusResult>(StatusResult& data)
    {
        *this >> data.StatusCode;
        *this >> data.DiagnosticInfo;
    }


    template<>
    void DataDeserializer::Deserialize<SubscriptionDiagnosticsDataType>(SubscriptionDiagnosticsDataType& data)
    {
        *this >> data.SessionId;
        *this >> data.SubscriptionId;
        *this >> data.Priority;
        *this >> data.PublishingInterval;
        *this >> data.MaxKeepAliveCount;
        *this >> data.MaxLifetimeCount;
        *this >> data.MaxNotificationsPerPublish;
        *this >> data.PublishingEnabled;
        *this >> data.ModifyCount;
        *this >> data.EnableCount;
        *this >> data.DisableCount;
        *this >> data.RepublishRequestCount;
        *this >> data.RepublishMessageRequestCount;
        *this >> data.RepublishMessageCount;
        *this >> data.TransferRequestCount;
        *this >> data.TransferredToAltClientCount;
        *this >> data.TransferredToSameClientCount;
        *this >> data.PublishRequestCount;
        *this >> data.DataChangeNotificationsCount;
        *this >> data.EventNotificationsCount;
        *this >> data.NotificationsCount;
        *this >> data.LatePublishRequestCount;
        *this >> data.CurrentKeepAliveCount;
        *this >> data.CurrentLifetimeCount;
        *this >> data.UnacknowledgedMessageCount;
        *this >> data.DiscardedMessageCount;
        *this >> data.MonitoredItemCount;
        *this >> data.DisabledMonitoredItemCount;
        *this >> data.MonitoringQueueOverflowCount;
        *this >> data.NextSequenceNumber;
        *this >> data.EventQueueOverFlowCount;
    }


    template<>
    void DataDeserializer::Deserialize<ModelChangeStructureDataType>(ModelChangeStructureDataType& data)
    {
        *this >> data.Affected;
        *this >> data.AffectedType;
        *this >> data.Verb;
    }


    template<>
    void DataDeserializer::Deserialize<SemanticChangeStructureDataType>(SemanticChangeStructureDataType& data)
    {
        *this >> data.Affected;
        *this >> data.AffectedType;
    }


    template<>
    void DataDeserializer::Deserialize<Range>(Range& data)
    {
        *this >> data.Low;
        *this >> data.High;
    }


    template<>
    void DataDeserializer::Deserialize<EUInformation>(EUInformation& data)
    {
        *this >> data.NamespaceUri;
        *this >> data.UnitId;
        *this >> data.DisplayName;
        *this >> data.Description;
    }


    template<>
    void DataDeserializer::Deserialize<ComplexNumberType>(ComplexNumberType& data)
    {
        *this >> data.Real;
        *this >> data.Imaginary;
    }


    template<>
    void DataDeserializer::Deserialize<DoubleComplexNumberType>(DoubleComplexNumberType& data)
    {
        *this >> data.Real;
        *this >> data.Imaginary;
    }


    template<>
    void DataDeserializer::Deserialize<AxisInformation>(AxisInformation& data)
    {
        *this >> data.EngineeringUnits;
        *this >> data.EURange;
        *this >> data.Title;
        *this >> data.AxisScaleType;
        DeserializeContainer(*this, data.AxisSteps);
    }


    template<>
    void DataDeserializer::Deserialize<XVType>(XVType& data)
    {
        *this >> data.X;
        *this >> data.Value;
    }


    template<>
    void DataDeserializer::Deserialize<ProgramDiagnosticDataType>(ProgramDiagnosticDataType& data)
    {
        *this >> data.CreateSessionId;
        *this >> data.CreateClientName;
        *this >> data.InvocationCreationTime;
        *this >> data.LastTransitionTime;
        *this >> data.LastMethodCall;
        *this >> data.LastMethodSessionId;
        DeserializeContainer(*this, data.LastMethodInputArguments);
        DeserializeContainer(*this, data.LastMethodOutputArguments);
        *this >> data.LastMethodCallTime;
        *this >> data.LastMethodReturnStatus;
    }


    template<>
    void DataDeserializer::Deserialize<Annotation>(Annotation& data)
    {
        *this >> data.Message;
        *this >> data.UserName;
        *this >> data.AnnotationTime;
    }


   }

} // namespace
    
