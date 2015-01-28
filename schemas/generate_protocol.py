"""
Generate address space c++ code from xml file specification
"""
import sys

import xml.etree.ElementTree as ET

from IPython import embed


IgnoredStructs = ["Variant", "QualifiedName", "DataValue"]

class Bit(object):
    def __init__(self):
        self.name = None
        self.idx = None
        self.container = None
    def __str__(self):
        return "(Bit: {}, {}, {})".format(self.name, self.container, self.idx)
    __repr__ = __str__

class Struct(object):
    def __init__(self):
        self.name = None
        self.basetype = None
        self.doc = None
        self.fields = []
        self.bits = {}

class Field(object):
    def __init__(self):
        self.name = None
        self.type = None
        self.length = None
        self.sourcetype = None
        self.switchfield = None
        self.switchvalue = None
        self.sourcetype = None
        self.bitlength = 1 

class Enum(object):
    def __init__(self):
        self.name = None
        self.ctype = None
        self.values = []
        self.doc = None

class EnumValue(object):
    def __init__(self):
        self.name = None
        self.value = None

class CodeGenerator(object):
    def __init__(self, input_path, h_path, cpp_path):
        self.input_path = input_path
        self.h_path = h_path
        self.cpp_path = cpp_path
        self.h_file = None
        self.cpp_file = None

    def run(self):
        sys.stderr.write("Generating header file {} and C++ file {} for XML file {}".format(self.h_path, self.cpp_path, self.input_path) + "\n")
        self.h_file = open(self.h_path, "w")
        self.cpp_file = open(self.cpp_path, "w")

        self.make_header_h()
        self.make_header_cpp()

        tree = ET.parse(xmlpath)
        root = tree.getroot()
        for child in root:
            tag = child.tag[40:]
            if tag == "StructuredType":
                struct = self.parse_struct(child)
                if not struct.name.endswith("Node") and not struct.name in IgnoredStructs:
                    self.make_struct_h(struct)
                    self.make_struct_cpp(struct)
            elif tag == "EnumeratedType":
                enum = self.parse_enum(child)
                self.make_enum_h(enum)
            else:
                print("Not implemented node type: " + tag + "\n")

        self.make_footer_h()
        self.make_footer_cpp()

    def parse_struct(self, child):
        tag = child.tag[40:]
        struct = Struct()
        for key, val in child.attrib.items():
            if key == "Name":
                struct.name = val
            elif key == "BaseType":
                struct.basetype = val
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
                        field.type = val
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
                        print("Uknown field item: ",struct.name,  key) 
                struct.fields.append(field)
            elif tag == "Documentation":
                struct.doc = val
            else:
                print("Uknown tag: ", tag)
        struct = self.add_encoding_field(struct)
        return struct
    
    def add_encoding_field(self, struct):
        newfields = []
        container = None
        idx = 0
        for field in struct.fields:
            if field.type in ("opc:UInt6", "ua:NodeIdType"):
                container = field.name
                idx = 6
            if field.type == "opc:Bit":
                if not container or idx > 7:
                    container = "Encoding"
                    idx = 0
                    f = Field()
                    f.name = "Encoding"
                    f.type = "opc:UInt8"
                    newfields.append(f)

                nb = field.bitlength
                for i in range(0, nb):
                    b = Bit()
                    b.name  = field.name
                    b.idx = idx
                    b.container = container
                    idx += 1
                    struct.bits[b.name] = b
            else:
                newfields.append(field)
        struct.fields = newfields
        return struct

    def make_struct_h(self, struct):
        self.writecode_h("")
        if struct.doc: self.writecode_h("    //", struct.doc)
        self.writecode_h("    struct %s \n    {""" % struct.name)
        for field in struct.fields: 
            self.writecode_h("        ", self.to_cpp_type(field), field.name + ";" )
        self.writecode_h("    };")

    def make_raw_size(self, struct):
        self.writecode_cpp("")
        self.writecode_cpp("    template<>")
        self.writecode_cpp("    std::size_t RawSize(const {}& data)".format(struct.name))
        self.writecode_cpp("    {")
        tmp = ["RawSizeContainer(data.{})".format(field.name) if field.length else  "RawSize(data.{})".format(field.name) for field in struct.fields]
        tmp = " + ".join(tmp)
        self.writecode_cpp("        return " + tmp + ";")
        self.writecode_cpp("    }")
        self.writecode_cpp("")

    def make_serialize(self, struct):
        #FIXME: handle encoding
        #FIXME: handle containers
        self.writecode_cpp("")
        self.writecode_cpp("    template<>")
        self.writecode_cpp("    void DataSerializer::Serialize<{}>(const {}& data)".format(struct.name, struct.name))
        self.writecode_cpp("    {")
        for field in struct.fields:
            switch = ""
            if field.switchfield:
                if field.switchvalue:
                    switch = "if (data.{}) & (1<<({})) ".format(field.switchfield, field.switchvalue)
                else:
                    container = struct.bits[field.switchfield].container
                    idx = struct.bits[field.switchfield].idx
                    switch = "if (data.{}) & (1<<({})) ".format(container, idx)
            if field.length:
                self.writecode_cpp("        {}SerializeContainer(*this, data.{});".format(switch, field.name))
            else:
                self.writecode_cpp("        {}*this << data.{};".format(switch, field.name))
        self.writecode_cpp("    }")
        self.writecode_cpp("")
 

    def make_struct_cpp(self, struct):
        self.make_raw_size(struct)
        self.make_serialize(struct)
 


    def parse_enum(self, child):
        tag = child.tag[40:]
        enum = Enum()
        for k, v in child.items():
            if k == "Name":
                enum.name = v
            elif k == "LengthInBits":
                enum.ctype = v
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

    def make_enum_h(self, enum):
        self.writecode_h("\n")
        if enum.doc: self.writecode_h("    //", enum.doc)
        self.writecode_h("    enum %s : %s\n    {" % (enum.name, self.to_enum_type(enum.ctype)))
        for val in enum.values:
            self.writecode_h("        ", val.name, "=", val.value + ",")
        self.writecode_h("    };")



    def to_cpp_type(self, field):
        ty = ""
        if field.type == "opc:String":
            ty = "std::string"
        elif field.type == "opc:CharArray":
            ty = "std::string"
        elif field.type == "opc:Char":
            ty = "char"
        elif field.type == "opc:SByte":
            ty = "char"
        elif field.type == "opc:Int8":
            ty = "int8_t"
        elif field.type == "opc:Int16":
            ty = "int16_t"
        elif field.type == "opc:Int32":
            ty = "int32_t"
        elif field.type == "opc:Int64":
            ty = "int64_t"
        elif field.type == "opc:UInt8":
            ty = "uint8_t"
        elif field.type == "opc:UInt16":
            ty = "uint16_t"
        elif field.type == "opc:UInt32":
            ty = "uint32_t"
        elif field.type == "opc:UInt64":
            ty = "uint64_t"
        elif field.type == "opc:DateTime":
            ty = "DateTime"
        elif field.type == "opc:Boolean":
            ty = "bool"
        elif field.type == "opc:Double":
            ty = "double"
        elif field.type == "opc:Float":
            ty = "float"
        elif field.type == "opc:ByteString":
            ty = "ByteString"
        elif field.type == "opc:Byte":
            ty = "uint8_t"
        elif field.type.startswith("tns:"):
            ty = field.type[4:]
        elif field.type.startswith("ua:"):
            ty = field.type[3:]
        else:
            print("Error unknown type: ", field.type)
            ty = field.type
        if field.length:
            ty = "std::vector<{}>".format(ty)
        return ty


    def to_enum_type(self, val):
        if val == "6":
            val = "8"
        return "uint{}_t".format(val)

    def writecode_h(self, *args):
        self.h_file.write(" ".join(args) + "\n")

    def writecode_cpp(self, *args):
        self.cpp_file.write(" ".join(args) + "\n")

    def make_header_h(self, ):
        self.writecode_h('''
// DO NOT EDIT THIS FILE!
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

#include <opc/ua/protocol/attribute_ids.h>
#include <opc/ua/protocol/data_value.h>
#include <opc/ua/protocol/types.h>
#include <opc/ua/protocol/variant.h>
#include <opc/ua/protocol/strings.h>
#include <opc/ua/protocol/node_classes.h>
#include <opc/ua/protocol/variable_access_level.h>
#include <map>
#include <bitset>

namespace OcpUa
{
    ''' )

    def make_footer_h(self):
        self.writecode_h('''
   }

} // namespace
    ''')

    def make_header_cpp(self, ):
        self.writecode_h('''
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

#include <opc/ua/protocol/binary/stream.h>
#include <opc/ua/protocol/subscriptions.h>
#include <opc/ua/protocol/monitored_items.h>

namespace OpcUa
{   ''')

    def make_footer_cpp(self):
        self.writecode_h('''
   }

} // namespace
    ''')



if __name__ == "__main__":
    xmlpath = "Opc.Ua.Types.bsd"
    hpath = "test_protocol.h"
    cpppath = "test_protocol.cpp"
    c = CodeGenerator(xmlpath, hpath, cpppath)
    c.run()


