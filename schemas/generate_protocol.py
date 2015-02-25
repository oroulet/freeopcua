"""
Generate address space c++ code from xml file specification
"""
import sys
from copy import copy

import xml.etree.ElementTree as ET

from IPython import embed

NeedOverride = []
NeedConstructor = ["RelativePathElement", "ReadValueId", "OpenSecureChannelParameters", "UserIdentityToken", "RequestHeader", "ResponseHeader", "ReadParameters", "UserIdentityToken", "BrowseDescription", "ReferenceDescription", "CreateSubscriptionParameters", "PublishResult", "NotificationMessage", "SetPublishingModeParameters"]
IgnoredEnums = ["IdType", "NodeIdType"]
#we want to implement som struct by hand, to make better interface or simply because they are too complicated 
IgnoredStructs = ["NodeId", "ExpandedNodeId", "Variant", "QualifiedName", "DataValue", "LocalizedText"]#, "ExtensionObject"]
#by default we split requests and respons in header and parameters, but some are so simple we do not split them
NoSplitStruct = ["GetEndpointsResponse", "CloseSessionRequest", "AddNodesResponse", "BrowseResponse", "HistoryReadResponse", "HistoryUpdateResponse", "RegisterServerResponse", "CloseSecureChannelRequest", "CloseSecureChannelResponse", "CloseSessionRequest", "CloseSessionResponse", "UnregisterNodesResponse", "MonitoredItemModifyRequest", "MonitoredItemsCreateRequest"]
OverrideTypes = {"AttributeId": "AttributeID",  "ResultMask": "BrowseResultMask", "NodeClassMask": "NodeClass", "AccessLevel": "VariableAccessLevel", "UserAccessLevel": "VariableAccessLevel", "NotificationData": "NotificationData"}
OverrideNames = {"RequestHeader": "Header", "ResponseHeader": "Header", "StatusCode": "Status", "NodesToRead": "AttributesToRead"} # "MonitoringMode": "Mode",, "NotificationMessage": "Notification", "NodeIdType": "Type"}

"""
def rename_field(s):
    tmp = re.sub(r'([a-z])([A-Z])', r'\1 \2', string) 
    return tmp[1:].join("")
    r = []
    tmp = []
    for c in s:
        if c.isupper():
            r.append(tmp.join(""))
            tmp = []
        else:
            tmp.append(c)
            r.append(' ')
        l = not c.isupper()
        r.append(c)
    return ''.join(r)
"""

class Bit(object):
    def __init__(self):
        self.name = None
        self.idx = None
        self.container = None
        self.length = 1

    def __str__(self):
        return "(Bit: {}, container:{}, idx:{})".format(self.name, self.container, self.idx)
    __repr__ = __str__

class Struct(object):
    def __init__(self):
        self.name = None
        self.basetype = None
        self.doc = None
        self.fields = []
        self.bits = {}
        self.needconstructor = None
        self.needoverride = False
        self.children = []
        self.parents = []

    def is_extension_object(self):
        if "ExtensionObject" in self.parents:
            return True
        return False

    def get_field(self, name):
        for f in self.fields:
            if f.name == name:
                return f
        raise Exception("field not found: " + name)
    
    def __str__(self):
        return "Struct {}:{}".format(self.name, self.basetype)

    __repr__ = __str__


