'''
Autogenerate code from xml spec
'''

import struct

import types



class NodeIdType(object):
    def __init__(self):
        self.TwoByte = 0
        self.FourByte = 1
        self.Numeric = 2
        self.String = 3
        self.Guid = 4
        self.ByteString = 5

class OpenFileMode(object):
    def __init__(self):
        self.Read = 1
        self.Write = 2
        self.EraseExisiting = 4
        self.Append = 8

class IdType(object):
    def __init__(self):
        self.Numeric = 0
        self.String = 1
        self.Guid = 2
        self.Opaque = 3

class NodeClass(object):
    def __init__(self):
        self.Unspecified = 0
        self.Object = 1
        self.Variable = 2
        self.Method = 4
        self.ObjectType = 8
        self.VariableType = 16
        self.ReferenceType = 32
        self.DataType = 64
        self.View = 128

class ApplicationType(object):
    def __init__(self):
        self.Server = 0
        self.Client = 1
        self.ClientAndServer = 2
        self.DiscoveryServer = 3

class MessageSecurityMode(object):
    def __init__(self):
        self.Invalid = 0
        self.None = 1
        self.Sign = 2
        self.SignAndEncrypt = 3

class UserTokenType(object):
    def __init__(self):
        self.Anonymous = 0
        self.UserName = 1
        self.Certificate = 2
        self.IssuedToken = 3

class SecurityTokenRequestType(object):
    def __init__(self):
        self.Issue = 0
        self.Renew = 1

class NodeAttributesMask(object):
    def __init__(self):
        self.None = 0
        self.AccessLevel = 1
        self.ArrayDimensions = 2
        self.BrowseName = 4
        self.ContainsNoLoops = 8
        self.DataType = 16
        self.Description = 32
        self.DisplayName = 64
        self.EventNotifier = 128
        self.Executable = 256
        self.Historizing = 512
        self.InverseName = 1024
        self.IsAbstract = 2048
        self.MinimumSamplingInterval = 4096
        self.NodeClass = 8192
        self.NodeId = 16384
        self.Symmetric = 32768
        self.UserAccessLevel = 65536
        self.UserExecutable = 131072
        self.UserWriteMask = 262144
        self.ValueRank = 524288
        self.WriteMask = 1048576
        self.Value = 2097152
        self.All = 4194303
        self.BaseNode = 1335396
        self.Object = 1335524
        self.ObjectTypeOrDataType = 1337444
        self.Variable = 4026999
        self.VariableType = 3958902
        self.Method = 1466724
        self.ReferenceType = 1371236
        self.View = 1335532

class AttributeWriteMask(object):
    def __init__(self):
        self.None = 0
        self.AccessLevel = 1
        self.ArrayDimensions = 2
        self.BrowseName = 4
        self.ContainsNoLoops = 8
        self.DataType = 16
        self.Description = 32
        self.DisplayName = 64
        self.EventNotifier = 128
        self.Executable = 256
        self.Historizing = 512
        self.InverseName = 1024
        self.IsAbstract = 2048
        self.MinimumSamplingInterval = 4096
        self.NodeClass = 8192
        self.NodeId = 16384
        self.Symmetric = 32768
        self.UserAccessLevel = 65536
        self.UserExecutable = 131072
        self.UserWriteMask = 262144
        self.ValueRank = 524288
        self.WriteMask = 1048576
        self.ValueForVariableType = 2097152

class BrowseDirection(object):
    def __init__(self):
        self.Forward = 0
        self.Inverse = 1
        self.Both = 2

class BrowseResultMask(object):
    def __init__(self):
        self.None = 0
        self.ReferenceTypeId = 1
        self.IsForward = 2
        self.NodeClass = 4
        self.BrowseName = 8
        self.DisplayName = 16
        self.TypeDefinition = 32
        self.All = 63
        self.ReferenceTypeInfo = 3
        self.TargetInfo = 60

class ComplianceLevel(object):
    def __init__(self):
        self.Untested = 0
        self.Partial = 1
        self.SelfTested = 2
        self.Certified = 3

class FilterOperator(object):
    def __init__(self):
        self.Equals = 0
        self.IsNull = 1
        self.GreaterThan = 2
        self.LessThan = 3
        self.GreaterThanOrEqual = 4
        self.LessThanOrEqual = 5
        self.Like = 6
        self.Not = 7
        self.Between = 8
        self.InList = 9
        self.And = 10
        self.Or = 11
        self.Cast = 12
        self.InView = 13
        self.OfType = 14
        self.RelatedTo = 15
        self.BitwiseAnd = 16
        self.BitwiseOr = 17

class TimestampsToReturn(object):
    def __init__(self):
        self.Source = 0
        self.Server = 1
        self.Both = 2
        self.Neither = 3

class HistoryUpdateType(object):
    def __init__(self):
        self.Insert = 1
        self.Replace = 2
        self.Update = 3
        self.Delete = 4

class PerformUpdateType(object):
    def __init__(self):
        self.Insert = 1
        self.Replace = 2
        self.Update = 3
        self.Remove = 4

class MonitoringMode(object):
    def __init__(self):
        self.Disabled = 0
        self.Sampling = 1
        self.Reporting = 2

class DataChangeTrigger(object):
    def __init__(self):
        self.Status = 0
        self.StatusValue = 1
        self.StatusValueTimestamp = 2

class DeadbandType(object):
    def __init__(self):
        self.None = 0
        self.Absolute = 1
        self.Percent = 2

class EnumeratedTestType(object):
    def __init__(self):
        self.Red = 1
        self.Yellow = 4
        self.Green = 5

class RedundancySupport(object):
    def __init__(self):
        self.None = 0
        self.Cold = 1
        self.Warm = 2
        self.Hot = 3
        self.Transparent = 4
        self.HotAndMirrored = 5

class ServerState(object):
    def __init__(self):
        self.Running = 0
        self.Failed = 1
        self.NoConfiguration = 2
        self.Suspended = 3
        self.Shutdown = 4
        self.Test = 5
        self.CommunicationFault = 6
        self.Unknown = 7

class ModelChangeStructureVerbMask(object):
    def __init__(self):
        self.NodeAdded = 1
        self.NodeDeleted = 2
        self.ReferenceAdded = 4
        self.ReferenceDeleted = 8
        self.DataTypeChanged = 16

class AxisScaleEnumeration(object):
    def __init__(self):
        self.Linear = 0
        self.Log = 1
        self.Ln = 2

class ExceptionDeviationFormat(object):
    def __init__(self):
        self.AbsoluteValue = 0
        self.PercentOfRange = 1
        self.PercentOfValue = 2
        self.PercentOfEURange = 3
        self.Unknown = 4

