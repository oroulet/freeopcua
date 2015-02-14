import struct

import  generate_protocol as gp


class CodeGenerator(object):
    def __init__(self, model, output):
        self.model = model
        self.output_path = output
        self.indent = "    "
        self.iidx = 0 #indent index

    def run(self):
        self.output_file = open(self.output_path, "w")
        self.make_header()
        for enum in self.model.enums:
            self.generate_enum_code(enum)
        for struct in self.model.structs:
            self.generate_struct_code(struct)

    def write(self, *args):
        args = list(args)
        args.insert(0, self.indent * self.iidx)
        line = " ".join(args) 
        self.output_file.write(line[1:] + "\n")

    def make_header(self):
        self.write("'''")
        self.write("Autogenerate code from xml spec")
        self.write("'''")
        self.write("")
        self.write("import struct")
        self.write("")
        self.write("import types")
        self.write("")
        self.write("")

    def generate_enum_code(self, enum):
        self.write("")
        self.write("class {}(object):".format(enum.name))
        self.iidx = 1
        self.write("def __init__(self):")
        for val in enum.values:
            self.write("        self.{} = {}".format(val.name, val.value))
        self.iidx = 0

    def generate_struct_code(self, obj):
        self.write("")
        self.iidx = 0
        self.write("class {}(object):".format(obj.name))
        self.iidx += 1
        self.write("def __init__(self):")
        self.iidx += 1
        for field in obj.fields:
            self.write("self.{} = {}".format(field.name, "[]" if field.length else "None"))
        self.iidx = 1

        #serialize code
        self.write("")
        self.write("def to_binary(self):")
        self.iidx += 1
        self.write("b = []")
        for field in obj.fields:
            if field.switchfield:
                if field.switchvalue:
                    self.write("if self.{}: self.{} |= (value << {})".format(field.name, field.switchfield, field.switchvalue))
                else:
                    bit = obj.bits[field.switchfield]
                    self.write("if self.{}: self.{} |= (value << {})".format(field.name, bit.container, bit.idx))
        iidx = self.iidx
        for field in obj.fields:
            self.iidx = iidx
            switch = ""
            if field.switchfield:
                self.write("if self.{}: ".format(field.name))
                self.iidx += 1
            if field.length:
                self.write("b.append(struct.pack('!i', len(self.{})))".format(field.name))
                self.write("for i in {}:".format(field.name))
                self.iidx += 1
            if field.is_struct():
                self.write("b.append(self.{}.to_binary())".format(field.name))
            else:
                self.write("b.append(struct.pack('!{}', self.{}))".format(self.to_fmt(field.uatype), field.name))
            if field.length:
                self.iidx -= 1
        self.iidx = 2
        self.write("return b"".join()")
        self.write("")

        #deserialize
        self.write("def from_binary(self, data):")
        self.iidx += 1 
        iidx = self.iidx
        for field in obj.fields:
            self.iidx = iidx
            if field.switchfield:
                if field.switchvalue:
                    self.write("if self.{} & (1 << {}):".format(field.switchfield, field.switchvalue))
                else:
                    bit = obj.bits[field.switchfield]
                    self.write("if self.{} & (1 << {}):".format(bit.container, bit.idx))
                self.iidx += 1
            if field.length:
                self.write("length = struct.unpack('!i', data[:4])")
                self.write("data = data[4:]")
                self.write("if length != -1:")
                self.iidx += 1
                self.write("for i in range(0, length):")
                self.iidx += 1
            if field.is_struct():
                self.write("data = self.{}.from_binary(data)".format(field.name))
            else:
                fmt = self.to_fmt(field.uatype)
                size = struct.calcsize(fmt)
                self.write("self.{} = struct.unpack({}, data[:{}])".format(field.name, fmt, size))
                self.write("data = data[{}:]".format(size))
        self.iidx = 3
        self.write("return data")
        self.iix = 0


    def to_fmt(self, uatype):
        if uatype == "String":
            return "s"
        elif uatype == "CharArray":
            return "s"
        elif uatype == "Char":
            return "c"
        elif uatype == "SByte":
            return "B"
        elif uatype == "Int8":
            return "b"
        elif uatype == "Int16":
            return "h"
        elif uatype == "Int32":
            return "i"
        elif uatype == "Int64":
            return "q"
        elif uatype == "UInt8":
            return "B"
        elif uatype == "UInt16":
            return "H"
        elif uatype == "UInt32":
            return "I"
        elif uatype == "UInt64":
            return "Q"
        elif uatype == "DateTime":
            return "d"
        elif uatype == "Boolean":
            return "?"
        elif uatype == "Double":
            return "d"
        elif uatype == "Float":
            return "f"
        elif uatype == "Byte":
            return "c"
        else:
            print("Error unknown uatype: ", uatype)




def fix_names(model):
    for s in model.enums:
        for f in s.values:
            if f.name == "None":
                f.name = "None_"


if __name__ == "__main__":
    gp.IgnoredEnums = []
    gp.IgnoredStructs = []
    xmlpath = "Opc.Ua.Types.bsd"
    protocolpath = "protocol_auto.py"
    p = gp.Parser(xmlpath)
    model = p.parse()
    gp.add_encoding_field(model)
    gp.remove_duplicates(model)
    fix_names(model)
    c = CodeGenerator(model, protocolpath)
    c.run()