class Field(object):
    def __init__(self):
        self.name = None
        self.uatype = None
        self.length = None
        self.sourcetype = None
        self.switchfield = None
        self.switchvalue = None
        self.bitlength = 1 

    def __str__(self):
        return "Field {}({})".format(self.name, self.uatype)

    __repr__ = __str__

    def is_native_type(self):
        if self.uatype in ("Char", "CharArray", "SByte", "Int8", "Int16", "Int32", "Int64", "UInt8", "UInt16", "UInt32", "UInt64", "Boolean", "Double", "Float", "Byte", "String"):
            return True
        return False

    def get_ctype(self):
        if self.uatype == "String":
            ty = "std::string"
        elif self.uatype == "CharArray":
            ty = "std::string"
        elif self.uatype == "Char":
            ty = "char"
        elif self.uatype == "SByte":
            ty = "char"
        elif self.uatype == "Int8":
            ty = "int8_t"
        elif self.uatype == "Int16":
            ty = "int16_t"
        elif self.uatype == "Int32":
            ty = "int32_t"
        elif self.uatype == "Int64":
            ty = "int64_t"
        elif self.uatype == "UInt8":
            ty = "uint8_t"
        elif self.uatype == "UInt16":
            ty = "uint16_t"
        elif self.uatype == "UInt32":
            ty = "uint32_t"
        elif self.uatype == "UInt64":
            ty = "uint64_t"
        elif self.uatype == "DateTime":
            ty = "OpcUa::DateTime"
        elif self.uatype == "Boolean":
            ty = "bool"
        elif self.uatype == "Double":
            ty = "double"
        elif self.uatype == "Float":
            ty = "float"
        elif self.uatype == "ByteString":
            ty = "OpcUa::ByteString"
        elif self.uatype == "Byte":
            ty = "uint8_t"
        else:
            ty = "OpcUa::" + self.uatype
        if self.length:
            ty = "std::vector<{}>".format(ty)
        return ty

class Enum(object):
    def __init__(self):
        self.name = None
        self.uatype = None
        self.values = []
        self.doc = None

    def get_ctype(self):
        return "uint{}_t".format(self.uatype)

class EnumValue(object):
    def __init__(self):
        self.name = None
        self.value = None

class Model(object):
    def __init__(self):
        self.structs = []
        self.enums = []
        self.struct_list = []
        self.enum_list = []

    def get_struct(self, name):
        for struct in self.structs:
            if name == struct.name:
                return struct
        raise Exception("No struct named: " + str(name))

    def get_enum(self, name):
        for s in self.enums:
            if name == s.name:
                return s
        raise Exception("No enum named: " + str(name))




def reorder_structs(model):
    types = IgnoredStructs + IgnoredEnums + ["Bit", "Char", "CharArray", "Guid", "SByte", "Int8", "Int16", "Int32", "Int64", "UInt8", "UInt16", "UInt32", "UInt64", "DateTime", "Boolean", "Double", "Float", "ByteString", "Byte", "StatusCode", "DiagnosticInfo", "String", "AttributeID"] + [enum.name for enum in model.enums] + ["VariableAccessLevel"]
    waiting = {}
    newstructs = []
    for s in model.structs:
        types.append(s.name)
        s.waitingfor = []
        ok = True
        for f in s.fields:
            if f.uatype not in types:
                if f.uatype in waiting.keys():
                    waiting[f.uatype].append(s)
                    s.waitingfor.append(f.uatype)
                else:
                    waiting[f.uatype] = [s]
                    s.waitingfor.append(f.uatype)
                ok = False
        if ok:
            newstructs.append(s)
            waitings = waiting.pop(s.name, None)
            if waitings:
                for s2 in waitings:
                    s2.waitingfor.remove(s.name)
                    if not s2.waitingfor:
                        newstructs.append(s2)
    if len(model.structs) != len(newstructs):
        print("Error while reordering structs, some structs could not be reinserted, had {} structs, we now have {} structs".format(len(model.structs), len(newstructs)))
        s1 = set(model.structs)
        s2 = set(newstructs)
        rest = s1 -s2
        print("Variant" in types)
        for s in s1-s2:
            print("{} is waiting for: {}".format(s, s.waitingfor))
        #print(s1 -s2)
        #print(waiting)
    model.structs = newstructs

def override_types(model):
    for struct in model.structs:
        for field in struct.fields:
            if field.name in OverrideTypes.keys():
                field.uatype = OverrideTypes[field.name]

def remove_duplicates(model):
    for struct in model.structs:
        fields = []
        names = []
        for field in struct.fields:
            if field.name not in names:
                names.append(field.name)
                fields.append(field)
        struct.fields = fields
    
