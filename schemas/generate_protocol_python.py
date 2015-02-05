from  generate_protocol import Parser, add_encoding_field


class CodeGenerator(object):
    def __init__(self, model, output):
        self.model = model
        self.output_path = output

    def run(self):
        self.output_file = open(self.output_path, "w")
        self.make_header()
        for enum in self.model.enums:
            self.generate_enum_code(enum)
        for struct in self.model.structs:
            self.generate_struct_code(struct)

    def write(self, *args):
        self.output_file.write(" ".join(args) + "\n")

    def make_header(self):
        self.write("'''")
        self.write("Autogenerate code from xml spec")
        self.write("'''")
        self.write("import struct")
        self.write("")
        self.write("")

    def generate_enum_code(self, enum):
        self.write("")
        self.write("class {}(object):".format(enum.name))
        self.write("    def __init__(self):")
        for val in enum.values:
            self.write("        self.{} = {}".format(val.name, val.value))

    def generate_struct_code(self, obj):
        self.write("")
        self.write("class {}(object):".format(obj.name))
        self.write("    def __init__(self):")
        for field in obj.fields:
            self.write("        self.{} = {}".format(field.name, "[]" if field.length else "None"))

        for bitname, bit in obj.bits.items():
            self.write("")
            self.write("    @property")
            self.write("    def {}(self):".format(bitname))
            self.write("        return self.{} & (1 << {})".format(bit.container, bit.idx))
            self.write("")
            self.write("    @{}.setter".format(bitname))
            self.write("    def {}(self, value):".format(bitname))
            self.write("        return self.{} | (value << {})".format(bit.container, bit.idx))
        self.write("")
        self.write("    def to_binary(self):")
        self.write("        b = bytes()")
        for field in obj.fields:
            switch = ""
            if field.switchfield:
                switch = "if self.{} ".format(field.switchfield)
                
            else:
                if field.length:
                    self.write("        {}b += struct.pack('!{}', len(self.{})".format(switch, self.to_fmt(obj.get_field(field.length).uatype), field.name))
                if field.is_struct():
                    self.write("        {}b += self.{}.to_binary()".format(switch, field.name))
                else:
                    self.write("        b += struct.pack('!{}', self.{})".format(self.to_fmt(field.uatype), field.name))
        self.write("        return b")


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
        elif uatype == "ByteString":
            return "c"
        elif uatype == "Byte":
            return "c"
        else:
            print("Error unknown uatype: ", uatype)







if __name__ == "__main__":

    xmlpath = "Opc.Ua.Types.bsd"
    protocolpath = "protocol_auto.py"
    p = Parser(xmlpath)
    model = p.parse()
    add_encoding_field(model)
    c = CodeGenerator(model, protocolpath)
    c.run()