class XmlElement(object):
    def __init__(self):
        self.Length = None
        self.Value = []

    def to_binary(self):
        b = []
        b.append(struct.pack('!i', self.Length))
        b.append(struct.pack('!i', len(self.Value))
        b.append(struct.pack('!c', self.Value))
        return b.join()

    def from_binary(self, data):
        self.Length = struct.unpack(i, data[:4])
        data = data[4:]
        self.Value = struct.unpack(c, data[:1])
        data = data[1:]
        return data

class TwoByteNodeId(object):
    def __init__(self):
        self.Identifier = None

    def to_binary(self):
        b = []
        b.append(struct.pack('!c', self.Identifier))
        return b.join()

    def from_binary(self, data):
        self.Identifier = struct.unpack(c, data[:1])
        data = data[1:]
        return data

class FourByteNodeId(object):
    def __init__(self):
        self.NamespaceIndex = None
        self.Identifier = None

    def to_binary(self):
        b = []
        b.append(struct.pack('!c', self.NamespaceIndex))
        b.append(struct.pack('!H', self.Identifier))
        return b.join()

    def from_binary(self, data):
        self.NamespaceIndex = struct.unpack(c, data[:1])
        data = data[1:]
        self.Identifier = struct.unpack(H, data[:2])
        data = data[2:]
        return data

class NumericNodeId(object):
    def __init__(self):
        self.NamespaceIndex = None
        self.Identifier = None

    def to_binary(self):
        b = []
        b.append(struct.pack('!H', self.NamespaceIndex))
        b.append(struct.pack('!I', self.Identifier))
        return b.join()

    def from_binary(self, data):
        self.NamespaceIndex = struct.unpack(H, data[:2])
        data = data[2:]
        self.Identifier = struct.unpack(I, data[:4])
        data = data[4:]
        return data

class StringNodeId(object):
    def __init__(self):
        self.NamespaceIndex = None
        self.Identifier = None

    def to_binary(self):
        b = []
        b.append(struct.pack('!H', self.NamespaceIndex))
        b.append(struct.pack('!s', self.Identifier))
        return b.join()

    def from_binary(self, data):
        self.NamespaceIndex = struct.unpack(H, data[:2])
        data = data[2:]
        self.Identifier = struct.unpack(s, data[:1])
        data = data[1:]
        return data

class GuidNodeId(object):
    def __init__(self):
        self.NamespaceIndex = None
        self.Identifier = None

    def to_binary(self):
        b = []
        b.append(struct.pack('!H', self.NamespaceIndex))
        b.append(self.Identifier.to_binary())
        return b.join()

    def from_binary(self, data):
        self.NamespaceIndex = struct.unpack(H, data[:2])
        data = data[2:]
        data = self.Identifier.from_binary(data)
        return data

class ByteStringNodeId(object):
    def __init__(self):
        self.NamespaceIndex = None
        self.Identifier = None

    def to_binary(self):
        b = []
        b.append(struct.pack('!H', self.NamespaceIndex))
        b.append(self.Identifier.to_binary())
        return b.join()

    def from_binary(self, data):
        self.NamespaceIndex = struct.unpack(H, data[:2])
        data = data[2:]
        data = self.Identifier.from_binary(data)
        return data

class NodeId(object):
    def __init__(self):
        self.NodeIdType = None
        self.TwoByte = None
        self.FourByte = None
        self.Numeric = None
        self.String = None
        self.Guid = None
        self.ByteString = None

    def to_binary(self):
        b = []
        if self.TwoByte: self.NodeIdType |= (value << 0):
        if self.FourByte: self.NodeIdType |= (value << 1):
        if self.Numeric: self.NodeIdType |= (value << 2):
        if self.String: self.NodeIdType |= (value << 3):
        if self.Guid: self.NodeIdType |= (value << 4):
        if self.ByteString: self.NodeIdType |= (value << 5):
        b.append(self.NodeIdType.to_binary())
        if self.TwoByte: b.append(self.TwoByte.to_binary())
        if self.FourByte: b.append(self.FourByte.to_binary())
        if self.Numeric: b.append(self.Numeric.to_binary())
        if self.String: b.append(self.String.to_binary())
        if self.Guid: b.append(self.Guid.to_binary())
        if self.ByteString: b.append(self.ByteString.to_binary())
        return b.join()

    def from_binary(self, data):
        data = self.NodeIdType.from_binary(data)
        if self.NodeIdType & (1 << 0):
            data = self.TwoByte.from_binary(data)
        if self.NodeIdType & (1 << 1):
            data = self.FourByte.from_binary(data)
        if self.NodeIdType & (1 << 2):
            data = self.Numeric.from_binary(data)
        if self.NodeIdType & (1 << 3):
            data = self.String.from_binary(data)
        if self.NodeIdType & (1 << 4):
            data = self.Guid.from_binary(data)
        if self.NodeIdType & (1 << 5):
            data = self.ByteString.from_binary(data)
        return data

class ExpandedNodeId(object):
    def __init__(self):
        self.NodeIdType = None
        self.TwoByte = None
        self.FourByte = None
        self.Numeric = None
        self.String = None
        self.Guid = None
        self.ByteString = None
        self.NamespaceURI = None
        self.ServerIndex = None

    def to_binary(self):
        b = []
        if self.TwoByte: self.NodeIdType |= (value << 0):
        if self.FourByte: self.NodeIdType |= (value << 1):
        if self.Numeric: self.NodeIdType |= (value << 2):
        if self.String: self.NodeIdType |= (value << 3):
        if self.Guid: self.NodeIdType |= (value << 4):
        if self.ByteString: self.NodeIdType |= (value << 5):
        if self.NamespaceURI: self.NodeIdType |= (value << 7):
        if self.ServerIndex: self.NodeIdType |= (value << 6):
        b.append(self.NodeIdType.to_binary())
        if self.TwoByte: b.append(self.TwoByte.to_binary())
        if self.FourByte: b.append(self.FourByte.to_binary())
        if self.Numeric: b.append(self.Numeric.to_binary())
        if self.String: b.append(self.String.to_binary())
        if self.Guid: b.append(self.Guid.to_binary())
        if self.ByteString: b.append(self.ByteString.to_binary())
        if self.NamespaceURI: b.append(struct.pack('!s', self.NamespaceURI))
        if self.ServerIndex: b.append(struct.pack('!I', self.ServerIndex))
        return b.join()

    def from_binary(self, data):
        data = self.NodeIdType.from_binary(data)
        if self.NodeIdType & (1 << 0):
            data = self.TwoByte.from_binary(data)
        if self.NodeIdType & (1 << 1):
            data = self.FourByte.from_binary(data)
        if self.NodeIdType & (1 << 2):
            data = self.Numeric.from_binary(data)
        if self.NodeIdType & (1 << 3):
            data = self.String.from_binary(data)
        if self.NodeIdType & (1 << 4):
            data = self.Guid.from_binary(data)
        if self.NodeIdType & (1 << 5):
            data = self.ByteString.from_binary(data)
        if self.NodeIdType & (1 << 7):
            self.NamespaceURI = struct.unpack(s, data[:1])
            data = data[1:]
        if self.NodeIdType & (1 << 6):
            self.ServerIndex = struct.unpack(I, data[:4])
            data = data[4:]
        return data

class DiagnosticInfo(object):
    def __init__(self):
        self.Encoding = None
        self.SymbolicId = None
        self.NamespaceURI = None
        self.LocalizedText = None
        self.AdditionalInfo = None
        self.InnerStatusCode = None
        self.InnerDiagnosticInfo = None

    def to_binary(self):
        b = []
        if self.SymbolicId: self.Encoding |= (value << 0):
        if self.NamespaceURI: self.Encoding |= (value << 1):
        if self.LocalizedText: self.Encoding |= (value << 2):
        if self.AdditionalInfo: self.Encoding |= (value << 4):
        if self.InnerStatusCode: self.Encoding |= (value << 5):
        if self.InnerDiagnosticInfo: self.Encoding |= (value << 6):
        b.append(struct.pack('!B', self.Encoding))
        if self.SymbolicId: b.append(struct.pack('!i', self.SymbolicId))
        if self.NamespaceURI: b.append(struct.pack('!i', self.NamespaceURI))
        if self.LocalizedText: b.append(struct.pack('!i', self.LocalizedText))
        if self.AdditionalInfo: b.append(struct.pack('!s', self.AdditionalInfo))
        if self.InnerStatusCode: b.append(self.InnerStatusCode.to_binary())
        if self.InnerDiagnosticInfo: b.append(self.InnerDiagnosticInfo.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            self.SymbolicId = struct.unpack(i, data[:4])
            data = data[4:]
        if self.Encoding & (1 << 1):
            self.NamespaceURI = struct.unpack(i, data[:4])
            data = data[4:]
        if self.Encoding & (1 << 2):
            self.LocalizedText = struct.unpack(i, data[:4])
            data = data[4:]
        if self.Encoding & (1 << 4):
            self.AdditionalInfo = struct.unpack(s, data[:1])
            data = data[1:]
        if self.Encoding & (1 << 5):
            data = self.InnerStatusCode.from_binary(data)
        if self.Encoding & (1 << 6):
            data = self.InnerDiagnosticInfo.from_binary(data)
        return data

class QualifiedName(object):
    def __init__(self):
        self.NamespaceIndex = None
        self.Name = None

    def to_binary(self):
        b = []
        b.append(struct.pack('!i', self.NamespaceIndex))
        b.append(struct.pack('!s', self.Name))
        return b.join()

    def from_binary(self, data):
        self.NamespaceIndex = struct.unpack(i, data[:4])
        data = data[4:]
        self.Name = struct.unpack(s, data[:1])
        data = data[1:]
        return data

class LocalizedText(object):
    def __init__(self):
        self.Encoding = None
        self.Locale = None
        self.Text = None

    def to_binary(self):
        b = []
        if self.Locale: self.Encoding |= (value << 0):
        if self.Text: self.Encoding |= (value << 1):
        b.append(struct.pack('!B', self.Encoding))
        if self.Locale: b.append(struct.pack('!s', self.Locale))
        if self.Text: b.append(struct.pack('!s', self.Text))
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            self.Locale = struct.unpack(s, data[:1])
            data = data[1:]
        if self.Encoding & (1 << 1):
            self.Text = struct.unpack(s, data[:1])
            data = data[1:]
        return data

class DataValue(object):
    def __init__(self):
        self.Encoding = None
        self.Value = None
        self.StatusCode = None
        self.SourceTimestamp = None
        self.SourcePicoseconds = None
        self.ServerTimestamp = None
        self.ServerPicoseconds = None

    def to_binary(self):
        b = []
        if self.Value: self.Encoding |= (value << 0):
        if self.StatusCode: self.Encoding |= (value << 1):
        if self.SourceTimestamp: self.Encoding |= (value << 2):
        if self.SourcePicoseconds: self.Encoding |= (value << 3):
        if self.ServerTimestamp: self.Encoding |= (value << 4):
        if self.ServerPicoseconds: self.Encoding |= (value << 5):
        b.append(struct.pack('!B', self.Encoding))
        if self.Value: b.append(self.Value.to_binary())
        if self.StatusCode: b.append(self.StatusCode.to_binary())
        if self.SourceTimestamp: b.append(struct.pack('!d', self.SourceTimestamp))
        if self.SourcePicoseconds: b.append(struct.pack('!H', self.SourcePicoseconds))
        if self.ServerTimestamp: b.append(struct.pack('!d', self.ServerTimestamp))
        if self.ServerPicoseconds: b.append(struct.pack('!H', self.ServerPicoseconds))
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.Value.from_binary(data)
        if self.Encoding & (1 << 1):
            data = self.StatusCode.from_binary(data)
        if self.Encoding & (1 << 2):
            self.SourceTimestamp = struct.unpack(d, data[:8])
            data = data[8:]
        if self.Encoding & (1 << 3):
            self.SourcePicoseconds = struct.unpack(H, data[:2])
            data = data[2:]
        if self.Encoding & (1 << 4):
            self.ServerTimestamp = struct.unpack(d, data[:8])
            data = data[8:]
        if self.Encoding & (1 << 5):
            self.ServerPicoseconds = struct.unpack(H, data[:2])
            data = data[2:]
        return data

class ExtensionObject(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.Body = []

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(struct.pack('!i', len(self.Body))
        b.append(struct.pack('!c', self.Body))
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        self.Body = struct.unpack(c, data[:1])
        data = data[1:]
        return data

class Variant(object):
    def __init__(self):
        self.Encoding = None
        self.ArrayLength = None
        self.Boolean = []
        self.SByte = []
        self.Byte = []
        self.Int16 = []
        self.UInt16 = []
        self.Int32 = []
        self.UInt32 = []
        self.Int64 = []
        self.UInt64 = []
        self.Float = []
        self.Double = []
        self.String = []
        self.DateTime = []
        self.Guid = []
        self.ByteString = []
        self.XmlElement = []
        self.NodeId = []
        self.ExpandedNodeId = []
        self.StatusCode = []
        self.DiagnosticInfo = []
        self.QualifiedName = []
        self.LocalizedText = []
        self.ExtensionObject = []
        self.DataValue = []
        self.Variant = []

    def to_binary(self):
        b = []
        if self.ArrayLength: self.Encoding |= (value << 7):
        if self.Boolean: self.VariantType |= (value << 1):
        if self.SByte: self.VariantType |= (value << 2):
        if self.Byte: self.VariantType |= (value << 3):
        if self.Int16: self.VariantType |= (value << 4):
        if self.UInt16: self.VariantType |= (value << 5):
        if self.Int32: self.VariantType |= (value << 6):
        if self.UInt32: self.VariantType |= (value << 7):
        if self.Int64: self.VariantType |= (value << 8):
        if self.UInt64: self.VariantType |= (value << 9):
        if self.Float: self.VariantType |= (value << 10):
        if self.Double: self.VariantType |= (value << 11):
        if self.String: self.VariantType |= (value << 12):
        if self.DateTime: self.VariantType |= (value << 13):
        if self.Guid: self.VariantType |= (value << 14):
        if self.ByteString: self.VariantType |= (value << 15):
        if self.XmlElement: self.VariantType |= (value << 16):
        if self.NodeId: self.VariantType |= (value << 17):
        if self.ExpandedNodeId: self.VariantType |= (value << 18):
        if self.StatusCode: self.VariantType |= (value << 19):
        if self.DiagnosticInfo: self.VariantType |= (value << 20):
        if self.QualifiedName: self.VariantType |= (value << 21):
        if self.LocalizedText: self.VariantType |= (value << 22):
        if self.ExtensionObject: self.VariantType |= (value << 23):
        if self.DataValue: self.VariantType |= (value << 24):
        if self.Variant: self.VariantType |= (value << 25):
        b.append(struct.pack('!B', self.Encoding))
        if self.ArrayLength: b.append(struct.pack('!i', self.ArrayLength))
        if self.Boolean: b.append(struct.pack('!i', len(self.Boolean))
        if self.Boolean: b.append(struct.pack('!?', self.Boolean))
        if self.SByte: b.append(struct.pack('!i', len(self.SByte))
        if self.SByte: b.append(struct.pack('!B', self.SByte))
        if self.Byte: b.append(struct.pack('!i', len(self.Byte))
        if self.Byte: b.append(struct.pack('!c', self.Byte))
        if self.Int16: b.append(struct.pack('!i', len(self.Int16))
        if self.Int16: b.append(struct.pack('!h', self.Int16))
        if self.UInt16: b.append(struct.pack('!i', len(self.UInt16))
        if self.UInt16: b.append(struct.pack('!H', self.UInt16))
        if self.Int32: b.append(struct.pack('!i', len(self.Int32))
        if self.Int32: b.append(struct.pack('!i', self.Int32))
        if self.UInt32: b.append(struct.pack('!i', len(self.UInt32))
        if self.UInt32: b.append(struct.pack('!I', self.UInt32))
        if self.Int64: b.append(struct.pack('!i', len(self.Int64))
        if self.Int64: b.append(struct.pack('!q', self.Int64))
        if self.UInt64: b.append(struct.pack('!i', len(self.UInt64))
        if self.UInt64: b.append(struct.pack('!Q', self.UInt64))
        if self.Float: b.append(struct.pack('!i', len(self.Float))
        if self.Float: b.append(struct.pack('!f', self.Float))
        if self.Double: b.append(struct.pack('!i', len(self.Double))
        if self.Double: b.append(struct.pack('!d', self.Double))
        if self.String: b.append(struct.pack('!i', len(self.String))
        if self.String: b.append(self.String.to_binary())
        if self.DateTime: b.append(struct.pack('!i', len(self.DateTime))
        if self.DateTime: b.append(struct.pack('!d', self.DateTime))
        if self.Guid: b.append(struct.pack('!i', len(self.Guid))
        if self.Guid: b.append(self.Guid.to_binary())
        if self.ByteString: b.append(struct.pack('!i', len(self.ByteString))
        if self.ByteString: b.append(self.ByteString.to_binary())
        if self.XmlElement: b.append(struct.pack('!i', len(self.XmlElement))
        if self.XmlElement: b.append(self.XmlElement.to_binary())
        if self.NodeId: b.append(struct.pack('!i', len(self.NodeId))
        if self.NodeId: b.append(self.NodeId.to_binary())
        if self.ExpandedNodeId: b.append(struct.pack('!i', len(self.ExpandedNodeId))
        if self.ExpandedNodeId: b.append(self.ExpandedNodeId.to_binary())
        if self.StatusCode: b.append(struct.pack('!i', len(self.StatusCode))
        if self.StatusCode: b.append(self.StatusCode.to_binary())
        if self.DiagnosticInfo: b.append(struct.pack('!i', len(self.DiagnosticInfo))
        if self.DiagnosticInfo: b.append(self.DiagnosticInfo.to_binary())
        if self.QualifiedName: b.append(struct.pack('!i', len(self.QualifiedName))
        if self.QualifiedName: b.append(self.QualifiedName.to_binary())
        if self.LocalizedText: b.append(struct.pack('!i', len(self.LocalizedText))
        if self.LocalizedText: b.append(self.LocalizedText.to_binary())
        if self.ExtensionObject: b.append(struct.pack('!i', len(self.ExtensionObject))
        if self.ExtensionObject: b.append(self.ExtensionObject.to_binary())
        if self.DataValue: b.append(struct.pack('!i', len(self.DataValue))
        if self.DataValue: b.append(self.DataValue.to_binary())
        if self.Variant: b.append(struct.pack('!i', len(self.Variant))
        if self.Variant: b.append(self.Variant.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 7):
            self.ArrayLength = struct.unpack(i, data[:4])
            data = data[4:]
        if self.VariantType & (1 << 1):
            self.Boolean = struct.unpack(?, data[:1])
            data = data[1:]
        if self.VariantType & (1 << 2):
            self.SByte = struct.unpack(B, data[:1])
            data = data[1:]
        if self.VariantType & (1 << 3):
            self.Byte = struct.unpack(c, data[:1])
            data = data[1:]
        if self.VariantType & (1 << 4):
            self.Int16 = struct.unpack(h, data[:2])
            data = data[2:]
        if self.VariantType & (1 << 5):
            self.UInt16 = struct.unpack(H, data[:2])
            data = data[2:]
        if self.VariantType & (1 << 6):
            self.Int32 = struct.unpack(i, data[:4])
            data = data[4:]
        if self.VariantType & (1 << 7):
            self.UInt32 = struct.unpack(I, data[:4])
            data = data[4:]
        if self.VariantType & (1 << 8):
            self.Int64 = struct.unpack(q, data[:8])
            data = data[8:]
        if self.VariantType & (1 << 9):
            self.UInt64 = struct.unpack(Q, data[:8])
            data = data[8:]
        if self.VariantType & (1 << 10):
            self.Float = struct.unpack(f, data[:4])
            data = data[4:]
        if self.VariantType & (1 << 11):
            self.Double = struct.unpack(d, data[:8])
            data = data[8:]
        if self.VariantType & (1 << 12):
            data = self.String.from_binary(data)
        if self.VariantType & (1 << 13):
            self.DateTime = struct.unpack(d, data[:8])
            data = data[8:]
        if self.VariantType & (1 << 14):
            data = self.Guid.from_binary(data)
        if self.VariantType & (1 << 15):
            data = self.ByteString.from_binary(data)
        if self.VariantType & (1 << 16):
            data = self.XmlElement.from_binary(data)
        if self.VariantType & (1 << 17):
            data = self.NodeId.from_binary(data)
        if self.VariantType & (1 << 18):
            data = self.ExpandedNodeId.from_binary(data)
        if self.VariantType & (1 << 19):
            data = self.StatusCode.from_binary(data)
        if self.VariantType & (1 << 20):
            data = self.DiagnosticInfo.from_binary(data)
        if self.VariantType & (1 << 21):
            data = self.QualifiedName.from_binary(data)
        if self.VariantType & (1 << 22):
            data = self.LocalizedText.from_binary(data)
        if self.VariantType & (1 << 23):
            data = self.ExtensionObject.from_binary(data)
        if self.VariantType & (1 << 24):
            data = self.DataValue.from_binary(data)
        if self.VariantType & (1 << 25):
            data = self.Variant.from_binary(data)
        return data

class ReferenceNode(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.ReferenceTypeId = None
        self.IsInverse = None
        self.TargetId = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.ReferenceTypeId.to_binary())
        b.append(struct.pack('!?', self.IsInverse))
        b.append(self.TargetId.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.ReferenceTypeId.from_binary(data)
        self.IsInverse = struct.unpack(?, data[:1])
        data = data[1:]
        data = self.TargetId.from_binary(data)
        return data

class Node(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.NodeId = None
        self.NodeClass = None
        self.BrowseName = None
        self.DisplayName = None
        self.Description = None
        self.WriteMask = None
        self.UserWriteMask = None
        self.NoOfReferences = None
        self.References = []

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.NodeId.to_binary())
        b.append(self.NodeClass.to_binary())
        b.append(self.BrowseName.to_binary())
        b.append(self.DisplayName.to_binary())
        b.append(self.Description.to_binary())
        b.append(struct.pack('!I', self.WriteMask))
        b.append(struct.pack('!I', self.UserWriteMask))
        b.append(struct.pack('!i', self.NoOfReferences))
        b.append(struct.pack('!i', len(self.References))
        b.append(self.References.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.NodeId.from_binary(data)
        data = self.NodeClass.from_binary(data)
        data = self.BrowseName.from_binary(data)
        data = self.DisplayName.from_binary(data)
        data = self.Description.from_binary(data)
        self.WriteMask = struct.unpack(I, data[:4])
        data = data[4:]
        self.UserWriteMask = struct.unpack(I, data[:4])
        data = data[4:]
        self.NoOfReferences = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.References.from_binary(data)
        return data

class InstanceNode(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.NodeId = None
        self.NodeClass = None
        self.BrowseName = None
        self.DisplayName = None
        self.Description = None
        self.WriteMask = None
        self.UserWriteMask = None
        self.NoOfReferences = None
        self.References = []
        self.NodeId = None
        self.NodeClass = None
        self.BrowseName = None
        self.DisplayName = None
        self.Description = None
        self.WriteMask = None
        self.UserWriteMask = None
        self.NoOfReferences = None
        self.References = []

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.NodeId.to_binary())
        b.append(self.NodeClass.to_binary())
        b.append(self.BrowseName.to_binary())
        b.append(self.DisplayName.to_binary())
        b.append(self.Description.to_binary())
        b.append(struct.pack('!I', self.WriteMask))
        b.append(struct.pack('!I', self.UserWriteMask))
        b.append(struct.pack('!i', self.NoOfReferences))
        b.append(struct.pack('!i', len(self.References))
        b.append(self.References.to_binary())
        b.append(self.NodeId.to_binary())
        b.append(self.NodeClass.to_binary())
        b.append(self.BrowseName.to_binary())
        b.append(self.DisplayName.to_binary())
        b.append(self.Description.to_binary())
        b.append(struct.pack('!I', self.WriteMask))
        b.append(struct.pack('!I', self.UserWriteMask))
        b.append(struct.pack('!i', self.NoOfReferences))
        b.append(struct.pack('!i', len(self.References))
        b.append(self.References.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.NodeId.from_binary(data)
        data = self.NodeClass.from_binary(data)
        data = self.BrowseName.from_binary(data)
        data = self.DisplayName.from_binary(data)
        data = self.Description.from_binary(data)
        self.WriteMask = struct.unpack(I, data[:4])
        data = data[4:]
        self.UserWriteMask = struct.unpack(I, data[:4])
        data = data[4:]
        self.NoOfReferences = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.References.from_binary(data)
        data = self.NodeId.from_binary(data)
        data = self.NodeClass.from_binary(data)
        data = self.BrowseName.from_binary(data)
        data = self.DisplayName.from_binary(data)
        data = self.Description.from_binary(data)
        self.WriteMask = struct.unpack(I, data[:4])
        data = data[4:]
        self.UserWriteMask = struct.unpack(I, data[:4])
        data = data[4:]
        self.NoOfReferences = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.References.from_binary(data)
        return data

class TypeNode(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.NodeId = None
        self.NodeClass = None
        self.BrowseName = None
        self.DisplayName = None
        self.Description = None
        self.WriteMask = None
        self.UserWriteMask = None
        self.NoOfReferences = None
        self.References = []
        self.NodeId = None
        self.NodeClass = None
        self.BrowseName = None
        self.DisplayName = None
        self.Description = None
        self.WriteMask = None
        self.UserWriteMask = None
        self.NoOfReferences = None
        self.References = []

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.NodeId.to_binary())
        b.append(self.NodeClass.to_binary())
        b.append(self.BrowseName.to_binary())
        b.append(self.DisplayName.to_binary())
        b.append(self.Description.to_binary())
        b.append(struct.pack('!I', self.WriteMask))
        b.append(struct.pack('!I', self.UserWriteMask))
        b.append(struct.pack('!i', self.NoOfReferences))
        b.append(struct.pack('!i', len(self.References))
        b.append(self.References.to_binary())
        b.append(self.NodeId.to_binary())
        b.append(self.NodeClass.to_binary())
        b.append(self.BrowseName.to_binary())
        b.append(self.DisplayName.to_binary())
        b.append(self.Description.to_binary())
        b.append(struct.pack('!I', self.WriteMask))
        b.append(struct.pack('!I', self.UserWriteMask))
        b.append(struct.pack('!i', self.NoOfReferences))
        b.append(struct.pack('!i', len(self.References))
        b.append(self.References.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.NodeId.from_binary(data)
        data = self.NodeClass.from_binary(data)
        data = self.BrowseName.from_binary(data)
        data = self.DisplayName.from_binary(data)
        data = self.Description.from_binary(data)
        self.WriteMask = struct.unpack(I, data[:4])
        data = data[4:]
        self.UserWriteMask = struct.unpack(I, data[:4])
        data = data[4:]
        self.NoOfReferences = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.References.from_binary(data)
        data = self.NodeId.from_binary(data)
        data = self.NodeClass.from_binary(data)
        data = self.BrowseName.from_binary(data)
        data = self.DisplayName.from_binary(data)
        data = self.Description.from_binary(data)
        self.WriteMask = struct.unpack(I, data[:4])
        data = data[4:]
        self.UserWriteMask = struct.unpack(I, data[:4])
        data = data[4:]
        self.NoOfReferences = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.References.from_binary(data)
        return data

class ObjectNode(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.NodeId = None
        self.NodeClass = None
        self.BrowseName = None
        self.DisplayName = None
        self.Description = None
        self.WriteMask = None
        self.UserWriteMask = None
        self.NoOfReferences = None
        self.References = []
        self.NodeId = None
        self.NodeClass = None
        self.BrowseName = None
        self.DisplayName = None
        self.Description = None
        self.WriteMask = None
        self.UserWriteMask = None
        self.NoOfReferences = None
        self.References = []
        self.NodeId = None
        self.NodeClass = None
        self.BrowseName = None
        self.DisplayName = None
        self.Description = None
        self.WriteMask = None
        self.UserWriteMask = None
        self.NoOfReferences = None
        self.References = []
        self.EventNotifier = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.NodeId.to_binary())
        b.append(self.NodeClass.to_binary())
        b.append(self.BrowseName.to_binary())
        b.append(self.DisplayName.to_binary())
        b.append(self.Description.to_binary())
        b.append(struct.pack('!I', self.WriteMask))
        b.append(struct.pack('!I', self.UserWriteMask))
        b.append(struct.pack('!i', self.NoOfReferences))
        b.append(struct.pack('!i', len(self.References))
        b.append(self.References.to_binary())
        b.append(self.NodeId.to_binary())
        b.append(self.NodeClass.to_binary())
        b.append(self.BrowseName.to_binary())
        b.append(self.DisplayName.to_binary())
        b.append(self.Description.to_binary())
        b.append(struct.pack('!I', self.WriteMask))
        b.append(struct.pack('!I', self.UserWriteMask))
        b.append(struct.pack('!i', self.NoOfReferences))
        b.append(struct.pack('!i', len(self.References))
        b.append(self.References.to_binary())
        b.append(self.NodeId.to_binary())
        b.append(self.NodeClass.to_binary())
        b.append(self.BrowseName.to_binary())
        b.append(self.DisplayName.to_binary())
        b.append(self.Description.to_binary())
        b.append(struct.pack('!I', self.WriteMask))
        b.append(struct.pack('!I', self.UserWriteMask))
        b.append(struct.pack('!i', self.NoOfReferences))
        b.append(struct.pack('!i', len(self.References))
        b.append(self.References.to_binary())
        b.append(struct.pack('!c', self.EventNotifier))
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.NodeId.from_binary(data)
        data = self.NodeClass.from_binary(data)
        data = self.BrowseName.from_binary(data)
        data = self.DisplayName.from_binary(data)
        data = self.Description.from_binary(data)
        self.WriteMask = struct.unpack(I, data[:4])
        data = data[4:]
        self.UserWriteMask = struct.unpack(I, data[:4])
        data = data[4:]
        self.NoOfReferences = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.References.from_binary(data)
        data = self.NodeId.from_binary(data)
        data = self.NodeClass.from_binary(data)
        data = self.BrowseName.from_binary(data)
        data = self.DisplayName.from_binary(data)
        data = self.Description.from_binary(data)
        self.WriteMask = struct.unpack(I, data[:4])
        data = data[4:]
        self.UserWriteMask = struct.unpack(I, data[:4])
        data = data[4:]
        self.NoOfReferences = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.References.from_binary(data)
        data = self.NodeId.from_binary(data)
        data = self.NodeClass.from_binary(data)
        data = self.BrowseName.from_binary(data)
        data = self.DisplayName.from_binary(data)
        data = self.Description.from_binary(data)
        self.WriteMask = struct.unpack(I, data[:4])
        data = data[4:]
        self.UserWriteMask = struct.unpack(I, data[:4])
        data = data[4:]
        self.NoOfReferences = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.References.from_binary(data)
        self.EventNotifier = struct.unpack(c, data[:1])
        data = data[1:]
        return data

class ObjectTypeNode(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.NodeId = None
        self.NodeClass = None
        self.BrowseName = None
        self.DisplayName = None
        self.Description = None
        self.WriteMask = None
        self.UserWriteMask = None
        self.NoOfReferences = None
        self.References = []
        self.NodeId = None
        self.NodeClass = None
        self.BrowseName = None
        self.DisplayName = None
        self.Description = None
        self.WriteMask = None
        self.UserWriteMask = None
        self.NoOfReferences = None
        self.References = []
        self.NodeId = None
        self.NodeClass = None
        self.BrowseName = None
        self.DisplayName = None
        self.Description = None
        self.WriteMask = None
        self.UserWriteMask = None
        self.NoOfReferences = None
        self.References = []
        self.IsAbstract = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.NodeId.to_binary())
        b.append(self.NodeClass.to_binary())
        b.append(self.BrowseName.to_binary())
        b.append(self.DisplayName.to_binary())
        b.append(self.Description.to_binary())
        b.append(struct.pack('!I', self.WriteMask))
        b.append(struct.pack('!I', self.UserWriteMask))
        b.append(struct.pack('!i', self.NoOfReferences))
        b.append(struct.pack('!i', len(self.References))
        b.append(self.References.to_binary())
        b.append(self.NodeId.to_binary())
        b.append(self.NodeClass.to_binary())
        b.append(self.BrowseName.to_binary())
        b.append(self.DisplayName.to_binary())
        b.append(self.Description.to_binary())
        b.append(struct.pack('!I', self.WriteMask))
        b.append(struct.pack('!I', self.UserWriteMask))
        b.append(struct.pack('!i', self.NoOfReferences))
        b.append(struct.pack('!i', len(self.References))
        b.append(self.References.to_binary())
        b.append(self.NodeId.to_binary())
        b.append(self.NodeClass.to_binary())
        b.append(self.BrowseName.to_binary())
        b.append(self.DisplayName.to_binary())
        b.append(self.Description.to_binary())
        b.append(struct.pack('!I', self.WriteMask))
        b.append(struct.pack('!I', self.UserWriteMask))
        b.append(struct.pack('!i', self.NoOfReferences))
        b.append(struct.pack('!i', len(self.References))
        b.append(self.References.to_binary())
        b.append(struct.pack('!?', self.IsAbstract))
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.NodeId.from_binary(data)
        data = self.NodeClass.from_binary(data)
        data = self.BrowseName.from_binary(data)
        data = self.DisplayName.from_binary(data)
        data = self.Description.from_binary(data)
        self.WriteMask = struct.unpack(I, data[:4])
        data = data[4:]
        self.UserWriteMask = struct.unpack(I, data[:4])
        data = data[4:]
        self.NoOfReferences = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.References.from_binary(data)
        data = self.NodeId.from_binary(data)
        data = self.NodeClass.from_binary(data)
        data = self.BrowseName.from_binary(data)
        data = self.DisplayName.from_binary(data)
        data = self.Description.from_binary(data)
        self.WriteMask = struct.unpack(I, data[:4])
        data = data[4:]
        self.UserWriteMask = struct.unpack(I, data[:4])
        data = data[4:]
        self.NoOfReferences = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.References.from_binary(data)
        data = self.NodeId.from_binary(data)
        data = self.NodeClass.from_binary(data)
        data = self.BrowseName.from_binary(data)
        data = self.DisplayName.from_binary(data)
        data = self.Description.from_binary(data)
        self.WriteMask = struct.unpack(I, data[:4])
        data = data[4:]
        self.UserWriteMask = struct.unpack(I, data[:4])
        data = data[4:]
        self.NoOfReferences = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.References.from_binary(data)
        self.IsAbstract = struct.unpack(?, data[:1])
        data = data[1:]
        return data

class VariableNode(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.NodeId = None
        self.NodeClass = None
        self.BrowseName = None
        self.DisplayName = None
        self.Description = None
        self.WriteMask = None
        self.UserWriteMask = None
        self.NoOfReferences = None
        self.References = []
        self.NodeId = None
        self.NodeClass = None
        self.BrowseName = None
        self.DisplayName = None
        self.Description = None
        self.WriteMask = None
        self.UserWriteMask = None
        self.NoOfReferences = None
        self.References = []
        self.NodeId = None
        self.NodeClass = None
        self.BrowseName = None
        self.DisplayName = None
        self.Description = None
        self.WriteMask = None
        self.UserWriteMask = None
        self.NoOfReferences = None
        self.References = []
        self.Value = None
        self.DataType = None
        self.ValueRank = None
        self.NoOfArrayDimensions = None
        self.ArrayDimensions = []
        self.AccessLevel = None
        self.UserAccessLevel = None
        self.MinimumSamplingInterval = None
        self.Historizing = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.NodeId.to_binary())
        b.append(self.NodeClass.to_binary())
        b.append(self.BrowseName.to_binary())
        b.append(self.DisplayName.to_binary())
        b.append(self.Description.to_binary())
        b.append(struct.pack('!I', self.WriteMask))
        b.append(struct.pack('!I', self.UserWriteMask))
        b.append(struct.pack('!i', self.NoOfReferences))
        b.append(struct.pack('!i', len(self.References))
        b.append(self.References.to_binary())
        b.append(self.NodeId.to_binary())
        b.append(self.NodeClass.to_binary())
        b.append(self.BrowseName.to_binary())
        b.append(self.DisplayName.to_binary())
        b.append(self.Description.to_binary())
        b.append(struct.pack('!I', self.WriteMask))
        b.append(struct.pack('!I', self.UserWriteMask))
        b.append(struct.pack('!i', self.NoOfReferences))
        b.append(struct.pack('!i', len(self.References))
        b.append(self.References.to_binary())
        b.append(self.NodeId.to_binary())
        b.append(self.NodeClass.to_binary())
        b.append(self.BrowseName.to_binary())
        b.append(self.DisplayName.to_binary())
        b.append(self.Description.to_binary())
        b.append(struct.pack('!I', self.WriteMask))
        b.append(struct.pack('!I', self.UserWriteMask))
        b.append(struct.pack('!i', self.NoOfReferences))
        b.append(struct.pack('!i', len(self.References))
        b.append(self.References.to_binary())
        b.append(self.Value.to_binary())
        b.append(self.DataType.to_binary())
        b.append(struct.pack('!i', self.ValueRank))
        b.append(struct.pack('!i', self.NoOfArrayDimensions))
        b.append(struct.pack('!i', len(self.ArrayDimensions))
        b.append(struct.pack('!I', self.ArrayDimensions))
        b.append(struct.pack('!c', self.AccessLevel))
        b.append(struct.pack('!c', self.UserAccessLevel))
        b.append(struct.pack('!d', self.MinimumSamplingInterval))
        b.append(struct.pack('!?', self.Historizing))
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.NodeId.from_binary(data)
        data = self.NodeClass.from_binary(data)
        data = self.BrowseName.from_binary(data)
        data = self.DisplayName.from_binary(data)
        data = self.Description.from_binary(data)
        self.WriteMask = struct.unpack(I, data[:4])
        data = data[4:]
        self.UserWriteMask = struct.unpack(I, data[:4])
        data = data[4:]
        self.NoOfReferences = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.References.from_binary(data)
        data = self.NodeId.from_binary(data)
        data = self.NodeClass.from_binary(data)
        data = self.BrowseName.from_binary(data)
        data = self.DisplayName.from_binary(data)
        data = self.Description.from_binary(data)
        self.WriteMask = struct.unpack(I, data[:4])
        data = data[4:]
        self.UserWriteMask = struct.unpack(I, data[:4])
        data = data[4:]
        self.NoOfReferences = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.References.from_binary(data)
        data = self.NodeId.from_binary(data)
        data = self.NodeClass.from_binary(data)
        data = self.BrowseName.from_binary(data)
        data = self.DisplayName.from_binary(data)
        data = self.Description.from_binary(data)
        self.WriteMask = struct.unpack(I, data[:4])
        data = data[4:]
        self.UserWriteMask = struct.unpack(I, data[:4])
        data = data[4:]
        self.NoOfReferences = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.References.from_binary(data)
        data = self.Value.from_binary(data)
        data = self.DataType.from_binary(data)
        self.ValueRank = struct.unpack(i, data[:4])
        data = data[4:]
        self.NoOfArrayDimensions = struct.unpack(i, data[:4])
        data = data[4:]
        self.ArrayDimensions = struct.unpack(I, data[:4])
        data = data[4:]
        self.AccessLevel = struct.unpack(c, data[:1])
        data = data[1:]
        self.UserAccessLevel = struct.unpack(c, data[:1])
        data = data[1:]
        self.MinimumSamplingInterval = struct.unpack(d, data[:8])
        data = data[8:]
        self.Historizing = struct.unpack(?, data[:1])
        data = data[1:]
        return data

class VariableTypeNode(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.NodeId = None
        self.NodeClass = None
        self.BrowseName = None
        self.DisplayName = None
        self.Description = None
        self.WriteMask = None
        self.UserWriteMask = None
        self.NoOfReferences = None
        self.References = []
        self.NodeId = None
        self.NodeClass = None
        self.BrowseName = None
        self.DisplayName = None
        self.Description = None
        self.WriteMask = None
        self.UserWriteMask = None
        self.NoOfReferences = None
        self.References = []
        self.NodeId = None
        self.NodeClass = None
        self.BrowseName = None
        self.DisplayName = None
        self.Description = None
        self.WriteMask = None
        self.UserWriteMask = None
        self.NoOfReferences = None
        self.References = []
        self.Value = None
        self.DataType = None
        self.ValueRank = None
        self.NoOfArrayDimensions = None
        self.ArrayDimensions = []
        self.IsAbstract = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.NodeId.to_binary())
        b.append(self.NodeClass.to_binary())
        b.append(self.BrowseName.to_binary())
        b.append(self.DisplayName.to_binary())
        b.append(self.Description.to_binary())
        b.append(struct.pack('!I', self.WriteMask))
        b.append(struct.pack('!I', self.UserWriteMask))
        b.append(struct.pack('!i', self.NoOfReferences))
        b.append(struct.pack('!i', len(self.References))
        b.append(self.References.to_binary())
        b.append(self.NodeId.to_binary())
        b.append(self.NodeClass.to_binary())
        b.append(self.BrowseName.to_binary())
        b.append(self.DisplayName.to_binary())
        b.append(self.Description.to_binary())
        b.append(struct.pack('!I', self.WriteMask))
        b.append(struct.pack('!I', self.UserWriteMask))
        b.append(struct.pack('!i', self.NoOfReferences))
        b.append(struct.pack('!i', len(self.References))
        b.append(self.References.to_binary())
        b.append(self.NodeId.to_binary())
        b.append(self.NodeClass.to_binary())
        b.append(self.BrowseName.to_binary())
        b.append(self.DisplayName.to_binary())
        b.append(self.Description.to_binary())
        b.append(struct.pack('!I', self.WriteMask))
        b.append(struct.pack('!I', self.UserWriteMask))
        b.append(struct.pack('!i', self.NoOfReferences))
        b.append(struct.pack('!i', len(self.References))
        b.append(self.References.to_binary())
        b.append(self.Value.to_binary())
        b.append(self.DataType.to_binary())
        b.append(struct.pack('!i', self.ValueRank))
        b.append(struct.pack('!i', self.NoOfArrayDimensions))
        b.append(struct.pack('!i', len(self.ArrayDimensions))
        b.append(struct.pack('!I', self.ArrayDimensions))
        b.append(struct.pack('!?', self.IsAbstract))
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.NodeId.from_binary(data)
        data = self.NodeClass.from_binary(data)
        data = self.BrowseName.from_binary(data)
        data = self.DisplayName.from_binary(data)
        data = self.Description.from_binary(data)
        self.WriteMask = struct.unpack(I, data[:4])
        data = data[4:]
        self.UserWriteMask = struct.unpack(I, data[:4])
        data = data[4:]
        self.NoOfReferences = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.References.from_binary(data)
        data = self.NodeId.from_binary(data)
        data = self.NodeClass.from_binary(data)
        data = self.BrowseName.from_binary(data)
        data = self.DisplayName.from_binary(data)
        data = self.Description.from_binary(data)
        self.WriteMask = struct.unpack(I, data[:4])
        data = data[4:]
        self.UserWriteMask = struct.unpack(I, data[:4])
        data = data[4:]
        self.NoOfReferences = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.References.from_binary(data)
        data = self.NodeId.from_binary(data)
        data = self.NodeClass.from_binary(data)
        data = self.BrowseName.from_binary(data)
        data = self.DisplayName.from_binary(data)
        data = self.Description.from_binary(data)
        self.WriteMask = struct.unpack(I, data[:4])
        data = data[4:]
        self.UserWriteMask = struct.unpack(I, data[:4])
        data = data[4:]
        self.NoOfReferences = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.References.from_binary(data)
        data = self.Value.from_binary(data)
        data = self.DataType.from_binary(data)
        self.ValueRank = struct.unpack(i, data[:4])
        data = data[4:]
        self.NoOfArrayDimensions = struct.unpack(i, data[:4])
        data = data[4:]
        self.ArrayDimensions = struct.unpack(I, data[:4])
        data = data[4:]
        self.IsAbstract = struct.unpack(?, data[:1])
        data = data[1:]
        return data

class ReferenceTypeNode(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.NodeId = None
        self.NodeClass = None
        self.BrowseName = None
        self.DisplayName = None
        self.Description = None
        self.WriteMask = None
        self.UserWriteMask = None
        self.NoOfReferences = None
        self.References = []
        self.NodeId = None
        self.NodeClass = None
        self.BrowseName = None
        self.DisplayName = None
        self.Description = None
        self.WriteMask = None
        self.UserWriteMask = None
        self.NoOfReferences = None
        self.References = []
        self.NodeId = None
        self.NodeClass = None
        self.BrowseName = None
        self.DisplayName = None
        self.Description = None
        self.WriteMask = None
        self.UserWriteMask = None
        self.NoOfReferences = None
        self.References = []
        self.IsAbstract = None
        self.Symmetric = None
        self.InverseName = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.NodeId.to_binary())
        b.append(self.NodeClass.to_binary())
        b.append(self.BrowseName.to_binary())
        b.append(self.DisplayName.to_binary())
        b.append(self.Description.to_binary())
        b.append(struct.pack('!I', self.WriteMask))
        b.append(struct.pack('!I', self.UserWriteMask))
        b.append(struct.pack('!i', self.NoOfReferences))
        b.append(struct.pack('!i', len(self.References))
        b.append(self.References.to_binary())
        b.append(self.NodeId.to_binary())
        b.append(self.NodeClass.to_binary())
        b.append(self.BrowseName.to_binary())
        b.append(self.DisplayName.to_binary())
        b.append(self.Description.to_binary())
        b.append(struct.pack('!I', self.WriteMask))
        b.append(struct.pack('!I', self.UserWriteMask))
        b.append(struct.pack('!i', self.NoOfReferences))
        b.append(struct.pack('!i', len(self.References))
        b.append(self.References.to_binary())
        b.append(self.NodeId.to_binary())
        b.append(self.NodeClass.to_binary())
        b.append(self.BrowseName.to_binary())
        b.append(self.DisplayName.to_binary())
        b.append(self.Description.to_binary())
        b.append(struct.pack('!I', self.WriteMask))
        b.append(struct.pack('!I', self.UserWriteMask))
        b.append(struct.pack('!i', self.NoOfReferences))
        b.append(struct.pack('!i', len(self.References))
        b.append(self.References.to_binary())
        b.append(struct.pack('!?', self.IsAbstract))
        b.append(struct.pack('!?', self.Symmetric))
        b.append(self.InverseName.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.NodeId.from_binary(data)
        data = self.NodeClass.from_binary(data)
        data = self.BrowseName.from_binary(data)
        data = self.DisplayName.from_binary(data)
        data = self.Description.from_binary(data)
        self.WriteMask = struct.unpack(I, data[:4])
        data = data[4:]
        self.UserWriteMask = struct.unpack(I, data[:4])
        data = data[4:]
        self.NoOfReferences = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.References.from_binary(data)
        data = self.NodeId.from_binary(data)
        data = self.NodeClass.from_binary(data)
        data = self.BrowseName.from_binary(data)
        data = self.DisplayName.from_binary(data)
        data = self.Description.from_binary(data)
        self.WriteMask = struct.unpack(I, data[:4])
        data = data[4:]
        self.UserWriteMask = struct.unpack(I, data[:4])
        data = data[4:]
        self.NoOfReferences = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.References.from_binary(data)
        data = self.NodeId.from_binary(data)
        data = self.NodeClass.from_binary(data)
        data = self.BrowseName.from_binary(data)
        data = self.DisplayName.from_binary(data)
        data = self.Description.from_binary(data)
        self.WriteMask = struct.unpack(I, data[:4])
        data = data[4:]
        self.UserWriteMask = struct.unpack(I, data[:4])
        data = data[4:]
        self.NoOfReferences = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.References.from_binary(data)
        self.IsAbstract = struct.unpack(?, data[:1])
        data = data[1:]
        self.Symmetric = struct.unpack(?, data[:1])
        data = data[1:]
        data = self.InverseName.from_binary(data)
        return data

class MethodNode(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.NodeId = None
        self.NodeClass = None
        self.BrowseName = None
        self.DisplayName = None
        self.Description = None
        self.WriteMask = None
        self.UserWriteMask = None
        self.NoOfReferences = None
        self.References = []
        self.NodeId = None
        self.NodeClass = None
        self.BrowseName = None
        self.DisplayName = None
        self.Description = None
        self.WriteMask = None
        self.UserWriteMask = None
        self.NoOfReferences = None
        self.References = []
        self.NodeId = None
        self.NodeClass = None
        self.BrowseName = None
        self.DisplayName = None
        self.Description = None
        self.WriteMask = None
        self.UserWriteMask = None
        self.NoOfReferences = None
        self.References = []
        self.Executable = None
        self.UserExecutable = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.NodeId.to_binary())
        b.append(self.NodeClass.to_binary())
        b.append(self.BrowseName.to_binary())
        b.append(self.DisplayName.to_binary())
        b.append(self.Description.to_binary())
        b.append(struct.pack('!I', self.WriteMask))
        b.append(struct.pack('!I', self.UserWriteMask))
        b.append(struct.pack('!i', self.NoOfReferences))
        b.append(struct.pack('!i', len(self.References))
        b.append(self.References.to_binary())
        b.append(self.NodeId.to_binary())
        b.append(self.NodeClass.to_binary())
        b.append(self.BrowseName.to_binary())
        b.append(self.DisplayName.to_binary())
        b.append(self.Description.to_binary())
        b.append(struct.pack('!I', self.WriteMask))
        b.append(struct.pack('!I', self.UserWriteMask))
        b.append(struct.pack('!i', self.NoOfReferences))
        b.append(struct.pack('!i', len(self.References))
        b.append(self.References.to_binary())
        b.append(self.NodeId.to_binary())
        b.append(self.NodeClass.to_binary())
        b.append(self.BrowseName.to_binary())
        b.append(self.DisplayName.to_binary())
        b.append(self.Description.to_binary())
        b.append(struct.pack('!I', self.WriteMask))
        b.append(struct.pack('!I', self.UserWriteMask))
        b.append(struct.pack('!i', self.NoOfReferences))
        b.append(struct.pack('!i', len(self.References))
        b.append(self.References.to_binary())
        b.append(struct.pack('!?', self.Executable))
        b.append(struct.pack('!?', self.UserExecutable))
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.NodeId.from_binary(data)
        data = self.NodeClass.from_binary(data)
        data = self.BrowseName.from_binary(data)
        data = self.DisplayName.from_binary(data)
        data = self.Description.from_binary(data)
        self.WriteMask = struct.unpack(I, data[:4])
        data = data[4:]
        self.UserWriteMask = struct.unpack(I, data[:4])
        data = data[4:]
        self.NoOfReferences = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.References.from_binary(data)
        data = self.NodeId.from_binary(data)
        data = self.NodeClass.from_binary(data)
        data = self.BrowseName.from_binary(data)
        data = self.DisplayName.from_binary(data)
        data = self.Description.from_binary(data)
        self.WriteMask = struct.unpack(I, data[:4])
        data = data[4:]
        self.UserWriteMask = struct.unpack(I, data[:4])
        data = data[4:]
        self.NoOfReferences = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.References.from_binary(data)
        data = self.NodeId.from_binary(data)
        data = self.NodeClass.from_binary(data)
        data = self.BrowseName.from_binary(data)
        data = self.DisplayName.from_binary(data)
        data = self.Description.from_binary(data)
        self.WriteMask = struct.unpack(I, data[:4])
        data = data[4:]
        self.UserWriteMask = struct.unpack(I, data[:4])
        data = data[4:]
        self.NoOfReferences = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.References.from_binary(data)
        self.Executable = struct.unpack(?, data[:1])
        data = data[1:]
        self.UserExecutable = struct.unpack(?, data[:1])
        data = data[1:]
        return data

class ViewNode(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.NodeId = None
        self.NodeClass = None
        self.BrowseName = None
        self.DisplayName = None
        self.Description = None
        self.WriteMask = None
        self.UserWriteMask = None
        self.NoOfReferences = None
        self.References = []
        self.NodeId = None
        self.NodeClass = None
        self.BrowseName = None
        self.DisplayName = None
        self.Description = None
        self.WriteMask = None
        self.UserWriteMask = None
        self.NoOfReferences = None
        self.References = []
        self.NodeId = None
        self.NodeClass = None
        self.BrowseName = None
        self.DisplayName = None
        self.Description = None
        self.WriteMask = None
        self.UserWriteMask = None
        self.NoOfReferences = None
        self.References = []
        self.ContainsNoLoops = None
        self.EventNotifier = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.NodeId.to_binary())
        b.append(self.NodeClass.to_binary())
        b.append(self.BrowseName.to_binary())
        b.append(self.DisplayName.to_binary())
        b.append(self.Description.to_binary())
        b.append(struct.pack('!I', self.WriteMask))
        b.append(struct.pack('!I', self.UserWriteMask))
        b.append(struct.pack('!i', self.NoOfReferences))
        b.append(struct.pack('!i', len(self.References))
        b.append(self.References.to_binary())
        b.append(self.NodeId.to_binary())
        b.append(self.NodeClass.to_binary())
        b.append(self.BrowseName.to_binary())
        b.append(self.DisplayName.to_binary())
        b.append(self.Description.to_binary())
        b.append(struct.pack('!I', self.WriteMask))
        b.append(struct.pack('!I', self.UserWriteMask))
        b.append(struct.pack('!i', self.NoOfReferences))
        b.append(struct.pack('!i', len(self.References))
        b.append(self.References.to_binary())
        b.append(self.NodeId.to_binary())
        b.append(self.NodeClass.to_binary())
        b.append(self.BrowseName.to_binary())
        b.append(self.DisplayName.to_binary())
        b.append(self.Description.to_binary())
        b.append(struct.pack('!I', self.WriteMask))
        b.append(struct.pack('!I', self.UserWriteMask))
        b.append(struct.pack('!i', self.NoOfReferences))
        b.append(struct.pack('!i', len(self.References))
        b.append(self.References.to_binary())
        b.append(struct.pack('!?', self.ContainsNoLoops))
        b.append(struct.pack('!c', self.EventNotifier))
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.NodeId.from_binary(data)
        data = self.NodeClass.from_binary(data)
        data = self.BrowseName.from_binary(data)
        data = self.DisplayName.from_binary(data)
        data = self.Description.from_binary(data)
        self.WriteMask = struct.unpack(I, data[:4])
        data = data[4:]
        self.UserWriteMask = struct.unpack(I, data[:4])
        data = data[4:]
        self.NoOfReferences = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.References.from_binary(data)
        data = self.NodeId.from_binary(data)
        data = self.NodeClass.from_binary(data)
        data = self.BrowseName.from_binary(data)
        data = self.DisplayName.from_binary(data)
        data = self.Description.from_binary(data)
        self.WriteMask = struct.unpack(I, data[:4])
        data = data[4:]
        self.UserWriteMask = struct.unpack(I, data[:4])
        data = data[4:]
        self.NoOfReferences = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.References.from_binary(data)
        data = self.NodeId.from_binary(data)
        data = self.NodeClass.from_binary(data)
        data = self.BrowseName.from_binary(data)
        data = self.DisplayName.from_binary(data)
        data = self.Description.from_binary(data)
        self.WriteMask = struct.unpack(I, data[:4])
        data = data[4:]
        self.UserWriteMask = struct.unpack(I, data[:4])
        data = data[4:]
        self.NoOfReferences = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.References.from_binary(data)
        self.ContainsNoLoops = struct.unpack(?, data[:1])
        data = data[1:]
        self.EventNotifier = struct.unpack(c, data[:1])
        data = data[1:]
        return data

class DataTypeNode(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.NodeId = None
        self.NodeClass = None
        self.BrowseName = None
        self.DisplayName = None
        self.Description = None
        self.WriteMask = None
        self.UserWriteMask = None
        self.NoOfReferences = None
        self.References = []
        self.NodeId = None
        self.NodeClass = None
        self.BrowseName = None
        self.DisplayName = None
        self.Description = None
        self.WriteMask = None
        self.UserWriteMask = None
        self.NoOfReferences = None
        self.References = []
        self.NodeId = None
        self.NodeClass = None
        self.BrowseName = None
        self.DisplayName = None
        self.Description = None
        self.WriteMask = None
        self.UserWriteMask = None
        self.NoOfReferences = None
        self.References = []
        self.IsAbstract = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.NodeId.to_binary())
        b.append(self.NodeClass.to_binary())
        b.append(self.BrowseName.to_binary())
        b.append(self.DisplayName.to_binary())
        b.append(self.Description.to_binary())
        b.append(struct.pack('!I', self.WriteMask))
        b.append(struct.pack('!I', self.UserWriteMask))
        b.append(struct.pack('!i', self.NoOfReferences))
        b.append(struct.pack('!i', len(self.References))
        b.append(self.References.to_binary())
        b.append(self.NodeId.to_binary())
        b.append(self.NodeClass.to_binary())
        b.append(self.BrowseName.to_binary())
        b.append(self.DisplayName.to_binary())
        b.append(self.Description.to_binary())
        b.append(struct.pack('!I', self.WriteMask))
        b.append(struct.pack('!I', self.UserWriteMask))
        b.append(struct.pack('!i', self.NoOfReferences))
        b.append(struct.pack('!i', len(self.References))
        b.append(self.References.to_binary())
        b.append(self.NodeId.to_binary())
        b.append(self.NodeClass.to_binary())
        b.append(self.BrowseName.to_binary())
        b.append(self.DisplayName.to_binary())
        b.append(self.Description.to_binary())
        b.append(struct.pack('!I', self.WriteMask))
        b.append(struct.pack('!I', self.UserWriteMask))
        b.append(struct.pack('!i', self.NoOfReferences))
        b.append(struct.pack('!i', len(self.References))
        b.append(self.References.to_binary())
        b.append(struct.pack('!?', self.IsAbstract))
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.NodeId.from_binary(data)
        data = self.NodeClass.from_binary(data)
        data = self.BrowseName.from_binary(data)
        data = self.DisplayName.from_binary(data)
        data = self.Description.from_binary(data)
        self.WriteMask = struct.unpack(I, data[:4])
        data = data[4:]
        self.UserWriteMask = struct.unpack(I, data[:4])
        data = data[4:]
        self.NoOfReferences = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.References.from_binary(data)
        data = self.NodeId.from_binary(data)
        data = self.NodeClass.from_binary(data)
        data = self.BrowseName.from_binary(data)
        data = self.DisplayName.from_binary(data)
        data = self.Description.from_binary(data)
        self.WriteMask = struct.unpack(I, data[:4])
        data = data[4:]
        self.UserWriteMask = struct.unpack(I, data[:4])
        data = data[4:]
        self.NoOfReferences = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.References.from_binary(data)
        data = self.NodeId.from_binary(data)
        data = self.NodeClass.from_binary(data)
        data = self.BrowseName.from_binary(data)
        data = self.DisplayName.from_binary(data)
        data = self.Description.from_binary(data)
        self.WriteMask = struct.unpack(I, data[:4])
        data = data[4:]
        self.UserWriteMask = struct.unpack(I, data[:4])
        data = data[4:]
        self.NoOfReferences = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.References.from_binary(data)
        self.IsAbstract = struct.unpack(?, data[:1])
        data = data[1:]
        return data

class Argument(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.Name = None
        self.DataType = None
        self.ValueRank = None
        self.NoOfArrayDimensions = None
        self.ArrayDimensions = []
        self.Description = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.Name.to_binary())
        b.append(self.DataType.to_binary())
        b.append(struct.pack('!i', self.ValueRank))
        b.append(struct.pack('!i', self.NoOfArrayDimensions))
        b.append(struct.pack('!i', len(self.ArrayDimensions))
        b.append(struct.pack('!I', self.ArrayDimensions))
        b.append(self.Description.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.Name.from_binary(data)
        data = self.DataType.from_binary(data)
        self.ValueRank = struct.unpack(i, data[:4])
        data = data[4:]
        self.NoOfArrayDimensions = struct.unpack(i, data[:4])
        data = data[4:]
        self.ArrayDimensions = struct.unpack(I, data[:4])
        data = data[4:]
        data = self.Description.from_binary(data)
        return data

class EnumValueType(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.Value = None
        self.DisplayName = None
        self.Description = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(struct.pack('!q', self.Value))
        b.append(self.DisplayName.to_binary())
        b.append(self.Description.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        self.Value = struct.unpack(q, data[:8])
        data = data[8:]
        data = self.DisplayName.from_binary(data)
        data = self.Description.from_binary(data)
        return data

class TimeZoneDataType(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.Offset = None
        self.DaylightSavingInOffset = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(struct.pack('!h', self.Offset))
        b.append(struct.pack('!?', self.DaylightSavingInOffset))
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        self.Offset = struct.unpack(h, data[:2])
        data = data[2:]
        self.DaylightSavingInOffset = struct.unpack(?, data[:1])
        data = data[1:]
        return data

class ApplicationDescription(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.ApplicationUri = None
        self.ProductUri = None
        self.ApplicationName = None
        self.ApplicationType = None
        self.GatewayServerUri = None
        self.DiscoveryProfileUri = None
        self.NoOfDiscoveryUrls = None
        self.DiscoveryUrls = []

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.ApplicationUri.to_binary())
        b.append(self.ProductUri.to_binary())
        b.append(self.ApplicationName.to_binary())
        b.append(self.ApplicationType.to_binary())
        b.append(self.GatewayServerUri.to_binary())
        b.append(self.DiscoveryProfileUri.to_binary())
        b.append(struct.pack('!i', self.NoOfDiscoveryUrls))
        b.append(struct.pack('!i', len(self.DiscoveryUrls))
        b.append(self.DiscoveryUrls.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.ApplicationUri.from_binary(data)
        data = self.ProductUri.from_binary(data)
        data = self.ApplicationName.from_binary(data)
        data = self.ApplicationType.from_binary(data)
        data = self.GatewayServerUri.from_binary(data)
        data = self.DiscoveryProfileUri.from_binary(data)
        self.NoOfDiscoveryUrls = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.DiscoveryUrls.from_binary(data)
        return data

class RequestHeader(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.AuthenticationToken = None
        self.Timestamp = None
        self.RequestHandle = None
        self.ReturnDiagnostics = None
        self.AuditEntryId = None
        self.TimeoutHint = None
        self.AdditionalHeader = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.AuthenticationToken.to_binary())
        b.append(struct.pack('!d', self.Timestamp))
        b.append(struct.pack('!I', self.RequestHandle))
        b.append(struct.pack('!I', self.ReturnDiagnostics))
        b.append(self.AuditEntryId.to_binary())
        b.append(struct.pack('!I', self.TimeoutHint))
        b.append(self.AdditionalHeader.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.AuthenticationToken.from_binary(data)
        self.Timestamp = struct.unpack(d, data[:8])
        data = data[8:]
        self.RequestHandle = struct.unpack(I, data[:4])
        data = data[4:]
        self.ReturnDiagnostics = struct.unpack(I, data[:4])
        data = data[4:]
        data = self.AuditEntryId.from_binary(data)
        self.TimeoutHint = struct.unpack(I, data[:4])
        data = data[4:]
        data = self.AdditionalHeader.from_binary(data)
        return data

class ResponseHeader(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.Timestamp = None
        self.RequestHandle = None
        self.ServiceResult = None
        self.ServiceDiagnostics = None
        self.NoOfStringTable = None
        self.StringTable = []
        self.AdditionalHeader = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(struct.pack('!d', self.Timestamp))
        b.append(struct.pack('!I', self.RequestHandle))
        b.append(self.ServiceResult.to_binary())
        b.append(self.ServiceDiagnostics.to_binary())
        b.append(struct.pack('!i', self.NoOfStringTable))
        b.append(struct.pack('!i', len(self.StringTable))
        b.append(self.StringTable.to_binary())
        b.append(self.AdditionalHeader.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        self.Timestamp = struct.unpack(d, data[:8])
        data = data[8:]
        self.RequestHandle = struct.unpack(I, data[:4])
        data = data[4:]
        data = self.ServiceResult.from_binary(data)
        data = self.ServiceDiagnostics.from_binary(data)
        self.NoOfStringTable = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.StringTable.from_binary(data)
        data = self.AdditionalHeader.from_binary(data)
        return data

class ServiceFault(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.ResponseHeader = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.ResponseHeader.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.ResponseHeader.from_binary(data)
        return data

class FindServersRequest(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.RequestHeader = None
        self.EndpointUrl = None
        self.NoOfLocaleIds = None
        self.LocaleIds = []
        self.NoOfServerUris = None
        self.ServerUris = []

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.RequestHeader.to_binary())
        b.append(self.EndpointUrl.to_binary())
        b.append(struct.pack('!i', self.NoOfLocaleIds))
        b.append(struct.pack('!i', len(self.LocaleIds))
        b.append(self.LocaleIds.to_binary())
        b.append(struct.pack('!i', self.NoOfServerUris))
        b.append(struct.pack('!i', len(self.ServerUris))
        b.append(self.ServerUris.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.RequestHeader.from_binary(data)
        data = self.EndpointUrl.from_binary(data)
        self.NoOfLocaleIds = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.LocaleIds.from_binary(data)
        self.NoOfServerUris = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.ServerUris.from_binary(data)
        return data

class FindServersResponse(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.ResponseHeader = None
        self.NoOfServers = None
        self.Servers = []

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.ResponseHeader.to_binary())
        b.append(struct.pack('!i', self.NoOfServers))
        b.append(struct.pack('!i', len(self.Servers))
        b.append(self.Servers.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.ResponseHeader.from_binary(data)
        self.NoOfServers = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.Servers.from_binary(data)
        return data

class UserTokenPolicy(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.PolicyId = None
        self.TokenType = None
        self.IssuedTokenType = None
        self.IssuerEndpointUrl = None
        self.SecurityPolicyUri = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.PolicyId.to_binary())
        b.append(self.TokenType.to_binary())
        b.append(self.IssuedTokenType.to_binary())
        b.append(self.IssuerEndpointUrl.to_binary())
        b.append(self.SecurityPolicyUri.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.PolicyId.from_binary(data)
        data = self.TokenType.from_binary(data)
        data = self.IssuedTokenType.from_binary(data)
        data = self.IssuerEndpointUrl.from_binary(data)
        data = self.SecurityPolicyUri.from_binary(data)
        return data

class EndpointDescription(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.EndpointUrl = None
        self.Server = None
        self.ServerCertificate = None
        self.SecurityMode = None
        self.SecurityPolicyUri = None
        self.NoOfUserIdentityTokens = None
        self.UserIdentityTokens = []
        self.TransportProfileUri = None
        self.SecurityLevel = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.EndpointUrl.to_binary())
        b.append(self.Server.to_binary())
        b.append(self.ServerCertificate.to_binary())
        b.append(self.SecurityMode.to_binary())
        b.append(self.SecurityPolicyUri.to_binary())
        b.append(struct.pack('!i', self.NoOfUserIdentityTokens))
        b.append(struct.pack('!i', len(self.UserIdentityTokens))
        b.append(self.UserIdentityTokens.to_binary())
        b.append(self.TransportProfileUri.to_binary())
        b.append(struct.pack('!c', self.SecurityLevel))
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.EndpointUrl.from_binary(data)
        data = self.Server.from_binary(data)
        data = self.ServerCertificate.from_binary(data)
        data = self.SecurityMode.from_binary(data)
        data = self.SecurityPolicyUri.from_binary(data)
        self.NoOfUserIdentityTokens = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.UserIdentityTokens.from_binary(data)
        data = self.TransportProfileUri.from_binary(data)
        self.SecurityLevel = struct.unpack(c, data[:1])
        data = data[1:]
        return data

class GetEndpointsRequest(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.RequestHeader = None
        self.EndpointUrl = None
        self.NoOfLocaleIds = None
        self.LocaleIds = []
        self.NoOfProfileUris = None
        self.ProfileUris = []

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.RequestHeader.to_binary())
        b.append(self.EndpointUrl.to_binary())
        b.append(struct.pack('!i', self.NoOfLocaleIds))
        b.append(struct.pack('!i', len(self.LocaleIds))
        b.append(self.LocaleIds.to_binary())
        b.append(struct.pack('!i', self.NoOfProfileUris))
        b.append(struct.pack('!i', len(self.ProfileUris))
        b.append(self.ProfileUris.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.RequestHeader.from_binary(data)
        data = self.EndpointUrl.from_binary(data)
        self.NoOfLocaleIds = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.LocaleIds.from_binary(data)
        self.NoOfProfileUris = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.ProfileUris.from_binary(data)
        return data

class GetEndpointsResponse(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.ResponseHeader = None
        self.NoOfEndpoints = None
        self.Endpoints = []

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.ResponseHeader.to_binary())
        b.append(struct.pack('!i', self.NoOfEndpoints))
        b.append(struct.pack('!i', len(self.Endpoints))
        b.append(self.Endpoints.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.ResponseHeader.from_binary(data)
        self.NoOfEndpoints = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.Endpoints.from_binary(data)
        return data

class RegisteredServer(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.ServerUri = None
        self.ProductUri = None
        self.NoOfServerNames = None
        self.ServerNames = []
        self.ServerType = None
        self.GatewayServerUri = None
        self.NoOfDiscoveryUrls = None
        self.DiscoveryUrls = []
        self.SemaphoreFilePath = None
        self.IsOnline = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.ServerUri.to_binary())
        b.append(self.ProductUri.to_binary())
        b.append(struct.pack('!i', self.NoOfServerNames))
        b.append(struct.pack('!i', len(self.ServerNames))
        b.append(self.ServerNames.to_binary())
        b.append(self.ServerType.to_binary())
        b.append(self.GatewayServerUri.to_binary())
        b.append(struct.pack('!i', self.NoOfDiscoveryUrls))
        b.append(struct.pack('!i', len(self.DiscoveryUrls))
        b.append(self.DiscoveryUrls.to_binary())
        b.append(self.SemaphoreFilePath.to_binary())
        b.append(struct.pack('!?', self.IsOnline))
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.ServerUri.from_binary(data)
        data = self.ProductUri.from_binary(data)
        self.NoOfServerNames = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.ServerNames.from_binary(data)
        data = self.ServerType.from_binary(data)
        data = self.GatewayServerUri.from_binary(data)
        self.NoOfDiscoveryUrls = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.DiscoveryUrls.from_binary(data)
        data = self.SemaphoreFilePath.from_binary(data)
        self.IsOnline = struct.unpack(?, data[:1])
        data = data[1:]
        return data

class RegisterServerRequest(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.RequestHeader = None
        self.Server = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.RequestHeader.to_binary())
        b.append(self.Server.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.RequestHeader.from_binary(data)
        data = self.Server.from_binary(data)
        return data

class RegisterServerResponse(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.ResponseHeader = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.ResponseHeader.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.ResponseHeader.from_binary(data)
        return data

class ChannelSecurityToken(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.ChannelId = None
        self.TokenId = None
        self.CreatedAt = None
        self.RevisedLifetime = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(struct.pack('!I', self.ChannelId))
        b.append(struct.pack('!I', self.TokenId))
        b.append(struct.pack('!d', self.CreatedAt))
        b.append(struct.pack('!I', self.RevisedLifetime))
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        self.ChannelId = struct.unpack(I, data[:4])
        data = data[4:]
        self.TokenId = struct.unpack(I, data[:4])
        data = data[4:]
        self.CreatedAt = struct.unpack(d, data[:8])
        data = data[8:]
        self.RevisedLifetime = struct.unpack(I, data[:4])
        data = data[4:]
        return data

class OpenSecureChannelRequest(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.RequestHeader = None
        self.ClientProtocolVersion = None
        self.RequestType = None
        self.SecurityMode = None
        self.ClientNonce = None
        self.RequestedLifetime = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.RequestHeader.to_binary())
        b.append(struct.pack('!I', self.ClientProtocolVersion))
        b.append(self.RequestType.to_binary())
        b.append(self.SecurityMode.to_binary())
        b.append(self.ClientNonce.to_binary())
        b.append(struct.pack('!I', self.RequestedLifetime))
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.RequestHeader.from_binary(data)
        self.ClientProtocolVersion = struct.unpack(I, data[:4])
        data = data[4:]
        data = self.RequestType.from_binary(data)
        data = self.SecurityMode.from_binary(data)
        data = self.ClientNonce.from_binary(data)
        self.RequestedLifetime = struct.unpack(I, data[:4])
        data = data[4:]
        return data

class OpenSecureChannelResponse(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.ResponseHeader = None
        self.ServerProtocolVersion = None
        self.SecurityToken = None
        self.ServerNonce = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.ResponseHeader.to_binary())
        b.append(struct.pack('!I', self.ServerProtocolVersion))
        b.append(self.SecurityToken.to_binary())
        b.append(self.ServerNonce.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.ResponseHeader.from_binary(data)
        self.ServerProtocolVersion = struct.unpack(I, data[:4])
        data = data[4:]
        data = self.SecurityToken.from_binary(data)
        data = self.ServerNonce.from_binary(data)
        return data

class CloseSecureChannelRequest(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.RequestHeader = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.RequestHeader.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.RequestHeader.from_binary(data)
        return data

class CloseSecureChannelResponse(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.ResponseHeader = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.ResponseHeader.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.ResponseHeader.from_binary(data)
        return data

class SignedSoftwareCertificate(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.CertificateData = None
        self.Signature = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.CertificateData.to_binary())
        b.append(self.Signature.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.CertificateData.from_binary(data)
        data = self.Signature.from_binary(data)
        return data

class SignatureData(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.Algorithm = None
        self.Signature = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.Algorithm.to_binary())
        b.append(self.Signature.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.Algorithm.from_binary(data)
        data = self.Signature.from_binary(data)
        return data

class CreateSessionRequest(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.RequestHeader = None
        self.ClientDescription = None
        self.ServerUri = None
        self.EndpointUrl = None
        self.SessionName = None
        self.ClientNonce = None
        self.ClientCertificate = None
        self.RequestedSessionTimeout = None
        self.MaxResponseMessageSize = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.RequestHeader.to_binary())
        b.append(self.ClientDescription.to_binary())
        b.append(self.ServerUri.to_binary())
        b.append(self.EndpointUrl.to_binary())
        b.append(self.SessionName.to_binary())
        b.append(self.ClientNonce.to_binary())
        b.append(self.ClientCertificate.to_binary())
        b.append(struct.pack('!d', self.RequestedSessionTimeout))
        b.append(struct.pack('!I', self.MaxResponseMessageSize))
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.RequestHeader.from_binary(data)
        data = self.ClientDescription.from_binary(data)
        data = self.ServerUri.from_binary(data)
        data = self.EndpointUrl.from_binary(data)
        data = self.SessionName.from_binary(data)
        data = self.ClientNonce.from_binary(data)
        data = self.ClientCertificate.from_binary(data)
        self.RequestedSessionTimeout = struct.unpack(d, data[:8])
        data = data[8:]
        self.MaxResponseMessageSize = struct.unpack(I, data[:4])
        data = data[4:]
        return data

class CreateSessionResponse(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.ResponseHeader = None
        self.SessionId = None
        self.AuthenticationToken = None
        self.RevisedSessionTimeout = None
        self.ServerNonce = None
        self.ServerCertificate = None
        self.NoOfServerEndpoints = None
        self.ServerEndpoints = []
        self.NoOfServerSoftwareCertificates = None
        self.ServerSoftwareCertificates = []
        self.ServerSignature = None
        self.MaxRequestMessageSize = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.ResponseHeader.to_binary())
        b.append(self.SessionId.to_binary())
        b.append(self.AuthenticationToken.to_binary())
        b.append(struct.pack('!d', self.RevisedSessionTimeout))
        b.append(self.ServerNonce.to_binary())
        b.append(self.ServerCertificate.to_binary())
        b.append(struct.pack('!i', self.NoOfServerEndpoints))
        b.append(struct.pack('!i', len(self.ServerEndpoints))
        b.append(self.ServerEndpoints.to_binary())
        b.append(struct.pack('!i', self.NoOfServerSoftwareCertificates))
        b.append(struct.pack('!i', len(self.ServerSoftwareCertificates))
        b.append(self.ServerSoftwareCertificates.to_binary())
        b.append(self.ServerSignature.to_binary())
        b.append(struct.pack('!I', self.MaxRequestMessageSize))
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.ResponseHeader.from_binary(data)
        data = self.SessionId.from_binary(data)
        data = self.AuthenticationToken.from_binary(data)
        self.RevisedSessionTimeout = struct.unpack(d, data[:8])
        data = data[8:]
        data = self.ServerNonce.from_binary(data)
        data = self.ServerCertificate.from_binary(data)
        self.NoOfServerEndpoints = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.ServerEndpoints.from_binary(data)
        self.NoOfServerSoftwareCertificates = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.ServerSoftwareCertificates.from_binary(data)
        data = self.ServerSignature.from_binary(data)
        self.MaxRequestMessageSize = struct.unpack(I, data[:4])
        data = data[4:]
        return data

class UserIdentityToken(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.PolicyId = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.PolicyId.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.PolicyId.from_binary(data)
        return data

class AnonymousIdentityToken(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.PolicyId = None
        self.PolicyId = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.PolicyId.to_binary())
        b.append(self.PolicyId.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.PolicyId.from_binary(data)
        data = self.PolicyId.from_binary(data)
        return data

class UserNameIdentityToken(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.PolicyId = None
        self.PolicyId = None
        self.UserName = None
        self.Password = None
        self.EncryptionAlgorithm = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.PolicyId.to_binary())
        b.append(self.PolicyId.to_binary())
        b.append(self.UserName.to_binary())
        b.append(self.Password.to_binary())
        b.append(self.EncryptionAlgorithm.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.PolicyId.from_binary(data)
        data = self.PolicyId.from_binary(data)
        data = self.UserName.from_binary(data)
        data = self.Password.from_binary(data)
        data = self.EncryptionAlgorithm.from_binary(data)
        return data

class X509IdentityToken(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.PolicyId = None
        self.PolicyId = None
        self.CertificateData = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.PolicyId.to_binary())
        b.append(self.PolicyId.to_binary())
        b.append(self.CertificateData.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.PolicyId.from_binary(data)
        data = self.PolicyId.from_binary(data)
        data = self.CertificateData.from_binary(data)
        return data

class IssuedIdentityToken(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.PolicyId = None
        self.PolicyId = None
        self.TokenData = None
        self.EncryptionAlgorithm = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.PolicyId.to_binary())
        b.append(self.PolicyId.to_binary())
        b.append(self.TokenData.to_binary())
        b.append(self.EncryptionAlgorithm.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.PolicyId.from_binary(data)
        data = self.PolicyId.from_binary(data)
        data = self.TokenData.from_binary(data)
        data = self.EncryptionAlgorithm.from_binary(data)
        return data

class ActivateSessionRequest(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.RequestHeader = None
        self.ClientSignature = None
        self.NoOfClientSoftwareCertificates = None
        self.ClientSoftwareCertificates = []
        self.NoOfLocaleIds = None
        self.LocaleIds = []
        self.UserIdentityToken = None
        self.UserTokenSignature = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.RequestHeader.to_binary())
        b.append(self.ClientSignature.to_binary())
        b.append(struct.pack('!i', self.NoOfClientSoftwareCertificates))
        b.append(struct.pack('!i', len(self.ClientSoftwareCertificates))
        b.append(self.ClientSoftwareCertificates.to_binary())
        b.append(struct.pack('!i', self.NoOfLocaleIds))
        b.append(struct.pack('!i', len(self.LocaleIds))
        b.append(self.LocaleIds.to_binary())
        b.append(self.UserIdentityToken.to_binary())
        b.append(self.UserTokenSignature.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.RequestHeader.from_binary(data)
        data = self.ClientSignature.from_binary(data)
        self.NoOfClientSoftwareCertificates = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.ClientSoftwareCertificates.from_binary(data)
        self.NoOfLocaleIds = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.LocaleIds.from_binary(data)
        data = self.UserIdentityToken.from_binary(data)
        data = self.UserTokenSignature.from_binary(data)
        return data

class ActivateSessionResponse(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.ResponseHeader = None
        self.ServerNonce = None
        self.NoOfResults = None
        self.Results = []
        self.NoOfDiagnosticInfos = None
        self.DiagnosticInfos = []

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.ResponseHeader.to_binary())
        b.append(self.ServerNonce.to_binary())
        b.append(struct.pack('!i', self.NoOfResults))
        b.append(struct.pack('!i', len(self.Results))
        b.append(self.Results.to_binary())
        b.append(struct.pack('!i', self.NoOfDiagnosticInfos))
        b.append(struct.pack('!i', len(self.DiagnosticInfos))
        b.append(self.DiagnosticInfos.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.ResponseHeader.from_binary(data)
        data = self.ServerNonce.from_binary(data)
        self.NoOfResults = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.Results.from_binary(data)
        self.NoOfDiagnosticInfos = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.DiagnosticInfos.from_binary(data)
        return data

class CloseSessionRequest(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.RequestHeader = None
        self.DeleteSubscriptions = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.RequestHeader.to_binary())
        b.append(struct.pack('!?', self.DeleteSubscriptions))
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.RequestHeader.from_binary(data)
        self.DeleteSubscriptions = struct.unpack(?, data[:1])
        data = data[1:]
        return data

class CloseSessionResponse(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.ResponseHeader = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.ResponseHeader.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.ResponseHeader.from_binary(data)
        return data

class CancelRequest(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.RequestHeader = None
        self.RequestHandle = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.RequestHeader.to_binary())
        b.append(struct.pack('!I', self.RequestHandle))
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.RequestHeader.from_binary(data)
        self.RequestHandle = struct.unpack(I, data[:4])
        data = data[4:]
        return data

class CancelResponse(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.ResponseHeader = None
        self.CancelCount = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.ResponseHeader.to_binary())
        b.append(struct.pack('!I', self.CancelCount))
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.ResponseHeader.from_binary(data)
        self.CancelCount = struct.unpack(I, data[:4])
        data = data[4:]
        return data

class NodeAttributes(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.SpecifiedAttributes = None
        self.DisplayName = None
        self.Description = None
        self.WriteMask = None
        self.UserWriteMask = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(struct.pack('!I', self.SpecifiedAttributes))
        b.append(self.DisplayName.to_binary())
        b.append(self.Description.to_binary())
        b.append(struct.pack('!I', self.WriteMask))
        b.append(struct.pack('!I', self.UserWriteMask))
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        self.SpecifiedAttributes = struct.unpack(I, data[:4])
        data = data[4:]
        data = self.DisplayName.from_binary(data)
        data = self.Description.from_binary(data)
        self.WriteMask = struct.unpack(I, data[:4])
        data = data[4:]
        self.UserWriteMask = struct.unpack(I, data[:4])
        data = data[4:]
        return data

class ObjectAttributes(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.SpecifiedAttributes = None
        self.DisplayName = None
        self.Description = None
        self.WriteMask = None
        self.UserWriteMask = None
        self.SpecifiedAttributes = None
        self.DisplayName = None
        self.Description = None
        self.WriteMask = None
        self.UserWriteMask = None
        self.EventNotifier = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(struct.pack('!I', self.SpecifiedAttributes))
        b.append(self.DisplayName.to_binary())
        b.append(self.Description.to_binary())
        b.append(struct.pack('!I', self.WriteMask))
        b.append(struct.pack('!I', self.UserWriteMask))
        b.append(struct.pack('!I', self.SpecifiedAttributes))
        b.append(self.DisplayName.to_binary())
        b.append(self.Description.to_binary())
        b.append(struct.pack('!I', self.WriteMask))
        b.append(struct.pack('!I', self.UserWriteMask))
        b.append(struct.pack('!c', self.EventNotifier))
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        self.SpecifiedAttributes = struct.unpack(I, data[:4])
        data = data[4:]
        data = self.DisplayName.from_binary(data)
        data = self.Description.from_binary(data)
        self.WriteMask = struct.unpack(I, data[:4])
        data = data[4:]
        self.UserWriteMask = struct.unpack(I, data[:4])
        data = data[4:]
        self.SpecifiedAttributes = struct.unpack(I, data[:4])
        data = data[4:]
        data = self.DisplayName.from_binary(data)
        data = self.Description.from_binary(data)
        self.WriteMask = struct.unpack(I, data[:4])
        data = data[4:]
        self.UserWriteMask = struct.unpack(I, data[:4])
        data = data[4:]
        self.EventNotifier = struct.unpack(c, data[:1])
        data = data[1:]
        return data

class VariableAttributes(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.SpecifiedAttributes = None
        self.DisplayName = None
        self.Description = None
        self.WriteMask = None
        self.UserWriteMask = None
        self.SpecifiedAttributes = None
        self.DisplayName = None
        self.Description = None
        self.WriteMask = None
        self.UserWriteMask = None
        self.Value = None
        self.DataType = None
        self.ValueRank = None
        self.NoOfArrayDimensions = None
        self.ArrayDimensions = []
        self.AccessLevel = None
        self.UserAccessLevel = None
        self.MinimumSamplingInterval = None
        self.Historizing = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(struct.pack('!I', self.SpecifiedAttributes))
        b.append(self.DisplayName.to_binary())
        b.append(self.Description.to_binary())
        b.append(struct.pack('!I', self.WriteMask))
        b.append(struct.pack('!I', self.UserWriteMask))
        b.append(struct.pack('!I', self.SpecifiedAttributes))
        b.append(self.DisplayName.to_binary())
        b.append(self.Description.to_binary())
        b.append(struct.pack('!I', self.WriteMask))
        b.append(struct.pack('!I', self.UserWriteMask))
        b.append(self.Value.to_binary())
        b.append(self.DataType.to_binary())
        b.append(struct.pack('!i', self.ValueRank))
        b.append(struct.pack('!i', self.NoOfArrayDimensions))
        b.append(struct.pack('!i', len(self.ArrayDimensions))
        b.append(struct.pack('!I', self.ArrayDimensions))
        b.append(struct.pack('!c', self.AccessLevel))
        b.append(struct.pack('!c', self.UserAccessLevel))
        b.append(struct.pack('!d', self.MinimumSamplingInterval))
        b.append(struct.pack('!?', self.Historizing))
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        self.SpecifiedAttributes = struct.unpack(I, data[:4])
        data = data[4:]
        data = self.DisplayName.from_binary(data)
        data = self.Description.from_binary(data)
        self.WriteMask = struct.unpack(I, data[:4])
        data = data[4:]
        self.UserWriteMask = struct.unpack(I, data[:4])
        data = data[4:]
        self.SpecifiedAttributes = struct.unpack(I, data[:4])
        data = data[4:]
        data = self.DisplayName.from_binary(data)
        data = self.Description.from_binary(data)
        self.WriteMask = struct.unpack(I, data[:4])
        data = data[4:]
        self.UserWriteMask = struct.unpack(I, data[:4])
        data = data[4:]
        data = self.Value.from_binary(data)
        data = self.DataType.from_binary(data)
        self.ValueRank = struct.unpack(i, data[:4])
        data = data[4:]
        self.NoOfArrayDimensions = struct.unpack(i, data[:4])
        data = data[4:]
        self.ArrayDimensions = struct.unpack(I, data[:4])
        data = data[4:]
        self.AccessLevel = struct.unpack(c, data[:1])
        data = data[1:]
        self.UserAccessLevel = struct.unpack(c, data[:1])
        data = data[1:]
        self.MinimumSamplingInterval = struct.unpack(d, data[:8])
        data = data[8:]
        self.Historizing = struct.unpack(?, data[:1])
        data = data[1:]
        return data

class MethodAttributes(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.SpecifiedAttributes = None
        self.DisplayName = None
        self.Description = None
        self.WriteMask = None
        self.UserWriteMask = None
        self.SpecifiedAttributes = None
        self.DisplayName = None
        self.Description = None
        self.WriteMask = None
        self.UserWriteMask = None
        self.Executable = None
        self.UserExecutable = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(struct.pack('!I', self.SpecifiedAttributes))
        b.append(self.DisplayName.to_binary())
        b.append(self.Description.to_binary())
        b.append(struct.pack('!I', self.WriteMask))
        b.append(struct.pack('!I', self.UserWriteMask))
        b.append(struct.pack('!I', self.SpecifiedAttributes))
        b.append(self.DisplayName.to_binary())
        b.append(self.Description.to_binary())
        b.append(struct.pack('!I', self.WriteMask))
        b.append(struct.pack('!I', self.UserWriteMask))
        b.append(struct.pack('!?', self.Executable))
        b.append(struct.pack('!?', self.UserExecutable))
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        self.SpecifiedAttributes = struct.unpack(I, data[:4])
        data = data[4:]
        data = self.DisplayName.from_binary(data)
        data = self.Description.from_binary(data)
        self.WriteMask = struct.unpack(I, data[:4])
        data = data[4:]
        self.UserWriteMask = struct.unpack(I, data[:4])
        data = data[4:]
        self.SpecifiedAttributes = struct.unpack(I, data[:4])
        data = data[4:]
        data = self.DisplayName.from_binary(data)
        data = self.Description.from_binary(data)
        self.WriteMask = struct.unpack(I, data[:4])
        data = data[4:]
        self.UserWriteMask = struct.unpack(I, data[:4])
        data = data[4:]
        self.Executable = struct.unpack(?, data[:1])
        data = data[1:]
        self.UserExecutable = struct.unpack(?, data[:1])
        data = data[1:]
        return data

class ObjectTypeAttributes(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.SpecifiedAttributes = None
        self.DisplayName = None
        self.Description = None
        self.WriteMask = None
        self.UserWriteMask = None
        self.SpecifiedAttributes = None
        self.DisplayName = None
        self.Description = None
        self.WriteMask = None
        self.UserWriteMask = None
        self.IsAbstract = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(struct.pack('!I', self.SpecifiedAttributes))
        b.append(self.DisplayName.to_binary())
        b.append(self.Description.to_binary())
        b.append(struct.pack('!I', self.WriteMask))
        b.append(struct.pack('!I', self.UserWriteMask))
        b.append(struct.pack('!I', self.SpecifiedAttributes))
        b.append(self.DisplayName.to_binary())
        b.append(self.Description.to_binary())
        b.append(struct.pack('!I', self.WriteMask))
        b.append(struct.pack('!I', self.UserWriteMask))
        b.append(struct.pack('!?', self.IsAbstract))
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        self.SpecifiedAttributes = struct.unpack(I, data[:4])
        data = data[4:]
        data = self.DisplayName.from_binary(data)
        data = self.Description.from_binary(data)
        self.WriteMask = struct.unpack(I, data[:4])
        data = data[4:]
        self.UserWriteMask = struct.unpack(I, data[:4])
        data = data[4:]
        self.SpecifiedAttributes = struct.unpack(I, data[:4])
        data = data[4:]
        data = self.DisplayName.from_binary(data)
        data = self.Description.from_binary(data)
        self.WriteMask = struct.unpack(I, data[:4])
        data = data[4:]
        self.UserWriteMask = struct.unpack(I, data[:4])
        data = data[4:]
        self.IsAbstract = struct.unpack(?, data[:1])
        data = data[1:]
        return data

class VariableTypeAttributes(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.SpecifiedAttributes = None
        self.DisplayName = None
        self.Description = None
        self.WriteMask = None
        self.UserWriteMask = None
        self.SpecifiedAttributes = None
        self.DisplayName = None
        self.Description = None
        self.WriteMask = None
        self.UserWriteMask = None
        self.Value = None
        self.DataType = None
        self.ValueRank = None
        self.NoOfArrayDimensions = None
        self.ArrayDimensions = []
        self.IsAbstract = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(struct.pack('!I', self.SpecifiedAttributes))
        b.append(self.DisplayName.to_binary())
        b.append(self.Description.to_binary())
        b.append(struct.pack('!I', self.WriteMask))
        b.append(struct.pack('!I', self.UserWriteMask))
        b.append(struct.pack('!I', self.SpecifiedAttributes))
        b.append(self.DisplayName.to_binary())
        b.append(self.Description.to_binary())
        b.append(struct.pack('!I', self.WriteMask))
        b.append(struct.pack('!I', self.UserWriteMask))
        b.append(self.Value.to_binary())
        b.append(self.DataType.to_binary())
        b.append(struct.pack('!i', self.ValueRank))
        b.append(struct.pack('!i', self.NoOfArrayDimensions))
        b.append(struct.pack('!i', len(self.ArrayDimensions))
        b.append(struct.pack('!I', self.ArrayDimensions))
        b.append(struct.pack('!?', self.IsAbstract))
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        self.SpecifiedAttributes = struct.unpack(I, data[:4])
        data = data[4:]
        data = self.DisplayName.from_binary(data)
        data = self.Description.from_binary(data)
        self.WriteMask = struct.unpack(I, data[:4])
        data = data[4:]
        self.UserWriteMask = struct.unpack(I, data[:4])
        data = data[4:]
        self.SpecifiedAttributes = struct.unpack(I, data[:4])
        data = data[4:]
        data = self.DisplayName.from_binary(data)
        data = self.Description.from_binary(data)
        self.WriteMask = struct.unpack(I, data[:4])
        data = data[4:]
        self.UserWriteMask = struct.unpack(I, data[:4])
        data = data[4:]
        data = self.Value.from_binary(data)
        data = self.DataType.from_binary(data)
        self.ValueRank = struct.unpack(i, data[:4])
        data = data[4:]
        self.NoOfArrayDimensions = struct.unpack(i, data[:4])
        data = data[4:]
        self.ArrayDimensions = struct.unpack(I, data[:4])
        data = data[4:]
        self.IsAbstract = struct.unpack(?, data[:1])
        data = data[1:]
        return data

class ReferenceTypeAttributes(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.SpecifiedAttributes = None
        self.DisplayName = None
        self.Description = None
        self.WriteMask = None
        self.UserWriteMask = None
        self.SpecifiedAttributes = None
        self.DisplayName = None
        self.Description = None
        self.WriteMask = None
        self.UserWriteMask = None
        self.IsAbstract = None
        self.Symmetric = None
        self.InverseName = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(struct.pack('!I', self.SpecifiedAttributes))
        b.append(self.DisplayName.to_binary())
        b.append(self.Description.to_binary())
        b.append(struct.pack('!I', self.WriteMask))
        b.append(struct.pack('!I', self.UserWriteMask))
        b.append(struct.pack('!I', self.SpecifiedAttributes))
        b.append(self.DisplayName.to_binary())
        b.append(self.Description.to_binary())
        b.append(struct.pack('!I', self.WriteMask))
        b.append(struct.pack('!I', self.UserWriteMask))
        b.append(struct.pack('!?', self.IsAbstract))
        b.append(struct.pack('!?', self.Symmetric))
        b.append(self.InverseName.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        self.SpecifiedAttributes = struct.unpack(I, data[:4])
        data = data[4:]
        data = self.DisplayName.from_binary(data)
        data = self.Description.from_binary(data)
        self.WriteMask = struct.unpack(I, data[:4])
        data = data[4:]
        self.UserWriteMask = struct.unpack(I, data[:4])
        data = data[4:]
        self.SpecifiedAttributes = struct.unpack(I, data[:4])
        data = data[4:]
        data = self.DisplayName.from_binary(data)
        data = self.Description.from_binary(data)
        self.WriteMask = struct.unpack(I, data[:4])
        data = data[4:]
        self.UserWriteMask = struct.unpack(I, data[:4])
        data = data[4:]
        self.IsAbstract = struct.unpack(?, data[:1])
        data = data[1:]
        self.Symmetric = struct.unpack(?, data[:1])
        data = data[1:]
        data = self.InverseName.from_binary(data)
        return data

class DataTypeAttributes(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.SpecifiedAttributes = None
        self.DisplayName = None
        self.Description = None
        self.WriteMask = None
        self.UserWriteMask = None
        self.SpecifiedAttributes = None
        self.DisplayName = None
        self.Description = None
        self.WriteMask = None
        self.UserWriteMask = None
        self.IsAbstract = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(struct.pack('!I', self.SpecifiedAttributes))
        b.append(self.DisplayName.to_binary())
        b.append(self.Description.to_binary())
        b.append(struct.pack('!I', self.WriteMask))
        b.append(struct.pack('!I', self.UserWriteMask))
        b.append(struct.pack('!I', self.SpecifiedAttributes))
        b.append(self.DisplayName.to_binary())
        b.append(self.Description.to_binary())
        b.append(struct.pack('!I', self.WriteMask))
        b.append(struct.pack('!I', self.UserWriteMask))
        b.append(struct.pack('!?', self.IsAbstract))
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        self.SpecifiedAttributes = struct.unpack(I, data[:4])
        data = data[4:]
        data = self.DisplayName.from_binary(data)
        data = self.Description.from_binary(data)
        self.WriteMask = struct.unpack(I, data[:4])
        data = data[4:]
        self.UserWriteMask = struct.unpack(I, data[:4])
        data = data[4:]
        self.SpecifiedAttributes = struct.unpack(I, data[:4])
        data = data[4:]
        data = self.DisplayName.from_binary(data)
        data = self.Description.from_binary(data)
        self.WriteMask = struct.unpack(I, data[:4])
        data = data[4:]
        self.UserWriteMask = struct.unpack(I, data[:4])
        data = data[4:]
        self.IsAbstract = struct.unpack(?, data[:1])
        data = data[1:]
        return data

class ViewAttributes(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.SpecifiedAttributes = None
        self.DisplayName = None
        self.Description = None
        self.WriteMask = None
        self.UserWriteMask = None
        self.SpecifiedAttributes = None
        self.DisplayName = None
        self.Description = None
        self.WriteMask = None
        self.UserWriteMask = None
        self.ContainsNoLoops = None
        self.EventNotifier = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(struct.pack('!I', self.SpecifiedAttributes))
        b.append(self.DisplayName.to_binary())
        b.append(self.Description.to_binary())
        b.append(struct.pack('!I', self.WriteMask))
        b.append(struct.pack('!I', self.UserWriteMask))
        b.append(struct.pack('!I', self.SpecifiedAttributes))
        b.append(self.DisplayName.to_binary())
        b.append(self.Description.to_binary())
        b.append(struct.pack('!I', self.WriteMask))
        b.append(struct.pack('!I', self.UserWriteMask))
        b.append(struct.pack('!?', self.ContainsNoLoops))
        b.append(struct.pack('!c', self.EventNotifier))
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        self.SpecifiedAttributes = struct.unpack(I, data[:4])
        data = data[4:]
        data = self.DisplayName.from_binary(data)
        data = self.Description.from_binary(data)
        self.WriteMask = struct.unpack(I, data[:4])
        data = data[4:]
        self.UserWriteMask = struct.unpack(I, data[:4])
        data = data[4:]
        self.SpecifiedAttributes = struct.unpack(I, data[:4])
        data = data[4:]
        data = self.DisplayName.from_binary(data)
        data = self.Description.from_binary(data)
        self.WriteMask = struct.unpack(I, data[:4])
        data = data[4:]
        self.UserWriteMask = struct.unpack(I, data[:4])
        data = data[4:]
        self.ContainsNoLoops = struct.unpack(?, data[:1])
        data = data[1:]
        self.EventNotifier = struct.unpack(c, data[:1])
        data = data[1:]
        return data

class AddNodesItem(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.ParentNodeId = None
        self.ReferenceTypeId = None
        self.RequestedNewNodeId = None
        self.BrowseName = None
        self.NodeClass = None
        self.NodeAttributes = None
        self.TypeDefinition = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.ParentNodeId.to_binary())
        b.append(self.ReferenceTypeId.to_binary())
        b.append(self.RequestedNewNodeId.to_binary())
        b.append(self.BrowseName.to_binary())
        b.append(self.NodeClass.to_binary())
        b.append(self.NodeAttributes.to_binary())
        b.append(self.TypeDefinition.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.ParentNodeId.from_binary(data)
        data = self.ReferenceTypeId.from_binary(data)
        data = self.RequestedNewNodeId.from_binary(data)
        data = self.BrowseName.from_binary(data)
        data = self.NodeClass.from_binary(data)
        data = self.NodeAttributes.from_binary(data)
        data = self.TypeDefinition.from_binary(data)
        return data

class AddNodesResult(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.StatusCode = None
        self.AddedNodeId = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.StatusCode.to_binary())
        b.append(self.AddedNodeId.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.StatusCode.from_binary(data)
        data = self.AddedNodeId.from_binary(data)
        return data

class AddNodesRequest(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.RequestHeader = None
        self.NoOfNodesToAdd = None
        self.NodesToAdd = []

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.RequestHeader.to_binary())
        b.append(struct.pack('!i', self.NoOfNodesToAdd))
        b.append(struct.pack('!i', len(self.NodesToAdd))
        b.append(self.NodesToAdd.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.RequestHeader.from_binary(data)
        self.NoOfNodesToAdd = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.NodesToAdd.from_binary(data)
        return data

class AddNodesResponse(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.ResponseHeader = None
        self.NoOfResults = None
        self.Results = []
        self.NoOfDiagnosticInfos = None
        self.DiagnosticInfos = []

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.ResponseHeader.to_binary())
        b.append(struct.pack('!i', self.NoOfResults))
        b.append(struct.pack('!i', len(self.Results))
        b.append(self.Results.to_binary())
        b.append(struct.pack('!i', self.NoOfDiagnosticInfos))
        b.append(struct.pack('!i', len(self.DiagnosticInfos))
        b.append(self.DiagnosticInfos.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.ResponseHeader.from_binary(data)
        self.NoOfResults = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.Results.from_binary(data)
        self.NoOfDiagnosticInfos = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.DiagnosticInfos.from_binary(data)
        return data

class AddReferencesItem(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.SourceNodeId = None
        self.ReferenceTypeId = None
        self.IsForward = None
        self.TargetServerUri = None
        self.TargetNodeId = None
        self.TargetNodeClass = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.SourceNodeId.to_binary())
        b.append(self.ReferenceTypeId.to_binary())
        b.append(struct.pack('!?', self.IsForward))
        b.append(self.TargetServerUri.to_binary())
        b.append(self.TargetNodeId.to_binary())
        b.append(self.TargetNodeClass.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.SourceNodeId.from_binary(data)
        data = self.ReferenceTypeId.from_binary(data)
        self.IsForward = struct.unpack(?, data[:1])
        data = data[1:]
        data = self.TargetServerUri.from_binary(data)
        data = self.TargetNodeId.from_binary(data)
        data = self.TargetNodeClass.from_binary(data)
        return data

class AddReferencesRequest(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.RequestHeader = None
        self.NoOfReferencesToAdd = None
        self.ReferencesToAdd = []

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.RequestHeader.to_binary())
        b.append(struct.pack('!i', self.NoOfReferencesToAdd))
        b.append(struct.pack('!i', len(self.ReferencesToAdd))
        b.append(self.ReferencesToAdd.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.RequestHeader.from_binary(data)
        self.NoOfReferencesToAdd = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.ReferencesToAdd.from_binary(data)
        return data

class AddReferencesResponse(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.ResponseHeader = None
        self.NoOfResults = None
        self.Results = []
        self.NoOfDiagnosticInfos = None
        self.DiagnosticInfos = []

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.ResponseHeader.to_binary())
        b.append(struct.pack('!i', self.NoOfResults))
        b.append(struct.pack('!i', len(self.Results))
        b.append(self.Results.to_binary())
        b.append(struct.pack('!i', self.NoOfDiagnosticInfos))
        b.append(struct.pack('!i', len(self.DiagnosticInfos))
        b.append(self.DiagnosticInfos.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.ResponseHeader.from_binary(data)
        self.NoOfResults = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.Results.from_binary(data)
        self.NoOfDiagnosticInfos = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.DiagnosticInfos.from_binary(data)
        return data

class DeleteNodesItem(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.NodeId = None
        self.DeleteTargetReferences = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.NodeId.to_binary())
        b.append(struct.pack('!?', self.DeleteTargetReferences))
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.NodeId.from_binary(data)
        self.DeleteTargetReferences = struct.unpack(?, data[:1])
        data = data[1:]
        return data

class DeleteNodesRequest(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.RequestHeader = None
        self.NoOfNodesToDelete = None
        self.NodesToDelete = []

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.RequestHeader.to_binary())
        b.append(struct.pack('!i', self.NoOfNodesToDelete))
        b.append(struct.pack('!i', len(self.NodesToDelete))
        b.append(self.NodesToDelete.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.RequestHeader.from_binary(data)
        self.NoOfNodesToDelete = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.NodesToDelete.from_binary(data)
        return data

class DeleteNodesResponse(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.ResponseHeader = None
        self.NoOfResults = None
        self.Results = []
        self.NoOfDiagnosticInfos = None
        self.DiagnosticInfos = []

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.ResponseHeader.to_binary())
        b.append(struct.pack('!i', self.NoOfResults))
        b.append(struct.pack('!i', len(self.Results))
        b.append(self.Results.to_binary())
        b.append(struct.pack('!i', self.NoOfDiagnosticInfos))
        b.append(struct.pack('!i', len(self.DiagnosticInfos))
        b.append(self.DiagnosticInfos.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.ResponseHeader.from_binary(data)
        self.NoOfResults = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.Results.from_binary(data)
        self.NoOfDiagnosticInfos = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.DiagnosticInfos.from_binary(data)
        return data

class DeleteReferencesItem(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.SourceNodeId = None
        self.ReferenceTypeId = None
        self.IsForward = None
        self.TargetNodeId = None
        self.DeleteBidirectional = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.SourceNodeId.to_binary())
        b.append(self.ReferenceTypeId.to_binary())
        b.append(struct.pack('!?', self.IsForward))
        b.append(self.TargetNodeId.to_binary())
        b.append(struct.pack('!?', self.DeleteBidirectional))
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.SourceNodeId.from_binary(data)
        data = self.ReferenceTypeId.from_binary(data)
        self.IsForward = struct.unpack(?, data[:1])
        data = data[1:]
        data = self.TargetNodeId.from_binary(data)
        self.DeleteBidirectional = struct.unpack(?, data[:1])
        data = data[1:]
        return data

class DeleteReferencesRequest(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.RequestHeader = None
        self.NoOfReferencesToDelete = None
        self.ReferencesToDelete = []

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.RequestHeader.to_binary())
        b.append(struct.pack('!i', self.NoOfReferencesToDelete))
        b.append(struct.pack('!i', len(self.ReferencesToDelete))
        b.append(self.ReferencesToDelete.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.RequestHeader.from_binary(data)
        self.NoOfReferencesToDelete = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.ReferencesToDelete.from_binary(data)
        return data

class DeleteReferencesResponse(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.ResponseHeader = None
        self.NoOfResults = None
        self.Results = []
        self.NoOfDiagnosticInfos = None
        self.DiagnosticInfos = []

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.ResponseHeader.to_binary())
        b.append(struct.pack('!i', self.NoOfResults))
        b.append(struct.pack('!i', len(self.Results))
        b.append(self.Results.to_binary())
        b.append(struct.pack('!i', self.NoOfDiagnosticInfos))
        b.append(struct.pack('!i', len(self.DiagnosticInfos))
        b.append(self.DiagnosticInfos.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.ResponseHeader.from_binary(data)
        self.NoOfResults = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.Results.from_binary(data)
        self.NoOfDiagnosticInfos = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.DiagnosticInfos.from_binary(data)
        return data

class ViewDescription(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.ViewId = None
        self.Timestamp = None
        self.ViewVersion = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.ViewId.to_binary())
        b.append(struct.pack('!d', self.Timestamp))
        b.append(struct.pack('!I', self.ViewVersion))
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.ViewId.from_binary(data)
        self.Timestamp = struct.unpack(d, data[:8])
        data = data[8:]
        self.ViewVersion = struct.unpack(I, data[:4])
        data = data[4:]
        return data

class BrowseDescription(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.NodeId = None
        self.BrowseDirection = None
        self.ReferenceTypeId = None
        self.IncludeSubtypes = None
        self.NodeClassMask = None
        self.ResultMask = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.NodeId.to_binary())
        b.append(self.BrowseDirection.to_binary())
        b.append(self.ReferenceTypeId.to_binary())
        b.append(struct.pack('!?', self.IncludeSubtypes))
        b.append(struct.pack('!I', self.NodeClassMask))
        b.append(struct.pack('!I', self.ResultMask))
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.NodeId.from_binary(data)
        data = self.BrowseDirection.from_binary(data)
        data = self.ReferenceTypeId.from_binary(data)
        self.IncludeSubtypes = struct.unpack(?, data[:1])
        data = data[1:]
        self.NodeClassMask = struct.unpack(I, data[:4])
        data = data[4:]
        self.ResultMask = struct.unpack(I, data[:4])
        data = data[4:]
        return data

class ReferenceDescription(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.ReferenceTypeId = None
        self.IsForward = None
        self.NodeId = None
        self.BrowseName = None
        self.DisplayName = None
        self.NodeClass = None
        self.TypeDefinition = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.ReferenceTypeId.to_binary())
        b.append(struct.pack('!?', self.IsForward))
        b.append(self.NodeId.to_binary())
        b.append(self.BrowseName.to_binary())
        b.append(self.DisplayName.to_binary())
        b.append(self.NodeClass.to_binary())
        b.append(self.TypeDefinition.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.ReferenceTypeId.from_binary(data)
        self.IsForward = struct.unpack(?, data[:1])
        data = data[1:]
        data = self.NodeId.from_binary(data)
        data = self.BrowseName.from_binary(data)
        data = self.DisplayName.from_binary(data)
        data = self.NodeClass.from_binary(data)
        data = self.TypeDefinition.from_binary(data)
        return data

class BrowseResult(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.StatusCode = None
        self.ContinuationPoint = None
        self.NoOfReferences = None
        self.References = []

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.StatusCode.to_binary())
        b.append(self.ContinuationPoint.to_binary())
        b.append(struct.pack('!i', self.NoOfReferences))
        b.append(struct.pack('!i', len(self.References))
        b.append(self.References.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.StatusCode.from_binary(data)
        data = self.ContinuationPoint.from_binary(data)
        self.NoOfReferences = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.References.from_binary(data)
        return data

class BrowseRequest(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.RequestHeader = None
        self.View = None
        self.RequestedMaxReferencesPerNode = None
        self.NoOfNodesToBrowse = None
        self.NodesToBrowse = []

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.RequestHeader.to_binary())
        b.append(self.View.to_binary())
        b.append(struct.pack('!I', self.RequestedMaxReferencesPerNode))
        b.append(struct.pack('!i', self.NoOfNodesToBrowse))
        b.append(struct.pack('!i', len(self.NodesToBrowse))
        b.append(self.NodesToBrowse.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.RequestHeader.from_binary(data)
        data = self.View.from_binary(data)
        self.RequestedMaxReferencesPerNode = struct.unpack(I, data[:4])
        data = data[4:]
        self.NoOfNodesToBrowse = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.NodesToBrowse.from_binary(data)
        return data

class BrowseResponse(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.ResponseHeader = None
        self.NoOfResults = None
        self.Results = []
        self.NoOfDiagnosticInfos = None
        self.DiagnosticInfos = []

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.ResponseHeader.to_binary())
        b.append(struct.pack('!i', self.NoOfResults))
        b.append(struct.pack('!i', len(self.Results))
        b.append(self.Results.to_binary())
        b.append(struct.pack('!i', self.NoOfDiagnosticInfos))
        b.append(struct.pack('!i', len(self.DiagnosticInfos))
        b.append(self.DiagnosticInfos.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.ResponseHeader.from_binary(data)
        self.NoOfResults = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.Results.from_binary(data)
        self.NoOfDiagnosticInfos = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.DiagnosticInfos.from_binary(data)
        return data

class BrowseNextRequest(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.RequestHeader = None
        self.ReleaseContinuationPoints = None
        self.NoOfContinuationPoints = None
        self.ContinuationPoints = []

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.RequestHeader.to_binary())
        b.append(struct.pack('!?', self.ReleaseContinuationPoints))
        b.append(struct.pack('!i', self.NoOfContinuationPoints))
        b.append(struct.pack('!i', len(self.ContinuationPoints))
        b.append(self.ContinuationPoints.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.RequestHeader.from_binary(data)
        self.ReleaseContinuationPoints = struct.unpack(?, data[:1])
        data = data[1:]
        self.NoOfContinuationPoints = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.ContinuationPoints.from_binary(data)
        return data

class BrowseNextResponse(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.ResponseHeader = None
        self.NoOfResults = None
        self.Results = []
        self.NoOfDiagnosticInfos = None
        self.DiagnosticInfos = []

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.ResponseHeader.to_binary())
        b.append(struct.pack('!i', self.NoOfResults))
        b.append(struct.pack('!i', len(self.Results))
        b.append(self.Results.to_binary())
        b.append(struct.pack('!i', self.NoOfDiagnosticInfos))
        b.append(struct.pack('!i', len(self.DiagnosticInfos))
        b.append(self.DiagnosticInfos.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.ResponseHeader.from_binary(data)
        self.NoOfResults = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.Results.from_binary(data)
        self.NoOfDiagnosticInfos = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.DiagnosticInfos.from_binary(data)
        return data

class RelativePathElement(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.ReferenceTypeId = None
        self.IsInverse = None
        self.IncludeSubtypes = None
        self.TargetName = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.ReferenceTypeId.to_binary())
        b.append(struct.pack('!?', self.IsInverse))
        b.append(struct.pack('!?', self.IncludeSubtypes))
        b.append(self.TargetName.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.ReferenceTypeId.from_binary(data)
        self.IsInverse = struct.unpack(?, data[:1])
        data = data[1:]
        self.IncludeSubtypes = struct.unpack(?, data[:1])
        data = data[1:]
        data = self.TargetName.from_binary(data)
        return data

class RelativePath(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.NoOfElements = None
        self.Elements = []

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(struct.pack('!i', self.NoOfElements))
        b.append(struct.pack('!i', len(self.Elements))
        b.append(self.Elements.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        self.NoOfElements = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.Elements.from_binary(data)
        return data

class BrowsePath(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.StartingNode = None
        self.RelativePath = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.StartingNode.to_binary())
        b.append(self.RelativePath.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.StartingNode.from_binary(data)
        data = self.RelativePath.from_binary(data)
        return data

class BrowsePathTarget(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.TargetId = None
        self.RemainingPathIndex = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.TargetId.to_binary())
        b.append(struct.pack('!I', self.RemainingPathIndex))
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.TargetId.from_binary(data)
        self.RemainingPathIndex = struct.unpack(I, data[:4])
        data = data[4:]
        return data

class BrowsePathResult(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.StatusCode = None
        self.NoOfTargets = None
        self.Targets = []

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.StatusCode.to_binary())
        b.append(struct.pack('!i', self.NoOfTargets))
        b.append(struct.pack('!i', len(self.Targets))
        b.append(self.Targets.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.StatusCode.from_binary(data)
        self.NoOfTargets = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.Targets.from_binary(data)
        return data

class TranslateBrowsePathsToNodeIdsRequest(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.RequestHeader = None
        self.NoOfBrowsePaths = None
        self.BrowsePaths = []

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.RequestHeader.to_binary())
        b.append(struct.pack('!i', self.NoOfBrowsePaths))
        b.append(struct.pack('!i', len(self.BrowsePaths))
        b.append(self.BrowsePaths.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.RequestHeader.from_binary(data)
        self.NoOfBrowsePaths = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.BrowsePaths.from_binary(data)
        return data

class TranslateBrowsePathsToNodeIdsResponse(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.ResponseHeader = None
        self.NoOfResults = None
        self.Results = []
        self.NoOfDiagnosticInfos = None
        self.DiagnosticInfos = []

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.ResponseHeader.to_binary())
        b.append(struct.pack('!i', self.NoOfResults))
        b.append(struct.pack('!i', len(self.Results))
        b.append(self.Results.to_binary())
        b.append(struct.pack('!i', self.NoOfDiagnosticInfos))
        b.append(struct.pack('!i', len(self.DiagnosticInfos))
        b.append(self.DiagnosticInfos.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.ResponseHeader.from_binary(data)
        self.NoOfResults = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.Results.from_binary(data)
        self.NoOfDiagnosticInfos = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.DiagnosticInfos.from_binary(data)
        return data

class RegisterNodesRequest(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.RequestHeader = None
        self.NoOfNodesToRegister = None
        self.NodesToRegister = []

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.RequestHeader.to_binary())
        b.append(struct.pack('!i', self.NoOfNodesToRegister))
        b.append(struct.pack('!i', len(self.NodesToRegister))
        b.append(self.NodesToRegister.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.RequestHeader.from_binary(data)
        self.NoOfNodesToRegister = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.NodesToRegister.from_binary(data)
        return data

class RegisterNodesResponse(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.ResponseHeader = None
        self.NoOfRegisteredNodeIds = None
        self.RegisteredNodeIds = []

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.ResponseHeader.to_binary())
        b.append(struct.pack('!i', self.NoOfRegisteredNodeIds))
        b.append(struct.pack('!i', len(self.RegisteredNodeIds))
        b.append(self.RegisteredNodeIds.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.ResponseHeader.from_binary(data)
        self.NoOfRegisteredNodeIds = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.RegisteredNodeIds.from_binary(data)
        return data

class UnregisterNodesRequest(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.RequestHeader = None
        self.NoOfNodesToUnregister = None
        self.NodesToUnregister = []

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.RequestHeader.to_binary())
        b.append(struct.pack('!i', self.NoOfNodesToUnregister))
        b.append(struct.pack('!i', len(self.NodesToUnregister))
        b.append(self.NodesToUnregister.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.RequestHeader.from_binary(data)
        self.NoOfNodesToUnregister = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.NodesToUnregister.from_binary(data)
        return data

class UnregisterNodesResponse(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.ResponseHeader = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.ResponseHeader.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.ResponseHeader.from_binary(data)
        return data

class EndpointConfiguration(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.OperationTimeout = None
        self.UseBinaryEncoding = None
        self.MaxStringLength = None
        self.MaxByteStringLength = None
        self.MaxArrayLength = None
        self.MaxMessageSize = None
        self.MaxBufferSize = None
        self.ChannelLifetime = None
        self.SecurityTokenLifetime = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(struct.pack('!i', self.OperationTimeout))
        b.append(struct.pack('!?', self.UseBinaryEncoding))
        b.append(struct.pack('!i', self.MaxStringLength))
        b.append(struct.pack('!i', self.MaxByteStringLength))
        b.append(struct.pack('!i', self.MaxArrayLength))
        b.append(struct.pack('!i', self.MaxMessageSize))
        b.append(struct.pack('!i', self.MaxBufferSize))
        b.append(struct.pack('!i', self.ChannelLifetime))
        b.append(struct.pack('!i', self.SecurityTokenLifetime))
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        self.OperationTimeout = struct.unpack(i, data[:4])
        data = data[4:]
        self.UseBinaryEncoding = struct.unpack(?, data[:1])
        data = data[1:]
        self.MaxStringLength = struct.unpack(i, data[:4])
        data = data[4:]
        self.MaxByteStringLength = struct.unpack(i, data[:4])
        data = data[4:]
        self.MaxArrayLength = struct.unpack(i, data[:4])
        data = data[4:]
        self.MaxMessageSize = struct.unpack(i, data[:4])
        data = data[4:]
        self.MaxBufferSize = struct.unpack(i, data[:4])
        data = data[4:]
        self.ChannelLifetime = struct.unpack(i, data[:4])
        data = data[4:]
        self.SecurityTokenLifetime = struct.unpack(i, data[:4])
        data = data[4:]
        return data

class SupportedProfile(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.OrganizationUri = None
        self.ProfileId = None
        self.ComplianceTool = None
        self.ComplianceDate = None
        self.ComplianceLevel = None
        self.NoOfUnsupportedUnitIds = None
        self.UnsupportedUnitIds = []

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.OrganizationUri.to_binary())
        b.append(self.ProfileId.to_binary())
        b.append(self.ComplianceTool.to_binary())
        b.append(struct.pack('!d', self.ComplianceDate))
        b.append(self.ComplianceLevel.to_binary())
        b.append(struct.pack('!i', self.NoOfUnsupportedUnitIds))
        b.append(struct.pack('!i', len(self.UnsupportedUnitIds))
        b.append(self.UnsupportedUnitIds.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.OrganizationUri.from_binary(data)
        data = self.ProfileId.from_binary(data)
        data = self.ComplianceTool.from_binary(data)
        self.ComplianceDate = struct.unpack(d, data[:8])
        data = data[8:]
        data = self.ComplianceLevel.from_binary(data)
        self.NoOfUnsupportedUnitIds = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.UnsupportedUnitIds.from_binary(data)
        return data

class SoftwareCertificate(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.ProductName = None
        self.ProductUri = None
        self.VendorName = None
        self.VendorProductCertificate = None
        self.SoftwareVersion = None
        self.BuildNumber = None
        self.BuildDate = None
        self.IssuedBy = None
        self.IssueDate = None
        self.NoOfSupportedProfiles = None
        self.SupportedProfiles = []

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.ProductName.to_binary())
        b.append(self.ProductUri.to_binary())
        b.append(self.VendorName.to_binary())
        b.append(self.VendorProductCertificate.to_binary())
        b.append(self.SoftwareVersion.to_binary())
        b.append(self.BuildNumber.to_binary())
        b.append(struct.pack('!d', self.BuildDate))
        b.append(self.IssuedBy.to_binary())
        b.append(struct.pack('!d', self.IssueDate))
        b.append(struct.pack('!i', self.NoOfSupportedProfiles))
        b.append(struct.pack('!i', len(self.SupportedProfiles))
        b.append(self.SupportedProfiles.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.ProductName.from_binary(data)
        data = self.ProductUri.from_binary(data)
        data = self.VendorName.from_binary(data)
        data = self.VendorProductCertificate.from_binary(data)
        data = self.SoftwareVersion.from_binary(data)
        data = self.BuildNumber.from_binary(data)
        self.BuildDate = struct.unpack(d, data[:8])
        data = data[8:]
        data = self.IssuedBy.from_binary(data)
        self.IssueDate = struct.unpack(d, data[:8])
        data = data[8:]
        self.NoOfSupportedProfiles = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.SupportedProfiles.from_binary(data)
        return data

class QueryDataDescription(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.RelativePath = None
        self.AttributeId = None
        self.IndexRange = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.RelativePath.to_binary())
        b.append(struct.pack('!I', self.AttributeId))
        b.append(self.IndexRange.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.RelativePath.from_binary(data)
        self.AttributeId = struct.unpack(I, data[:4])
        data = data[4:]
        data = self.IndexRange.from_binary(data)
        return data

class NodeTypeDescription(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.TypeDefinitionNode = None
        self.IncludeSubTypes = None
        self.NoOfDataToReturn = None
        self.DataToReturn = []

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.TypeDefinitionNode.to_binary())
        b.append(struct.pack('!?', self.IncludeSubTypes))
        b.append(struct.pack('!i', self.NoOfDataToReturn))
        b.append(struct.pack('!i', len(self.DataToReturn))
        b.append(self.DataToReturn.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.TypeDefinitionNode.from_binary(data)
        self.IncludeSubTypes = struct.unpack(?, data[:1])
        data = data[1:]
        self.NoOfDataToReturn = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.DataToReturn.from_binary(data)
        return data

class QueryDataSet(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.NodeId = None
        self.TypeDefinitionNode = None
        self.NoOfValues = None
        self.Values = []

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.NodeId.to_binary())
        b.append(self.TypeDefinitionNode.to_binary())
        b.append(struct.pack('!i', self.NoOfValues))
        b.append(struct.pack('!i', len(self.Values))
        b.append(self.Values.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.NodeId.from_binary(data)
        data = self.TypeDefinitionNode.from_binary(data)
        self.NoOfValues = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.Values.from_binary(data)
        return data

class NodeReference(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.NodeId = None
        self.ReferenceTypeId = None
        self.IsForward = None
        self.NoOfReferencedNodeIds = None
        self.ReferencedNodeIds = []

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.NodeId.to_binary())
        b.append(self.ReferenceTypeId.to_binary())
        b.append(struct.pack('!?', self.IsForward))
        b.append(struct.pack('!i', self.NoOfReferencedNodeIds))
        b.append(struct.pack('!i', len(self.ReferencedNodeIds))
        b.append(self.ReferencedNodeIds.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.NodeId.from_binary(data)
        data = self.ReferenceTypeId.from_binary(data)
        self.IsForward = struct.unpack(?, data[:1])
        data = data[1:]
        self.NoOfReferencedNodeIds = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.ReferencedNodeIds.from_binary(data)
        return data

class ContentFilterElement(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.FilterOperator = None
        self.NoOfFilterOperands = None
        self.FilterOperands = []

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.FilterOperator.to_binary())
        b.append(struct.pack('!i', self.NoOfFilterOperands))
        b.append(struct.pack('!i', len(self.FilterOperands))
        b.append(self.FilterOperands.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.FilterOperator.from_binary(data)
        self.NoOfFilterOperands = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.FilterOperands.from_binary(data)
        return data

class ContentFilter(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.NoOfElements = None
        self.Elements = []

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(struct.pack('!i', self.NoOfElements))
        b.append(struct.pack('!i', len(self.Elements))
        b.append(self.Elements.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        self.NoOfElements = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.Elements.from_binary(data)
        return data

class FilterOperand(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        return data

class ElementOperand(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.Index = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(struct.pack('!I', self.Index))
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        self.Index = struct.unpack(I, data[:4])
        data = data[4:]
        return data

class LiteralOperand(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.Value = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.Value.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.Value.from_binary(data)
        return data

class AttributeOperand(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.NodeId = None
        self.Alias = None
        self.BrowsePath = None
        self.AttributeId = None
        self.IndexRange = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.NodeId.to_binary())
        b.append(self.Alias.to_binary())
        b.append(self.BrowsePath.to_binary())
        b.append(struct.pack('!I', self.AttributeId))
        b.append(self.IndexRange.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.NodeId.from_binary(data)
        data = self.Alias.from_binary(data)
        data = self.BrowsePath.from_binary(data)
        self.AttributeId = struct.unpack(I, data[:4])
        data = data[4:]
        data = self.IndexRange.from_binary(data)
        return data

class SimpleAttributeOperand(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.TypeDefinitionId = None
        self.NoOfBrowsePath = None
        self.BrowsePath = []
        self.AttributeId = None
        self.IndexRange = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.TypeDefinitionId.to_binary())
        b.append(struct.pack('!i', self.NoOfBrowsePath))
        b.append(struct.pack('!i', len(self.BrowsePath))
        b.append(self.BrowsePath.to_binary())
        b.append(struct.pack('!I', self.AttributeId))
        b.append(self.IndexRange.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.TypeDefinitionId.from_binary(data)
        self.NoOfBrowsePath = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.BrowsePath.from_binary(data)
        self.AttributeId = struct.unpack(I, data[:4])
        data = data[4:]
        data = self.IndexRange.from_binary(data)
        return data

class ContentFilterElementResult(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.StatusCode = None
        self.NoOfOperandStatusCodes = None
        self.OperandStatusCodes = []
        self.NoOfOperandDiagnosticInfos = None
        self.OperandDiagnosticInfos = []

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.StatusCode.to_binary())
        b.append(struct.pack('!i', self.NoOfOperandStatusCodes))
        b.append(struct.pack('!i', len(self.OperandStatusCodes))
        b.append(self.OperandStatusCodes.to_binary())
        b.append(struct.pack('!i', self.NoOfOperandDiagnosticInfos))
        b.append(struct.pack('!i', len(self.OperandDiagnosticInfos))
        b.append(self.OperandDiagnosticInfos.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.StatusCode.from_binary(data)
        self.NoOfOperandStatusCodes = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.OperandStatusCodes.from_binary(data)
        self.NoOfOperandDiagnosticInfos = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.OperandDiagnosticInfos.from_binary(data)
        return data

class ContentFilterResult(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.NoOfElementResults = None
        self.ElementResults = []
        self.NoOfElementDiagnosticInfos = None
        self.ElementDiagnosticInfos = []

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(struct.pack('!i', self.NoOfElementResults))
        b.append(struct.pack('!i', len(self.ElementResults))
        b.append(self.ElementResults.to_binary())
        b.append(struct.pack('!i', self.NoOfElementDiagnosticInfos))
        b.append(struct.pack('!i', len(self.ElementDiagnosticInfos))
        b.append(self.ElementDiagnosticInfos.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        self.NoOfElementResults = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.ElementResults.from_binary(data)
        self.NoOfElementDiagnosticInfos = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.ElementDiagnosticInfos.from_binary(data)
        return data

class ParsingResult(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.StatusCode = None
        self.NoOfDataStatusCodes = None
        self.DataStatusCodes = []
        self.NoOfDataDiagnosticInfos = None
        self.DataDiagnosticInfos = []

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.StatusCode.to_binary())
        b.append(struct.pack('!i', self.NoOfDataStatusCodes))
        b.append(struct.pack('!i', len(self.DataStatusCodes))
        b.append(self.DataStatusCodes.to_binary())
        b.append(struct.pack('!i', self.NoOfDataDiagnosticInfos))
        b.append(struct.pack('!i', len(self.DataDiagnosticInfos))
        b.append(self.DataDiagnosticInfos.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.StatusCode.from_binary(data)
        self.NoOfDataStatusCodes = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.DataStatusCodes.from_binary(data)
        self.NoOfDataDiagnosticInfos = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.DataDiagnosticInfos.from_binary(data)
        return data

class QueryFirstRequest(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.RequestHeader = None
        self.View = None
        self.NoOfNodeTypes = None
        self.NodeTypes = []
        self.Filter = None
        self.MaxDataSetsToReturn = None
        self.MaxReferencesToReturn = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.RequestHeader.to_binary())
        b.append(self.View.to_binary())
        b.append(struct.pack('!i', self.NoOfNodeTypes))
        b.append(struct.pack('!i', len(self.NodeTypes))
        b.append(self.NodeTypes.to_binary())
        b.append(self.Filter.to_binary())
        b.append(struct.pack('!I', self.MaxDataSetsToReturn))
        b.append(struct.pack('!I', self.MaxReferencesToReturn))
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.RequestHeader.from_binary(data)
        data = self.View.from_binary(data)
        self.NoOfNodeTypes = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.NodeTypes.from_binary(data)
        data = self.Filter.from_binary(data)
        self.MaxDataSetsToReturn = struct.unpack(I, data[:4])
        data = data[4:]
        self.MaxReferencesToReturn = struct.unpack(I, data[:4])
        data = data[4:]
        return data

class QueryFirstResponse(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.ResponseHeader = None
        self.NoOfQueryDataSets = None
        self.QueryDataSets = []
        self.ContinuationPoint = None
        self.NoOfParsingResults = None
        self.ParsingResults = []
        self.NoOfDiagnosticInfos = None
        self.DiagnosticInfos = []
        self.FilterResult = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.ResponseHeader.to_binary())
        b.append(struct.pack('!i', self.NoOfQueryDataSets))
        b.append(struct.pack('!i', len(self.QueryDataSets))
        b.append(self.QueryDataSets.to_binary())
        b.append(self.ContinuationPoint.to_binary())
        b.append(struct.pack('!i', self.NoOfParsingResults))
        b.append(struct.pack('!i', len(self.ParsingResults))
        b.append(self.ParsingResults.to_binary())
        b.append(struct.pack('!i', self.NoOfDiagnosticInfos))
        b.append(struct.pack('!i', len(self.DiagnosticInfos))
        b.append(self.DiagnosticInfos.to_binary())
        b.append(self.FilterResult.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.ResponseHeader.from_binary(data)
        self.NoOfQueryDataSets = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.QueryDataSets.from_binary(data)
        data = self.ContinuationPoint.from_binary(data)
        self.NoOfParsingResults = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.ParsingResults.from_binary(data)
        self.NoOfDiagnosticInfos = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.DiagnosticInfos.from_binary(data)
        data = self.FilterResult.from_binary(data)
        return data

class QueryNextRequest(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.RequestHeader = None
        self.ReleaseContinuationPoint = None
        self.ContinuationPoint = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.RequestHeader.to_binary())
        b.append(struct.pack('!?', self.ReleaseContinuationPoint))
        b.append(self.ContinuationPoint.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.RequestHeader.from_binary(data)
        self.ReleaseContinuationPoint = struct.unpack(?, data[:1])
        data = data[1:]
        data = self.ContinuationPoint.from_binary(data)
        return data

class QueryNextResponse(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.ResponseHeader = None
        self.NoOfQueryDataSets = None
        self.QueryDataSets = []
        self.RevisedContinuationPoint = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.ResponseHeader.to_binary())
        b.append(struct.pack('!i', self.NoOfQueryDataSets))
        b.append(struct.pack('!i', len(self.QueryDataSets))
        b.append(self.QueryDataSets.to_binary())
        b.append(self.RevisedContinuationPoint.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.ResponseHeader.from_binary(data)
        self.NoOfQueryDataSets = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.QueryDataSets.from_binary(data)
        data = self.RevisedContinuationPoint.from_binary(data)
        return data

class ReadValueId(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.NodeId = None
        self.AttributeId = None
        self.IndexRange = None
        self.DataEncoding = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.NodeId.to_binary())
        b.append(struct.pack('!I', self.AttributeId))
        b.append(self.IndexRange.to_binary())
        b.append(self.DataEncoding.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.NodeId.from_binary(data)
        self.AttributeId = struct.unpack(I, data[:4])
        data = data[4:]
        data = self.IndexRange.from_binary(data)
        data = self.DataEncoding.from_binary(data)
        return data

class ReadRequest(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.RequestHeader = None
        self.MaxAge = None
        self.TimestampsToReturn = None
        self.NoOfNodesToRead = None
        self.NodesToRead = []

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.RequestHeader.to_binary())
        b.append(struct.pack('!d', self.MaxAge))
        b.append(self.TimestampsToReturn.to_binary())
        b.append(struct.pack('!i', self.NoOfNodesToRead))
        b.append(struct.pack('!i', len(self.NodesToRead))
        b.append(self.NodesToRead.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.RequestHeader.from_binary(data)
        self.MaxAge = struct.unpack(d, data[:8])
        data = data[8:]
        data = self.TimestampsToReturn.from_binary(data)
        self.NoOfNodesToRead = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.NodesToRead.from_binary(data)
        return data

class ReadResponse(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.ResponseHeader = None
        self.NoOfResults = None
        self.Results = []
        self.NoOfDiagnosticInfos = None
        self.DiagnosticInfos = []

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.ResponseHeader.to_binary())
        b.append(struct.pack('!i', self.NoOfResults))
        b.append(struct.pack('!i', len(self.Results))
        b.append(self.Results.to_binary())
        b.append(struct.pack('!i', self.NoOfDiagnosticInfos))
        b.append(struct.pack('!i', len(self.DiagnosticInfos))
        b.append(self.DiagnosticInfos.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.ResponseHeader.from_binary(data)
        self.NoOfResults = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.Results.from_binary(data)
        self.NoOfDiagnosticInfos = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.DiagnosticInfos.from_binary(data)
        return data

class HistoryReadValueId(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.NodeId = None
        self.IndexRange = None
        self.DataEncoding = None
        self.ContinuationPoint = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.NodeId.to_binary())
        b.append(self.IndexRange.to_binary())
        b.append(self.DataEncoding.to_binary())
        b.append(self.ContinuationPoint.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.NodeId.from_binary(data)
        data = self.IndexRange.from_binary(data)
        data = self.DataEncoding.from_binary(data)
        data = self.ContinuationPoint.from_binary(data)
        return data

class HistoryReadResult(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.StatusCode = None
        self.ContinuationPoint = None
        self.HistoryData = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.StatusCode.to_binary())
        b.append(self.ContinuationPoint.to_binary())
        b.append(self.HistoryData.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.StatusCode.from_binary(data)
        data = self.ContinuationPoint.from_binary(data)
        data = self.HistoryData.from_binary(data)
        return data

class HistoryReadDetails(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        return data

class ReadRawModifiedDetails(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.IsReadModified = None
        self.StartTime = None
        self.EndTime = None
        self.NumValuesPerNode = None
        self.ReturnBounds = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(struct.pack('!?', self.IsReadModified))
        b.append(struct.pack('!d', self.StartTime))
        b.append(struct.pack('!d', self.EndTime))
        b.append(struct.pack('!I', self.NumValuesPerNode))
        b.append(struct.pack('!?', self.ReturnBounds))
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        self.IsReadModified = struct.unpack(?, data[:1])
        data = data[1:]
        self.StartTime = struct.unpack(d, data[:8])
        data = data[8:]
        self.EndTime = struct.unpack(d, data[:8])
        data = data[8:]
        self.NumValuesPerNode = struct.unpack(I, data[:4])
        data = data[4:]
        self.ReturnBounds = struct.unpack(?, data[:1])
        data = data[1:]
        return data

class ReadAtTimeDetails(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.NoOfReqTimes = None
        self.ReqTimes = []
        self.UseSimpleBounds = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(struct.pack('!i', self.NoOfReqTimes))
        b.append(struct.pack('!i', len(self.ReqTimes))
        b.append(struct.pack('!d', self.ReqTimes))
        b.append(struct.pack('!?', self.UseSimpleBounds))
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        self.NoOfReqTimes = struct.unpack(i, data[:4])
        data = data[4:]
        self.ReqTimes = struct.unpack(d, data[:8])
        data = data[8:]
        self.UseSimpleBounds = struct.unpack(?, data[:1])
        data = data[1:]
        return data

class HistoryData(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.NoOfDataValues = None
        self.DataValues = []

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(struct.pack('!i', self.NoOfDataValues))
        b.append(struct.pack('!i', len(self.DataValues))
        b.append(self.DataValues.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        self.NoOfDataValues = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.DataValues.from_binary(data)
        return data

class ModificationInfo(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.ModificationTime = None
        self.UpdateType = None
        self.UserName = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(struct.pack('!d', self.ModificationTime))
        b.append(self.UpdateType.to_binary())
        b.append(self.UserName.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        self.ModificationTime = struct.unpack(d, data[:8])
        data = data[8:]
        data = self.UpdateType.from_binary(data)
        data = self.UserName.from_binary(data)
        return data

class HistoryModifiedData(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.NoOfDataValues = None
        self.DataValues = []
        self.NoOfDataValues = None
        self.DataValues = []
        self.NoOfModificationInfos = None
        self.ModificationInfos = []

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(struct.pack('!i', self.NoOfDataValues))
        b.append(struct.pack('!i', len(self.DataValues))
        b.append(self.DataValues.to_binary())
        b.append(struct.pack('!i', self.NoOfDataValues))
        b.append(struct.pack('!i', len(self.DataValues))
        b.append(self.DataValues.to_binary())
        b.append(struct.pack('!i', self.NoOfModificationInfos))
        b.append(struct.pack('!i', len(self.ModificationInfos))
        b.append(self.ModificationInfos.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        self.NoOfDataValues = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.DataValues.from_binary(data)
        self.NoOfDataValues = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.DataValues.from_binary(data)
        self.NoOfModificationInfos = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.ModificationInfos.from_binary(data)
        return data

class HistoryReadRequest(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.RequestHeader = None
        self.HistoryReadDetails = None
        self.TimestampsToReturn = None
        self.ReleaseContinuationPoints = None
        self.NoOfNodesToRead = None
        self.NodesToRead = []

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.RequestHeader.to_binary())
        b.append(self.HistoryReadDetails.to_binary())
        b.append(self.TimestampsToReturn.to_binary())
        b.append(struct.pack('!?', self.ReleaseContinuationPoints))
        b.append(struct.pack('!i', self.NoOfNodesToRead))
        b.append(struct.pack('!i', len(self.NodesToRead))
        b.append(self.NodesToRead.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.RequestHeader.from_binary(data)
        data = self.HistoryReadDetails.from_binary(data)
        data = self.TimestampsToReturn.from_binary(data)
        self.ReleaseContinuationPoints = struct.unpack(?, data[:1])
        data = data[1:]
        self.NoOfNodesToRead = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.NodesToRead.from_binary(data)
        return data

class HistoryReadResponse(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.ResponseHeader = None
        self.NoOfResults = None
        self.Results = []
        self.NoOfDiagnosticInfos = None
        self.DiagnosticInfos = []

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.ResponseHeader.to_binary())
        b.append(struct.pack('!i', self.NoOfResults))
        b.append(struct.pack('!i', len(self.Results))
        b.append(self.Results.to_binary())
        b.append(struct.pack('!i', self.NoOfDiagnosticInfos))
        b.append(struct.pack('!i', len(self.DiagnosticInfos))
        b.append(self.DiagnosticInfos.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.ResponseHeader.from_binary(data)
        self.NoOfResults = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.Results.from_binary(data)
        self.NoOfDiagnosticInfos = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.DiagnosticInfos.from_binary(data)
        return data

class WriteValue(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.NodeId = None
        self.AttributeId = None
        self.IndexRange = None
        self.Value = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.NodeId.to_binary())
        b.append(struct.pack('!I', self.AttributeId))
        b.append(self.IndexRange.to_binary())
        b.append(self.Value.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.NodeId.from_binary(data)
        self.AttributeId = struct.unpack(I, data[:4])
        data = data[4:]
        data = self.IndexRange.from_binary(data)
        data = self.Value.from_binary(data)
        return data

class WriteRequest(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.RequestHeader = None
        self.NoOfNodesToWrite = None
        self.NodesToWrite = []

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.RequestHeader.to_binary())
        b.append(struct.pack('!i', self.NoOfNodesToWrite))
        b.append(struct.pack('!i', len(self.NodesToWrite))
        b.append(self.NodesToWrite.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.RequestHeader.from_binary(data)
        self.NoOfNodesToWrite = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.NodesToWrite.from_binary(data)
        return data

class WriteResponse(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.ResponseHeader = None
        self.NoOfResults = None
        self.Results = []
        self.NoOfDiagnosticInfos = None
        self.DiagnosticInfos = []

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.ResponseHeader.to_binary())
        b.append(struct.pack('!i', self.NoOfResults))
        b.append(struct.pack('!i', len(self.Results))
        b.append(self.Results.to_binary())
        b.append(struct.pack('!i', self.NoOfDiagnosticInfos))
        b.append(struct.pack('!i', len(self.DiagnosticInfos))
        b.append(self.DiagnosticInfos.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.ResponseHeader.from_binary(data)
        self.NoOfResults = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.Results.from_binary(data)
        self.NoOfDiagnosticInfos = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.DiagnosticInfos.from_binary(data)
        return data

class HistoryUpdateDetails(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.NodeId = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.NodeId.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.NodeId.from_binary(data)
        return data

class UpdateDataDetails(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.NodeId = None
        self.NodeId = None
        self.PerformInsertReplace = None
        self.NoOfUpdateValues = None
        self.UpdateValues = []

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.NodeId.to_binary())
        b.append(self.NodeId.to_binary())
        b.append(self.PerformInsertReplace.to_binary())
        b.append(struct.pack('!i', self.NoOfUpdateValues))
        b.append(struct.pack('!i', len(self.UpdateValues))
        b.append(self.UpdateValues.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.NodeId.from_binary(data)
        data = self.NodeId.from_binary(data)
        data = self.PerformInsertReplace.from_binary(data)
        self.NoOfUpdateValues = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.UpdateValues.from_binary(data)
        return data

class UpdateStructureDataDetails(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.NodeId = None
        self.NodeId = None
        self.PerformInsertReplace = None
        self.NoOfUpdateValues = None
        self.UpdateValues = []

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.NodeId.to_binary())
        b.append(self.NodeId.to_binary())
        b.append(self.PerformInsertReplace.to_binary())
        b.append(struct.pack('!i', self.NoOfUpdateValues))
        b.append(struct.pack('!i', len(self.UpdateValues))
        b.append(self.UpdateValues.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.NodeId.from_binary(data)
        data = self.NodeId.from_binary(data)
        data = self.PerformInsertReplace.from_binary(data)
        self.NoOfUpdateValues = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.UpdateValues.from_binary(data)
        return data

class DeleteRawModifiedDetails(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.NodeId = None
        self.NodeId = None
        self.IsDeleteModified = None
        self.StartTime = None
        self.EndTime = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.NodeId.to_binary())
        b.append(self.NodeId.to_binary())
        b.append(struct.pack('!?', self.IsDeleteModified))
        b.append(struct.pack('!d', self.StartTime))
        b.append(struct.pack('!d', self.EndTime))
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.NodeId.from_binary(data)
        data = self.NodeId.from_binary(data)
        self.IsDeleteModified = struct.unpack(?, data[:1])
        data = data[1:]
        self.StartTime = struct.unpack(d, data[:8])
        data = data[8:]
        self.EndTime = struct.unpack(d, data[:8])
        data = data[8:]
        return data

class DeleteAtTimeDetails(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.NodeId = None
        self.NodeId = None
        self.NoOfReqTimes = None
        self.ReqTimes = []

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.NodeId.to_binary())
        b.append(self.NodeId.to_binary())
        b.append(struct.pack('!i', self.NoOfReqTimes))
        b.append(struct.pack('!i', len(self.ReqTimes))
        b.append(struct.pack('!d', self.ReqTimes))
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.NodeId.from_binary(data)
        data = self.NodeId.from_binary(data)
        self.NoOfReqTimes = struct.unpack(i, data[:4])
        data = data[4:]
        self.ReqTimes = struct.unpack(d, data[:8])
        data = data[8:]
        return data

class DeleteEventDetails(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.NodeId = None
        self.NodeId = None
        self.NoOfEventIds = None
        self.EventIds = []

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.NodeId.to_binary())
        b.append(self.NodeId.to_binary())
        b.append(struct.pack('!i', self.NoOfEventIds))
        b.append(struct.pack('!i', len(self.EventIds))
        b.append(self.EventIds.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.NodeId.from_binary(data)
        data = self.NodeId.from_binary(data)
        self.NoOfEventIds = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.EventIds.from_binary(data)
        return data

class HistoryUpdateResult(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.StatusCode = None
        self.NoOfOperationResults = None
        self.OperationResults = []
        self.NoOfDiagnosticInfos = None
        self.DiagnosticInfos = []

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.StatusCode.to_binary())
        b.append(struct.pack('!i', self.NoOfOperationResults))
        b.append(struct.pack('!i', len(self.OperationResults))
        b.append(self.OperationResults.to_binary())
        b.append(struct.pack('!i', self.NoOfDiagnosticInfos))
        b.append(struct.pack('!i', len(self.DiagnosticInfos))
        b.append(self.DiagnosticInfos.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.StatusCode.from_binary(data)
        self.NoOfOperationResults = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.OperationResults.from_binary(data)
        self.NoOfDiagnosticInfos = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.DiagnosticInfos.from_binary(data)
        return data

class HistoryUpdateRequest(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.RequestHeader = None
        self.NoOfHistoryUpdateDetails = None
        self.HistoryUpdateDetails = []

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.RequestHeader.to_binary())
        b.append(struct.pack('!i', self.NoOfHistoryUpdateDetails))
        b.append(struct.pack('!i', len(self.HistoryUpdateDetails))
        b.append(self.HistoryUpdateDetails.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.RequestHeader.from_binary(data)
        self.NoOfHistoryUpdateDetails = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.HistoryUpdateDetails.from_binary(data)
        return data

class HistoryUpdateResponse(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.ResponseHeader = None
        self.NoOfResults = None
        self.Results = []
        self.NoOfDiagnosticInfos = None
        self.DiagnosticInfos = []

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.ResponseHeader.to_binary())
        b.append(struct.pack('!i', self.NoOfResults))
        b.append(struct.pack('!i', len(self.Results))
        b.append(self.Results.to_binary())
        b.append(struct.pack('!i', self.NoOfDiagnosticInfos))
        b.append(struct.pack('!i', len(self.DiagnosticInfos))
        b.append(self.DiagnosticInfos.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.ResponseHeader.from_binary(data)
        self.NoOfResults = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.Results.from_binary(data)
        self.NoOfDiagnosticInfos = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.DiagnosticInfos.from_binary(data)
        return data

class CallMethodRequest(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.ObjectId = None
        self.MethodId = None
        self.NoOfInputArguments = None
        self.InputArguments = []

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.ObjectId.to_binary())
        b.append(self.MethodId.to_binary())
        b.append(struct.pack('!i', self.NoOfInputArguments))
        b.append(struct.pack('!i', len(self.InputArguments))
        b.append(self.InputArguments.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.ObjectId.from_binary(data)
        data = self.MethodId.from_binary(data)
        self.NoOfInputArguments = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.InputArguments.from_binary(data)
        return data

class CallMethodResult(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.StatusCode = None
        self.NoOfInputArgumentResults = None
        self.InputArgumentResults = []
        self.NoOfInputArgumentDiagnosticInfos = None
        self.InputArgumentDiagnosticInfos = []
        self.NoOfOutputArguments = None
        self.OutputArguments = []

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.StatusCode.to_binary())
        b.append(struct.pack('!i', self.NoOfInputArgumentResults))
        b.append(struct.pack('!i', len(self.InputArgumentResults))
        b.append(self.InputArgumentResults.to_binary())
        b.append(struct.pack('!i', self.NoOfInputArgumentDiagnosticInfos))
        b.append(struct.pack('!i', len(self.InputArgumentDiagnosticInfos))
        b.append(self.InputArgumentDiagnosticInfos.to_binary())
        b.append(struct.pack('!i', self.NoOfOutputArguments))
        b.append(struct.pack('!i', len(self.OutputArguments))
        b.append(self.OutputArguments.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.StatusCode.from_binary(data)
        self.NoOfInputArgumentResults = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.InputArgumentResults.from_binary(data)
        self.NoOfInputArgumentDiagnosticInfos = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.InputArgumentDiagnosticInfos.from_binary(data)
        self.NoOfOutputArguments = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.OutputArguments.from_binary(data)
        return data

class CallRequest(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.RequestHeader = None
        self.NoOfMethodsToCall = None
        self.MethodsToCall = []

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.RequestHeader.to_binary())
        b.append(struct.pack('!i', self.NoOfMethodsToCall))
        b.append(struct.pack('!i', len(self.MethodsToCall))
        b.append(self.MethodsToCall.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.RequestHeader.from_binary(data)
        self.NoOfMethodsToCall = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.MethodsToCall.from_binary(data)
        return data

class CallResponse(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.ResponseHeader = None
        self.NoOfResults = None
        self.Results = []
        self.NoOfDiagnosticInfos = None
        self.DiagnosticInfos = []

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.ResponseHeader.to_binary())
        b.append(struct.pack('!i', self.NoOfResults))
        b.append(struct.pack('!i', len(self.Results))
        b.append(self.Results.to_binary())
        b.append(struct.pack('!i', self.NoOfDiagnosticInfos))
        b.append(struct.pack('!i', len(self.DiagnosticInfos))
        b.append(self.DiagnosticInfos.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.ResponseHeader.from_binary(data)
        self.NoOfResults = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.Results.from_binary(data)
        self.NoOfDiagnosticInfos = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.DiagnosticInfos.from_binary(data)
        return data

class MonitoringFilter(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        return data

class DataChangeFilter(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.Trigger = None
        self.DeadbandType = None
        self.DeadbandValue = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.Trigger.to_binary())
        b.append(struct.pack('!I', self.DeadbandType))
        b.append(struct.pack('!d', self.DeadbandValue))
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.Trigger.from_binary(data)
        self.DeadbandType = struct.unpack(I, data[:4])
        data = data[4:]
        self.DeadbandValue = struct.unpack(d, data[:8])
        data = data[8:]
        return data

class EventFilter(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.NoOfSelectClauses = None
        self.SelectClauses = []
        self.WhereClause = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(struct.pack('!i', self.NoOfSelectClauses))
        b.append(struct.pack('!i', len(self.SelectClauses))
        b.append(self.SelectClauses.to_binary())
        b.append(self.WhereClause.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        self.NoOfSelectClauses = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.SelectClauses.from_binary(data)
        data = self.WhereClause.from_binary(data)
        return data

class ReadEventDetails(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.NumValuesPerNode = None
        self.StartTime = None
        self.EndTime = None
        self.Filter = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(struct.pack('!I', self.NumValuesPerNode))
        b.append(struct.pack('!d', self.StartTime))
        b.append(struct.pack('!d', self.EndTime))
        b.append(self.Filter.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        self.NumValuesPerNode = struct.unpack(I, data[:4])
        data = data[4:]
        self.StartTime = struct.unpack(d, data[:8])
        data = data[8:]
        self.EndTime = struct.unpack(d, data[:8])
        data = data[8:]
        data = self.Filter.from_binary(data)
        return data

class AggregateConfiguration(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.UseServerCapabilitiesDefaults = None
        self.TreatUncertainAsBad = None
        self.PercentDataBad = None
        self.PercentDataGood = None
        self.UseSlopedExtrapolation = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(struct.pack('!?', self.UseServerCapabilitiesDefaults))
        b.append(struct.pack('!?', self.TreatUncertainAsBad))
        b.append(struct.pack('!c', self.PercentDataBad))
        b.append(struct.pack('!c', self.PercentDataGood))
        b.append(struct.pack('!?', self.UseSlopedExtrapolation))
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        self.UseServerCapabilitiesDefaults = struct.unpack(?, data[:1])
        data = data[1:]
        self.TreatUncertainAsBad = struct.unpack(?, data[:1])
        data = data[1:]
        self.PercentDataBad = struct.unpack(c, data[:1])
        data = data[1:]
        self.PercentDataGood = struct.unpack(c, data[:1])
        data = data[1:]
        self.UseSlopedExtrapolation = struct.unpack(?, data[:1])
        data = data[1:]
        return data

class ReadProcessedDetails(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.StartTime = None
        self.EndTime = None
        self.ProcessingInterval = None
        self.NoOfAggregateType = None
        self.AggregateType = []
        self.AggregateConfiguration = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(struct.pack('!d', self.StartTime))
        b.append(struct.pack('!d', self.EndTime))
        b.append(struct.pack('!d', self.ProcessingInterval))
        b.append(struct.pack('!i', self.NoOfAggregateType))
        b.append(struct.pack('!i', len(self.AggregateType))
        b.append(self.AggregateType.to_binary())
        b.append(self.AggregateConfiguration.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        self.StartTime = struct.unpack(d, data[:8])
        data = data[8:]
        self.EndTime = struct.unpack(d, data[:8])
        data = data[8:]
        self.ProcessingInterval = struct.unpack(d, data[:8])
        data = data[8:]
        self.NoOfAggregateType = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.AggregateType.from_binary(data)
        data = self.AggregateConfiguration.from_binary(data)
        return data

class AggregateFilter(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.StartTime = None
        self.AggregateType = None
        self.ProcessingInterval = None
        self.AggregateConfiguration = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(struct.pack('!d', self.StartTime))
        b.append(self.AggregateType.to_binary())
        b.append(struct.pack('!d', self.ProcessingInterval))
        b.append(self.AggregateConfiguration.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        self.StartTime = struct.unpack(d, data[:8])
        data = data[8:]
        data = self.AggregateType.from_binary(data)
        self.ProcessingInterval = struct.unpack(d, data[:8])
        data = data[8:]
        data = self.AggregateConfiguration.from_binary(data)
        return data

class MonitoringFilterResult(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        return data

class EventFilterResult(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.NoOfSelectClauseResults = None
        self.SelectClauseResults = []
        self.NoOfSelectClauseDiagnosticInfos = None
        self.SelectClauseDiagnosticInfos = []
        self.WhereClauseResult = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(struct.pack('!i', self.NoOfSelectClauseResults))
        b.append(struct.pack('!i', len(self.SelectClauseResults))
        b.append(self.SelectClauseResults.to_binary())
        b.append(struct.pack('!i', self.NoOfSelectClauseDiagnosticInfos))
        b.append(struct.pack('!i', len(self.SelectClauseDiagnosticInfos))
        b.append(self.SelectClauseDiagnosticInfos.to_binary())
        b.append(self.WhereClauseResult.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        self.NoOfSelectClauseResults = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.SelectClauseResults.from_binary(data)
        self.NoOfSelectClauseDiagnosticInfos = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.SelectClauseDiagnosticInfos.from_binary(data)
        data = self.WhereClauseResult.from_binary(data)
        return data

class HistoryUpdateEventResult(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.StatusCode = None
        self.EventFilterResult = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.StatusCode.to_binary())
        b.append(self.EventFilterResult.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.StatusCode.from_binary(data)
        data = self.EventFilterResult.from_binary(data)
        return data

class AggregateFilterResult(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.RevisedStartTime = None
        self.RevisedProcessingInterval = None
        self.RevisedAggregateConfiguration = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(struct.pack('!d', self.RevisedStartTime))
        b.append(struct.pack('!d', self.RevisedProcessingInterval))
        b.append(self.RevisedAggregateConfiguration.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        self.RevisedStartTime = struct.unpack(d, data[:8])
        data = data[8:]
        self.RevisedProcessingInterval = struct.unpack(d, data[:8])
        data = data[8:]
        data = self.RevisedAggregateConfiguration.from_binary(data)
        return data

class MonitoringParameters(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.ClientHandle = None
        self.SamplingInterval = None
        self.Filter = None
        self.QueueSize = None
        self.DiscardOldest = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(struct.pack('!I', self.ClientHandle))
        b.append(struct.pack('!d', self.SamplingInterval))
        b.append(self.Filter.to_binary())
        b.append(struct.pack('!I', self.QueueSize))
        b.append(struct.pack('!?', self.DiscardOldest))
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        self.ClientHandle = struct.unpack(I, data[:4])
        data = data[4:]
        self.SamplingInterval = struct.unpack(d, data[:8])
        data = data[8:]
        data = self.Filter.from_binary(data)
        self.QueueSize = struct.unpack(I, data[:4])
        data = data[4:]
        self.DiscardOldest = struct.unpack(?, data[:1])
        data = data[1:]
        return data

class MonitoredItemCreateRequest(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.ItemToMonitor = None
        self.MonitoringMode = None
        self.RequestedParameters = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.ItemToMonitor.to_binary())
        b.append(self.MonitoringMode.to_binary())
        b.append(self.RequestedParameters.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.ItemToMonitor.from_binary(data)
        data = self.MonitoringMode.from_binary(data)
        data = self.RequestedParameters.from_binary(data)
        return data

class MonitoredItemCreateResult(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.StatusCode = None
        self.MonitoredItemId = None
        self.RevisedSamplingInterval = None
        self.RevisedQueueSize = None
        self.FilterResult = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.StatusCode.to_binary())
        b.append(struct.pack('!I', self.MonitoredItemId))
        b.append(struct.pack('!d', self.RevisedSamplingInterval))
        b.append(struct.pack('!I', self.RevisedQueueSize))
        b.append(self.FilterResult.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.StatusCode.from_binary(data)
        self.MonitoredItemId = struct.unpack(I, data[:4])
        data = data[4:]
        self.RevisedSamplingInterval = struct.unpack(d, data[:8])
        data = data[8:]
        self.RevisedQueueSize = struct.unpack(I, data[:4])
        data = data[4:]
        data = self.FilterResult.from_binary(data)
        return data

class CreateMonitoredItemsRequest(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.RequestHeader = None
        self.SubscriptionId = None
        self.TimestampsToReturn = None
        self.NoOfItemsToCreate = None
        self.ItemsToCreate = []

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.RequestHeader.to_binary())
        b.append(struct.pack('!I', self.SubscriptionId))
        b.append(self.TimestampsToReturn.to_binary())
        b.append(struct.pack('!i', self.NoOfItemsToCreate))
        b.append(struct.pack('!i', len(self.ItemsToCreate))
        b.append(self.ItemsToCreate.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.RequestHeader.from_binary(data)
        self.SubscriptionId = struct.unpack(I, data[:4])
        data = data[4:]
        data = self.TimestampsToReturn.from_binary(data)
        self.NoOfItemsToCreate = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.ItemsToCreate.from_binary(data)
        return data

class CreateMonitoredItemsResponse(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.ResponseHeader = None
        self.NoOfResults = None
        self.Results = []
        self.NoOfDiagnosticInfos = None
        self.DiagnosticInfos = []

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.ResponseHeader.to_binary())
        b.append(struct.pack('!i', self.NoOfResults))
        b.append(struct.pack('!i', len(self.Results))
        b.append(self.Results.to_binary())
        b.append(struct.pack('!i', self.NoOfDiagnosticInfos))
        b.append(struct.pack('!i', len(self.DiagnosticInfos))
        b.append(self.DiagnosticInfos.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.ResponseHeader.from_binary(data)
        self.NoOfResults = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.Results.from_binary(data)
        self.NoOfDiagnosticInfos = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.DiagnosticInfos.from_binary(data)
        return data

class MonitoredItemModifyRequest(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.MonitoredItemId = None
        self.RequestedParameters = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(struct.pack('!I', self.MonitoredItemId))
        b.append(self.RequestedParameters.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        self.MonitoredItemId = struct.unpack(I, data[:4])
        data = data[4:]
        data = self.RequestedParameters.from_binary(data)
        return data

class MonitoredItemModifyResult(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.StatusCode = None
        self.RevisedSamplingInterval = None
        self.RevisedQueueSize = None
        self.FilterResult = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.StatusCode.to_binary())
        b.append(struct.pack('!d', self.RevisedSamplingInterval))
        b.append(struct.pack('!I', self.RevisedQueueSize))
        b.append(self.FilterResult.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.StatusCode.from_binary(data)
        self.RevisedSamplingInterval = struct.unpack(d, data[:8])
        data = data[8:]
        self.RevisedQueueSize = struct.unpack(I, data[:4])
        data = data[4:]
        data = self.FilterResult.from_binary(data)
        return data

class ModifyMonitoredItemsRequest(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.RequestHeader = None
        self.SubscriptionId = None
        self.TimestampsToReturn = None
        self.NoOfItemsToModify = None
        self.ItemsToModify = []

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.RequestHeader.to_binary())
        b.append(struct.pack('!I', self.SubscriptionId))
        b.append(self.TimestampsToReturn.to_binary())
        b.append(struct.pack('!i', self.NoOfItemsToModify))
        b.append(struct.pack('!i', len(self.ItemsToModify))
        b.append(self.ItemsToModify.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.RequestHeader.from_binary(data)
        self.SubscriptionId = struct.unpack(I, data[:4])
        data = data[4:]
        data = self.TimestampsToReturn.from_binary(data)
        self.NoOfItemsToModify = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.ItemsToModify.from_binary(data)
        return data

class ModifyMonitoredItemsResponse(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.ResponseHeader = None
        self.NoOfResults = None
        self.Results = []
        self.NoOfDiagnosticInfos = None
        self.DiagnosticInfos = []

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.ResponseHeader.to_binary())
        b.append(struct.pack('!i', self.NoOfResults))
        b.append(struct.pack('!i', len(self.Results))
        b.append(self.Results.to_binary())
        b.append(struct.pack('!i', self.NoOfDiagnosticInfos))
        b.append(struct.pack('!i', len(self.DiagnosticInfos))
        b.append(self.DiagnosticInfos.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.ResponseHeader.from_binary(data)
        self.NoOfResults = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.Results.from_binary(data)
        self.NoOfDiagnosticInfos = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.DiagnosticInfos.from_binary(data)
        return data

class SetMonitoringModeRequest(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.RequestHeader = None
        self.SubscriptionId = None
        self.MonitoringMode = None
        self.NoOfMonitoredItemIds = None
        self.MonitoredItemIds = []

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.RequestHeader.to_binary())
        b.append(struct.pack('!I', self.SubscriptionId))
        b.append(self.MonitoringMode.to_binary())
        b.append(struct.pack('!i', self.NoOfMonitoredItemIds))
        b.append(struct.pack('!i', len(self.MonitoredItemIds))
        b.append(struct.pack('!I', self.MonitoredItemIds))
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.RequestHeader.from_binary(data)
        self.SubscriptionId = struct.unpack(I, data[:4])
        data = data[4:]
        data = self.MonitoringMode.from_binary(data)
        self.NoOfMonitoredItemIds = struct.unpack(i, data[:4])
        data = data[4:]
        self.MonitoredItemIds = struct.unpack(I, data[:4])
        data = data[4:]
        return data

class SetMonitoringModeResponse(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.ResponseHeader = None
        self.NoOfResults = None
        self.Results = []
        self.NoOfDiagnosticInfos = None
        self.DiagnosticInfos = []

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.ResponseHeader.to_binary())
        b.append(struct.pack('!i', self.NoOfResults))
        b.append(struct.pack('!i', len(self.Results))
        b.append(self.Results.to_binary())
        b.append(struct.pack('!i', self.NoOfDiagnosticInfos))
        b.append(struct.pack('!i', len(self.DiagnosticInfos))
        b.append(self.DiagnosticInfos.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.ResponseHeader.from_binary(data)
        self.NoOfResults = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.Results.from_binary(data)
        self.NoOfDiagnosticInfos = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.DiagnosticInfos.from_binary(data)
        return data

class SetTriggeringRequest(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.RequestHeader = None
        self.SubscriptionId = None
        self.TriggeringItemId = None
        self.NoOfLinksToAdd = None
        self.LinksToAdd = []
        self.NoOfLinksToRemove = None
        self.LinksToRemove = []

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.RequestHeader.to_binary())
        b.append(struct.pack('!I', self.SubscriptionId))
        b.append(struct.pack('!I', self.TriggeringItemId))
        b.append(struct.pack('!i', self.NoOfLinksToAdd))
        b.append(struct.pack('!i', len(self.LinksToAdd))
        b.append(struct.pack('!I', self.LinksToAdd))
        b.append(struct.pack('!i', self.NoOfLinksToRemove))
        b.append(struct.pack('!i', len(self.LinksToRemove))
        b.append(struct.pack('!I', self.LinksToRemove))
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.RequestHeader.from_binary(data)
        self.SubscriptionId = struct.unpack(I, data[:4])
        data = data[4:]
        self.TriggeringItemId = struct.unpack(I, data[:4])
        data = data[4:]
        self.NoOfLinksToAdd = struct.unpack(i, data[:4])
        data = data[4:]
        self.LinksToAdd = struct.unpack(I, data[:4])
        data = data[4:]
        self.NoOfLinksToRemove = struct.unpack(i, data[:4])
        data = data[4:]
        self.LinksToRemove = struct.unpack(I, data[:4])
        data = data[4:]
        return data

class SetTriggeringResponse(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.ResponseHeader = None
        self.NoOfAddResults = None
        self.AddResults = []
        self.NoOfAddDiagnosticInfos = None
        self.AddDiagnosticInfos = []
        self.NoOfRemoveResults = None
        self.RemoveResults = []
        self.NoOfRemoveDiagnosticInfos = None
        self.RemoveDiagnosticInfos = []

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.ResponseHeader.to_binary())
        b.append(struct.pack('!i', self.NoOfAddResults))
        b.append(struct.pack('!i', len(self.AddResults))
        b.append(self.AddResults.to_binary())
        b.append(struct.pack('!i', self.NoOfAddDiagnosticInfos))
        b.append(struct.pack('!i', len(self.AddDiagnosticInfos))
        b.append(self.AddDiagnosticInfos.to_binary())
        b.append(struct.pack('!i', self.NoOfRemoveResults))
        b.append(struct.pack('!i', len(self.RemoveResults))
        b.append(self.RemoveResults.to_binary())
        b.append(struct.pack('!i', self.NoOfRemoveDiagnosticInfos))
        b.append(struct.pack('!i', len(self.RemoveDiagnosticInfos))
        b.append(self.RemoveDiagnosticInfos.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.ResponseHeader.from_binary(data)
        self.NoOfAddResults = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.AddResults.from_binary(data)
        self.NoOfAddDiagnosticInfos = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.AddDiagnosticInfos.from_binary(data)
        self.NoOfRemoveResults = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.RemoveResults.from_binary(data)
        self.NoOfRemoveDiagnosticInfos = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.RemoveDiagnosticInfos.from_binary(data)
        return data

class DeleteMonitoredItemsRequest(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.RequestHeader = None
        self.SubscriptionId = None
        self.NoOfMonitoredItemIds = None
        self.MonitoredItemIds = []

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.RequestHeader.to_binary())
        b.append(struct.pack('!I', self.SubscriptionId))
        b.append(struct.pack('!i', self.NoOfMonitoredItemIds))
        b.append(struct.pack('!i', len(self.MonitoredItemIds))
        b.append(struct.pack('!I', self.MonitoredItemIds))
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.RequestHeader.from_binary(data)
        self.SubscriptionId = struct.unpack(I, data[:4])
        data = data[4:]
        self.NoOfMonitoredItemIds = struct.unpack(i, data[:4])
        data = data[4:]
        self.MonitoredItemIds = struct.unpack(I, data[:4])
        data = data[4:]
        return data

class DeleteMonitoredItemsResponse(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.ResponseHeader = None
        self.NoOfResults = None
        self.Results = []
        self.NoOfDiagnosticInfos = None
        self.DiagnosticInfos = []

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.ResponseHeader.to_binary())
        b.append(struct.pack('!i', self.NoOfResults))
        b.append(struct.pack('!i', len(self.Results))
        b.append(self.Results.to_binary())
        b.append(struct.pack('!i', self.NoOfDiagnosticInfos))
        b.append(struct.pack('!i', len(self.DiagnosticInfos))
        b.append(self.DiagnosticInfos.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.ResponseHeader.from_binary(data)
        self.NoOfResults = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.Results.from_binary(data)
        self.NoOfDiagnosticInfos = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.DiagnosticInfos.from_binary(data)
        return data

class CreateSubscriptionRequest(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.RequestHeader = None
        self.RequestedPublishingInterval = None
        self.RequestedLifetimeCount = None
        self.RequestedMaxKeepAliveCount = None
        self.MaxNotificationsPerPublish = None
        self.PublishingEnabled = None
        self.Priority = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.RequestHeader.to_binary())
        b.append(struct.pack('!d', self.RequestedPublishingInterval))
        b.append(struct.pack('!I', self.RequestedLifetimeCount))
        b.append(struct.pack('!I', self.RequestedMaxKeepAliveCount))
        b.append(struct.pack('!I', self.MaxNotificationsPerPublish))
        b.append(struct.pack('!?', self.PublishingEnabled))
        b.append(struct.pack('!c', self.Priority))
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.RequestHeader.from_binary(data)
        self.RequestedPublishingInterval = struct.unpack(d, data[:8])
        data = data[8:]
        self.RequestedLifetimeCount = struct.unpack(I, data[:4])
        data = data[4:]
        self.RequestedMaxKeepAliveCount = struct.unpack(I, data[:4])
        data = data[4:]
        self.MaxNotificationsPerPublish = struct.unpack(I, data[:4])
        data = data[4:]
        self.PublishingEnabled = struct.unpack(?, data[:1])
        data = data[1:]
        self.Priority = struct.unpack(c, data[:1])
        data = data[1:]
        return data

class CreateSubscriptionResponse(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.ResponseHeader = None
        self.SubscriptionId = None
        self.RevisedPublishingInterval = None
        self.RevisedLifetimeCount = None
        self.RevisedMaxKeepAliveCount = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.ResponseHeader.to_binary())
        b.append(struct.pack('!I', self.SubscriptionId))
        b.append(struct.pack('!d', self.RevisedPublishingInterval))
        b.append(struct.pack('!I', self.RevisedLifetimeCount))
        b.append(struct.pack('!I', self.RevisedMaxKeepAliveCount))
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.ResponseHeader.from_binary(data)
        self.SubscriptionId = struct.unpack(I, data[:4])
        data = data[4:]
        self.RevisedPublishingInterval = struct.unpack(d, data[:8])
        data = data[8:]
        self.RevisedLifetimeCount = struct.unpack(I, data[:4])
        data = data[4:]
        self.RevisedMaxKeepAliveCount = struct.unpack(I, data[:4])
        data = data[4:]
        return data

class ModifySubscriptionRequest(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.RequestHeader = None
        self.SubscriptionId = None
        self.RequestedPublishingInterval = None
        self.RequestedLifetimeCount = None
        self.RequestedMaxKeepAliveCount = None
        self.MaxNotificationsPerPublish = None
        self.Priority = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.RequestHeader.to_binary())
        b.append(struct.pack('!I', self.SubscriptionId))
        b.append(struct.pack('!d', self.RequestedPublishingInterval))
        b.append(struct.pack('!I', self.RequestedLifetimeCount))
        b.append(struct.pack('!I', self.RequestedMaxKeepAliveCount))
        b.append(struct.pack('!I', self.MaxNotificationsPerPublish))
        b.append(struct.pack('!c', self.Priority))
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.RequestHeader.from_binary(data)
        self.SubscriptionId = struct.unpack(I, data[:4])
        data = data[4:]
        self.RequestedPublishingInterval = struct.unpack(d, data[:8])
        data = data[8:]
        self.RequestedLifetimeCount = struct.unpack(I, data[:4])
        data = data[4:]
        self.RequestedMaxKeepAliveCount = struct.unpack(I, data[:4])
        data = data[4:]
        self.MaxNotificationsPerPublish = struct.unpack(I, data[:4])
        data = data[4:]
        self.Priority = struct.unpack(c, data[:1])
        data = data[1:]
        return data

class ModifySubscriptionResponse(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.ResponseHeader = None
        self.RevisedPublishingInterval = None
        self.RevisedLifetimeCount = None
        self.RevisedMaxKeepAliveCount = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.ResponseHeader.to_binary())
        b.append(struct.pack('!d', self.RevisedPublishingInterval))
        b.append(struct.pack('!I', self.RevisedLifetimeCount))
        b.append(struct.pack('!I', self.RevisedMaxKeepAliveCount))
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.ResponseHeader.from_binary(data)
        self.RevisedPublishingInterval = struct.unpack(d, data[:8])
        data = data[8:]
        self.RevisedLifetimeCount = struct.unpack(I, data[:4])
        data = data[4:]
        self.RevisedMaxKeepAliveCount = struct.unpack(I, data[:4])
        data = data[4:]
        return data

class SetPublishingModeRequest(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.RequestHeader = None
        self.PublishingEnabled = None
        self.NoOfSubscriptionIds = None
        self.SubscriptionIds = []

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.RequestHeader.to_binary())
        b.append(struct.pack('!?', self.PublishingEnabled))
        b.append(struct.pack('!i', self.NoOfSubscriptionIds))
        b.append(struct.pack('!i', len(self.SubscriptionIds))
        b.append(struct.pack('!I', self.SubscriptionIds))
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.RequestHeader.from_binary(data)
        self.PublishingEnabled = struct.unpack(?, data[:1])
        data = data[1:]
        self.NoOfSubscriptionIds = struct.unpack(i, data[:4])
        data = data[4:]
        self.SubscriptionIds = struct.unpack(I, data[:4])
        data = data[4:]
        return data

class SetPublishingModeResponse(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.ResponseHeader = None
        self.NoOfResults = None
        self.Results = []
        self.NoOfDiagnosticInfos = None
        self.DiagnosticInfos = []

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.ResponseHeader.to_binary())
        b.append(struct.pack('!i', self.NoOfResults))
        b.append(struct.pack('!i', len(self.Results))
        b.append(self.Results.to_binary())
        b.append(struct.pack('!i', self.NoOfDiagnosticInfos))
        b.append(struct.pack('!i', len(self.DiagnosticInfos))
        b.append(self.DiagnosticInfos.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.ResponseHeader.from_binary(data)
        self.NoOfResults = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.Results.from_binary(data)
        self.NoOfDiagnosticInfos = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.DiagnosticInfos.from_binary(data)
        return data

class NotificationMessage(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.SequenceNumber = None
        self.PublishTime = None
        self.NoOfNotificationData = None
        self.NotificationData = []

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(struct.pack('!I', self.SequenceNumber))
        b.append(struct.pack('!d', self.PublishTime))
        b.append(struct.pack('!i', self.NoOfNotificationData))
        b.append(struct.pack('!i', len(self.NotificationData))
        b.append(self.NotificationData.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        self.SequenceNumber = struct.unpack(I, data[:4])
        data = data[4:]
        self.PublishTime = struct.unpack(d, data[:8])
        data = data[8:]
        self.NoOfNotificationData = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.NotificationData.from_binary(data)
        return data

class NotificationData(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        return data

class MonitoredItemNotification(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.ClientHandle = None
        self.Value = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(struct.pack('!I', self.ClientHandle))
        b.append(self.Value.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        self.ClientHandle = struct.unpack(I, data[:4])
        data = data[4:]
        data = self.Value.from_binary(data)
        return data

class DataChangeNotification(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.NoOfMonitoredItems = None
        self.MonitoredItems = []
        self.NoOfDiagnosticInfos = None
        self.DiagnosticInfos = []

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(struct.pack('!i', self.NoOfMonitoredItems))
        b.append(struct.pack('!i', len(self.MonitoredItems))
        b.append(self.MonitoredItems.to_binary())
        b.append(struct.pack('!i', self.NoOfDiagnosticInfos))
        b.append(struct.pack('!i', len(self.DiagnosticInfos))
        b.append(self.DiagnosticInfos.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        self.NoOfMonitoredItems = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.MonitoredItems.from_binary(data)
        self.NoOfDiagnosticInfos = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.DiagnosticInfos.from_binary(data)
        return data

class EventFieldList(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.ClientHandle = None
        self.NoOfEventFields = None
        self.EventFields = []

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(struct.pack('!I', self.ClientHandle))
        b.append(struct.pack('!i', self.NoOfEventFields))
        b.append(struct.pack('!i', len(self.EventFields))
        b.append(self.EventFields.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        self.ClientHandle = struct.unpack(I, data[:4])
        data = data[4:]
        self.NoOfEventFields = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.EventFields.from_binary(data)
        return data

class EventNotificationList(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.NoOfEvents = None
        self.Events = []

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(struct.pack('!i', self.NoOfEvents))
        b.append(struct.pack('!i', len(self.Events))
        b.append(self.Events.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        self.NoOfEvents = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.Events.from_binary(data)
        return data

class HistoryEventFieldList(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.NoOfEventFields = None
        self.EventFields = []

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(struct.pack('!i', self.NoOfEventFields))
        b.append(struct.pack('!i', len(self.EventFields))
        b.append(self.EventFields.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        self.NoOfEventFields = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.EventFields.from_binary(data)
        return data

class HistoryEvent(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.NoOfEvents = None
        self.Events = []

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(struct.pack('!i', self.NoOfEvents))
        b.append(struct.pack('!i', len(self.Events))
        b.append(self.Events.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        self.NoOfEvents = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.Events.from_binary(data)
        return data

class UpdateEventDetails(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.NodeId = None
        self.NodeId = None
        self.PerformInsertReplace = None
        self.Filter = None
        self.NoOfEventData = None
        self.EventData = []

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.NodeId.to_binary())
        b.append(self.NodeId.to_binary())
        b.append(self.PerformInsertReplace.to_binary())
        b.append(self.Filter.to_binary())
        b.append(struct.pack('!i', self.NoOfEventData))
        b.append(struct.pack('!i', len(self.EventData))
        b.append(self.EventData.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.NodeId.from_binary(data)
        data = self.NodeId.from_binary(data)
        data = self.PerformInsertReplace.from_binary(data)
        data = self.Filter.from_binary(data)
        self.NoOfEventData = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.EventData.from_binary(data)
        return data

class StatusChangeNotification(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.Status = None
        self.DiagnosticInfo = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.Status.to_binary())
        b.append(self.DiagnosticInfo.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.Status.from_binary(data)
        data = self.DiagnosticInfo.from_binary(data)
        return data

class SubscriptionAcknowledgement(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.SubscriptionId = None
        self.SequenceNumber = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(struct.pack('!I', self.SubscriptionId))
        b.append(struct.pack('!I', self.SequenceNumber))
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        self.SubscriptionId = struct.unpack(I, data[:4])
        data = data[4:]
        self.SequenceNumber = struct.unpack(I, data[:4])
        data = data[4:]
        return data

class PublishRequest(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.RequestHeader = None
        self.NoOfSubscriptionAcknowledgements = None
        self.SubscriptionAcknowledgements = []

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.RequestHeader.to_binary())
        b.append(struct.pack('!i', self.NoOfSubscriptionAcknowledgements))
        b.append(struct.pack('!i', len(self.SubscriptionAcknowledgements))
        b.append(self.SubscriptionAcknowledgements.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.RequestHeader.from_binary(data)
        self.NoOfSubscriptionAcknowledgements = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.SubscriptionAcknowledgements.from_binary(data)
        return data

class PublishResponse(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.ResponseHeader = None
        self.SubscriptionId = None
        self.NoOfAvailableSequenceNumbers = None
        self.AvailableSequenceNumbers = []
        self.MoreNotifications = None
        self.NotificationMessage = None
        self.NoOfResults = None
        self.Results = []
        self.NoOfDiagnosticInfos = None
        self.DiagnosticInfos = []

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.ResponseHeader.to_binary())
        b.append(struct.pack('!I', self.SubscriptionId))
        b.append(struct.pack('!i', self.NoOfAvailableSequenceNumbers))
        b.append(struct.pack('!i', len(self.AvailableSequenceNumbers))
        b.append(struct.pack('!I', self.AvailableSequenceNumbers))
        b.append(struct.pack('!?', self.MoreNotifications))
        b.append(self.NotificationMessage.to_binary())
        b.append(struct.pack('!i', self.NoOfResults))
        b.append(struct.pack('!i', len(self.Results))
        b.append(self.Results.to_binary())
        b.append(struct.pack('!i', self.NoOfDiagnosticInfos))
        b.append(struct.pack('!i', len(self.DiagnosticInfos))
        b.append(self.DiagnosticInfos.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.ResponseHeader.from_binary(data)
        self.SubscriptionId = struct.unpack(I, data[:4])
        data = data[4:]
        self.NoOfAvailableSequenceNumbers = struct.unpack(i, data[:4])
        data = data[4:]
        self.AvailableSequenceNumbers = struct.unpack(I, data[:4])
        data = data[4:]
        self.MoreNotifications = struct.unpack(?, data[:1])
        data = data[1:]
        data = self.NotificationMessage.from_binary(data)
        self.NoOfResults = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.Results.from_binary(data)
        self.NoOfDiagnosticInfos = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.DiagnosticInfos.from_binary(data)
        return data

class RepublishRequest(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.RequestHeader = None
        self.SubscriptionId = None
        self.RetransmitSequenceNumber = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.RequestHeader.to_binary())
        b.append(struct.pack('!I', self.SubscriptionId))
        b.append(struct.pack('!I', self.RetransmitSequenceNumber))
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.RequestHeader.from_binary(data)
        self.SubscriptionId = struct.unpack(I, data[:4])
        data = data[4:]
        self.RetransmitSequenceNumber = struct.unpack(I, data[:4])
        data = data[4:]
        return data

class RepublishResponse(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.ResponseHeader = None
        self.NotificationMessage = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.ResponseHeader.to_binary())
        b.append(self.NotificationMessage.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.ResponseHeader.from_binary(data)
        data = self.NotificationMessage.from_binary(data)
        return data

class TransferResult(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.StatusCode = None
        self.NoOfAvailableSequenceNumbers = None
        self.AvailableSequenceNumbers = []

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.StatusCode.to_binary())
        b.append(struct.pack('!i', self.NoOfAvailableSequenceNumbers))
        b.append(struct.pack('!i', len(self.AvailableSequenceNumbers))
        b.append(struct.pack('!I', self.AvailableSequenceNumbers))
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.StatusCode.from_binary(data)
        self.NoOfAvailableSequenceNumbers = struct.unpack(i, data[:4])
        data = data[4:]
        self.AvailableSequenceNumbers = struct.unpack(I, data[:4])
        data = data[4:]
        return data

class TransferSubscriptionsRequest(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.RequestHeader = None
        self.NoOfSubscriptionIds = None
        self.SubscriptionIds = []
        self.SendInitialValues = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.RequestHeader.to_binary())
        b.append(struct.pack('!i', self.NoOfSubscriptionIds))
        b.append(struct.pack('!i', len(self.SubscriptionIds))
        b.append(struct.pack('!I', self.SubscriptionIds))
        b.append(struct.pack('!?', self.SendInitialValues))
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.RequestHeader.from_binary(data)
        self.NoOfSubscriptionIds = struct.unpack(i, data[:4])
        data = data[4:]
        self.SubscriptionIds = struct.unpack(I, data[:4])
        data = data[4:]
        self.SendInitialValues = struct.unpack(?, data[:1])
        data = data[1:]
        return data

class TransferSubscriptionsResponse(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.ResponseHeader = None
        self.NoOfResults = None
        self.Results = []
        self.NoOfDiagnosticInfos = None
        self.DiagnosticInfos = []

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.ResponseHeader.to_binary())
        b.append(struct.pack('!i', self.NoOfResults))
        b.append(struct.pack('!i', len(self.Results))
        b.append(self.Results.to_binary())
        b.append(struct.pack('!i', self.NoOfDiagnosticInfos))
        b.append(struct.pack('!i', len(self.DiagnosticInfos))
        b.append(self.DiagnosticInfos.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.ResponseHeader.from_binary(data)
        self.NoOfResults = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.Results.from_binary(data)
        self.NoOfDiagnosticInfos = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.DiagnosticInfos.from_binary(data)
        return data

class DeleteSubscriptionsRequest(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.RequestHeader = None
        self.NoOfSubscriptionIds = None
        self.SubscriptionIds = []

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.RequestHeader.to_binary())
        b.append(struct.pack('!i', self.NoOfSubscriptionIds))
        b.append(struct.pack('!i', len(self.SubscriptionIds))
        b.append(struct.pack('!I', self.SubscriptionIds))
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.RequestHeader.from_binary(data)
        self.NoOfSubscriptionIds = struct.unpack(i, data[:4])
        data = data[4:]
        self.SubscriptionIds = struct.unpack(I, data[:4])
        data = data[4:]
        return data

class DeleteSubscriptionsResponse(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.ResponseHeader = None
        self.NoOfResults = None
        self.Results = []
        self.NoOfDiagnosticInfos = None
        self.DiagnosticInfos = []

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.ResponseHeader.to_binary())
        b.append(struct.pack('!i', self.NoOfResults))
        b.append(struct.pack('!i', len(self.Results))
        b.append(self.Results.to_binary())
        b.append(struct.pack('!i', self.NoOfDiagnosticInfos))
        b.append(struct.pack('!i', len(self.DiagnosticInfos))
        b.append(self.DiagnosticInfos.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.ResponseHeader.from_binary(data)
        self.NoOfResults = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.Results.from_binary(data)
        self.NoOfDiagnosticInfos = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.DiagnosticInfos.from_binary(data)
        return data

class ScalarTestType(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.Boolean = None
        self.SByte = None
        self.Byte = None
        self.Int16 = None
        self.UInt16 = None
        self.Int32 = None
        self.UInt32 = None
        self.Int64 = None
        self.UInt64 = None
        self.Float = None
        self.Double = None
        self.String = None
        self.DateTime = None
        self.Guid = None
        self.ByteString = None
        self.XmlElement = None
        self.NodeId = None
        self.ExpandedNodeId = None
        self.StatusCode = None
        self.DiagnosticInfo = None
        self.QualifiedName = None
        self.LocalizedText = None
        self.ExtensionObject = None
        self.DataValue = None
        self.EnumeratedValue = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(struct.pack('!?', self.Boolean))
        b.append(struct.pack('!B', self.SByte))
        b.append(struct.pack('!c', self.Byte))
        b.append(struct.pack('!h', self.Int16))
        b.append(struct.pack('!H', self.UInt16))
        b.append(struct.pack('!i', self.Int32))
        b.append(struct.pack('!I', self.UInt32))
        b.append(struct.pack('!q', self.Int64))
        b.append(struct.pack('!Q', self.UInt64))
        b.append(struct.pack('!f', self.Float))
        b.append(struct.pack('!d', self.Double))
        b.append(self.String.to_binary())
        b.append(struct.pack('!d', self.DateTime))
        b.append(self.Guid.to_binary())
        b.append(self.ByteString.to_binary())
        b.append(self.XmlElement.to_binary())
        b.append(self.NodeId.to_binary())
        b.append(self.ExpandedNodeId.to_binary())
        b.append(self.StatusCode.to_binary())
        b.append(self.DiagnosticInfo.to_binary())
        b.append(self.QualifiedName.to_binary())
        b.append(self.LocalizedText.to_binary())
        b.append(self.ExtensionObject.to_binary())
        b.append(self.DataValue.to_binary())
        b.append(self.EnumeratedValue.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        self.Boolean = struct.unpack(?, data[:1])
        data = data[1:]
        self.SByte = struct.unpack(B, data[:1])
        data = data[1:]
        self.Byte = struct.unpack(c, data[:1])
        data = data[1:]
        self.Int16 = struct.unpack(h, data[:2])
        data = data[2:]
        self.UInt16 = struct.unpack(H, data[:2])
        data = data[2:]
        self.Int32 = struct.unpack(i, data[:4])
        data = data[4:]
        self.UInt32 = struct.unpack(I, data[:4])
        data = data[4:]
        self.Int64 = struct.unpack(q, data[:8])
        data = data[8:]
        self.UInt64 = struct.unpack(Q, data[:8])
        data = data[8:]
        self.Float = struct.unpack(f, data[:4])
        data = data[4:]
        self.Double = struct.unpack(d, data[:8])
        data = data[8:]
        data = self.String.from_binary(data)
        self.DateTime = struct.unpack(d, data[:8])
        data = data[8:]
        data = self.Guid.from_binary(data)
        data = self.ByteString.from_binary(data)
        data = self.XmlElement.from_binary(data)
        data = self.NodeId.from_binary(data)
        data = self.ExpandedNodeId.from_binary(data)
        data = self.StatusCode.from_binary(data)
        data = self.DiagnosticInfo.from_binary(data)
        data = self.QualifiedName.from_binary(data)
        data = self.LocalizedText.from_binary(data)
        data = self.ExtensionObject.from_binary(data)
        data = self.DataValue.from_binary(data)
        data = self.EnumeratedValue.from_binary(data)
        return data

class ArrayTestType(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.NoOfBooleans = None
        self.Booleans = []
        self.NoOfSBytes = None
        self.SBytes = []
        self.NoOfInt16s = None
        self.Int16s = []
        self.NoOfUInt16s = None
        self.UInt16s = []
        self.NoOfInt32s = None
        self.Int32s = []
        self.NoOfUInt32s = None
        self.UInt32s = []
        self.NoOfInt64s = None
        self.Int64s = []
        self.NoOfUInt64s = None
        self.UInt64s = []
        self.NoOfFloats = None
        self.Floats = []
        self.NoOfDoubles = None
        self.Doubles = []
        self.NoOfStrings = None
        self.Strings = []
        self.NoOfDateTimes = None
        self.DateTimes = []
        self.NoOfGuids = None
        self.Guids = []
        self.NoOfByteStrings = None
        self.ByteStrings = []
        self.NoOfXmlElements = None
        self.XmlElements = []
        self.NoOfNodeIds = None
        self.NodeIds = []
        self.NoOfExpandedNodeIds = None
        self.ExpandedNodeIds = []
        self.NoOfStatusCodes = None
        self.StatusCodes = []
        self.NoOfDiagnosticInfos = None
        self.DiagnosticInfos = []
        self.NoOfQualifiedNames = None
        self.QualifiedNames = []
        self.NoOfLocalizedTexts = None
        self.LocalizedTexts = []
        self.NoOfExtensionObjects = None
        self.ExtensionObjects = []
        self.NoOfDataValues = None
        self.DataValues = []
        self.NoOfVariants = None
        self.Variants = []
        self.NoOfEnumeratedValues = None
        self.EnumeratedValues = []

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(struct.pack('!i', self.NoOfBooleans))
        b.append(struct.pack('!i', len(self.Booleans))
        b.append(struct.pack('!?', self.Booleans))
        b.append(struct.pack('!i', self.NoOfSBytes))
        b.append(struct.pack('!i', len(self.SBytes))
        b.append(struct.pack('!B', self.SBytes))
        b.append(struct.pack('!i', self.NoOfInt16s))
        b.append(struct.pack('!i', len(self.Int16s))
        b.append(struct.pack('!h', self.Int16s))
        b.append(struct.pack('!i', self.NoOfUInt16s))
        b.append(struct.pack('!i', len(self.UInt16s))
        b.append(struct.pack('!H', self.UInt16s))
        b.append(struct.pack('!i', self.NoOfInt32s))
        b.append(struct.pack('!i', len(self.Int32s))
        b.append(struct.pack('!i', self.Int32s))
        b.append(struct.pack('!i', self.NoOfUInt32s))
        b.append(struct.pack('!i', len(self.UInt32s))
        b.append(struct.pack('!I', self.UInt32s))
        b.append(struct.pack('!i', self.NoOfInt64s))
        b.append(struct.pack('!i', len(self.Int64s))
        b.append(struct.pack('!q', self.Int64s))
        b.append(struct.pack('!i', self.NoOfUInt64s))
        b.append(struct.pack('!i', len(self.UInt64s))
        b.append(struct.pack('!Q', self.UInt64s))
        b.append(struct.pack('!i', self.NoOfFloats))
        b.append(struct.pack('!i', len(self.Floats))
        b.append(struct.pack('!f', self.Floats))
        b.append(struct.pack('!i', self.NoOfDoubles))
        b.append(struct.pack('!i', len(self.Doubles))
        b.append(struct.pack('!d', self.Doubles))
        b.append(struct.pack('!i', self.NoOfStrings))
        b.append(struct.pack('!i', len(self.Strings))
        b.append(self.Strings.to_binary())
        b.append(struct.pack('!i', self.NoOfDateTimes))
        b.append(struct.pack('!i', len(self.DateTimes))
        b.append(struct.pack('!d', self.DateTimes))
        b.append(struct.pack('!i', self.NoOfGuids))
        b.append(struct.pack('!i', len(self.Guids))
        b.append(self.Guids.to_binary())
        b.append(struct.pack('!i', self.NoOfByteStrings))
        b.append(struct.pack('!i', len(self.ByteStrings))
        b.append(self.ByteStrings.to_binary())
        b.append(struct.pack('!i', self.NoOfXmlElements))
        b.append(struct.pack('!i', len(self.XmlElements))
        b.append(self.XmlElements.to_binary())
        b.append(struct.pack('!i', self.NoOfNodeIds))
        b.append(struct.pack('!i', len(self.NodeIds))
        b.append(self.NodeIds.to_binary())
        b.append(struct.pack('!i', self.NoOfExpandedNodeIds))
        b.append(struct.pack('!i', len(self.ExpandedNodeIds))
        b.append(self.ExpandedNodeIds.to_binary())
        b.append(struct.pack('!i', self.NoOfStatusCodes))
        b.append(struct.pack('!i', len(self.StatusCodes))
        b.append(self.StatusCodes.to_binary())
        b.append(struct.pack('!i', self.NoOfDiagnosticInfos))
        b.append(struct.pack('!i', len(self.DiagnosticInfos))
        b.append(self.DiagnosticInfos.to_binary())
        b.append(struct.pack('!i', self.NoOfQualifiedNames))
        b.append(struct.pack('!i', len(self.QualifiedNames))
        b.append(self.QualifiedNames.to_binary())
        b.append(struct.pack('!i', self.NoOfLocalizedTexts))
        b.append(struct.pack('!i', len(self.LocalizedTexts))
        b.append(self.LocalizedTexts.to_binary())
        b.append(struct.pack('!i', self.NoOfExtensionObjects))
        b.append(struct.pack('!i', len(self.ExtensionObjects))
        b.append(self.ExtensionObjects.to_binary())
        b.append(struct.pack('!i', self.NoOfDataValues))
        b.append(struct.pack('!i', len(self.DataValues))
        b.append(self.DataValues.to_binary())
        b.append(struct.pack('!i', self.NoOfVariants))
        b.append(struct.pack('!i', len(self.Variants))
        b.append(self.Variants.to_binary())
        b.append(struct.pack('!i', self.NoOfEnumeratedValues))
        b.append(struct.pack('!i', len(self.EnumeratedValues))
        b.append(self.EnumeratedValues.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        self.NoOfBooleans = struct.unpack(i, data[:4])
        data = data[4:]
        self.Booleans = struct.unpack(?, data[:1])
        data = data[1:]
        self.NoOfSBytes = struct.unpack(i, data[:4])
        data = data[4:]
        self.SBytes = struct.unpack(B, data[:1])
        data = data[1:]
        self.NoOfInt16s = struct.unpack(i, data[:4])
        data = data[4:]
        self.Int16s = struct.unpack(h, data[:2])
        data = data[2:]
        self.NoOfUInt16s = struct.unpack(i, data[:4])
        data = data[4:]
        self.UInt16s = struct.unpack(H, data[:2])
        data = data[2:]
        self.NoOfInt32s = struct.unpack(i, data[:4])
        data = data[4:]
        self.Int32s = struct.unpack(i, data[:4])
        data = data[4:]
        self.NoOfUInt32s = struct.unpack(i, data[:4])
        data = data[4:]
        self.UInt32s = struct.unpack(I, data[:4])
        data = data[4:]
        self.NoOfInt64s = struct.unpack(i, data[:4])
        data = data[4:]
        self.Int64s = struct.unpack(q, data[:8])
        data = data[8:]
        self.NoOfUInt64s = struct.unpack(i, data[:4])
        data = data[4:]
        self.UInt64s = struct.unpack(Q, data[:8])
        data = data[8:]
        self.NoOfFloats = struct.unpack(i, data[:4])
        data = data[4:]
        self.Floats = struct.unpack(f, data[:4])
        data = data[4:]
        self.NoOfDoubles = struct.unpack(i, data[:4])
        data = data[4:]
        self.Doubles = struct.unpack(d, data[:8])
        data = data[8:]
        self.NoOfStrings = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.Strings.from_binary(data)
        self.NoOfDateTimes = struct.unpack(i, data[:4])
        data = data[4:]
        self.DateTimes = struct.unpack(d, data[:8])
        data = data[8:]
        self.NoOfGuids = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.Guids.from_binary(data)
        self.NoOfByteStrings = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.ByteStrings.from_binary(data)
        self.NoOfXmlElements = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.XmlElements.from_binary(data)
        self.NoOfNodeIds = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.NodeIds.from_binary(data)
        self.NoOfExpandedNodeIds = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.ExpandedNodeIds.from_binary(data)
        self.NoOfStatusCodes = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.StatusCodes.from_binary(data)
        self.NoOfDiagnosticInfos = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.DiagnosticInfos.from_binary(data)
        self.NoOfQualifiedNames = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.QualifiedNames.from_binary(data)
        self.NoOfLocalizedTexts = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.LocalizedTexts.from_binary(data)
        self.NoOfExtensionObjects = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.ExtensionObjects.from_binary(data)
        self.NoOfDataValues = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.DataValues.from_binary(data)
        self.NoOfVariants = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.Variants.from_binary(data)
        self.NoOfEnumeratedValues = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.EnumeratedValues.from_binary(data)
        return data

class CompositeTestType(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.Field1 = None
        self.Field2 = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.Field1.to_binary())
        b.append(self.Field2.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.Field1.from_binary(data)
        data = self.Field2.from_binary(data)
        return data

class TestStackRequest(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.RequestHeader = None
        self.TestId = None
        self.Iteration = None
        self.Input = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.RequestHeader.to_binary())
        b.append(struct.pack('!I', self.TestId))
        b.append(struct.pack('!i', self.Iteration))
        b.append(self.Input.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.RequestHeader.from_binary(data)
        self.TestId = struct.unpack(I, data[:4])
        data = data[4:]
        self.Iteration = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.Input.from_binary(data)
        return data

class TestStackResponse(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.ResponseHeader = None
        self.Output = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.ResponseHeader.to_binary())
        b.append(self.Output.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.ResponseHeader.from_binary(data)
        data = self.Output.from_binary(data)
        return data

class TestStackExRequest(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.RequestHeader = None
        self.TestId = None
        self.Iteration = None
        self.Input = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.RequestHeader.to_binary())
        b.append(struct.pack('!I', self.TestId))
        b.append(struct.pack('!i', self.Iteration))
        b.append(self.Input.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.RequestHeader.from_binary(data)
        self.TestId = struct.unpack(I, data[:4])
        data = data[4:]
        self.Iteration = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.Input.from_binary(data)
        return data

class TestStackExResponse(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.ResponseHeader = None
        self.Output = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.ResponseHeader.to_binary())
        b.append(self.Output.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.ResponseHeader.from_binary(data)
        data = self.Output.from_binary(data)
        return data

class BuildInfo(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.ProductUri = None
        self.ManufacturerName = None
        self.ProductName = None
        self.SoftwareVersion = None
        self.BuildNumber = None
        self.BuildDate = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.ProductUri.to_binary())
        b.append(self.ManufacturerName.to_binary())
        b.append(self.ProductName.to_binary())
        b.append(self.SoftwareVersion.to_binary())
        b.append(self.BuildNumber.to_binary())
        b.append(struct.pack('!d', self.BuildDate))
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.ProductUri.from_binary(data)
        data = self.ManufacturerName.from_binary(data)
        data = self.ProductName.from_binary(data)
        data = self.SoftwareVersion.from_binary(data)
        data = self.BuildNumber.from_binary(data)
        self.BuildDate = struct.unpack(d, data[:8])
        data = data[8:]
        return data

class RedundantServerDataType(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.ServerId = None
        self.ServiceLevel = None
        self.ServerState = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.ServerId.to_binary())
        b.append(struct.pack('!c', self.ServiceLevel))
        b.append(self.ServerState.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.ServerId.from_binary(data)
        self.ServiceLevel = struct.unpack(c, data[:1])
        data = data[1:]
        data = self.ServerState.from_binary(data)
        return data

class EndpointUrlListDataType(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.NoOfEndpointUrlList = None
        self.EndpointUrlList = []

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(struct.pack('!i', self.NoOfEndpointUrlList))
        b.append(struct.pack('!i', len(self.EndpointUrlList))
        b.append(self.EndpointUrlList.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        self.NoOfEndpointUrlList = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.EndpointUrlList.from_binary(data)
        return data

class NetworkGroupDataType(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.ServerUri = None
        self.NoOfNetworkPaths = None
        self.NetworkPaths = []

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.ServerUri.to_binary())
        b.append(struct.pack('!i', self.NoOfNetworkPaths))
        b.append(struct.pack('!i', len(self.NetworkPaths))
        b.append(self.NetworkPaths.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.ServerUri.from_binary(data)
        self.NoOfNetworkPaths = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.NetworkPaths.from_binary(data)
        return data

class SamplingIntervalDiagnosticsDataType(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.SamplingInterval = None
        self.MonitoredItemCount = None
        self.MaxMonitoredItemCount = None
        self.DisabledMonitoredItemCount = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(struct.pack('!d', self.SamplingInterval))
        b.append(struct.pack('!I', self.MonitoredItemCount))
        b.append(struct.pack('!I', self.MaxMonitoredItemCount))
        b.append(struct.pack('!I', self.DisabledMonitoredItemCount))
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        self.SamplingInterval = struct.unpack(d, data[:8])
        data = data[8:]
        self.MonitoredItemCount = struct.unpack(I, data[:4])
        data = data[4:]
        self.MaxMonitoredItemCount = struct.unpack(I, data[:4])
        data = data[4:]
        self.DisabledMonitoredItemCount = struct.unpack(I, data[:4])
        data = data[4:]
        return data

class ServerDiagnosticsSummaryDataType(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.ServerViewCount = None
        self.CurrentSessionCount = None
        self.CumulatedSessionCount = None
        self.SecurityRejectedSessionCount = None
        self.RejectedSessionCount = None
        self.SessionTimeoutCount = None
        self.SessionAbortCount = None
        self.CurrentSubscriptionCount = None
        self.CumulatedSubscriptionCount = None
        self.PublishingIntervalCount = None
        self.SecurityRejectedRequestsCount = None
        self.RejectedRequestsCount = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(struct.pack('!I', self.ServerViewCount))
        b.append(struct.pack('!I', self.CurrentSessionCount))
        b.append(struct.pack('!I', self.CumulatedSessionCount))
        b.append(struct.pack('!I', self.SecurityRejectedSessionCount))
        b.append(struct.pack('!I', self.RejectedSessionCount))
        b.append(struct.pack('!I', self.SessionTimeoutCount))
        b.append(struct.pack('!I', self.SessionAbortCount))
        b.append(struct.pack('!I', self.CurrentSubscriptionCount))
        b.append(struct.pack('!I', self.CumulatedSubscriptionCount))
        b.append(struct.pack('!I', self.PublishingIntervalCount))
        b.append(struct.pack('!I', self.SecurityRejectedRequestsCount))
        b.append(struct.pack('!I', self.RejectedRequestsCount))
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        self.ServerViewCount = struct.unpack(I, data[:4])
        data = data[4:]
        self.CurrentSessionCount = struct.unpack(I, data[:4])
        data = data[4:]
        self.CumulatedSessionCount = struct.unpack(I, data[:4])
        data = data[4:]
        self.SecurityRejectedSessionCount = struct.unpack(I, data[:4])
        data = data[4:]
        self.RejectedSessionCount = struct.unpack(I, data[:4])
        data = data[4:]
        self.SessionTimeoutCount = struct.unpack(I, data[:4])
        data = data[4:]
        self.SessionAbortCount = struct.unpack(I, data[:4])
        data = data[4:]
        self.CurrentSubscriptionCount = struct.unpack(I, data[:4])
        data = data[4:]
        self.CumulatedSubscriptionCount = struct.unpack(I, data[:4])
        data = data[4:]
        self.PublishingIntervalCount = struct.unpack(I, data[:4])
        data = data[4:]
        self.SecurityRejectedRequestsCount = struct.unpack(I, data[:4])
        data = data[4:]
        self.RejectedRequestsCount = struct.unpack(I, data[:4])
        data = data[4:]
        return data

class ServerStatusDataType(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.StartTime = None
        self.CurrentTime = None
        self.State = None
        self.BuildInfo = None
        self.SecondsTillShutdown = None
        self.ShutdownReason = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(struct.pack('!d', self.StartTime))
        b.append(struct.pack('!d', self.CurrentTime))
        b.append(self.State.to_binary())
        b.append(self.BuildInfo.to_binary())
        b.append(struct.pack('!I', self.SecondsTillShutdown))
        b.append(self.ShutdownReason.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        self.StartTime = struct.unpack(d, data[:8])
        data = data[8:]
        self.CurrentTime = struct.unpack(d, data[:8])
        data = data[8:]
        data = self.State.from_binary(data)
        data = self.BuildInfo.from_binary(data)
        self.SecondsTillShutdown = struct.unpack(I, data[:4])
        data = data[4:]
        data = self.ShutdownReason.from_binary(data)
        return data

class SessionSecurityDiagnosticsDataType(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.SessionId = None
        self.ClientUserIdOfSession = None
        self.NoOfClientUserIdHistory = None
        self.ClientUserIdHistory = []
        self.AuthenticationMechanism = None
        self.Encoding = None
        self.TransportProtocol = None
        self.SecurityMode = None
        self.SecurityPolicyUri = None
        self.ClientCertificate = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.SessionId.to_binary())
        b.append(self.ClientUserIdOfSession.to_binary())
        b.append(struct.pack('!i', self.NoOfClientUserIdHistory))
        b.append(struct.pack('!i', len(self.ClientUserIdHistory))
        b.append(self.ClientUserIdHistory.to_binary())
        b.append(self.AuthenticationMechanism.to_binary())
        b.append(self.Encoding.to_binary())
        b.append(self.TransportProtocol.to_binary())
        b.append(self.SecurityMode.to_binary())
        b.append(self.SecurityPolicyUri.to_binary())
        b.append(self.ClientCertificate.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.SessionId.from_binary(data)
        data = self.ClientUserIdOfSession.from_binary(data)
        self.NoOfClientUserIdHistory = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.ClientUserIdHistory.from_binary(data)
        data = self.AuthenticationMechanism.from_binary(data)
        data = self.Encoding.from_binary(data)
        data = self.TransportProtocol.from_binary(data)
        data = self.SecurityMode.from_binary(data)
        data = self.SecurityPolicyUri.from_binary(data)
        data = self.ClientCertificate.from_binary(data)
        return data

class ServiceCounterDataType(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.TotalCount = None
        self.ErrorCount = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(struct.pack('!I', self.TotalCount))
        b.append(struct.pack('!I', self.ErrorCount))
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        self.TotalCount = struct.unpack(I, data[:4])
        data = data[4:]
        self.ErrorCount = struct.unpack(I, data[:4])
        data = data[4:]
        return data

class SessionDiagnosticsDataType(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.SessionId = None
        self.SessionName = None
        self.ClientDescription = None
        self.ServerUri = None
        self.EndpointUrl = None
        self.NoOfLocaleIds = None
        self.LocaleIds = []
        self.ActualSessionTimeout = None
        self.MaxResponseMessageSize = None
        self.ClientConnectionTime = None
        self.ClientLastContactTime = None
        self.CurrentSubscriptionsCount = None
        self.CurrentMonitoredItemsCount = None
        self.CurrentPublishRequestsInQueue = None
        self.TotalRequestCount = None
        self.UnauthorizedRequestCount = None
        self.ReadCount = None
        self.HistoryReadCount = None
        self.WriteCount = None
        self.HistoryUpdateCount = None
        self.CallCount = None
        self.CreateMonitoredItemsCount = None
        self.ModifyMonitoredItemsCount = None
        self.SetMonitoringModeCount = None
        self.SetTriggeringCount = None
        self.DeleteMonitoredItemsCount = None
        self.CreateSubscriptionCount = None
        self.ModifySubscriptionCount = None
        self.SetPublishingModeCount = None
        self.PublishCount = None
        self.RepublishCount = None
        self.TransferSubscriptionsCount = None
        self.DeleteSubscriptionsCount = None
        self.AddNodesCount = None
        self.AddReferencesCount = None
        self.DeleteNodesCount = None
        self.DeleteReferencesCount = None
        self.BrowseCount = None
        self.BrowseNextCount = None
        self.TranslateBrowsePathsToNodeIdsCount = None
        self.QueryFirstCount = None
        self.QueryNextCount = None
        self.RegisterNodesCount = None
        self.UnregisterNodesCount = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.SessionId.to_binary())
        b.append(self.SessionName.to_binary())
        b.append(self.ClientDescription.to_binary())
        b.append(self.ServerUri.to_binary())
        b.append(self.EndpointUrl.to_binary())
        b.append(struct.pack('!i', self.NoOfLocaleIds))
        b.append(struct.pack('!i', len(self.LocaleIds))
        b.append(self.LocaleIds.to_binary())
        b.append(struct.pack('!d', self.ActualSessionTimeout))
        b.append(struct.pack('!I', self.MaxResponseMessageSize))
        b.append(struct.pack('!d', self.ClientConnectionTime))
        b.append(struct.pack('!d', self.ClientLastContactTime))
        b.append(struct.pack('!I', self.CurrentSubscriptionsCount))
        b.append(struct.pack('!I', self.CurrentMonitoredItemsCount))
        b.append(struct.pack('!I', self.CurrentPublishRequestsInQueue))
        b.append(self.TotalRequestCount.to_binary())
        b.append(struct.pack('!I', self.UnauthorizedRequestCount))
        b.append(self.ReadCount.to_binary())
        b.append(self.HistoryReadCount.to_binary())
        b.append(self.WriteCount.to_binary())
        b.append(self.HistoryUpdateCount.to_binary())
        b.append(self.CallCount.to_binary())
        b.append(self.CreateMonitoredItemsCount.to_binary())
        b.append(self.ModifyMonitoredItemsCount.to_binary())
        b.append(self.SetMonitoringModeCount.to_binary())
        b.append(self.SetTriggeringCount.to_binary())
        b.append(self.DeleteMonitoredItemsCount.to_binary())
        b.append(self.CreateSubscriptionCount.to_binary())
        b.append(self.ModifySubscriptionCount.to_binary())
        b.append(self.SetPublishingModeCount.to_binary())
        b.append(self.PublishCount.to_binary())
        b.append(self.RepublishCount.to_binary())
        b.append(self.TransferSubscriptionsCount.to_binary())
        b.append(self.DeleteSubscriptionsCount.to_binary())
        b.append(self.AddNodesCount.to_binary())
        b.append(self.AddReferencesCount.to_binary())
        b.append(self.DeleteNodesCount.to_binary())
        b.append(self.DeleteReferencesCount.to_binary())
        b.append(self.BrowseCount.to_binary())
        b.append(self.BrowseNextCount.to_binary())
        b.append(self.TranslateBrowsePathsToNodeIdsCount.to_binary())
        b.append(self.QueryFirstCount.to_binary())
        b.append(self.QueryNextCount.to_binary())
        b.append(self.RegisterNodesCount.to_binary())
        b.append(self.UnregisterNodesCount.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.SessionId.from_binary(data)
        data = self.SessionName.from_binary(data)
        data = self.ClientDescription.from_binary(data)
        data = self.ServerUri.from_binary(data)
        data = self.EndpointUrl.from_binary(data)
        self.NoOfLocaleIds = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.LocaleIds.from_binary(data)
        self.ActualSessionTimeout = struct.unpack(d, data[:8])
        data = data[8:]
        self.MaxResponseMessageSize = struct.unpack(I, data[:4])
        data = data[4:]
        self.ClientConnectionTime = struct.unpack(d, data[:8])
        data = data[8:]
        self.ClientLastContactTime = struct.unpack(d, data[:8])
        data = data[8:]
        self.CurrentSubscriptionsCount = struct.unpack(I, data[:4])
        data = data[4:]
        self.CurrentMonitoredItemsCount = struct.unpack(I, data[:4])
        data = data[4:]
        self.CurrentPublishRequestsInQueue = struct.unpack(I, data[:4])
        data = data[4:]
        data = self.TotalRequestCount.from_binary(data)
        self.UnauthorizedRequestCount = struct.unpack(I, data[:4])
        data = data[4:]
        data = self.ReadCount.from_binary(data)
        data = self.HistoryReadCount.from_binary(data)
        data = self.WriteCount.from_binary(data)
        data = self.HistoryUpdateCount.from_binary(data)
        data = self.CallCount.from_binary(data)
        data = self.CreateMonitoredItemsCount.from_binary(data)
        data = self.ModifyMonitoredItemsCount.from_binary(data)
        data = self.SetMonitoringModeCount.from_binary(data)
        data = self.SetTriggeringCount.from_binary(data)
        data = self.DeleteMonitoredItemsCount.from_binary(data)
        data = self.CreateSubscriptionCount.from_binary(data)
        data = self.ModifySubscriptionCount.from_binary(data)
        data = self.SetPublishingModeCount.from_binary(data)
        data = self.PublishCount.from_binary(data)
        data = self.RepublishCount.from_binary(data)
        data = self.TransferSubscriptionsCount.from_binary(data)
        data = self.DeleteSubscriptionsCount.from_binary(data)
        data = self.AddNodesCount.from_binary(data)
        data = self.AddReferencesCount.from_binary(data)
        data = self.DeleteNodesCount.from_binary(data)
        data = self.DeleteReferencesCount.from_binary(data)
        data = self.BrowseCount.from_binary(data)
        data = self.BrowseNextCount.from_binary(data)
        data = self.TranslateBrowsePathsToNodeIdsCount.from_binary(data)
        data = self.QueryFirstCount.from_binary(data)
        data = self.QueryNextCount.from_binary(data)
        data = self.RegisterNodesCount.from_binary(data)
        data = self.UnregisterNodesCount.from_binary(data)
        return data

class StatusResult(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.StatusCode = None
        self.DiagnosticInfo = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.StatusCode.to_binary())
        b.append(self.DiagnosticInfo.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.StatusCode.from_binary(data)
        data = self.DiagnosticInfo.from_binary(data)
        return data

class SubscriptionDiagnosticsDataType(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.SessionId = None
        self.SubscriptionId = None
        self.Priority = None
        self.PublishingInterval = None
        self.MaxKeepAliveCount = None
        self.MaxLifetimeCount = None
        self.MaxNotificationsPerPublish = None
        self.PublishingEnabled = None
        self.ModifyCount = None
        self.EnableCount = None
        self.DisableCount = None
        self.RepublishRequestCount = None
        self.RepublishMessageRequestCount = None
        self.RepublishMessageCount = None
        self.TransferRequestCount = None
        self.TransferredToAltClientCount = None
        self.TransferredToSameClientCount = None
        self.PublishRequestCount = None
        self.DataChangeNotificationsCount = None
        self.EventNotificationsCount = None
        self.NotificationsCount = None
        self.LatePublishRequestCount = None
        self.CurrentKeepAliveCount = None
        self.CurrentLifetimeCount = None
        self.UnacknowledgedMessageCount = None
        self.DiscardedMessageCount = None
        self.MonitoredItemCount = None
        self.DisabledMonitoredItemCount = None
        self.MonitoringQueueOverflowCount = None
        self.NextSequenceNumber = None
        self.EventQueueOverFlowCount = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.SessionId.to_binary())
        b.append(struct.pack('!I', self.SubscriptionId))
        b.append(struct.pack('!c', self.Priority))
        b.append(struct.pack('!d', self.PublishingInterval))
        b.append(struct.pack('!I', self.MaxKeepAliveCount))
        b.append(struct.pack('!I', self.MaxLifetimeCount))
        b.append(struct.pack('!I', self.MaxNotificationsPerPublish))
        b.append(struct.pack('!?', self.PublishingEnabled))
        b.append(struct.pack('!I', self.ModifyCount))
        b.append(struct.pack('!I', self.EnableCount))
        b.append(struct.pack('!I', self.DisableCount))
        b.append(struct.pack('!I', self.RepublishRequestCount))
        b.append(struct.pack('!I', self.RepublishMessageRequestCount))
        b.append(struct.pack('!I', self.RepublishMessageCount))
        b.append(struct.pack('!I', self.TransferRequestCount))
        b.append(struct.pack('!I', self.TransferredToAltClientCount))
        b.append(struct.pack('!I', self.TransferredToSameClientCount))
        b.append(struct.pack('!I', self.PublishRequestCount))
        b.append(struct.pack('!I', self.DataChangeNotificationsCount))
        b.append(struct.pack('!I', self.EventNotificationsCount))
        b.append(struct.pack('!I', self.NotificationsCount))
        b.append(struct.pack('!I', self.LatePublishRequestCount))
        b.append(struct.pack('!I', self.CurrentKeepAliveCount))
        b.append(struct.pack('!I', self.CurrentLifetimeCount))
        b.append(struct.pack('!I', self.UnacknowledgedMessageCount))
        b.append(struct.pack('!I', self.DiscardedMessageCount))
        b.append(struct.pack('!I', self.MonitoredItemCount))
        b.append(struct.pack('!I', self.DisabledMonitoredItemCount))
        b.append(struct.pack('!I', self.MonitoringQueueOverflowCount))
        b.append(struct.pack('!I', self.NextSequenceNumber))
        b.append(struct.pack('!I', self.EventQueueOverFlowCount))
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.SessionId.from_binary(data)
        self.SubscriptionId = struct.unpack(I, data[:4])
        data = data[4:]
        self.Priority = struct.unpack(c, data[:1])
        data = data[1:]
        self.PublishingInterval = struct.unpack(d, data[:8])
        data = data[8:]
        self.MaxKeepAliveCount = struct.unpack(I, data[:4])
        data = data[4:]
        self.MaxLifetimeCount = struct.unpack(I, data[:4])
        data = data[4:]
        self.MaxNotificationsPerPublish = struct.unpack(I, data[:4])
        data = data[4:]
        self.PublishingEnabled = struct.unpack(?, data[:1])
        data = data[1:]
        self.ModifyCount = struct.unpack(I, data[:4])
        data = data[4:]
        self.EnableCount = struct.unpack(I, data[:4])
        data = data[4:]
        self.DisableCount = struct.unpack(I, data[:4])
        data = data[4:]
        self.RepublishRequestCount = struct.unpack(I, data[:4])
        data = data[4:]
        self.RepublishMessageRequestCount = struct.unpack(I, data[:4])
        data = data[4:]
        self.RepublishMessageCount = struct.unpack(I, data[:4])
        data = data[4:]
        self.TransferRequestCount = struct.unpack(I, data[:4])
        data = data[4:]
        self.TransferredToAltClientCount = struct.unpack(I, data[:4])
        data = data[4:]
        self.TransferredToSameClientCount = struct.unpack(I, data[:4])
        data = data[4:]
        self.PublishRequestCount = struct.unpack(I, data[:4])
        data = data[4:]
        self.DataChangeNotificationsCount = struct.unpack(I, data[:4])
        data = data[4:]
        self.EventNotificationsCount = struct.unpack(I, data[:4])
        data = data[4:]
        self.NotificationsCount = struct.unpack(I, data[:4])
        data = data[4:]
        self.LatePublishRequestCount = struct.unpack(I, data[:4])
        data = data[4:]
        self.CurrentKeepAliveCount = struct.unpack(I, data[:4])
        data = data[4:]
        self.CurrentLifetimeCount = struct.unpack(I, data[:4])
        data = data[4:]
        self.UnacknowledgedMessageCount = struct.unpack(I, data[:4])
        data = data[4:]
        self.DiscardedMessageCount = struct.unpack(I, data[:4])
        data = data[4:]
        self.MonitoredItemCount = struct.unpack(I, data[:4])
        data = data[4:]
        self.DisabledMonitoredItemCount = struct.unpack(I, data[:4])
        data = data[4:]
        self.MonitoringQueueOverflowCount = struct.unpack(I, data[:4])
        data = data[4:]
        self.NextSequenceNumber = struct.unpack(I, data[:4])
        data = data[4:]
        self.EventQueueOverFlowCount = struct.unpack(I, data[:4])
        data = data[4:]
        return data

class ModelChangeStructureDataType(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.Affected = None
        self.AffectedType = None
        self.Verb = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.Affected.to_binary())
        b.append(self.AffectedType.to_binary())
        b.append(struct.pack('!c', self.Verb))
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.Affected.from_binary(data)
        data = self.AffectedType.from_binary(data)
        self.Verb = struct.unpack(c, data[:1])
        data = data[1:]
        return data

class SemanticChangeStructureDataType(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.Affected = None
        self.AffectedType = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.Affected.to_binary())
        b.append(self.AffectedType.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.Affected.from_binary(data)
        data = self.AffectedType.from_binary(data)
        return data

class Range(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.Low = None
        self.High = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(struct.pack('!d', self.Low))
        b.append(struct.pack('!d', self.High))
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        self.Low = struct.unpack(d, data[:8])
        data = data[8:]
        self.High = struct.unpack(d, data[:8])
        data = data[8:]
        return data

class EUInformation(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.NamespaceUri = None
        self.UnitId = None
        self.DisplayName = None
        self.Description = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.NamespaceUri.to_binary())
        b.append(struct.pack('!i', self.UnitId))
        b.append(self.DisplayName.to_binary())
        b.append(self.Description.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.NamespaceUri.from_binary(data)
        self.UnitId = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.DisplayName.from_binary(data)
        data = self.Description.from_binary(data)
        return data

class ComplexNumberType(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.Real = None
        self.Imaginary = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(struct.pack('!f', self.Real))
        b.append(struct.pack('!f', self.Imaginary))
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        self.Real = struct.unpack(f, data[:4])
        data = data[4:]
        self.Imaginary = struct.unpack(f, data[:4])
        data = data[4:]
        return data

class DoubleComplexNumberType(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.Real = None
        self.Imaginary = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(struct.pack('!d', self.Real))
        b.append(struct.pack('!d', self.Imaginary))
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        self.Real = struct.unpack(d, data[:8])
        data = data[8:]
        self.Imaginary = struct.unpack(d, data[:8])
        data = data[8:]
        return data

class AxisInformation(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.EngineeringUnits = None
        self.EURange = None
        self.Title = None
        self.AxisScaleType = None
        self.NoOfAxisSteps = None
        self.AxisSteps = []

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.EngineeringUnits.to_binary())
        b.append(self.EURange.to_binary())
        b.append(self.Title.to_binary())
        b.append(self.AxisScaleType.to_binary())
        b.append(struct.pack('!i', self.NoOfAxisSteps))
        b.append(struct.pack('!i', len(self.AxisSteps))
        b.append(struct.pack('!d', self.AxisSteps))
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.EngineeringUnits.from_binary(data)
        data = self.EURange.from_binary(data)
        data = self.Title.from_binary(data)
        data = self.AxisScaleType.from_binary(data)
        self.NoOfAxisSteps = struct.unpack(i, data[:4])
        data = data[4:]
        self.AxisSteps = struct.unpack(d, data[:8])
        data = data[8:]
        return data

class XVType(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.X = None
        self.Value = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(struct.pack('!d', self.X))
        b.append(struct.pack('!f', self.Value))
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        self.X = struct.unpack(d, data[:8])
        data = data[8:]
        self.Value = struct.unpack(f, data[:4])
        data = data[4:]
        return data

class ProgramDiagnosticDataType(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.CreateSessionId = None
        self.CreateClientName = None
        self.InvocationCreationTime = None
        self.LastTransitionTime = None
        self.LastMethodCall = None
        self.LastMethodSessionId = None
        self.NoOfLastMethodInputArguments = None
        self.LastMethodInputArguments = []
        self.NoOfLastMethodOutputArguments = None
        self.LastMethodOutputArguments = []
        self.LastMethodCallTime = None
        self.LastMethodReturnStatus = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.CreateSessionId.to_binary())
        b.append(self.CreateClientName.to_binary())
        b.append(struct.pack('!d', self.InvocationCreationTime))
        b.append(struct.pack('!d', self.LastTransitionTime))
        b.append(self.LastMethodCall.to_binary())
        b.append(self.LastMethodSessionId.to_binary())
        b.append(struct.pack('!i', self.NoOfLastMethodInputArguments))
        b.append(struct.pack('!i', len(self.LastMethodInputArguments))
        b.append(self.LastMethodInputArguments.to_binary())
        b.append(struct.pack('!i', self.NoOfLastMethodOutputArguments))
        b.append(struct.pack('!i', len(self.LastMethodOutputArguments))
        b.append(self.LastMethodOutputArguments.to_binary())
        b.append(struct.pack('!d', self.LastMethodCallTime))
        b.append(self.LastMethodReturnStatus.to_binary())
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.CreateSessionId.from_binary(data)
        data = self.CreateClientName.from_binary(data)
        self.InvocationCreationTime = struct.unpack(d, data[:8])
        data = data[8:]
        self.LastTransitionTime = struct.unpack(d, data[:8])
        data = data[8:]
        data = self.LastMethodCall.from_binary(data)
        data = self.LastMethodSessionId.from_binary(data)
        self.NoOfLastMethodInputArguments = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.LastMethodInputArguments.from_binary(data)
        self.NoOfLastMethodOutputArguments = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.LastMethodOutputArguments.from_binary(data)
        self.LastMethodCallTime = struct.unpack(d, data[:8])
        data = data[8:]
        data = self.LastMethodReturnStatus.from_binary(data)
        return data

class Annotation(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.Message = None
        self.UserName = None
        self.AnnotationTime = None

    def to_binary(self):
        b = []
        if self.TypeId: self.Encoding |= (value << 0):
        b.append(struct.pack('!B', self.Encoding))
        if self.TypeId: b.append(self.TypeId.to_binary())
        b.append(struct.pack('!i', self.BodyLength))
        b.append(self.Message.to_binary())
        b.append(self.UserName.to_binary())
        b.append(struct.pack('!d', self.AnnotationTime))
        return b.join()

    def from_binary(self, data):
        self.Encoding = struct.unpack(B, data[:1])
        data = data[1:]
        if self.Encoding & (1 << 0):
            data = self.TypeId.from_binary(data)
        self.BodyLength = struct.unpack(i, data[:4])
        data = data[4:]
        data = self.Message.from_binary(data)
        data = self.UserName.from_binary(data)
        self.AnnotationTime = struct.unpack(d, data[:8])
        data = data[8:]
        return data