def add_encoding_field(model):
    for struct in model.structs:
        newfields = []
        container = None
        idx = 0
        for field in struct.fields:
            if field.uatype in ("UInt6", "NodeIdType"):
                container = field.name
                b = Bit()
                b.name = field.name
                b.idx = 0
                b.container = container
                b.length = 6 
                idx = b.length
                struct.bits[b.name] = b

            if field.uatype == "Bit":
                if not container or idx > 7:
                    container = "Encoding"
                    idx = 0
                    f = Field()
                    f.sourcetype = field.sourcetype
                    f.name = "Encoding"
                    f.uatype = "UInt8"
                    newfields.append(f)

                b = Bit()
                b.name = field.name
                b.idx = idx
                b.container = container
                b.length = field.bitlength
                idx += field.bitlength
                struct.bits[b.name] = b
            else:
                newfields.append(field)
        struct.fields = newfields

def remove_vector_length(model):
    for struct in model.structs:
        new = []
        for field in struct.fields:
            if not field.name.startswith("NoOf"):
                new.append(field)
        struct.fields = new

def remove_body_length(model):
    for struct in model.structs:
        new = []
        for field in struct.fields:
            if not field.name == "BodyLength":
                new.append(field)
        struct.fields = new

#def remove_extensionobject_fields(model):
    #for obj in model.structs:
        #if obj.name.endswith("Request") or obj.name.endswith("Response"):
            #obj.fields = [el for el in obj.fields if el.name not in ("TypeId", "Body", "Encoding")]

def split_requests(model):
    structs = []
    for struct in model.structs:
        structtype = None
        if struct.name.endswith("Request"):
            structtype = "Request"
        elif struct.name.endswith("Response"):
            structtype = "Response"
        if structtype:
            struct.needconstructor = True
            field = Field()
            field.name = "TypeId"
            field.uatype = "NodeId"
            struct.fields.insert(0, field)

        if structtype and not struct.name in NoSplitStruct:
            paramstruct = Struct()
            if structtype == "Request":
                basename = struct.name.replace("Request", "") + "Parameters"
                paramstruct.name = basename 
            else:
                basename = struct.name.replace("Response", "") + "Result"
                paramstruct.name = basename 
            paramstruct.fields = struct.fields[2:]
            paramstruct.bits = struct.bits

            struct.fields = struct.fields[:2]
            #struct.bits = {}
            structs.append(paramstruct)

            typeid = Field()
            typeid.name = "Parameters" 
            typeid.uatype = paramstruct.name 
            struct.fields.append(typeid)
        structs.append(struct)
    model.structs = structs


class Parser(object):
    def __init__(self, path):
        self.path = path
        self.model = None

    def parse(self):
        print("Parsing: ", self.path)
        self.model = Model()
        tree = ET.parse(self.path)
        root = tree.getroot()
        self.add_extension_object()
        for child in root:
            tag = child.tag[40:]
            if tag == "StructuredType":
                struct = self.parse_struct(child)
                if struct.name != "ExtensionObject":
                    self.model.structs.append(struct)
                    self.model.struct_list.append(struct.name)
            elif tag == "EnumeratedType":
                enum = self.parse_enum(child)
                self.model.enums.append(enum)
                self.model.enum_list.append(enum.name)
            #else:
                #print("Not implemented node type: " + tag + "\n")
        return self.model

    def add_extension_object(self):
        obj = Struct()
        obj.name = "ExtensionObject"
        f = Field()
        f.name = "TypeId"
        f.uatype = "NodeId"
        obj.fields.append(f)
        f = Field()
        f.name = "BinaryBody"
        f.uatype = "Bit"
        obj.fields.append(f)
        f = Field()
        f.name = "XmlBody"
        f.uatype = "Bit"
        obj.fields.append(f)
        f = Field()
        f.name = "Body"
        f.uatype = "ByteString"
        f.switchfield = "BinaryBody"
        obj.fields.append(f)
        self.model.struct_list.append(obj.name)

        self.model.structs.append(obj)

    def parse_struct(self, child):
        tag = child.tag[40:]
        struct = Struct()
        for key, val in child.attrib.items():
            if key == "Name":
                struct.name = val
            elif key == "BaseType":
                if ":" in val:
                    prefix, val = val.split(":")
                struct.basetype = val
                tmp = struct
                while tmp.basetype:
                    struct.parents.append(tmp.basetype)
                    tmp = self.model.get_struct(tmp.basetype)
                #self.add_basetype_members(struct)
            else:
                print("Error unknown key: ", key)
        for el in child:
            tag = el.tag[40:]
            if tag == "Field":
                field = Field()
                for key, val in el.attrib.items():
                    if key == "Name":
                        field.name = val
                    elif key == "TypeName":
                        field.uatype = val.split(":")[1]
                    elif key == "LengthField":
                        field.length = val
                    elif key == "SourceType":
                        field.sourcetype = val
                    elif key == "SwitchField":
                        field.switchfield = val
                    elif key == "SwitchValue":
                        field.switchvalue = val
                    elif key == "Length":
                        field.bitlength = int(val)
                    else:
                        print("Uknown field item: ", struct.name, key) 

                struct.fields.append(field)
            elif tag == "Documentation":
                struct.doc = el.text
            else:
                print("Uknown tag: ", tag)

        return struct

    def parse_enum(self, child):
        tag = child.tag[40:]
        enum = Enum()
        for k, v in child.items():
            if k == "Name":
                enum.name = v
            elif k == "LengthInBits":
                enum.uatype = v
            else:
                print("Unknown attr for enum: ", k)
        for el in child:
            tag = el.tag[40:]
            if tag == "EnumeratedValue":
                ev = EnumValue()
                for k, v in el.attrib.items():
                    if k == "Name":
                        ev.name = v
                    elif k == "Value":
                        ev.value = v
                    else:
                        print("Uknown field attrib: ", k) 
                enum.values.append(ev)
            elif tag == "Documentation":
                enum.doc = el.text
            else:
                print("Unknown enum tag: ", tag)
        return enum


