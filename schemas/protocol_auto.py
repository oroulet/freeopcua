'''
Autogenerate code from xml spec
'''
import struct



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
        b = bytes()
        b += struct.pack('!i', self.Length)
        b += struct.pack('!i', len(self.Value)
        b += struct.pack('!c', self.Value)
        return b

class TwoByteNodeId(object):
    def __init__(self):
        self.Identifier = None

    def to_binary(self):
        b = bytes()
        b += struct.pack('!c', self.Identifier)
        return b

class FourByteNodeId(object):
    def __init__(self):
        self.NamespaceIndex = None
        self.Identifier = None

    def to_binary(self):
        b = bytes()
        b += struct.pack('!c', self.NamespaceIndex)
        b += struct.pack('!H', self.Identifier)
        return b

class NumericNodeId(object):
    def __init__(self):
        self.NamespaceIndex = None
        self.Identifier = None

    def to_binary(self):
        b = bytes()
        b += struct.pack('!H', self.NamespaceIndex)
        b += struct.pack('!I', self.Identifier)
        return b

class StringNodeId(object):
    def __init__(self):
        self.NamespaceIndex = None
        self.Identifier = None

    def to_binary(self):
        b = bytes()
        b += struct.pack('!H', self.NamespaceIndex)
        b += struct.pack('!s', self.Identifier)
        return b

class GuidNodeId(object):
    def __init__(self):
        self.NamespaceIndex = None
        self.Identifier = None

    def to_binary(self):
        b = bytes()
        b += struct.pack('!H', self.NamespaceIndex)
        b += struct.pack('!None', self.Identifier)
        return b

class ByteStringNodeId(object):
    def __init__(self):
        self.NamespaceIndex = None
        self.Identifier = None

    def to_binary(self):
        b = bytes()
        b += struct.pack('!H', self.NamespaceIndex)
        b += struct.pack('!c', self.Identifier)
        return b

class NodeId(object):
    def __init__(self):
        self.NodeIdType = None
        self.TwoByte = None
        self.FourByte = None
        self.Numeric = None
        self.String = None
        self.Guid = None
        self.ByteString = None

    @property
    def Reserved1(self):
        return self.NodeIdType & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.NodeIdType | (value << 7)

    def to_binary(self):
        b = bytes()
        b += self.NodeIdType.to_binary()
        return b

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

    @property
    def NamespaceURISpecified(self):
        return self.NodeIdType & (1 << 7)

    @NamespaceURISpecified.setter
    def NamespaceURISpecified(self, value):
        return self.NodeIdType | (value << 7)

    @property
    def ServerIndexSpecified(self):
        return self.NodeIdType & (1 << 6)

    @ServerIndexSpecified.setter
    def ServerIndexSpecified(self, value):
        return self.NodeIdType | (value << 6)

    def to_binary(self):
        b = bytes()
        b += self.NodeIdType.to_binary()
        return b

class DiagnosticInfo(object):
    def __init__(self):
        self.Encoding = None
        self.SymbolicId = None
        self.NamespaceURI = None
        self.LocalizedText = None
        self.AdditionalInfo = None
        self.InnerStatusCode = None
        self.InnerDiagnosticInfo = None

    @property
    def LocaleSpecified(self):
        return self.Encoding & (1 << 3)

    @LocaleSpecified.setter
    def LocaleSpecified(self, value):
        return self.Encoding | (value << 3)

    @property
    def InnerDiagnosticInfoSpecified(self):
        return self.Encoding & (1 << 6)

    @InnerDiagnosticInfoSpecified.setter
    def InnerDiagnosticInfoSpecified(self, value):
        return self.Encoding | (value << 6)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def SymbolicIdSpecified(self):
        return self.Encoding & (1 << 0)

    @SymbolicIdSpecified.setter
    def SymbolicIdSpecified(self, value):
        return self.Encoding | (value << 0)

    @property
    def NamespaceURISpecified(self):
        return self.Encoding & (1 << 1)

    @NamespaceURISpecified.setter
    def NamespaceURISpecified(self, value):
        return self.Encoding | (value << 1)

    @property
    def InnerStatusCodeSpecified(self):
        return self.Encoding & (1 << 5)

    @InnerStatusCodeSpecified.setter
    def InnerStatusCodeSpecified(self, value):
        return self.Encoding | (value << 5)

    @property
    def LocalizedTextSpecified(self):
        return self.Encoding & (1 << 2)

    @LocalizedTextSpecified.setter
    def LocalizedTextSpecified(self, value):
        return self.Encoding | (value << 2)

    @property
    def AdditionalInfoSpecified(self):
        return self.Encoding & (1 << 4)

    @AdditionalInfoSpecified.setter
    def AdditionalInfoSpecified(self, value):
        return self.Encoding | (value << 4)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        return b

class QualifiedName(object):
    def __init__(self):
        self.NamespaceIndex = None
        self.Name = None

    def to_binary(self):
        b = bytes()
        b += struct.pack('!i', self.NamespaceIndex)
        b += struct.pack('!s', self.Name)
        return b

class LocalizedText(object):
    def __init__(self):
        self.Encoding = None
        self.Locale = None
        self.Text = None

    @property
    def LocaleSpecified(self):
        return self.Encoding & (1 << 0)

    @LocaleSpecified.setter
    def LocaleSpecified(self, value):
        return self.Encoding | (value << 0)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def TextSpecified(self):
        return self.Encoding & (1 << 1)

    @TextSpecified.setter
    def TextSpecified(self, value):
        return self.Encoding | (value << 1)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        return b

class DataValue(object):
    def __init__(self):
        self.Encoding = None
        self.Value = None
        self.StatusCode = None
        self.SourceTimestamp = None
        self.SourcePicoseconds = None
        self.ServerTimestamp = None
        self.ServerPicoseconds = None

    @property
    def ValueSpecified(self):
        return self.Encoding & (1 << 0)

    @ValueSpecified.setter
    def ValueSpecified(self, value):
        return self.Encoding | (value << 0)

    @property
    def SourceTimestampSpecified(self):
        return self.Encoding & (1 << 2)

    @SourceTimestampSpecified.setter
    def SourceTimestampSpecified(self, value):
        return self.Encoding | (value << 2)

    @property
    def StatusCodeSpecified(self):
        return self.Encoding & (1 << 1)

    @StatusCodeSpecified.setter
    def StatusCodeSpecified(self, value):
        return self.Encoding | (value << 1)

    @property
    def ServerPicosecondsSpecified(self):
        return self.Encoding & (1 << 5)

    @ServerPicosecondsSpecified.setter
    def ServerPicosecondsSpecified(self, value):
        return self.Encoding | (value << 5)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def ServerTimestampSpecified(self):
        return self.Encoding & (1 << 4)

    @ServerTimestampSpecified.setter
    def ServerTimestampSpecified(self, value):
        return self.Encoding | (value << 4)

    @property
    def SourcePicosecondsSpecified(self):
        return self.Encoding & (1 << 3)

    @SourcePicosecondsSpecified.setter
    def SourcePicosecondsSpecified(self, value):
        return self.Encoding | (value << 3)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        return b

class ExtensionObject(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.Body = []

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += struct.pack('!i', len(self.Body)
        b += struct.pack('!c', self.Body)
        return b

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

    @property
    def ArrayLengthSpecified(self):
        return self.Encoding & (1 << 7)

    @ArrayLengthSpecified.setter
    def ArrayLengthSpecified(self, value):
        return self.Encoding | (value << 7)

    @property
    def VariantType(self):
        return self.Encoding & (1 << 6)

    @VariantType.setter
    def VariantType(self, value):
        return self.Encoding | (value << 6)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        return b

class ReferenceNode(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.ReferenceTypeId = None
        self.IsInverse = None
        self.TargetId = None

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.ReferenceTypeId.to_binary()
        b += struct.pack('!?', self.IsInverse)
        b += self.TargetId.to_binary()
        return b

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

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.NodeId.to_binary()
        b += self.NodeClass.to_binary()
        b += self.BrowseName.to_binary()
        b += self.DisplayName.to_binary()
        b += self.Description.to_binary()
        b += struct.pack('!I', self.WriteMask)
        b += struct.pack('!I', self.UserWriteMask)
        b += struct.pack('!i', self.NoOfReferences)
        b += struct.pack('!i', len(self.References)
        b += self.References.to_binary()
        return b

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

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.NodeId.to_binary()
        b += self.NodeClass.to_binary()
        b += self.BrowseName.to_binary()
        b += self.DisplayName.to_binary()
        b += self.Description.to_binary()
        b += struct.pack('!I', self.WriteMask)
        b += struct.pack('!I', self.UserWriteMask)
        b += struct.pack('!i', self.NoOfReferences)
        b += struct.pack('!i', len(self.References)
        b += self.References.to_binary()
        b += self.NodeId.to_binary()
        b += self.NodeClass.to_binary()
        b += self.BrowseName.to_binary()
        b += self.DisplayName.to_binary()
        b += self.Description.to_binary()
        b += struct.pack('!I', self.WriteMask)
        b += struct.pack('!I', self.UserWriteMask)
        b += struct.pack('!i', self.NoOfReferences)
        b += struct.pack('!i', len(self.References)
        b += self.References.to_binary()
        return b

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

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.NodeId.to_binary()
        b += self.NodeClass.to_binary()
        b += self.BrowseName.to_binary()
        b += self.DisplayName.to_binary()
        b += self.Description.to_binary()
        b += struct.pack('!I', self.WriteMask)
        b += struct.pack('!I', self.UserWriteMask)
        b += struct.pack('!i', self.NoOfReferences)
        b += struct.pack('!i', len(self.References)
        b += self.References.to_binary()
        b += self.NodeId.to_binary()
        b += self.NodeClass.to_binary()
        b += self.BrowseName.to_binary()
        b += self.DisplayName.to_binary()
        b += self.Description.to_binary()
        b += struct.pack('!I', self.WriteMask)
        b += struct.pack('!I', self.UserWriteMask)
        b += struct.pack('!i', self.NoOfReferences)
        b += struct.pack('!i', len(self.References)
        b += self.References.to_binary()
        return b

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

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.NodeId.to_binary()
        b += self.NodeClass.to_binary()
        b += self.BrowseName.to_binary()
        b += self.DisplayName.to_binary()
        b += self.Description.to_binary()
        b += struct.pack('!I', self.WriteMask)
        b += struct.pack('!I', self.UserWriteMask)
        b += struct.pack('!i', self.NoOfReferences)
        b += struct.pack('!i', len(self.References)
        b += self.References.to_binary()
        b += self.NodeId.to_binary()
        b += self.NodeClass.to_binary()
        b += self.BrowseName.to_binary()
        b += self.DisplayName.to_binary()
        b += self.Description.to_binary()
        b += struct.pack('!I', self.WriteMask)
        b += struct.pack('!I', self.UserWriteMask)
        b += struct.pack('!i', self.NoOfReferences)
        b += struct.pack('!i', len(self.References)
        b += self.References.to_binary()
        b += self.NodeId.to_binary()
        b += self.NodeClass.to_binary()
        b += self.BrowseName.to_binary()
        b += self.DisplayName.to_binary()
        b += self.Description.to_binary()
        b += struct.pack('!I', self.WriteMask)
        b += struct.pack('!I', self.UserWriteMask)
        b += struct.pack('!i', self.NoOfReferences)
        b += struct.pack('!i', len(self.References)
        b += self.References.to_binary()
        b += struct.pack('!c', self.EventNotifier)
        return b

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

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.NodeId.to_binary()
        b += self.NodeClass.to_binary()
        b += self.BrowseName.to_binary()
        b += self.DisplayName.to_binary()
        b += self.Description.to_binary()
        b += struct.pack('!I', self.WriteMask)
        b += struct.pack('!I', self.UserWriteMask)
        b += struct.pack('!i', self.NoOfReferences)
        b += struct.pack('!i', len(self.References)
        b += self.References.to_binary()
        b += self.NodeId.to_binary()
        b += self.NodeClass.to_binary()
        b += self.BrowseName.to_binary()
        b += self.DisplayName.to_binary()
        b += self.Description.to_binary()
        b += struct.pack('!I', self.WriteMask)
        b += struct.pack('!I', self.UserWriteMask)
        b += struct.pack('!i', self.NoOfReferences)
        b += struct.pack('!i', len(self.References)
        b += self.References.to_binary()
        b += self.NodeId.to_binary()
        b += self.NodeClass.to_binary()
        b += self.BrowseName.to_binary()
        b += self.DisplayName.to_binary()
        b += self.Description.to_binary()
        b += struct.pack('!I', self.WriteMask)
        b += struct.pack('!I', self.UserWriteMask)
        b += struct.pack('!i', self.NoOfReferences)
        b += struct.pack('!i', len(self.References)
        b += self.References.to_binary()
        b += struct.pack('!?', self.IsAbstract)
        return b

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

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.NodeId.to_binary()
        b += self.NodeClass.to_binary()
        b += self.BrowseName.to_binary()
        b += self.DisplayName.to_binary()
        b += self.Description.to_binary()
        b += struct.pack('!I', self.WriteMask)
        b += struct.pack('!I', self.UserWriteMask)
        b += struct.pack('!i', self.NoOfReferences)
        b += struct.pack('!i', len(self.References)
        b += self.References.to_binary()
        b += self.NodeId.to_binary()
        b += self.NodeClass.to_binary()
        b += self.BrowseName.to_binary()
        b += self.DisplayName.to_binary()
        b += self.Description.to_binary()
        b += struct.pack('!I', self.WriteMask)
        b += struct.pack('!I', self.UserWriteMask)
        b += struct.pack('!i', self.NoOfReferences)
        b += struct.pack('!i', len(self.References)
        b += self.References.to_binary()
        b += self.NodeId.to_binary()
        b += self.NodeClass.to_binary()
        b += self.BrowseName.to_binary()
        b += self.DisplayName.to_binary()
        b += self.Description.to_binary()
        b += struct.pack('!I', self.WriteMask)
        b += struct.pack('!I', self.UserWriteMask)
        b += struct.pack('!i', self.NoOfReferences)
        b += struct.pack('!i', len(self.References)
        b += self.References.to_binary()
        b += self.Value.to_binary()
        b += self.DataType.to_binary()
        b += struct.pack('!i', self.ValueRank)
        b += struct.pack('!i', self.NoOfArrayDimensions)
        b += struct.pack('!i', len(self.ArrayDimensions)
        b += struct.pack('!I', self.ArrayDimensions)
        b += struct.pack('!c', self.AccessLevel)
        b += struct.pack('!c', self.UserAccessLevel)
        b += struct.pack('!d', self.MinimumSamplingInterval)
        b += struct.pack('!?', self.Historizing)
        return b

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

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.NodeId.to_binary()
        b += self.NodeClass.to_binary()
        b += self.BrowseName.to_binary()
        b += self.DisplayName.to_binary()
        b += self.Description.to_binary()
        b += struct.pack('!I', self.WriteMask)
        b += struct.pack('!I', self.UserWriteMask)
        b += struct.pack('!i', self.NoOfReferences)
        b += struct.pack('!i', len(self.References)
        b += self.References.to_binary()
        b += self.NodeId.to_binary()
        b += self.NodeClass.to_binary()
        b += self.BrowseName.to_binary()
        b += self.DisplayName.to_binary()
        b += self.Description.to_binary()
        b += struct.pack('!I', self.WriteMask)
        b += struct.pack('!I', self.UserWriteMask)
        b += struct.pack('!i', self.NoOfReferences)
        b += struct.pack('!i', len(self.References)
        b += self.References.to_binary()
        b += self.NodeId.to_binary()
        b += self.NodeClass.to_binary()
        b += self.BrowseName.to_binary()
        b += self.DisplayName.to_binary()
        b += self.Description.to_binary()
        b += struct.pack('!I', self.WriteMask)
        b += struct.pack('!I', self.UserWriteMask)
        b += struct.pack('!i', self.NoOfReferences)
        b += struct.pack('!i', len(self.References)
        b += self.References.to_binary()
        b += self.Value.to_binary()
        b += self.DataType.to_binary()
        b += struct.pack('!i', self.ValueRank)
        b += struct.pack('!i', self.NoOfArrayDimensions)
        b += struct.pack('!i', len(self.ArrayDimensions)
        b += struct.pack('!I', self.ArrayDimensions)
        b += struct.pack('!?', self.IsAbstract)
        return b

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

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.NodeId.to_binary()
        b += self.NodeClass.to_binary()
        b += self.BrowseName.to_binary()
        b += self.DisplayName.to_binary()
        b += self.Description.to_binary()
        b += struct.pack('!I', self.WriteMask)
        b += struct.pack('!I', self.UserWriteMask)
        b += struct.pack('!i', self.NoOfReferences)
        b += struct.pack('!i', len(self.References)
        b += self.References.to_binary()
        b += self.NodeId.to_binary()
        b += self.NodeClass.to_binary()
        b += self.BrowseName.to_binary()
        b += self.DisplayName.to_binary()
        b += self.Description.to_binary()
        b += struct.pack('!I', self.WriteMask)
        b += struct.pack('!I', self.UserWriteMask)
        b += struct.pack('!i', self.NoOfReferences)
        b += struct.pack('!i', len(self.References)
        b += self.References.to_binary()
        b += self.NodeId.to_binary()
        b += self.NodeClass.to_binary()
        b += self.BrowseName.to_binary()
        b += self.DisplayName.to_binary()
        b += self.Description.to_binary()
        b += struct.pack('!I', self.WriteMask)
        b += struct.pack('!I', self.UserWriteMask)
        b += struct.pack('!i', self.NoOfReferences)
        b += struct.pack('!i', len(self.References)
        b += self.References.to_binary()
        b += struct.pack('!?', self.IsAbstract)
        b += struct.pack('!?', self.Symmetric)
        b += self.InverseName.to_binary()
        return b

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

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.NodeId.to_binary()
        b += self.NodeClass.to_binary()
        b += self.BrowseName.to_binary()
        b += self.DisplayName.to_binary()
        b += self.Description.to_binary()
        b += struct.pack('!I', self.WriteMask)
        b += struct.pack('!I', self.UserWriteMask)
        b += struct.pack('!i', self.NoOfReferences)
        b += struct.pack('!i', len(self.References)
        b += self.References.to_binary()
        b += self.NodeId.to_binary()
        b += self.NodeClass.to_binary()
        b += self.BrowseName.to_binary()
        b += self.DisplayName.to_binary()
        b += self.Description.to_binary()
        b += struct.pack('!I', self.WriteMask)
        b += struct.pack('!I', self.UserWriteMask)
        b += struct.pack('!i', self.NoOfReferences)
        b += struct.pack('!i', len(self.References)
        b += self.References.to_binary()
        b += self.NodeId.to_binary()
        b += self.NodeClass.to_binary()
        b += self.BrowseName.to_binary()
        b += self.DisplayName.to_binary()
        b += self.Description.to_binary()
        b += struct.pack('!I', self.WriteMask)
        b += struct.pack('!I', self.UserWriteMask)
        b += struct.pack('!i', self.NoOfReferences)
        b += struct.pack('!i', len(self.References)
        b += self.References.to_binary()
        b += struct.pack('!?', self.Executable)
        b += struct.pack('!?', self.UserExecutable)
        return b

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

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.NodeId.to_binary()
        b += self.NodeClass.to_binary()
        b += self.BrowseName.to_binary()
        b += self.DisplayName.to_binary()
        b += self.Description.to_binary()
        b += struct.pack('!I', self.WriteMask)
        b += struct.pack('!I', self.UserWriteMask)
        b += struct.pack('!i', self.NoOfReferences)
        b += struct.pack('!i', len(self.References)
        b += self.References.to_binary()
        b += self.NodeId.to_binary()
        b += self.NodeClass.to_binary()
        b += self.BrowseName.to_binary()
        b += self.DisplayName.to_binary()
        b += self.Description.to_binary()
        b += struct.pack('!I', self.WriteMask)
        b += struct.pack('!I', self.UserWriteMask)
        b += struct.pack('!i', self.NoOfReferences)
        b += struct.pack('!i', len(self.References)
        b += self.References.to_binary()
        b += self.NodeId.to_binary()
        b += self.NodeClass.to_binary()
        b += self.BrowseName.to_binary()
        b += self.DisplayName.to_binary()
        b += self.Description.to_binary()
        b += struct.pack('!I', self.WriteMask)
        b += struct.pack('!I', self.UserWriteMask)
        b += struct.pack('!i', self.NoOfReferences)
        b += struct.pack('!i', len(self.References)
        b += self.References.to_binary()
        b += struct.pack('!?', self.ContainsNoLoops)
        b += struct.pack('!c', self.EventNotifier)
        return b

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

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.NodeId.to_binary()
        b += self.NodeClass.to_binary()
        b += self.BrowseName.to_binary()
        b += self.DisplayName.to_binary()
        b += self.Description.to_binary()
        b += struct.pack('!I', self.WriteMask)
        b += struct.pack('!I', self.UserWriteMask)
        b += struct.pack('!i', self.NoOfReferences)
        b += struct.pack('!i', len(self.References)
        b += self.References.to_binary()
        b += self.NodeId.to_binary()
        b += self.NodeClass.to_binary()
        b += self.BrowseName.to_binary()
        b += self.DisplayName.to_binary()
        b += self.Description.to_binary()
        b += struct.pack('!I', self.WriteMask)
        b += struct.pack('!I', self.UserWriteMask)
        b += struct.pack('!i', self.NoOfReferences)
        b += struct.pack('!i', len(self.References)
        b += self.References.to_binary()
        b += self.NodeId.to_binary()
        b += self.NodeClass.to_binary()
        b += self.BrowseName.to_binary()
        b += self.DisplayName.to_binary()
        b += self.Description.to_binary()
        b += struct.pack('!I', self.WriteMask)
        b += struct.pack('!I', self.UserWriteMask)
        b += struct.pack('!i', self.NoOfReferences)
        b += struct.pack('!i', len(self.References)
        b += self.References.to_binary()
        b += struct.pack('!?', self.IsAbstract)
        return b

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

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.Name.to_binary()
        b += self.DataType.to_binary()
        b += struct.pack('!i', self.ValueRank)
        b += struct.pack('!i', self.NoOfArrayDimensions)
        b += struct.pack('!i', len(self.ArrayDimensions)
        b += struct.pack('!I', self.ArrayDimensions)
        b += self.Description.to_binary()
        return b

class EnumValueType(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.Value = None
        self.DisplayName = None
        self.Description = None

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += struct.pack('!q', self.Value)
        b += self.DisplayName.to_binary()
        b += self.Description.to_binary()
        return b

class TimeZoneDataType(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.Offset = None
        self.DaylightSavingInOffset = None

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += struct.pack('!h', self.Offset)
        b += struct.pack('!?', self.DaylightSavingInOffset)
        return b

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

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.ApplicationUri.to_binary()
        b += self.ProductUri.to_binary()
        b += self.ApplicationName.to_binary()
        b += self.ApplicationType.to_binary()
        b += self.GatewayServerUri.to_binary()
        b += self.DiscoveryProfileUri.to_binary()
        b += struct.pack('!i', self.NoOfDiscoveryUrls)
        b += struct.pack('!i', len(self.DiscoveryUrls)
        b += self.DiscoveryUrls.to_binary()
        return b

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

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.AuthenticationToken.to_binary()
        b += struct.pack('!d', self.Timestamp)
        b += struct.pack('!I', self.RequestHandle)
        b += struct.pack('!I', self.ReturnDiagnostics)
        b += self.AuditEntryId.to_binary()
        b += struct.pack('!I', self.TimeoutHint)
        b += self.AdditionalHeader.to_binary()
        return b

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

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += struct.pack('!d', self.Timestamp)
        b += struct.pack('!I', self.RequestHandle)
        b += self.ServiceResult.to_binary()
        b += self.ServiceDiagnostics.to_binary()
        b += struct.pack('!i', self.NoOfStringTable)
        b += struct.pack('!i', len(self.StringTable)
        b += self.StringTable.to_binary()
        b += self.AdditionalHeader.to_binary()
        return b

class ServiceFault(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.ResponseHeader = None

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.ResponseHeader.to_binary()
        return b

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

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.RequestHeader.to_binary()
        b += self.EndpointUrl.to_binary()
        b += struct.pack('!i', self.NoOfLocaleIds)
        b += struct.pack('!i', len(self.LocaleIds)
        b += self.LocaleIds.to_binary()
        b += struct.pack('!i', self.NoOfServerUris)
        b += struct.pack('!i', len(self.ServerUris)
        b += self.ServerUris.to_binary()
        return b

class FindServersResponse(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.ResponseHeader = None
        self.NoOfServers = None
        self.Servers = []

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.ResponseHeader.to_binary()
        b += struct.pack('!i', self.NoOfServers)
        b += struct.pack('!i', len(self.Servers)
        b += self.Servers.to_binary()
        return b

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

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.PolicyId.to_binary()
        b += self.TokenType.to_binary()
        b += self.IssuedTokenType.to_binary()
        b += self.IssuerEndpointUrl.to_binary()
        b += self.SecurityPolicyUri.to_binary()
        return b

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

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.EndpointUrl.to_binary()
        b += self.Server.to_binary()
        b += struct.pack('!c', self.ServerCertificate)
        b += self.SecurityMode.to_binary()
        b += self.SecurityPolicyUri.to_binary()
        b += struct.pack('!i', self.NoOfUserIdentityTokens)
        b += struct.pack('!i', len(self.UserIdentityTokens)
        b += self.UserIdentityTokens.to_binary()
        b += self.TransportProfileUri.to_binary()
        b += struct.pack('!c', self.SecurityLevel)
        return b

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

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.RequestHeader.to_binary()
        b += self.EndpointUrl.to_binary()
        b += struct.pack('!i', self.NoOfLocaleIds)
        b += struct.pack('!i', len(self.LocaleIds)
        b += self.LocaleIds.to_binary()
        b += struct.pack('!i', self.NoOfProfileUris)
        b += struct.pack('!i', len(self.ProfileUris)
        b += self.ProfileUris.to_binary()
        return b

class GetEndpointsResponse(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.ResponseHeader = None
        self.NoOfEndpoints = None
        self.Endpoints = []

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.ResponseHeader.to_binary()
        b += struct.pack('!i', self.NoOfEndpoints)
        b += struct.pack('!i', len(self.Endpoints)
        b += self.Endpoints.to_binary()
        return b

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

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.ServerUri.to_binary()
        b += self.ProductUri.to_binary()
        b += struct.pack('!i', self.NoOfServerNames)
        b += struct.pack('!i', len(self.ServerNames)
        b += self.ServerNames.to_binary()
        b += self.ServerType.to_binary()
        b += self.GatewayServerUri.to_binary()
        b += struct.pack('!i', self.NoOfDiscoveryUrls)
        b += struct.pack('!i', len(self.DiscoveryUrls)
        b += self.DiscoveryUrls.to_binary()
        b += self.SemaphoreFilePath.to_binary()
        b += struct.pack('!?', self.IsOnline)
        return b

class RegisterServerRequest(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.RequestHeader = None
        self.Server = None

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.RequestHeader.to_binary()
        b += self.Server.to_binary()
        return b

class RegisterServerResponse(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.ResponseHeader = None

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.ResponseHeader.to_binary()
        return b

class ChannelSecurityToken(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.ChannelId = None
        self.TokenId = None
        self.CreatedAt = None
        self.RevisedLifetime = None

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += struct.pack('!I', self.ChannelId)
        b += struct.pack('!I', self.TokenId)
        b += struct.pack('!d', self.CreatedAt)
        b += struct.pack('!I', self.RevisedLifetime)
        return b

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

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.RequestHeader.to_binary()
        b += struct.pack('!I', self.ClientProtocolVersion)
        b += self.RequestType.to_binary()
        b += self.SecurityMode.to_binary()
        b += struct.pack('!c', self.ClientNonce)
        b += struct.pack('!I', self.RequestedLifetime)
        return b

class OpenSecureChannelResponse(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.ResponseHeader = None
        self.ServerProtocolVersion = None
        self.SecurityToken = None
        self.ServerNonce = None

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.ResponseHeader.to_binary()
        b += struct.pack('!I', self.ServerProtocolVersion)
        b += self.SecurityToken.to_binary()
        b += struct.pack('!c', self.ServerNonce)
        return b

class CloseSecureChannelRequest(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.RequestHeader = None

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.RequestHeader.to_binary()
        return b

class CloseSecureChannelResponse(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.ResponseHeader = None

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.ResponseHeader.to_binary()
        return b

class SignedSoftwareCertificate(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.CertificateData = None
        self.Signature = None

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += struct.pack('!c', self.CertificateData)
        b += struct.pack('!c', self.Signature)
        return b

class SignatureData(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.Algorithm = None
        self.Signature = None

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.Algorithm.to_binary()
        b += struct.pack('!c', self.Signature)
        return b

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

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.RequestHeader.to_binary()
        b += self.ClientDescription.to_binary()
        b += self.ServerUri.to_binary()
        b += self.EndpointUrl.to_binary()
        b += self.SessionName.to_binary()
        b += struct.pack('!c', self.ClientNonce)
        b += struct.pack('!c', self.ClientCertificate)
        b += struct.pack('!d', self.RequestedSessionTimeout)
        b += struct.pack('!I', self.MaxResponseMessageSize)
        return b

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

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.ResponseHeader.to_binary()
        b += self.SessionId.to_binary()
        b += self.AuthenticationToken.to_binary()
        b += struct.pack('!d', self.RevisedSessionTimeout)
        b += struct.pack('!c', self.ServerNonce)
        b += struct.pack('!c', self.ServerCertificate)
        b += struct.pack('!i', self.NoOfServerEndpoints)
        b += struct.pack('!i', len(self.ServerEndpoints)
        b += self.ServerEndpoints.to_binary()
        b += struct.pack('!i', self.NoOfServerSoftwareCertificates)
        b += struct.pack('!i', len(self.ServerSoftwareCertificates)
        b += self.ServerSoftwareCertificates.to_binary()
        b += self.ServerSignature.to_binary()
        b += struct.pack('!I', self.MaxRequestMessageSize)
        return b

class UserIdentityToken(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.PolicyId = None

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.PolicyId.to_binary()
        return b

class AnonymousIdentityToken(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.PolicyId = None
        self.PolicyId = None

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.PolicyId.to_binary()
        b += self.PolicyId.to_binary()
        return b

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

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.PolicyId.to_binary()
        b += self.PolicyId.to_binary()
        b += self.UserName.to_binary()
        b += struct.pack('!c', self.Password)
        b += self.EncryptionAlgorithm.to_binary()
        return b

class X509IdentityToken(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.PolicyId = None
        self.PolicyId = None
        self.CertificateData = None

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.PolicyId.to_binary()
        b += self.PolicyId.to_binary()
        b += struct.pack('!c', self.CertificateData)
        return b

class IssuedIdentityToken(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.PolicyId = None
        self.PolicyId = None
        self.TokenData = None
        self.EncryptionAlgorithm = None

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.PolicyId.to_binary()
        b += self.PolicyId.to_binary()
        b += struct.pack('!c', self.TokenData)
        b += self.EncryptionAlgorithm.to_binary()
        return b

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

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.RequestHeader.to_binary()
        b += self.ClientSignature.to_binary()
        b += struct.pack('!i', self.NoOfClientSoftwareCertificates)
        b += struct.pack('!i', len(self.ClientSoftwareCertificates)
        b += self.ClientSoftwareCertificates.to_binary()
        b += struct.pack('!i', self.NoOfLocaleIds)
        b += struct.pack('!i', len(self.LocaleIds)
        b += self.LocaleIds.to_binary()
        b += self.UserIdentityToken.to_binary()
        b += self.UserTokenSignature.to_binary()
        return b

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

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.ResponseHeader.to_binary()
        b += struct.pack('!c', self.ServerNonce)
        b += struct.pack('!i', self.NoOfResults)
        b += struct.pack('!i', len(self.Results)
        b += self.Results.to_binary()
        b += struct.pack('!i', self.NoOfDiagnosticInfos)
        b += struct.pack('!i', len(self.DiagnosticInfos)
        b += self.DiagnosticInfos.to_binary()
        return b

class CloseSessionRequest(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.RequestHeader = None
        self.DeleteSubscriptions = None

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.RequestHeader.to_binary()
        b += struct.pack('!?', self.DeleteSubscriptions)
        return b

class CloseSessionResponse(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.ResponseHeader = None

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.ResponseHeader.to_binary()
        return b

class CancelRequest(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.RequestHeader = None
        self.RequestHandle = None

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.RequestHeader.to_binary()
        b += struct.pack('!I', self.RequestHandle)
        return b

class CancelResponse(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.ResponseHeader = None
        self.CancelCount = None

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.ResponseHeader.to_binary()
        b += struct.pack('!I', self.CancelCount)
        return b

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

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += struct.pack('!I', self.SpecifiedAttributes)
        b += self.DisplayName.to_binary()
        b += self.Description.to_binary()
        b += struct.pack('!I', self.WriteMask)
        b += struct.pack('!I', self.UserWriteMask)
        return b

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

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += struct.pack('!I', self.SpecifiedAttributes)
        b += self.DisplayName.to_binary()
        b += self.Description.to_binary()
        b += struct.pack('!I', self.WriteMask)
        b += struct.pack('!I', self.UserWriteMask)
        b += struct.pack('!I', self.SpecifiedAttributes)
        b += self.DisplayName.to_binary()
        b += self.Description.to_binary()
        b += struct.pack('!I', self.WriteMask)
        b += struct.pack('!I', self.UserWriteMask)
        b += struct.pack('!c', self.EventNotifier)
        return b

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

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += struct.pack('!I', self.SpecifiedAttributes)
        b += self.DisplayName.to_binary()
        b += self.Description.to_binary()
        b += struct.pack('!I', self.WriteMask)
        b += struct.pack('!I', self.UserWriteMask)
        b += struct.pack('!I', self.SpecifiedAttributes)
        b += self.DisplayName.to_binary()
        b += self.Description.to_binary()
        b += struct.pack('!I', self.WriteMask)
        b += struct.pack('!I', self.UserWriteMask)
        b += self.Value.to_binary()
        b += self.DataType.to_binary()
        b += struct.pack('!i', self.ValueRank)
        b += struct.pack('!i', self.NoOfArrayDimensions)
        b += struct.pack('!i', len(self.ArrayDimensions)
        b += struct.pack('!I', self.ArrayDimensions)
        b += struct.pack('!c', self.AccessLevel)
        b += struct.pack('!c', self.UserAccessLevel)
        b += struct.pack('!d', self.MinimumSamplingInterval)
        b += struct.pack('!?', self.Historizing)
        return b

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

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += struct.pack('!I', self.SpecifiedAttributes)
        b += self.DisplayName.to_binary()
        b += self.Description.to_binary()
        b += struct.pack('!I', self.WriteMask)
        b += struct.pack('!I', self.UserWriteMask)
        b += struct.pack('!I', self.SpecifiedAttributes)
        b += self.DisplayName.to_binary()
        b += self.Description.to_binary()
        b += struct.pack('!I', self.WriteMask)
        b += struct.pack('!I', self.UserWriteMask)
        b += struct.pack('!?', self.Executable)
        b += struct.pack('!?', self.UserExecutable)
        return b

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

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += struct.pack('!I', self.SpecifiedAttributes)
        b += self.DisplayName.to_binary()
        b += self.Description.to_binary()
        b += struct.pack('!I', self.WriteMask)
        b += struct.pack('!I', self.UserWriteMask)
        b += struct.pack('!I', self.SpecifiedAttributes)
        b += self.DisplayName.to_binary()
        b += self.Description.to_binary()
        b += struct.pack('!I', self.WriteMask)
        b += struct.pack('!I', self.UserWriteMask)
        b += struct.pack('!?', self.IsAbstract)
        return b

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

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += struct.pack('!I', self.SpecifiedAttributes)
        b += self.DisplayName.to_binary()
        b += self.Description.to_binary()
        b += struct.pack('!I', self.WriteMask)
        b += struct.pack('!I', self.UserWriteMask)
        b += struct.pack('!I', self.SpecifiedAttributes)
        b += self.DisplayName.to_binary()
        b += self.Description.to_binary()
        b += struct.pack('!I', self.WriteMask)
        b += struct.pack('!I', self.UserWriteMask)
        b += self.Value.to_binary()
        b += self.DataType.to_binary()
        b += struct.pack('!i', self.ValueRank)
        b += struct.pack('!i', self.NoOfArrayDimensions)
        b += struct.pack('!i', len(self.ArrayDimensions)
        b += struct.pack('!I', self.ArrayDimensions)
        b += struct.pack('!?', self.IsAbstract)
        return b

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

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += struct.pack('!I', self.SpecifiedAttributes)
        b += self.DisplayName.to_binary()
        b += self.Description.to_binary()
        b += struct.pack('!I', self.WriteMask)
        b += struct.pack('!I', self.UserWriteMask)
        b += struct.pack('!I', self.SpecifiedAttributes)
        b += self.DisplayName.to_binary()
        b += self.Description.to_binary()
        b += struct.pack('!I', self.WriteMask)
        b += struct.pack('!I', self.UserWriteMask)
        b += struct.pack('!?', self.IsAbstract)
        b += struct.pack('!?', self.Symmetric)
        b += self.InverseName.to_binary()
        return b

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

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += struct.pack('!I', self.SpecifiedAttributes)
        b += self.DisplayName.to_binary()
        b += self.Description.to_binary()
        b += struct.pack('!I', self.WriteMask)
        b += struct.pack('!I', self.UserWriteMask)
        b += struct.pack('!I', self.SpecifiedAttributes)
        b += self.DisplayName.to_binary()
        b += self.Description.to_binary()
        b += struct.pack('!I', self.WriteMask)
        b += struct.pack('!I', self.UserWriteMask)
        b += struct.pack('!?', self.IsAbstract)
        return b

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

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += struct.pack('!I', self.SpecifiedAttributes)
        b += self.DisplayName.to_binary()
        b += self.Description.to_binary()
        b += struct.pack('!I', self.WriteMask)
        b += struct.pack('!I', self.UserWriteMask)
        b += struct.pack('!I', self.SpecifiedAttributes)
        b += self.DisplayName.to_binary()
        b += self.Description.to_binary()
        b += struct.pack('!I', self.WriteMask)
        b += struct.pack('!I', self.UserWriteMask)
        b += struct.pack('!?', self.ContainsNoLoops)
        b += struct.pack('!c', self.EventNotifier)
        return b

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

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.ParentNodeId.to_binary()
        b += self.ReferenceTypeId.to_binary()
        b += self.RequestedNewNodeId.to_binary()
        b += self.BrowseName.to_binary()
        b += self.NodeClass.to_binary()
        b += self.NodeAttributes.to_binary()
        b += self.TypeDefinition.to_binary()
        return b

class AddNodesResult(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.StatusCode = None
        self.AddedNodeId = None

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.StatusCode.to_binary()
        b += self.AddedNodeId.to_binary()
        return b

class AddNodesRequest(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.RequestHeader = None
        self.NoOfNodesToAdd = None
        self.NodesToAdd = []

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.RequestHeader.to_binary()
        b += struct.pack('!i', self.NoOfNodesToAdd)
        b += struct.pack('!i', len(self.NodesToAdd)
        b += self.NodesToAdd.to_binary()
        return b

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

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.ResponseHeader.to_binary()
        b += struct.pack('!i', self.NoOfResults)
        b += struct.pack('!i', len(self.Results)
        b += self.Results.to_binary()
        b += struct.pack('!i', self.NoOfDiagnosticInfos)
        b += struct.pack('!i', len(self.DiagnosticInfos)
        b += self.DiagnosticInfos.to_binary()
        return b

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

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.SourceNodeId.to_binary()
        b += self.ReferenceTypeId.to_binary()
        b += struct.pack('!?', self.IsForward)
        b += self.TargetServerUri.to_binary()
        b += self.TargetNodeId.to_binary()
        b += self.TargetNodeClass.to_binary()
        return b

class AddReferencesRequest(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.RequestHeader = None
        self.NoOfReferencesToAdd = None
        self.ReferencesToAdd = []

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.RequestHeader.to_binary()
        b += struct.pack('!i', self.NoOfReferencesToAdd)
        b += struct.pack('!i', len(self.ReferencesToAdd)
        b += self.ReferencesToAdd.to_binary()
        return b

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

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.ResponseHeader.to_binary()
        b += struct.pack('!i', self.NoOfResults)
        b += struct.pack('!i', len(self.Results)
        b += self.Results.to_binary()
        b += struct.pack('!i', self.NoOfDiagnosticInfos)
        b += struct.pack('!i', len(self.DiagnosticInfos)
        b += self.DiagnosticInfos.to_binary()
        return b

class DeleteNodesItem(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.NodeId = None
        self.DeleteTargetReferences = None

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.NodeId.to_binary()
        b += struct.pack('!?', self.DeleteTargetReferences)
        return b

class DeleteNodesRequest(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.RequestHeader = None
        self.NoOfNodesToDelete = None
        self.NodesToDelete = []

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.RequestHeader.to_binary()
        b += struct.pack('!i', self.NoOfNodesToDelete)
        b += struct.pack('!i', len(self.NodesToDelete)
        b += self.NodesToDelete.to_binary()
        return b

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

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.ResponseHeader.to_binary()
        b += struct.pack('!i', self.NoOfResults)
        b += struct.pack('!i', len(self.Results)
        b += self.Results.to_binary()
        b += struct.pack('!i', self.NoOfDiagnosticInfos)
        b += struct.pack('!i', len(self.DiagnosticInfos)
        b += self.DiagnosticInfos.to_binary()
        return b

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

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.SourceNodeId.to_binary()
        b += self.ReferenceTypeId.to_binary()
        b += struct.pack('!?', self.IsForward)
        b += self.TargetNodeId.to_binary()
        b += struct.pack('!?', self.DeleteBidirectional)
        return b

class DeleteReferencesRequest(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.RequestHeader = None
        self.NoOfReferencesToDelete = None
        self.ReferencesToDelete = []

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.RequestHeader.to_binary()
        b += struct.pack('!i', self.NoOfReferencesToDelete)
        b += struct.pack('!i', len(self.ReferencesToDelete)
        b += self.ReferencesToDelete.to_binary()
        return b

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

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.ResponseHeader.to_binary()
        b += struct.pack('!i', self.NoOfResults)
        b += struct.pack('!i', len(self.Results)
        b += self.Results.to_binary()
        b += struct.pack('!i', self.NoOfDiagnosticInfos)
        b += struct.pack('!i', len(self.DiagnosticInfos)
        b += self.DiagnosticInfos.to_binary()
        return b

class ViewDescription(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.ViewId = None
        self.Timestamp = None
        self.ViewVersion = None

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.ViewId.to_binary()
        b += struct.pack('!d', self.Timestamp)
        b += struct.pack('!I', self.ViewVersion)
        return b

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

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.NodeId.to_binary()
        b += self.BrowseDirection.to_binary()
        b += self.ReferenceTypeId.to_binary()
        b += struct.pack('!?', self.IncludeSubtypes)
        b += struct.pack('!I', self.NodeClassMask)
        b += struct.pack('!I', self.ResultMask)
        return b

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

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.ReferenceTypeId.to_binary()
        b += struct.pack('!?', self.IsForward)
        b += self.NodeId.to_binary()
        b += self.BrowseName.to_binary()
        b += self.DisplayName.to_binary()
        b += self.NodeClass.to_binary()
        b += self.TypeDefinition.to_binary()
        return b

class BrowseResult(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.StatusCode = None
        self.ContinuationPoint = None
        self.NoOfReferences = None
        self.References = []

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.StatusCode.to_binary()
        b += struct.pack('!c', self.ContinuationPoint)
        b += struct.pack('!i', self.NoOfReferences)
        b += struct.pack('!i', len(self.References)
        b += self.References.to_binary()
        return b

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

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.RequestHeader.to_binary()
        b += self.View.to_binary()
        b += struct.pack('!I', self.RequestedMaxReferencesPerNode)
        b += struct.pack('!i', self.NoOfNodesToBrowse)
        b += struct.pack('!i', len(self.NodesToBrowse)
        b += self.NodesToBrowse.to_binary()
        return b

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

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.ResponseHeader.to_binary()
        b += struct.pack('!i', self.NoOfResults)
        b += struct.pack('!i', len(self.Results)
        b += self.Results.to_binary()
        b += struct.pack('!i', self.NoOfDiagnosticInfos)
        b += struct.pack('!i', len(self.DiagnosticInfos)
        b += self.DiagnosticInfos.to_binary()
        return b

class BrowseNextRequest(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.RequestHeader = None
        self.ReleaseContinuationPoints = None
        self.NoOfContinuationPoints = None
        self.ContinuationPoints = []

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.RequestHeader.to_binary()
        b += struct.pack('!?', self.ReleaseContinuationPoints)
        b += struct.pack('!i', self.NoOfContinuationPoints)
        b += struct.pack('!i', len(self.ContinuationPoints)
        b += struct.pack('!c', self.ContinuationPoints)
        return b

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

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.ResponseHeader.to_binary()
        b += struct.pack('!i', self.NoOfResults)
        b += struct.pack('!i', len(self.Results)
        b += self.Results.to_binary()
        b += struct.pack('!i', self.NoOfDiagnosticInfos)
        b += struct.pack('!i', len(self.DiagnosticInfos)
        b += self.DiagnosticInfos.to_binary()
        return b

class RelativePathElement(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.ReferenceTypeId = None
        self.IsInverse = None
        self.IncludeSubtypes = None
        self.TargetName = None

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.ReferenceTypeId.to_binary()
        b += struct.pack('!?', self.IsInverse)
        b += struct.pack('!?', self.IncludeSubtypes)
        b += self.TargetName.to_binary()
        return b

class RelativePath(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.NoOfElements = None
        self.Elements = []

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += struct.pack('!i', self.NoOfElements)
        b += struct.pack('!i', len(self.Elements)
        b += self.Elements.to_binary()
        return b

class BrowsePath(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.StartingNode = None
        self.RelativePath = None

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.StartingNode.to_binary()
        b += self.RelativePath.to_binary()
        return b

class BrowsePathTarget(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.TargetId = None
        self.RemainingPathIndex = None

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.TargetId.to_binary()
        b += struct.pack('!I', self.RemainingPathIndex)
        return b

class BrowsePathResult(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.StatusCode = None
        self.NoOfTargets = None
        self.Targets = []

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.StatusCode.to_binary()
        b += struct.pack('!i', self.NoOfTargets)
        b += struct.pack('!i', len(self.Targets)
        b += self.Targets.to_binary()
        return b

class TranslateBrowsePathsToNodeIdsRequest(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.RequestHeader = None
        self.NoOfBrowsePaths = None
        self.BrowsePaths = []

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.RequestHeader.to_binary()
        b += struct.pack('!i', self.NoOfBrowsePaths)
        b += struct.pack('!i', len(self.BrowsePaths)
        b += self.BrowsePaths.to_binary()
        return b

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

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.ResponseHeader.to_binary()
        b += struct.pack('!i', self.NoOfResults)
        b += struct.pack('!i', len(self.Results)
        b += self.Results.to_binary()
        b += struct.pack('!i', self.NoOfDiagnosticInfos)
        b += struct.pack('!i', len(self.DiagnosticInfos)
        b += self.DiagnosticInfos.to_binary()
        return b

class RegisterNodesRequest(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.RequestHeader = None
        self.NoOfNodesToRegister = None
        self.NodesToRegister = []

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.RequestHeader.to_binary()
        b += struct.pack('!i', self.NoOfNodesToRegister)
        b += struct.pack('!i', len(self.NodesToRegister)
        b += self.NodesToRegister.to_binary()
        return b

class RegisterNodesResponse(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.ResponseHeader = None
        self.NoOfRegisteredNodeIds = None
        self.RegisteredNodeIds = []

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.ResponseHeader.to_binary()
        b += struct.pack('!i', self.NoOfRegisteredNodeIds)
        b += struct.pack('!i', len(self.RegisteredNodeIds)
        b += self.RegisteredNodeIds.to_binary()
        return b

class UnregisterNodesRequest(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.RequestHeader = None
        self.NoOfNodesToUnregister = None
        self.NodesToUnregister = []

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.RequestHeader.to_binary()
        b += struct.pack('!i', self.NoOfNodesToUnregister)
        b += struct.pack('!i', len(self.NodesToUnregister)
        b += self.NodesToUnregister.to_binary()
        return b

class UnregisterNodesResponse(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.ResponseHeader = None

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.ResponseHeader.to_binary()
        return b

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

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += struct.pack('!i', self.OperationTimeout)
        b += struct.pack('!?', self.UseBinaryEncoding)
        b += struct.pack('!i', self.MaxStringLength)
        b += struct.pack('!i', self.MaxByteStringLength)
        b += struct.pack('!i', self.MaxArrayLength)
        b += struct.pack('!i', self.MaxMessageSize)
        b += struct.pack('!i', self.MaxBufferSize)
        b += struct.pack('!i', self.ChannelLifetime)
        b += struct.pack('!i', self.SecurityTokenLifetime)
        return b

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

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.OrganizationUri.to_binary()
        b += self.ProfileId.to_binary()
        b += self.ComplianceTool.to_binary()
        b += struct.pack('!d', self.ComplianceDate)
        b += self.ComplianceLevel.to_binary()
        b += struct.pack('!i', self.NoOfUnsupportedUnitIds)
        b += struct.pack('!i', len(self.UnsupportedUnitIds)
        b += self.UnsupportedUnitIds.to_binary()
        return b

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

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.ProductName.to_binary()
        b += self.ProductUri.to_binary()
        b += self.VendorName.to_binary()
        b += struct.pack('!c', self.VendorProductCertificate)
        b += self.SoftwareVersion.to_binary()
        b += self.BuildNumber.to_binary()
        b += struct.pack('!d', self.BuildDate)
        b += self.IssuedBy.to_binary()
        b += struct.pack('!d', self.IssueDate)
        b += struct.pack('!i', self.NoOfSupportedProfiles)
        b += struct.pack('!i', len(self.SupportedProfiles)
        b += self.SupportedProfiles.to_binary()
        return b

class QueryDataDescription(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.RelativePath = None
        self.AttributeId = None
        self.IndexRange = None

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.RelativePath.to_binary()
        b += struct.pack('!I', self.AttributeId)
        b += self.IndexRange.to_binary()
        return b

class NodeTypeDescription(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.TypeDefinitionNode = None
        self.IncludeSubTypes = None
        self.NoOfDataToReturn = None
        self.DataToReturn = []

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.TypeDefinitionNode.to_binary()
        b += struct.pack('!?', self.IncludeSubTypes)
        b += struct.pack('!i', self.NoOfDataToReturn)
        b += struct.pack('!i', len(self.DataToReturn)
        b += self.DataToReturn.to_binary()
        return b

class QueryDataSet(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.NodeId = None
        self.TypeDefinitionNode = None
        self.NoOfValues = None
        self.Values = []

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.NodeId.to_binary()
        b += self.TypeDefinitionNode.to_binary()
        b += struct.pack('!i', self.NoOfValues)
        b += struct.pack('!i', len(self.Values)
        b += self.Values.to_binary()
        return b

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

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.NodeId.to_binary()
        b += self.ReferenceTypeId.to_binary()
        b += struct.pack('!?', self.IsForward)
        b += struct.pack('!i', self.NoOfReferencedNodeIds)
        b += struct.pack('!i', len(self.ReferencedNodeIds)
        b += self.ReferencedNodeIds.to_binary()
        return b

class ContentFilterElement(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.FilterOperator = None
        self.NoOfFilterOperands = None
        self.FilterOperands = []

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.FilterOperator.to_binary()
        b += struct.pack('!i', self.NoOfFilterOperands)
        b += struct.pack('!i', len(self.FilterOperands)
        b += self.FilterOperands.to_binary()
        return b

class ContentFilter(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.NoOfElements = None
        self.Elements = []

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += struct.pack('!i', self.NoOfElements)
        b += struct.pack('!i', len(self.Elements)
        b += self.Elements.to_binary()
        return b

class FilterOperand(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        return b

class ElementOperand(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.Index = None

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += struct.pack('!I', self.Index)
        return b

class LiteralOperand(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.Value = None

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.Value.to_binary()
        return b

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

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.NodeId.to_binary()
        b += self.Alias.to_binary()
        b += self.BrowsePath.to_binary()
        b += struct.pack('!I', self.AttributeId)
        b += self.IndexRange.to_binary()
        return b

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

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.TypeDefinitionId.to_binary()
        b += struct.pack('!i', self.NoOfBrowsePath)
        b += struct.pack('!i', len(self.BrowsePath)
        b += self.BrowsePath.to_binary()
        b += struct.pack('!I', self.AttributeId)
        b += self.IndexRange.to_binary()
        return b

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

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.StatusCode.to_binary()
        b += struct.pack('!i', self.NoOfOperandStatusCodes)
        b += struct.pack('!i', len(self.OperandStatusCodes)
        b += self.OperandStatusCodes.to_binary()
        b += struct.pack('!i', self.NoOfOperandDiagnosticInfos)
        b += struct.pack('!i', len(self.OperandDiagnosticInfos)
        b += self.OperandDiagnosticInfos.to_binary()
        return b

class ContentFilterResult(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.NoOfElementResults = None
        self.ElementResults = []
        self.NoOfElementDiagnosticInfos = None
        self.ElementDiagnosticInfos = []

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += struct.pack('!i', self.NoOfElementResults)
        b += struct.pack('!i', len(self.ElementResults)
        b += self.ElementResults.to_binary()
        b += struct.pack('!i', self.NoOfElementDiagnosticInfos)
        b += struct.pack('!i', len(self.ElementDiagnosticInfos)
        b += self.ElementDiagnosticInfos.to_binary()
        return b

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

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.StatusCode.to_binary()
        b += struct.pack('!i', self.NoOfDataStatusCodes)
        b += struct.pack('!i', len(self.DataStatusCodes)
        b += self.DataStatusCodes.to_binary()
        b += struct.pack('!i', self.NoOfDataDiagnosticInfos)
        b += struct.pack('!i', len(self.DataDiagnosticInfos)
        b += self.DataDiagnosticInfos.to_binary()
        return b

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

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.RequestHeader.to_binary()
        b += self.View.to_binary()
        b += struct.pack('!i', self.NoOfNodeTypes)
        b += struct.pack('!i', len(self.NodeTypes)
        b += self.NodeTypes.to_binary()
        b += self.Filter.to_binary()
        b += struct.pack('!I', self.MaxDataSetsToReturn)
        b += struct.pack('!I', self.MaxReferencesToReturn)
        return b

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

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.ResponseHeader.to_binary()
        b += struct.pack('!i', self.NoOfQueryDataSets)
        b += struct.pack('!i', len(self.QueryDataSets)
        b += self.QueryDataSets.to_binary()
        b += struct.pack('!c', self.ContinuationPoint)
        b += struct.pack('!i', self.NoOfParsingResults)
        b += struct.pack('!i', len(self.ParsingResults)
        b += self.ParsingResults.to_binary()
        b += struct.pack('!i', self.NoOfDiagnosticInfos)
        b += struct.pack('!i', len(self.DiagnosticInfos)
        b += self.DiagnosticInfos.to_binary()
        b += self.FilterResult.to_binary()
        return b

class QueryNextRequest(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.RequestHeader = None
        self.ReleaseContinuationPoint = None
        self.ContinuationPoint = None

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.RequestHeader.to_binary()
        b += struct.pack('!?', self.ReleaseContinuationPoint)
        b += struct.pack('!c', self.ContinuationPoint)
        return b

class QueryNextResponse(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.ResponseHeader = None
        self.NoOfQueryDataSets = None
        self.QueryDataSets = []
        self.RevisedContinuationPoint = None

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.ResponseHeader.to_binary()
        b += struct.pack('!i', self.NoOfQueryDataSets)
        b += struct.pack('!i', len(self.QueryDataSets)
        b += self.QueryDataSets.to_binary()
        b += struct.pack('!c', self.RevisedContinuationPoint)
        return b

class ReadValueId(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.NodeId = None
        self.AttributeId = None
        self.IndexRange = None
        self.DataEncoding = None

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.NodeId.to_binary()
        b += struct.pack('!I', self.AttributeId)
        b += self.IndexRange.to_binary()
        b += self.DataEncoding.to_binary()
        return b

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

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.RequestHeader.to_binary()
        b += struct.pack('!d', self.MaxAge)
        b += self.TimestampsToReturn.to_binary()
        b += struct.pack('!i', self.NoOfNodesToRead)
        b += struct.pack('!i', len(self.NodesToRead)
        b += self.NodesToRead.to_binary()
        return b

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

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.ResponseHeader.to_binary()
        b += struct.pack('!i', self.NoOfResults)
        b += struct.pack('!i', len(self.Results)
        b += self.Results.to_binary()
        b += struct.pack('!i', self.NoOfDiagnosticInfos)
        b += struct.pack('!i', len(self.DiagnosticInfos)
        b += self.DiagnosticInfos.to_binary()
        return b

class HistoryReadValueId(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.NodeId = None
        self.IndexRange = None
        self.DataEncoding = None
        self.ContinuationPoint = None

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.NodeId.to_binary()
        b += self.IndexRange.to_binary()
        b += self.DataEncoding.to_binary()
        b += struct.pack('!c', self.ContinuationPoint)
        return b

class HistoryReadResult(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.StatusCode = None
        self.ContinuationPoint = None
        self.HistoryData = None

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.StatusCode.to_binary()
        b += struct.pack('!c', self.ContinuationPoint)
        b += self.HistoryData.to_binary()
        return b

class HistoryReadDetails(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        return b

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

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += struct.pack('!?', self.IsReadModified)
        b += struct.pack('!d', self.StartTime)
        b += struct.pack('!d', self.EndTime)
        b += struct.pack('!I', self.NumValuesPerNode)
        b += struct.pack('!?', self.ReturnBounds)
        return b

class ReadAtTimeDetails(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.NoOfReqTimes = None
        self.ReqTimes = []
        self.UseSimpleBounds = None

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += struct.pack('!i', self.NoOfReqTimes)
        b += struct.pack('!i', len(self.ReqTimes)
        b += struct.pack('!d', self.ReqTimes)
        b += struct.pack('!?', self.UseSimpleBounds)
        return b

class HistoryData(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.NoOfDataValues = None
        self.DataValues = []

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += struct.pack('!i', self.NoOfDataValues)
        b += struct.pack('!i', len(self.DataValues)
        b += self.DataValues.to_binary()
        return b

class ModificationInfo(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.ModificationTime = None
        self.UpdateType = None
        self.UserName = None

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += struct.pack('!d', self.ModificationTime)
        b += self.UpdateType.to_binary()
        b += self.UserName.to_binary()
        return b

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

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += struct.pack('!i', self.NoOfDataValues)
        b += struct.pack('!i', len(self.DataValues)
        b += self.DataValues.to_binary()
        b += struct.pack('!i', self.NoOfDataValues)
        b += struct.pack('!i', len(self.DataValues)
        b += self.DataValues.to_binary()
        b += struct.pack('!i', self.NoOfModificationInfos)
        b += struct.pack('!i', len(self.ModificationInfos)
        b += self.ModificationInfos.to_binary()
        return b

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

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.RequestHeader.to_binary()
        b += self.HistoryReadDetails.to_binary()
        b += self.TimestampsToReturn.to_binary()
        b += struct.pack('!?', self.ReleaseContinuationPoints)
        b += struct.pack('!i', self.NoOfNodesToRead)
        b += struct.pack('!i', len(self.NodesToRead)
        b += self.NodesToRead.to_binary()
        return b

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

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.ResponseHeader.to_binary()
        b += struct.pack('!i', self.NoOfResults)
        b += struct.pack('!i', len(self.Results)
        b += self.Results.to_binary()
        b += struct.pack('!i', self.NoOfDiagnosticInfos)
        b += struct.pack('!i', len(self.DiagnosticInfos)
        b += self.DiagnosticInfos.to_binary()
        return b

class WriteValue(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.NodeId = None
        self.AttributeId = None
        self.IndexRange = None
        self.Value = None

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.NodeId.to_binary()
        b += struct.pack('!I', self.AttributeId)
        b += self.IndexRange.to_binary()
        b += self.Value.to_binary()
        return b

class WriteRequest(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.RequestHeader = None
        self.NoOfNodesToWrite = None
        self.NodesToWrite = []

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.RequestHeader.to_binary()
        b += struct.pack('!i', self.NoOfNodesToWrite)
        b += struct.pack('!i', len(self.NodesToWrite)
        b += self.NodesToWrite.to_binary()
        return b

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

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.ResponseHeader.to_binary()
        b += struct.pack('!i', self.NoOfResults)
        b += struct.pack('!i', len(self.Results)
        b += self.Results.to_binary()
        b += struct.pack('!i', self.NoOfDiagnosticInfos)
        b += struct.pack('!i', len(self.DiagnosticInfos)
        b += self.DiagnosticInfos.to_binary()
        return b

class HistoryUpdateDetails(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.NodeId = None

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.NodeId.to_binary()
        return b

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

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.NodeId.to_binary()
        b += self.NodeId.to_binary()
        b += self.PerformInsertReplace.to_binary()
        b += struct.pack('!i', self.NoOfUpdateValues)
        b += struct.pack('!i', len(self.UpdateValues)
        b += self.UpdateValues.to_binary()
        return b

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

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.NodeId.to_binary()
        b += self.NodeId.to_binary()
        b += self.PerformInsertReplace.to_binary()
        b += struct.pack('!i', self.NoOfUpdateValues)
        b += struct.pack('!i', len(self.UpdateValues)
        b += self.UpdateValues.to_binary()
        return b

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

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.NodeId.to_binary()
        b += self.NodeId.to_binary()
        b += struct.pack('!?', self.IsDeleteModified)
        b += struct.pack('!d', self.StartTime)
        b += struct.pack('!d', self.EndTime)
        return b

class DeleteAtTimeDetails(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.NodeId = None
        self.NodeId = None
        self.NoOfReqTimes = None
        self.ReqTimes = []

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.NodeId.to_binary()
        b += self.NodeId.to_binary()
        b += struct.pack('!i', self.NoOfReqTimes)
        b += struct.pack('!i', len(self.ReqTimes)
        b += struct.pack('!d', self.ReqTimes)
        return b

class DeleteEventDetails(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.NodeId = None
        self.NodeId = None
        self.NoOfEventIds = None
        self.EventIds = []

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.NodeId.to_binary()
        b += self.NodeId.to_binary()
        b += struct.pack('!i', self.NoOfEventIds)
        b += struct.pack('!i', len(self.EventIds)
        b += struct.pack('!c', self.EventIds)
        return b

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

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.StatusCode.to_binary()
        b += struct.pack('!i', self.NoOfOperationResults)
        b += struct.pack('!i', len(self.OperationResults)
        b += self.OperationResults.to_binary()
        b += struct.pack('!i', self.NoOfDiagnosticInfos)
        b += struct.pack('!i', len(self.DiagnosticInfos)
        b += self.DiagnosticInfos.to_binary()
        return b

class HistoryUpdateRequest(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.RequestHeader = None
        self.NoOfHistoryUpdateDetails = None
        self.HistoryUpdateDetails = []

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.RequestHeader.to_binary()
        b += struct.pack('!i', self.NoOfHistoryUpdateDetails)
        b += struct.pack('!i', len(self.HistoryUpdateDetails)
        b += self.HistoryUpdateDetails.to_binary()
        return b

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

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.ResponseHeader.to_binary()
        b += struct.pack('!i', self.NoOfResults)
        b += struct.pack('!i', len(self.Results)
        b += self.Results.to_binary()
        b += struct.pack('!i', self.NoOfDiagnosticInfos)
        b += struct.pack('!i', len(self.DiagnosticInfos)
        b += self.DiagnosticInfos.to_binary()
        return b

class CallMethodRequest(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.ObjectId = None
        self.MethodId = None
        self.NoOfInputArguments = None
        self.InputArguments = []

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.ObjectId.to_binary()
        b += self.MethodId.to_binary()
        b += struct.pack('!i', self.NoOfInputArguments)
        b += struct.pack('!i', len(self.InputArguments)
        b += self.InputArguments.to_binary()
        return b

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

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.StatusCode.to_binary()
        b += struct.pack('!i', self.NoOfInputArgumentResults)
        b += struct.pack('!i', len(self.InputArgumentResults)
        b += self.InputArgumentResults.to_binary()
        b += struct.pack('!i', self.NoOfInputArgumentDiagnosticInfos)
        b += struct.pack('!i', len(self.InputArgumentDiagnosticInfos)
        b += self.InputArgumentDiagnosticInfos.to_binary()
        b += struct.pack('!i', self.NoOfOutputArguments)
        b += struct.pack('!i', len(self.OutputArguments)
        b += self.OutputArguments.to_binary()
        return b

class CallRequest(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.RequestHeader = None
        self.NoOfMethodsToCall = None
        self.MethodsToCall = []

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.RequestHeader.to_binary()
        b += struct.pack('!i', self.NoOfMethodsToCall)
        b += struct.pack('!i', len(self.MethodsToCall)
        b += self.MethodsToCall.to_binary()
        return b

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

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.ResponseHeader.to_binary()
        b += struct.pack('!i', self.NoOfResults)
        b += struct.pack('!i', len(self.Results)
        b += self.Results.to_binary()
        b += struct.pack('!i', self.NoOfDiagnosticInfos)
        b += struct.pack('!i', len(self.DiagnosticInfos)
        b += self.DiagnosticInfos.to_binary()
        return b

class MonitoringFilter(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        return b

class DataChangeFilter(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.Trigger = None
        self.DeadbandType = None
        self.DeadbandValue = None

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.Trigger.to_binary()
        b += struct.pack('!I', self.DeadbandType)
        b += struct.pack('!d', self.DeadbandValue)
        return b

class EventFilter(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.NoOfSelectClauses = None
        self.SelectClauses = []
        self.WhereClause = None

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += struct.pack('!i', self.NoOfSelectClauses)
        b += struct.pack('!i', len(self.SelectClauses)
        b += self.SelectClauses.to_binary()
        b += self.WhereClause.to_binary()
        return b

class ReadEventDetails(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.NumValuesPerNode = None
        self.StartTime = None
        self.EndTime = None
        self.Filter = None

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += struct.pack('!I', self.NumValuesPerNode)
        b += struct.pack('!d', self.StartTime)
        b += struct.pack('!d', self.EndTime)
        b += self.Filter.to_binary()
        return b

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

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += struct.pack('!?', self.UseServerCapabilitiesDefaults)
        b += struct.pack('!?', self.TreatUncertainAsBad)
        b += struct.pack('!c', self.PercentDataBad)
        b += struct.pack('!c', self.PercentDataGood)
        b += struct.pack('!?', self.UseSlopedExtrapolation)
        return b

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

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += struct.pack('!d', self.StartTime)
        b += struct.pack('!d', self.EndTime)
        b += struct.pack('!d', self.ProcessingInterval)
        b += struct.pack('!i', self.NoOfAggregateType)
        b += struct.pack('!i', len(self.AggregateType)
        b += self.AggregateType.to_binary()
        b += self.AggregateConfiguration.to_binary()
        return b

class AggregateFilter(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.StartTime = None
        self.AggregateType = None
        self.ProcessingInterval = None
        self.AggregateConfiguration = None

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += struct.pack('!d', self.StartTime)
        b += self.AggregateType.to_binary()
        b += struct.pack('!d', self.ProcessingInterval)
        b += self.AggregateConfiguration.to_binary()
        return b

class MonitoringFilterResult(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        return b

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

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += struct.pack('!i', self.NoOfSelectClauseResults)
        b += struct.pack('!i', len(self.SelectClauseResults)
        b += self.SelectClauseResults.to_binary()
        b += struct.pack('!i', self.NoOfSelectClauseDiagnosticInfos)
        b += struct.pack('!i', len(self.SelectClauseDiagnosticInfos)
        b += self.SelectClauseDiagnosticInfos.to_binary()
        b += self.WhereClauseResult.to_binary()
        return b

class HistoryUpdateEventResult(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.StatusCode = None
        self.EventFilterResult = None

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.StatusCode.to_binary()
        b += self.EventFilterResult.to_binary()
        return b

class AggregateFilterResult(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.RevisedStartTime = None
        self.RevisedProcessingInterval = None
        self.RevisedAggregateConfiguration = None

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += struct.pack('!d', self.RevisedStartTime)
        b += struct.pack('!d', self.RevisedProcessingInterval)
        b += self.RevisedAggregateConfiguration.to_binary()
        return b

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

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += struct.pack('!I', self.ClientHandle)
        b += struct.pack('!d', self.SamplingInterval)
        b += self.Filter.to_binary()
        b += struct.pack('!I', self.QueueSize)
        b += struct.pack('!?', self.DiscardOldest)
        return b

class MonitoredItemCreateRequest(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.ItemToMonitor = None
        self.MonitoringMode = None
        self.RequestedParameters = None

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.ItemToMonitor.to_binary()
        b += self.MonitoringMode.to_binary()
        b += self.RequestedParameters.to_binary()
        return b

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

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.StatusCode.to_binary()
        b += struct.pack('!I', self.MonitoredItemId)
        b += struct.pack('!d', self.RevisedSamplingInterval)
        b += struct.pack('!I', self.RevisedQueueSize)
        b += self.FilterResult.to_binary()
        return b

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

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.RequestHeader.to_binary()
        b += struct.pack('!I', self.SubscriptionId)
        b += self.TimestampsToReturn.to_binary()
        b += struct.pack('!i', self.NoOfItemsToCreate)
        b += struct.pack('!i', len(self.ItemsToCreate)
        b += self.ItemsToCreate.to_binary()
        return b

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

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.ResponseHeader.to_binary()
        b += struct.pack('!i', self.NoOfResults)
        b += struct.pack('!i', len(self.Results)
        b += self.Results.to_binary()
        b += struct.pack('!i', self.NoOfDiagnosticInfos)
        b += struct.pack('!i', len(self.DiagnosticInfos)
        b += self.DiagnosticInfos.to_binary()
        return b

class MonitoredItemModifyRequest(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.MonitoredItemId = None
        self.RequestedParameters = None

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += struct.pack('!I', self.MonitoredItemId)
        b += self.RequestedParameters.to_binary()
        return b

class MonitoredItemModifyResult(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.StatusCode = None
        self.RevisedSamplingInterval = None
        self.RevisedQueueSize = None
        self.FilterResult = None

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.StatusCode.to_binary()
        b += struct.pack('!d', self.RevisedSamplingInterval)
        b += struct.pack('!I', self.RevisedQueueSize)
        b += self.FilterResult.to_binary()
        return b

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

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.RequestHeader.to_binary()
        b += struct.pack('!I', self.SubscriptionId)
        b += self.TimestampsToReturn.to_binary()
        b += struct.pack('!i', self.NoOfItemsToModify)
        b += struct.pack('!i', len(self.ItemsToModify)
        b += self.ItemsToModify.to_binary()
        return b

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

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.ResponseHeader.to_binary()
        b += struct.pack('!i', self.NoOfResults)
        b += struct.pack('!i', len(self.Results)
        b += self.Results.to_binary()
        b += struct.pack('!i', self.NoOfDiagnosticInfos)
        b += struct.pack('!i', len(self.DiagnosticInfos)
        b += self.DiagnosticInfos.to_binary()
        return b

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

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.RequestHeader.to_binary()
        b += struct.pack('!I', self.SubscriptionId)
        b += self.MonitoringMode.to_binary()
        b += struct.pack('!i', self.NoOfMonitoredItemIds)
        b += struct.pack('!i', len(self.MonitoredItemIds)
        b += struct.pack('!I', self.MonitoredItemIds)
        return b

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

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.ResponseHeader.to_binary()
        b += struct.pack('!i', self.NoOfResults)
        b += struct.pack('!i', len(self.Results)
        b += self.Results.to_binary()
        b += struct.pack('!i', self.NoOfDiagnosticInfos)
        b += struct.pack('!i', len(self.DiagnosticInfos)
        b += self.DiagnosticInfos.to_binary()
        return b

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

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.RequestHeader.to_binary()
        b += struct.pack('!I', self.SubscriptionId)
        b += struct.pack('!I', self.TriggeringItemId)
        b += struct.pack('!i', self.NoOfLinksToAdd)
        b += struct.pack('!i', len(self.LinksToAdd)
        b += struct.pack('!I', self.LinksToAdd)
        b += struct.pack('!i', self.NoOfLinksToRemove)
        b += struct.pack('!i', len(self.LinksToRemove)
        b += struct.pack('!I', self.LinksToRemove)
        return b

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

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.ResponseHeader.to_binary()
        b += struct.pack('!i', self.NoOfAddResults)
        b += struct.pack('!i', len(self.AddResults)
        b += self.AddResults.to_binary()
        b += struct.pack('!i', self.NoOfAddDiagnosticInfos)
        b += struct.pack('!i', len(self.AddDiagnosticInfos)
        b += self.AddDiagnosticInfos.to_binary()
        b += struct.pack('!i', self.NoOfRemoveResults)
        b += struct.pack('!i', len(self.RemoveResults)
        b += self.RemoveResults.to_binary()
        b += struct.pack('!i', self.NoOfRemoveDiagnosticInfos)
        b += struct.pack('!i', len(self.RemoveDiagnosticInfos)
        b += self.RemoveDiagnosticInfos.to_binary()
        return b

class DeleteMonitoredItemsRequest(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.RequestHeader = None
        self.SubscriptionId = None
        self.NoOfMonitoredItemIds = None
        self.MonitoredItemIds = []

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.RequestHeader.to_binary()
        b += struct.pack('!I', self.SubscriptionId)
        b += struct.pack('!i', self.NoOfMonitoredItemIds)
        b += struct.pack('!i', len(self.MonitoredItemIds)
        b += struct.pack('!I', self.MonitoredItemIds)
        return b

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

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.ResponseHeader.to_binary()
        b += struct.pack('!i', self.NoOfResults)
        b += struct.pack('!i', len(self.Results)
        b += self.Results.to_binary()
        b += struct.pack('!i', self.NoOfDiagnosticInfos)
        b += struct.pack('!i', len(self.DiagnosticInfos)
        b += self.DiagnosticInfos.to_binary()
        return b

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

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.RequestHeader.to_binary()
        b += struct.pack('!d', self.RequestedPublishingInterval)
        b += struct.pack('!I', self.RequestedLifetimeCount)
        b += struct.pack('!I', self.RequestedMaxKeepAliveCount)
        b += struct.pack('!I', self.MaxNotificationsPerPublish)
        b += struct.pack('!?', self.PublishingEnabled)
        b += struct.pack('!c', self.Priority)
        return b

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

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.ResponseHeader.to_binary()
        b += struct.pack('!I', self.SubscriptionId)
        b += struct.pack('!d', self.RevisedPublishingInterval)
        b += struct.pack('!I', self.RevisedLifetimeCount)
        b += struct.pack('!I', self.RevisedMaxKeepAliveCount)
        return b

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

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.RequestHeader.to_binary()
        b += struct.pack('!I', self.SubscriptionId)
        b += struct.pack('!d', self.RequestedPublishingInterval)
        b += struct.pack('!I', self.RequestedLifetimeCount)
        b += struct.pack('!I', self.RequestedMaxKeepAliveCount)
        b += struct.pack('!I', self.MaxNotificationsPerPublish)
        b += struct.pack('!c', self.Priority)
        return b

class ModifySubscriptionResponse(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.ResponseHeader = None
        self.RevisedPublishingInterval = None
        self.RevisedLifetimeCount = None
        self.RevisedMaxKeepAliveCount = None

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.ResponseHeader.to_binary()
        b += struct.pack('!d', self.RevisedPublishingInterval)
        b += struct.pack('!I', self.RevisedLifetimeCount)
        b += struct.pack('!I', self.RevisedMaxKeepAliveCount)
        return b

class SetPublishingModeRequest(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.RequestHeader = None
        self.PublishingEnabled = None
        self.NoOfSubscriptionIds = None
        self.SubscriptionIds = []

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.RequestHeader.to_binary()
        b += struct.pack('!?', self.PublishingEnabled)
        b += struct.pack('!i', self.NoOfSubscriptionIds)
        b += struct.pack('!i', len(self.SubscriptionIds)
        b += struct.pack('!I', self.SubscriptionIds)
        return b

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

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.ResponseHeader.to_binary()
        b += struct.pack('!i', self.NoOfResults)
        b += struct.pack('!i', len(self.Results)
        b += self.Results.to_binary()
        b += struct.pack('!i', self.NoOfDiagnosticInfos)
        b += struct.pack('!i', len(self.DiagnosticInfos)
        b += self.DiagnosticInfos.to_binary()
        return b

class NotificationMessage(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.SequenceNumber = None
        self.PublishTime = None
        self.NoOfNotificationData = None
        self.NotificationData = []

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += struct.pack('!I', self.SequenceNumber)
        b += struct.pack('!d', self.PublishTime)
        b += struct.pack('!i', self.NoOfNotificationData)
        b += struct.pack('!i', len(self.NotificationData)
        b += self.NotificationData.to_binary()
        return b

class NotificationData(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        return b

class MonitoredItemNotification(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.ClientHandle = None
        self.Value = None

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += struct.pack('!I', self.ClientHandle)
        b += self.Value.to_binary()
        return b

class DataChangeNotification(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.NoOfMonitoredItems = None
        self.MonitoredItems = []
        self.NoOfDiagnosticInfos = None
        self.DiagnosticInfos = []

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += struct.pack('!i', self.NoOfMonitoredItems)
        b += struct.pack('!i', len(self.MonitoredItems)
        b += self.MonitoredItems.to_binary()
        b += struct.pack('!i', self.NoOfDiagnosticInfos)
        b += struct.pack('!i', len(self.DiagnosticInfos)
        b += self.DiagnosticInfos.to_binary()
        return b

class EventFieldList(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.ClientHandle = None
        self.NoOfEventFields = None
        self.EventFields = []

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += struct.pack('!I', self.ClientHandle)
        b += struct.pack('!i', self.NoOfEventFields)
        b += struct.pack('!i', len(self.EventFields)
        b += self.EventFields.to_binary()
        return b

class EventNotificationList(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.NoOfEvents = None
        self.Events = []

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += struct.pack('!i', self.NoOfEvents)
        b += struct.pack('!i', len(self.Events)
        b += self.Events.to_binary()
        return b

class HistoryEventFieldList(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.NoOfEventFields = None
        self.EventFields = []

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += struct.pack('!i', self.NoOfEventFields)
        b += struct.pack('!i', len(self.EventFields)
        b += self.EventFields.to_binary()
        return b

class HistoryEvent(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.NoOfEvents = None
        self.Events = []

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += struct.pack('!i', self.NoOfEvents)
        b += struct.pack('!i', len(self.Events)
        b += self.Events.to_binary()
        return b

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

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.NodeId.to_binary()
        b += self.NodeId.to_binary()
        b += self.PerformInsertReplace.to_binary()
        b += self.Filter.to_binary()
        b += struct.pack('!i', self.NoOfEventData)
        b += struct.pack('!i', len(self.EventData)
        b += self.EventData.to_binary()
        return b

class StatusChangeNotification(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.Status = None
        self.DiagnosticInfo = None

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.Status.to_binary()
        b += self.DiagnosticInfo.to_binary()
        return b

class SubscriptionAcknowledgement(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.SubscriptionId = None
        self.SequenceNumber = None

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += struct.pack('!I', self.SubscriptionId)
        b += struct.pack('!I', self.SequenceNumber)
        return b

class PublishRequest(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.RequestHeader = None
        self.NoOfSubscriptionAcknowledgements = None
        self.SubscriptionAcknowledgements = []

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.RequestHeader.to_binary()
        b += struct.pack('!i', self.NoOfSubscriptionAcknowledgements)
        b += struct.pack('!i', len(self.SubscriptionAcknowledgements)
        b += self.SubscriptionAcknowledgements.to_binary()
        return b

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

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.ResponseHeader.to_binary()
        b += struct.pack('!I', self.SubscriptionId)
        b += struct.pack('!i', self.NoOfAvailableSequenceNumbers)
        b += struct.pack('!i', len(self.AvailableSequenceNumbers)
        b += struct.pack('!I', self.AvailableSequenceNumbers)
        b += struct.pack('!?', self.MoreNotifications)
        b += self.NotificationMessage.to_binary()
        b += struct.pack('!i', self.NoOfResults)
        b += struct.pack('!i', len(self.Results)
        b += self.Results.to_binary()
        b += struct.pack('!i', self.NoOfDiagnosticInfos)
        b += struct.pack('!i', len(self.DiagnosticInfos)
        b += self.DiagnosticInfos.to_binary()
        return b

class RepublishRequest(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.RequestHeader = None
        self.SubscriptionId = None
        self.RetransmitSequenceNumber = None

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.RequestHeader.to_binary()
        b += struct.pack('!I', self.SubscriptionId)
        b += struct.pack('!I', self.RetransmitSequenceNumber)
        return b

class RepublishResponse(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.ResponseHeader = None
        self.NotificationMessage = None

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.ResponseHeader.to_binary()
        b += self.NotificationMessage.to_binary()
        return b

class TransferResult(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.StatusCode = None
        self.NoOfAvailableSequenceNumbers = None
        self.AvailableSequenceNumbers = []

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.StatusCode.to_binary()
        b += struct.pack('!i', self.NoOfAvailableSequenceNumbers)
        b += struct.pack('!i', len(self.AvailableSequenceNumbers)
        b += struct.pack('!I', self.AvailableSequenceNumbers)
        return b

class TransferSubscriptionsRequest(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.RequestHeader = None
        self.NoOfSubscriptionIds = None
        self.SubscriptionIds = []
        self.SendInitialValues = None

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.RequestHeader.to_binary()
        b += struct.pack('!i', self.NoOfSubscriptionIds)
        b += struct.pack('!i', len(self.SubscriptionIds)
        b += struct.pack('!I', self.SubscriptionIds)
        b += struct.pack('!?', self.SendInitialValues)
        return b

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

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.ResponseHeader.to_binary()
        b += struct.pack('!i', self.NoOfResults)
        b += struct.pack('!i', len(self.Results)
        b += self.Results.to_binary()
        b += struct.pack('!i', self.NoOfDiagnosticInfos)
        b += struct.pack('!i', len(self.DiagnosticInfos)
        b += self.DiagnosticInfos.to_binary()
        return b

class DeleteSubscriptionsRequest(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.RequestHeader = None
        self.NoOfSubscriptionIds = None
        self.SubscriptionIds = []

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.RequestHeader.to_binary()
        b += struct.pack('!i', self.NoOfSubscriptionIds)
        b += struct.pack('!i', len(self.SubscriptionIds)
        b += struct.pack('!I', self.SubscriptionIds)
        return b

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

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.ResponseHeader.to_binary()
        b += struct.pack('!i', self.NoOfResults)
        b += struct.pack('!i', len(self.Results)
        b += self.Results.to_binary()
        b += struct.pack('!i', self.NoOfDiagnosticInfos)
        b += struct.pack('!i', len(self.DiagnosticInfos)
        b += self.DiagnosticInfos.to_binary()
        return b

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

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += struct.pack('!?', self.Boolean)
        b += struct.pack('!B', self.SByte)
        b += struct.pack('!c', self.Byte)
        b += struct.pack('!h', self.Int16)
        b += struct.pack('!H', self.UInt16)
        b += struct.pack('!i', self.Int32)
        b += struct.pack('!I', self.UInt32)
        b += struct.pack('!q', self.Int64)
        b += struct.pack('!Q', self.UInt64)
        b += struct.pack('!f', self.Float)
        b += struct.pack('!d', self.Double)
        b += self.String.to_binary()
        b += struct.pack('!d', self.DateTime)
        b += struct.pack('!None', self.Guid)
        b += struct.pack('!c', self.ByteString)
        b += self.XmlElement.to_binary()
        b += self.NodeId.to_binary()
        b += self.ExpandedNodeId.to_binary()
        b += self.StatusCode.to_binary()
        b += self.DiagnosticInfo.to_binary()
        b += self.QualifiedName.to_binary()
        b += self.LocalizedText.to_binary()
        b += self.ExtensionObject.to_binary()
        b += self.DataValue.to_binary()
        b += self.EnumeratedValue.to_binary()
        return b

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

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += struct.pack('!i', self.NoOfBooleans)
        b += struct.pack('!i', len(self.Booleans)
        b += struct.pack('!?', self.Booleans)
        b += struct.pack('!i', self.NoOfSBytes)
        b += struct.pack('!i', len(self.SBytes)
        b += struct.pack('!B', self.SBytes)
        b += struct.pack('!i', self.NoOfInt16s)
        b += struct.pack('!i', len(self.Int16s)
        b += struct.pack('!h', self.Int16s)
        b += struct.pack('!i', self.NoOfUInt16s)
        b += struct.pack('!i', len(self.UInt16s)
        b += struct.pack('!H', self.UInt16s)
        b += struct.pack('!i', self.NoOfInt32s)
        b += struct.pack('!i', len(self.Int32s)
        b += struct.pack('!i', self.Int32s)
        b += struct.pack('!i', self.NoOfUInt32s)
        b += struct.pack('!i', len(self.UInt32s)
        b += struct.pack('!I', self.UInt32s)
        b += struct.pack('!i', self.NoOfInt64s)
        b += struct.pack('!i', len(self.Int64s)
        b += struct.pack('!q', self.Int64s)
        b += struct.pack('!i', self.NoOfUInt64s)
        b += struct.pack('!i', len(self.UInt64s)
        b += struct.pack('!Q', self.UInt64s)
        b += struct.pack('!i', self.NoOfFloats)
        b += struct.pack('!i', len(self.Floats)
        b += struct.pack('!f', self.Floats)
        b += struct.pack('!i', self.NoOfDoubles)
        b += struct.pack('!i', len(self.Doubles)
        b += struct.pack('!d', self.Doubles)
        b += struct.pack('!i', self.NoOfStrings)
        b += struct.pack('!i', len(self.Strings)
        b += self.Strings.to_binary()
        b += struct.pack('!i', self.NoOfDateTimes)
        b += struct.pack('!i', len(self.DateTimes)
        b += struct.pack('!d', self.DateTimes)
        b += struct.pack('!i', self.NoOfGuids)
        b += struct.pack('!i', len(self.Guids)
        b += struct.pack('!None', self.Guids)
        b += struct.pack('!i', self.NoOfByteStrings)
        b += struct.pack('!i', len(self.ByteStrings)
        b += struct.pack('!c', self.ByteStrings)
        b += struct.pack('!i', self.NoOfXmlElements)
        b += struct.pack('!i', len(self.XmlElements)
        b += self.XmlElements.to_binary()
        b += struct.pack('!i', self.NoOfNodeIds)
        b += struct.pack('!i', len(self.NodeIds)
        b += self.NodeIds.to_binary()
        b += struct.pack('!i', self.NoOfExpandedNodeIds)
        b += struct.pack('!i', len(self.ExpandedNodeIds)
        b += self.ExpandedNodeIds.to_binary()
        b += struct.pack('!i', self.NoOfStatusCodes)
        b += struct.pack('!i', len(self.StatusCodes)
        b += self.StatusCodes.to_binary()
        b += struct.pack('!i', self.NoOfDiagnosticInfos)
        b += struct.pack('!i', len(self.DiagnosticInfos)
        b += self.DiagnosticInfos.to_binary()
        b += struct.pack('!i', self.NoOfQualifiedNames)
        b += struct.pack('!i', len(self.QualifiedNames)
        b += self.QualifiedNames.to_binary()
        b += struct.pack('!i', self.NoOfLocalizedTexts)
        b += struct.pack('!i', len(self.LocalizedTexts)
        b += self.LocalizedTexts.to_binary()
        b += struct.pack('!i', self.NoOfExtensionObjects)
        b += struct.pack('!i', len(self.ExtensionObjects)
        b += self.ExtensionObjects.to_binary()
        b += struct.pack('!i', self.NoOfDataValues)
        b += struct.pack('!i', len(self.DataValues)
        b += self.DataValues.to_binary()
        b += struct.pack('!i', self.NoOfVariants)
        b += struct.pack('!i', len(self.Variants)
        b += self.Variants.to_binary()
        b += struct.pack('!i', self.NoOfEnumeratedValues)
        b += struct.pack('!i', len(self.EnumeratedValues)
        b += self.EnumeratedValues.to_binary()
        return b

class CompositeTestType(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.Field1 = None
        self.Field2 = None

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.Field1.to_binary()
        b += self.Field2.to_binary()
        return b

class TestStackRequest(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.RequestHeader = None
        self.TestId = None
        self.Iteration = None
        self.Input = None

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.RequestHeader.to_binary()
        b += struct.pack('!I', self.TestId)
        b += struct.pack('!i', self.Iteration)
        b += self.Input.to_binary()
        return b

class TestStackResponse(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.ResponseHeader = None
        self.Output = None

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.ResponseHeader.to_binary()
        b += self.Output.to_binary()
        return b

class TestStackExRequest(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.RequestHeader = None
        self.TestId = None
        self.Iteration = None
        self.Input = None

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.RequestHeader.to_binary()
        b += struct.pack('!I', self.TestId)
        b += struct.pack('!i', self.Iteration)
        b += self.Input.to_binary()
        return b

class TestStackExResponse(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.ResponseHeader = None
        self.Output = None

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.ResponseHeader.to_binary()
        b += self.Output.to_binary()
        return b

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

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.ProductUri.to_binary()
        b += self.ManufacturerName.to_binary()
        b += self.ProductName.to_binary()
        b += self.SoftwareVersion.to_binary()
        b += self.BuildNumber.to_binary()
        b += struct.pack('!d', self.BuildDate)
        return b

class RedundantServerDataType(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.ServerId = None
        self.ServiceLevel = None
        self.ServerState = None

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.ServerId.to_binary()
        b += struct.pack('!c', self.ServiceLevel)
        b += self.ServerState.to_binary()
        return b

class EndpointUrlListDataType(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.NoOfEndpointUrlList = None
        self.EndpointUrlList = []

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += struct.pack('!i', self.NoOfEndpointUrlList)
        b += struct.pack('!i', len(self.EndpointUrlList)
        b += self.EndpointUrlList.to_binary()
        return b

class NetworkGroupDataType(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.ServerUri = None
        self.NoOfNetworkPaths = None
        self.NetworkPaths = []

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.ServerUri.to_binary()
        b += struct.pack('!i', self.NoOfNetworkPaths)
        b += struct.pack('!i', len(self.NetworkPaths)
        b += self.NetworkPaths.to_binary()
        return b

class SamplingIntervalDiagnosticsDataType(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.SamplingInterval = None
        self.MonitoredItemCount = None
        self.MaxMonitoredItemCount = None
        self.DisabledMonitoredItemCount = None

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += struct.pack('!d', self.SamplingInterval)
        b += struct.pack('!I', self.MonitoredItemCount)
        b += struct.pack('!I', self.MaxMonitoredItemCount)
        b += struct.pack('!I', self.DisabledMonitoredItemCount)
        return b

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

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += struct.pack('!I', self.ServerViewCount)
        b += struct.pack('!I', self.CurrentSessionCount)
        b += struct.pack('!I', self.CumulatedSessionCount)
        b += struct.pack('!I', self.SecurityRejectedSessionCount)
        b += struct.pack('!I', self.RejectedSessionCount)
        b += struct.pack('!I', self.SessionTimeoutCount)
        b += struct.pack('!I', self.SessionAbortCount)
        b += struct.pack('!I', self.CurrentSubscriptionCount)
        b += struct.pack('!I', self.CumulatedSubscriptionCount)
        b += struct.pack('!I', self.PublishingIntervalCount)
        b += struct.pack('!I', self.SecurityRejectedRequestsCount)
        b += struct.pack('!I', self.RejectedRequestsCount)
        return b

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

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += struct.pack('!d', self.StartTime)
        b += struct.pack('!d', self.CurrentTime)
        b += self.State.to_binary()
        b += self.BuildInfo.to_binary()
        b += struct.pack('!I', self.SecondsTillShutdown)
        b += self.ShutdownReason.to_binary()
        return b

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

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.SessionId.to_binary()
        b += self.ClientUserIdOfSession.to_binary()
        b += struct.pack('!i', self.NoOfClientUserIdHistory)
        b += struct.pack('!i', len(self.ClientUserIdHistory)
        b += self.ClientUserIdHistory.to_binary()
        b += self.AuthenticationMechanism.to_binary()
        b += self.Encoding.to_binary()
        b += self.TransportProtocol.to_binary()
        b += self.SecurityMode.to_binary()
        b += self.SecurityPolicyUri.to_binary()
        b += struct.pack('!c', self.ClientCertificate)
        return b

class ServiceCounterDataType(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.TotalCount = None
        self.ErrorCount = None

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += struct.pack('!I', self.TotalCount)
        b += struct.pack('!I', self.ErrorCount)
        return b

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

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.SessionId.to_binary()
        b += self.SessionName.to_binary()
        b += self.ClientDescription.to_binary()
        b += self.ServerUri.to_binary()
        b += self.EndpointUrl.to_binary()
        b += struct.pack('!i', self.NoOfLocaleIds)
        b += struct.pack('!i', len(self.LocaleIds)
        b += self.LocaleIds.to_binary()
        b += struct.pack('!d', self.ActualSessionTimeout)
        b += struct.pack('!I', self.MaxResponseMessageSize)
        b += struct.pack('!d', self.ClientConnectionTime)
        b += struct.pack('!d', self.ClientLastContactTime)
        b += struct.pack('!I', self.CurrentSubscriptionsCount)
        b += struct.pack('!I', self.CurrentMonitoredItemsCount)
        b += struct.pack('!I', self.CurrentPublishRequestsInQueue)
        b += self.TotalRequestCount.to_binary()
        b += struct.pack('!I', self.UnauthorizedRequestCount)
        b += self.ReadCount.to_binary()
        b += self.HistoryReadCount.to_binary()
        b += self.WriteCount.to_binary()
        b += self.HistoryUpdateCount.to_binary()
        b += self.CallCount.to_binary()
        b += self.CreateMonitoredItemsCount.to_binary()
        b += self.ModifyMonitoredItemsCount.to_binary()
        b += self.SetMonitoringModeCount.to_binary()
        b += self.SetTriggeringCount.to_binary()
        b += self.DeleteMonitoredItemsCount.to_binary()
        b += self.CreateSubscriptionCount.to_binary()
        b += self.ModifySubscriptionCount.to_binary()
        b += self.SetPublishingModeCount.to_binary()
        b += self.PublishCount.to_binary()
        b += self.RepublishCount.to_binary()
        b += self.TransferSubscriptionsCount.to_binary()
        b += self.DeleteSubscriptionsCount.to_binary()
        b += self.AddNodesCount.to_binary()
        b += self.AddReferencesCount.to_binary()
        b += self.DeleteNodesCount.to_binary()
        b += self.DeleteReferencesCount.to_binary()
        b += self.BrowseCount.to_binary()
        b += self.BrowseNextCount.to_binary()
        b += self.TranslateBrowsePathsToNodeIdsCount.to_binary()
        b += self.QueryFirstCount.to_binary()
        b += self.QueryNextCount.to_binary()
        b += self.RegisterNodesCount.to_binary()
        b += self.UnregisterNodesCount.to_binary()
        return b

class StatusResult(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.StatusCode = None
        self.DiagnosticInfo = None

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.StatusCode.to_binary()
        b += self.DiagnosticInfo.to_binary()
        return b

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

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.SessionId.to_binary()
        b += struct.pack('!I', self.SubscriptionId)
        b += struct.pack('!c', self.Priority)
        b += struct.pack('!d', self.PublishingInterval)
        b += struct.pack('!I', self.MaxKeepAliveCount)
        b += struct.pack('!I', self.MaxLifetimeCount)
        b += struct.pack('!I', self.MaxNotificationsPerPublish)
        b += struct.pack('!?', self.PublishingEnabled)
        b += struct.pack('!I', self.ModifyCount)
        b += struct.pack('!I', self.EnableCount)
        b += struct.pack('!I', self.DisableCount)
        b += struct.pack('!I', self.RepublishRequestCount)
        b += struct.pack('!I', self.RepublishMessageRequestCount)
        b += struct.pack('!I', self.RepublishMessageCount)
        b += struct.pack('!I', self.TransferRequestCount)
        b += struct.pack('!I', self.TransferredToAltClientCount)
        b += struct.pack('!I', self.TransferredToSameClientCount)
        b += struct.pack('!I', self.PublishRequestCount)
        b += struct.pack('!I', self.DataChangeNotificationsCount)
        b += struct.pack('!I', self.EventNotificationsCount)
        b += struct.pack('!I', self.NotificationsCount)
        b += struct.pack('!I', self.LatePublishRequestCount)
        b += struct.pack('!I', self.CurrentKeepAliveCount)
        b += struct.pack('!I', self.CurrentLifetimeCount)
        b += struct.pack('!I', self.UnacknowledgedMessageCount)
        b += struct.pack('!I', self.DiscardedMessageCount)
        b += struct.pack('!I', self.MonitoredItemCount)
        b += struct.pack('!I', self.DisabledMonitoredItemCount)
        b += struct.pack('!I', self.MonitoringQueueOverflowCount)
        b += struct.pack('!I', self.NextSequenceNumber)
        b += struct.pack('!I', self.EventQueueOverFlowCount)
        return b

class ModelChangeStructureDataType(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.Affected = None
        self.AffectedType = None
        self.Verb = None

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.Affected.to_binary()
        b += self.AffectedType.to_binary()
        b += struct.pack('!c', self.Verb)
        return b

class SemanticChangeStructureDataType(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.Affected = None
        self.AffectedType = None

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.Affected.to_binary()
        b += self.AffectedType.to_binary()
        return b

class Range(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.Low = None
        self.High = None

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += struct.pack('!d', self.Low)
        b += struct.pack('!d', self.High)
        return b

class EUInformation(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.NamespaceUri = None
        self.UnitId = None
        self.DisplayName = None
        self.Description = None

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.NamespaceUri.to_binary()
        b += struct.pack('!i', self.UnitId)
        b += self.DisplayName.to_binary()
        b += self.Description.to_binary()
        return b

class ComplexNumberType(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.Real = None
        self.Imaginary = None

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += struct.pack('!f', self.Real)
        b += struct.pack('!f', self.Imaginary)
        return b

class DoubleComplexNumberType(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.Real = None
        self.Imaginary = None

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += struct.pack('!d', self.Real)
        b += struct.pack('!d', self.Imaginary)
        return b

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

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.EngineeringUnits.to_binary()
        b += self.EURange.to_binary()
        b += self.Title.to_binary()
        b += self.AxisScaleType.to_binary()
        b += struct.pack('!i', self.NoOfAxisSteps)
        b += struct.pack('!i', len(self.AxisSteps)
        b += struct.pack('!d', self.AxisSteps)
        return b

class XVType(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.X = None
        self.Value = None

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += struct.pack('!d', self.X)
        b += struct.pack('!f', self.Value)
        return b

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

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.CreateSessionId.to_binary()
        b += self.CreateClientName.to_binary()
        b += struct.pack('!d', self.InvocationCreationTime)
        b += struct.pack('!d', self.LastTransitionTime)
        b += self.LastMethodCall.to_binary()
        b += self.LastMethodSessionId.to_binary()
        b += struct.pack('!i', self.NoOfLastMethodInputArguments)
        b += struct.pack('!i', len(self.LastMethodInputArguments)
        b += self.LastMethodInputArguments.to_binary()
        b += struct.pack('!i', self.NoOfLastMethodOutputArguments)
        b += struct.pack('!i', len(self.LastMethodOutputArguments)
        b += self.LastMethodOutputArguments.to_binary()
        b += struct.pack('!d', self.LastMethodCallTime)
        b += self.LastMethodReturnStatus.to_binary()
        return b

class Annotation(object):
    def __init__(self):
        self.Encoding = None
        self.TypeId = None
        self.BodyLength = None
        self.Message = None
        self.UserName = None
        self.AnnotationTime = None

    @property
    def XmlBody(self):
        return self.Encoding & (1 << 2)

    @XmlBody.setter
    def XmlBody(self, value):
        return self.Encoding | (value << 2)

    @property
    def Reserved1(self):
        return self.Encoding & (1 << 7)

    @Reserved1.setter
    def Reserved1(self, value):
        return self.Encoding | (value << 7)

    @property
    def BinaryBody(self):
        return self.Encoding & (1 << 1)

    @BinaryBody.setter
    def BinaryBody(self, value):
        return self.Encoding | (value << 1)

    @property
    def TypeIdSpecified(self):
        return self.Encoding & (1 << 0)

    @TypeIdSpecified.setter
    def TypeIdSpecified(self, value):
        return self.Encoding | (value << 0)

    def to_binary(self):
        b = bytes()
        b += struct.pack('!B', self.Encoding)
        b += struct.pack('!i', self.BodyLength)
        b += self.Message.to_binary()
        b += self.UserName.to_binary()
        b += struct.pack('!d', self.AnnotationTime)
        return b