#"def reorder_extobjects(model):
    #ext = model.get_struct("ExtensionObject")
    #print(ext)
    #typeid = ext.fields[4]
    #ext.fields.remove(typeid)
    #ext.fields.insert(0, typeid)

def add_basetype_members(model):
    for struct in model.structs:
        if not struct.basetype:
            continue
        base = model.get_struct(struct.basetype)
        if struct.basetype == "ExtensionObject" and len(struct.fields) != 0:
            #if struc
            #for f in base.fields:
                #if f.name == "TypeId":
                    #f2 = copy(f)
                    #f2.switchfield = None
                    #struct.fields.insert(0, f2)
                    #break
            continue
        for name, bit in base.bits.items():
            struct.bits[name] = bit
        for idx, field in enumerate(base.fields):
            #if field.name == "Body" and idx != ( len(base.fields) -1 ):
                #print("Field is names Body", struct.name, field.name)
                #field.name = "BodyLength"
                #field.uatype = "Int32"
                #field.length = None
                #print("Field is names Body 2", struct.name, field.name)
            #HACK EXTENSIONOBJECT
            #if base.name == "ExtensionObject":
                #continue
                #if field.uatype == "Bit":
                    #continue
                #if field.name == "Body":
                    #continue
                #if field.name == "TypeId":
                    #field.switchfield = None
            #END HACK
            field = copy(field)
            if not field.sourcetype:
                field.sourcetype = base.name
            struct.fields.insert(idx, field)




class CodeGenerator(object):
    def __init__(self, model, h_path, enum_path, size_path, ser_path, deser_path, const_path):
        self.model = model 
        self.h_path = h_path
        self.enum_path = enum_path
        self.rawsize_path = size_path
        self.serialize_path = ser_path
        self.deserialize_path = deser_path
        self.constructors_path = const_path
        self.h_file = None
        self.cpp_file = None
        self.structs = []

    def run(self):
        #sys.stderr.write("Generating header file {} and C++ files for XML file {}".format(self.h_path, self.input_path) + "\n")
        self.h_file = open(self.h_path, "w")
        self.enum_file = open(self.enum_path, "w")
        self.rawsize_file = open(self.rawsize_path, "w")
        self.serialize_file = open(self.serialize_path, "w")
        self.deserialize_file = open(self.deserialize_path, "w")
        self.constructors_file = open(self.constructors_path, "w")

        self.make_header_h()
        self.make_header_enum()
        self.make_header_rawsize()
        self.make_header_serialize()
        self.make_header_deserialize()
        self.make_header_constructors()
        
        for enum in self.model.enums:
            if not enum.name in IgnoredEnums:
                self.make_enum_h(enum)
                self.make_struct_ser(enum)
        for struct in self.model.structs:
            self.rename_fields(struct)
            if struct.name in NeedConstructor:
                struct.needconstructor = True
            if struct.name in NeedOverride:
                struct.needoverride = True
            if not struct.name.endswith("Node") and not struct.name.endswith("NodeId") and not struct.name in IgnoredStructs:
                self.make_struct_h(struct)
                self.make_struct_ser(struct)
                self.make_constructors(struct)

        self.make_footer_h()
        self.make_footer_enum()
        self.make_footer_rawsize()
        self.make_footer_serialize()
        self.make_footer_deserialize()
        self.make_footer_constructors()

    def rename_fields(self, struct):
        ##gcc does not want member with same name as a type
        for field in struct.fields:
            if field.name in OverrideNames:
                field.name = OverrideNames[field.name]
            #else:
                #print("Error name same as type: ", field.name, field.get_ctype(), field.uatype)

    def make_struct_h(self, struct):
        self.write_h("")
        if struct.doc: self.write_h("    //", struct.doc)
        name = struct.name
        base = ""
        if struct.needoverride:
            name = "_" + struct.name
        #if struct.basetype:
            #base = " : public " + struct.basetype
        self.write_h("    struct %s %s\n    {""" % (name, base))
        for field in struct.fields: 
            #if field.sourcetype:
                #continue
            
            if field.get_ctype() == "OpcUa::" + struct.name:
                #we have a problem selv referensing struct
                self.write_h("         std::shared_ptr<{}> {};".format(field.get_ctype(), field.name))
            else:
                self.write_h("        " , field.get_ctype(), field.name + ";")
        if struct.needconstructor:
            self.write_h("\n        ", struct.name + "();")
        self.write_h("    };")

    def make_raw_size(self, struct):
        self.write_size("")
        self.write_size("    template<>")
        self.write_size("    std::size_t RawSize<{}>(const {}& data)".format(struct.name, struct.name))
        self.write_size("    {")

        if type(struct) == Enum:
            self.write_size("        return sizeof({});".format(struct.get_ctype()))
        else:
            self.write_size("        size_t size = 0;")
            for field in struct.fields:
                switch = ""
                if field.switchfield:
                    if field.switchvalue:
                        switch = "if ((data.{}) & (1<<({}))) ".format(field.switchfield, field.switchvalue)
                    else:
                        container = struct.bits[field.switchfield].container
                        idx = struct.bits[field.switchfield].idx
                        switch = "if ((data.{}) & (1<<({}))) ".format(container, idx)
                prefix = ""
                if field.get_ctype() == struct.name:
                    prefix = "*"
                if field.length:
                    self.write_size("        {}size += RawSizeContainer({}data.{});".format(switch, prefix, field.name))
                else:
                    self.write_size("        {}size += RawSize({}data.{});".format(switch, prefix, field.name))
            self.write_size("        return size;")
        self.write_size("    }")
        self.write_size("")

    def make_serialize(self, struct):
        self.write_ser("")
        self.write_ser("    template<>")
        self.write_ser("    void DataSerializer::Serialize<{}>(const {}& data)".format(struct.name, struct.name))
        self.write_ser("    {")
        if type(struct) == Enum:
            self.write_ser("        *this << static_cast<{}>(data);".format(struct.get_ctype()))
        else:
            for idx, field in enumerate(struct.fields):
                if field.name == "Body" and idx != (len(struct.fields) - 1):
                    self.write_ser("        int32_t bodylength = RawSize(data) - RawSize(data.Encoding);")
                    self.write_ser("        if ((data.Encoding) & (1<<(0))) bodylength -= RawSize(data.TypeId);")
                    self.write_ser("        *this << bodylength;")
                    continue

                switch = ""
                if field.switchfield:
                    if field.switchvalue:
                        switch = "if ((data.{}) & (1<<({}))) ".format(field.switchfield, field.switchvalue)
                    else:
                        container = struct.bits[field.switchfield].container
                        idx = struct.bits[field.switchfield].idx
                        switch = "if ((data.{}) & (1<<({}))) ".format(container, idx)
                prefix = ""
                if field.get_ctype() == struct.name:
                    prefix = "*"
                if field.length:
                    self.write_ser("        {}SerializeContainer(*this, {}data.{});".format(switch, prefix, field.name))
                else:
                    self.write_ser("        {}*this << {}data.{};".format(switch, prefix, field.name))
        self.write_ser("    }")
        self.write_ser("")

    def make_deserialize(self, struct):
        self.write_deser("")
        self.write_deser("    template<>")
        self.write_deser("    void DataDeserializer::Deserialize<{}>({}& data)".format(struct.name, struct.name))
        self.write_deser("    {")
        if type(struct) == Enum:
            self.write_deser("        {} tmp;".format(struct.get_ctype()))
            self.write_deser("        *this >> tmp;")
            #self.write_deser("        data = static_cast<{}>(tmp);".format(struct.get_ctype()))
            self.write_deser("        data = static_cast<{}>(tmp);".format(struct.name))
        else:
            for idx, field in enumerate(struct.fields):
                if field.name == "Body" and idx != (len(struct.fields) - 1):
                    self.write_deser("        int32_t tmp; //Not used")
                    self.write_deser("        *this >> tmp;")
                    continue
                switch = ""
                if field.switchfield:
                    if field.switchvalue:
                        switch = "if ((data.{}) & (1>>({}))) ".format(field.switchfield, field.switchvalue)
                    else:
                        container = struct.bits[field.switchfield].container
                        idx = struct.bits[field.switchfield].idx
                        switch = "if ((data.{}) & (1>>({}))) ".format(container, idx)
                if field.length:
                    self.write_deser("        {}DeserializeContainer(*this, data.{});".format(switch, field.name))
                else:
                    self.write_deser("        {}*this >> data.{};".format(switch, field.name))
        self.write_deser("    }")
        self.write_deser("")
    
    def make_constructors(self, struct):
        if not struct.needconstructor:
            return
        self.write_const("")
        self.write_const("    ", struct.name + "::" + struct.name + "()")
        self.write_const("        : TypeId(ObjectId::" + struct.name +"_Encoding_DefaultBinary)")
        self.write_const("    {")
        self.write_const("    }")

    def make_struct_ser(self, struct):
        self.make_raw_size(struct)
        self.make_serialize(struct)
        self.make_deserialize(struct)

    def make_enum_h(self, enum):
        self.write_enum("\n")
        if enum.doc: self.write_enum("    //", enum.doc)
        self.write_enum("    enum class %s : %s\n    {" % (enum.name, self.to_enum_type(enum.uatype)))
        for val in enum.values:
            self.write_enum("        ", val.name, "=", val.value + ",")
        self.write_enum("    };")
        #if enum.name.endswith("Mask"):
        self.write_enum("    inline {name} operator|({name} a, {name} b) {{return static_cast<{name}>(static_cast<{type}>(a) | static_cast<{type}>(b));}}".format(name=enum.name, type=self.to_enum_type(enum.uatype)))


    def to_enum_type(self, val):
        if val == "6":
            val = "8"
        return "uint{}_t".format(val)

    def write_h(self, *args):
        self.h_file.write(" ".join(args) + "\n")

    def write_enum(self, *args):
        self.enum_file.write(" ".join(args) + "\n")

    def write_ser(self, *args):
        self.serialize_file.write(" ".join(args) + "\n")

    def write_size(self, *args):
        self.rawsize_file.write(" ".join(args) + "\n")

    def write_deser(self, *args):
        self.deserialize_file.write(" ".join(args) + "\n")

    def write_const(self, *args):
        self.constructors_file.write(" ".join(args) + "\n")

    def make_header_h(self, ):
        self.write_h('''// DO NOT EDIT THIS FILE!
// It is automatically generated from opcfoundation.org schemas.
//

/// @brief Opc Ua Binary.
/// @license GNU LGPL
///
/// Distributed under the GNU LGPL License
/// (See accompanying file LICENSE or copy at
/// http://www.gnu.org/licenses/lgpl.html)
///

#pragma once

#include <opc/ua/protocol/enum_auto.h>
#include <opc/ua/protocol/variable_access_level.h>
#include <opc/ua/protocol/attribute_ids.h>
#include <opc/ua/protocol/nodeid.h>
//#include <opc/ua/protocol/extension_object.h>
#include <opc/ua/protocol/types.h>
#include <opc/ua/protocol/variant.h>
#include <opc/ua/protocol/data_value.h>

namespace OpcUa
{''')

    def make_footer_h(self):
        self.write_h('''
} // namespace
    ''')

    def make_header_enum(self, ):
        self.write_enum('''// DO NOT EDIT THIS FILE!
// It is automatically generated from opcfoundation.org schemas.
//

/// @brief Opc Ua Binary.
/// @license GNU LGPL
///
/// Distributed under the GNU LGPL License
/// (See accompanying file LICENSE or copy at
/// http://www.gnu.org/licenses/lgpl.html)
///

#pragma once

#include <cstdint>
#include <vector>
#include <string>

#include <opc/ua/protocol/status_codes.h>

namespace OpcUa
{
  struct DiagnosticInfo;
''')

    def make_footer_enum(self):
        self.write_enum('''
} // namespace
    ''')

    def make_header_rawsize(self, ):
        self.write_size('''// DO NOT EDIT THIS FILE!
// It is automatically generated from opcfoundation.org schemas.
//

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
#include <opc/ua/protocol/protocol.h>

#include <opc/ua/protocol/binary/stream.h>

namespace OpcUa
{   
    namespace Binary
    {''')

    def make_footer_rawsize(self):
        self.write_size('''
   }

} // namespace
    ''')



    def make_header_serialize(self, ):
        self.write_ser('''// DO NOT EDIT THIS FILE!
// It is automatically generated from opcfoundation.org schemas.
//

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
#include <opc/ua/protocol/protocol.h>

#include <opc/ua/protocol/binary/stream.h>

namespace OpcUa
{   
    namespace Binary
    {''')

    def make_footer_serialize(self):
        self.write_ser('''
   }

} // namespace
    ''')

    def make_header_deserialize(self, ):
        self.write_deser('''// DO NOT EDIT THIS FILE!
// It is automatically generated from opcfoundation.org schemas.
//

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
#include <opc/ua/protocol/protocol.h>

#include <opc/ua/protocol/binary/stream.h>

namespace OpcUa
{   
    namespace Binary
    {''')

    def make_footer_deserialize(self):
        self.write_deser('''
   }

} // namespace
    ''')


    def make_header_constructors(self, ):
        self.write_const('''
/// @author Olivier Roulet-Dubonnet 
/// @email olivier@sintef.no 
/// @brief Opc Ua Binary. 
/// @license GNU LGPL
///
/// Distributed under the GNU LGPL License
/// (See accompanying file LICENSE or copy at
/// http://www.gnu.org/licenses/lgpl.html)
///

#include <opc/ua/protocol/protocol_auto.h>
#include <opc/ua/protocol/object_ids.h>

namespace OpcUa
{   ''')

    def make_footer_constructors(self):
        self.write_const('''
} // namespace
    ''')




if __name__ == "__main__":
    xmlpath = "Opc.Ua.Types.bsd"
    hpath = "../include/opc/ua/protocol/protocol_auto.h"
    enumpath = "../include/opc/ua/protocol/enum_auto.h"
    serializerpath = "../src/protocol/serialize_auto.cpp"
    rawsizepath = "../src/protocol/rawsize_auto.cpp"
    deserializerpath = "../src/protocol/deserialize_auto.cpp"
    constructorspath = "../src/protocol/construtors_auto.cpp"
    p = Parser(xmlpath)
    model = p.parse()
    #Changes specific to our C++ implementation
    #reorder_extobjects(model)
    add_basetype_members(model)
    add_encoding_field(model)
    remove_vector_length(model)
    remove_body_length(model)
    remove_duplicates(model)
    override_types(model)
    split_requests(model)
    reorder_structs(model)

    c = CodeGenerator(model, hpath, enumpath, rawsizepath, serializerpath, deserializerpath, constructorspath)
    c.run()


