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
            self.None_ = 1
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
            self.None_ = 0
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
            self.None_ = 0
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
            self.None_ = 0
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
            self.None_ = 0
            self.Absolute = 1
            self.Percent = 2

class EnumeratedTestType(object):
    def __init__(self):
            self.Red = 1
            self.Yellow = 4
            self.Green = 5

class RedundancySupport(object):
    def __init__(self):
            self.None_ = 0
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
        self._Length_fmt = '!i'
        self._Length_fmt_size = 4
        self.Value = []
        self._Value_fmt = '!c'
        self._Value_fmt_size = 1
    
    def to_binary(self):
        packet = []
        tmp = packet
        tmp.append(struct.pack(self._Length_fmt, self.Length))
        tmp.append(struct.pack('!i', len(self.Value)))
        for i in Value:
            tmp.append(struct.pack(self._Value_fmt, self.Value))
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Length = struct.unpack(self._Length_fmt, data.read(self._Length_fmt_size))
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    self.Value = struct.unpack(self._Value_fmt, data.read(self._Value_fmt_size))
            return data
            
class TwoByteNodeId(object):
    def __init__(self):
        self.Identifier = None
        self._Identifier_fmt = '!c'
        self._Identifier_fmt_size = 1
    
    def to_binary(self):
        packet = []
        tmp = packet
        tmp.append(struct.pack(self._Identifier_fmt, self.Identifier))
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Identifier = struct.unpack(self._Identifier_fmt, data.read(self._Identifier_fmt_size))
            return data
            
class FourByteNodeId(object):
    def __init__(self):
        self.NamespaceIndex = None
        self._NamespaceIndex_fmt = '!c'
        self._NamespaceIndex_fmt_size = 1
        self.Identifier = None
        self._Identifier_fmt = '!H'
        self._Identifier_fmt_size = 2
    
    def to_binary(self):
        packet = []
        tmp = packet
        tmp.append(struct.pack(self._NamespaceIndex_fmt, self.NamespaceIndex))
        tmp.append(struct.pack(self._Identifier_fmt, self.Identifier))
        return b''.join(packet)
        
        def from_binary(self, data):
            self.NamespaceIndex = struct.unpack(self._NamespaceIndex_fmt, data.read(self._NamespaceIndex_fmt_size))
            self.Identifier = struct.unpack(self._Identifier_fmt, data.read(self._Identifier_fmt_size))
            return data
            
class NumericNodeId(object):
    def __init__(self):
        self.NamespaceIndex = None
        self._NamespaceIndex_fmt = '!H'
        self._NamespaceIndex_fmt_size = 2
        self.Identifier = None
        self._Identifier_fmt = '!I'
        self._Identifier_fmt_size = 4
    
    def to_binary(self):
        packet = []
        tmp = packet
        tmp.append(struct.pack(self._NamespaceIndex_fmt, self.NamespaceIndex))
        tmp.append(struct.pack(self._Identifier_fmt, self.Identifier))
        return b''.join(packet)
        
        def from_binary(self, data):
            self.NamespaceIndex = struct.unpack(self._NamespaceIndex_fmt, data.read(self._NamespaceIndex_fmt_size))
            self.Identifier = struct.unpack(self._Identifier_fmt, data.read(self._Identifier_fmt_size))
            return data
            
class StringNodeId(object):
    def __init__(self):
        self.NamespaceIndex = None
        self._NamespaceIndex_fmt = '!H'
        self._NamespaceIndex_fmt_size = 2
        self.Identifier = None
        self._Identifier_fmt = '!s'
        self._Identifier_fmt_size = 1
    
    def to_binary(self):
        packet = []
        tmp = packet
        tmp.append(struct.pack(self._NamespaceIndex_fmt, self.NamespaceIndex))
        tmp.append(struct.pack(self._Identifier_fmt, self.Identifier))
        return b''.join(packet)
        
        def from_binary(self, data):
            self.NamespaceIndex = struct.unpack(self._NamespaceIndex_fmt, data.read(self._NamespaceIndex_fmt_size))
            self.Identifier = struct.unpack(self._Identifier_fmt, data.read(self._Identifier_fmt_size))
            return data
            
class GuidNodeId(object):
    def __init__(self):
        self.NamespaceIndex = None
        self._NamespaceIndex_fmt = '!H'
        self._NamespaceIndex_fmt_size = 2
        self.Identifier = None
    
    def to_binary(self):
        packet = []
        tmp = packet
        tmp.append(struct.pack(self._NamespaceIndex_fmt, self.NamespaceIndex))
        tmp.append(self.Identifier.to_binary())
        return b''.join(packet)
        
        def from_binary(self, data):
            self.NamespaceIndex = struct.unpack(self._NamespaceIndex_fmt, data.read(self._NamespaceIndex_fmt_size))
            data = self.Identifier.from_binary(data)
            return data
            
class ByteStringNodeId(object):
    def __init__(self):
        self.NamespaceIndex = None
        self._NamespaceIndex_fmt = '!H'
        self._NamespaceIndex_fmt_size = 2
        self.Identifier = None
    
    def to_binary(self):
        packet = []
        tmp = packet
        tmp.append(struct.pack(self._NamespaceIndex_fmt, self.NamespaceIndex))
        tmp.append(self.Identifier.to_binary())
        return b''.join(packet)
        
        def from_binary(self, data):
            self.NamespaceIndex = struct.unpack(self._NamespaceIndex_fmt, data.read(self._NamespaceIndex_fmt_size))
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
        packet = []
        tmp = packet
        others = self.NodeIdType & 0b00111111
        if self.TwoByte: self.NodeIdType = ( 0 | others )
        others = self.NodeIdType & 0b00111111
        if self.FourByte: self.NodeIdType = ( 1 | others )
        others = self.NodeIdType & 0b00111111
        if self.Numeric: self.NodeIdType = ( 2 | others )
        others = self.NodeIdType & 0b00111111
        if self.String: self.NodeIdType = ( 3 | others )
        others = self.NodeIdType & 0b00111111
        if self.Guid: self.NodeIdType = ( 4 | others )
        others = self.NodeIdType & 0b00111111
        if self.ByteString: self.NodeIdType = ( 5 | others )
        tmp.append(self.NodeIdType.to_binary())
        if self.TwoByte: 
            tmp.append(self.TwoByte.to_binary())
        if self.FourByte: 
            tmp.append(self.FourByte.to_binary())
        if self.Numeric: 
            tmp.append(self.Numeric.to_binary())
        if self.String: 
            tmp.append(self.String.to_binary())
        if self.Guid: 
            tmp.append(self.Guid.to_binary())
        if self.ByteString: 
            tmp.append(self.ByteString.to_binary())
        return b''.join(packet)
        
        def from_binary(self, data):
            data = self.NodeIdType.from_binary(data)
            val = self.NodeIdType & 0b00111111
            if val == 0:
                data = self.TwoByte.from_binary(data)
            val = self.NodeIdType & 0b00111111
            if val == 0:
                data = self.FourByte.from_binary(data)
            val = self.NodeIdType & 0b00111111
            if val == 0:
                data = self.Numeric.from_binary(data)
            val = self.NodeIdType & 0b00111111
            if val == 0:
                data = self.String.from_binary(data)
            val = self.NodeIdType & 0b00111111
            if val == 0:
                data = self.Guid.from_binary(data)
            val = self.NodeIdType & 0b00111111
            if val == 0:
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
        self._NamespaceURI_fmt = '!s'
        self._NamespaceURI_fmt_size = 1
        self.ServerIndex = None
        self._ServerIndex_fmt = '!I'
        self._ServerIndex_fmt_size = 4
    
    def to_binary(self):
        packet = []
        tmp = packet
        others = self.NodeIdType & 0b00111111
        if self.TwoByte: self.NodeIdType = ( 0 | others )
        others = self.NodeIdType & 0b00111111
        if self.FourByte: self.NodeIdType = ( 1 | others )
        others = self.NodeIdType & 0b00111111
        if self.Numeric: self.NodeIdType = ( 2 | others )
        others = self.NodeIdType & 0b00111111
        if self.String: self.NodeIdType = ( 3 | others )
        others = self.NodeIdType & 0b00111111
        if self.Guid: self.NodeIdType = ( 4 | others )
        others = self.NodeIdType & 0b00111111
        if self.ByteString: self.NodeIdType = ( 5 | others )
        if self.NamespaceURI: self.NodeIdType |= (value << 7)
        if self.ServerIndex: self.NodeIdType |= (value << 6)
        tmp.append(self.NodeIdType.to_binary())
        if self.TwoByte: 
            tmp.append(self.TwoByte.to_binary())
        if self.FourByte: 
            tmp.append(self.FourByte.to_binary())
        if self.Numeric: 
            tmp.append(self.Numeric.to_binary())
        if self.String: 
            tmp.append(self.String.to_binary())
        if self.Guid: 
            tmp.append(self.Guid.to_binary())
        if self.ByteString: 
            tmp.append(self.ByteString.to_binary())
        if self.NamespaceURI: 
            tmp.append(struct.pack(self._NamespaceURI_fmt, self.NamespaceURI))
        if self.ServerIndex: 
            tmp.append(struct.pack(self._ServerIndex_fmt, self.ServerIndex))
        return b''.join(packet)
        
        def from_binary(self, data):
            data = self.NodeIdType.from_binary(data)
            val = self.NodeIdType & 0b00111111
            if val == 0:
                data = self.TwoByte.from_binary(data)
            val = self.NodeIdType & 0b00111111
            if val == 0:
                data = self.FourByte.from_binary(data)
            val = self.NodeIdType & 0b00111111
            if val == 0:
                data = self.Numeric.from_binary(data)
            val = self.NodeIdType & 0b00111111
            if val == 0:
                data = self.String.from_binary(data)
            val = self.NodeIdType & 0b00111111
            if val == 0:
                data = self.Guid.from_binary(data)
            val = self.NodeIdType & 0b00111111
            if val == 0:
                data = self.ByteString.from_binary(data)
            if self.NodeIdType & (1 << 7):
                self.NamespaceURI = struct.unpack(self._NamespaceURI_fmt, data.read(self._NamespaceURI_fmt_size))
            if self.NodeIdType & (1 << 6):
                self.ServerIndex = struct.unpack(self._ServerIndex_fmt, data.read(self._ServerIndex_fmt_size))
            return data
            
class DiagnosticInfo(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.SymbolicId = None
        self._SymbolicId_fmt = '!i'
        self._SymbolicId_fmt_size = 4
        self.NamespaceURI = None
        self._NamespaceURI_fmt = '!i'
        self._NamespaceURI_fmt_size = 4
        self.LocalizedText = None
        self._LocalizedText_fmt = '!i'
        self._LocalizedText_fmt_size = 4
        self.AdditionalInfo = None
        self._AdditionalInfo_fmt = '!s'
        self._AdditionalInfo_fmt_size = 1
        self.InnerStatusCode = None
        self.InnerDiagnosticInfo = None
    
    def to_binary(self):
        packet = []
        tmp = packet
        if self.SymbolicId: self.Encoding |= (value << 0)
        if self.NamespaceURI: self.Encoding |= (value << 1)
        if self.LocalizedText: self.Encoding |= (value << 2)
        if self.AdditionalInfo: self.Encoding |= (value << 4)
        if self.InnerStatusCode: self.Encoding |= (value << 5)
        if self.InnerDiagnosticInfo: self.Encoding |= (value << 6)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.SymbolicId: 
            tmp.append(struct.pack(self._SymbolicId_fmt, self.SymbolicId))
        if self.NamespaceURI: 
            tmp.append(struct.pack(self._NamespaceURI_fmt, self.NamespaceURI))
        if self.LocalizedText: 
            tmp.append(struct.pack(self._LocalizedText_fmt, self.LocalizedText))
        if self.AdditionalInfo: 
            tmp.append(struct.pack(self._AdditionalInfo_fmt, self.AdditionalInfo))
        if self.InnerStatusCode: 
            tmp.append(self.InnerStatusCode.to_binary())
        if self.InnerDiagnosticInfo: 
            tmp.append(self.InnerDiagnosticInfo.to_binary())
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                self.SymbolicId = struct.unpack(self._SymbolicId_fmt, data.read(self._SymbolicId_fmt_size))
            if self.Encoding & (1 << 1):
                self.NamespaceURI = struct.unpack(self._NamespaceURI_fmt, data.read(self._NamespaceURI_fmt_size))
            if self.Encoding & (1 << 2):
                self.LocalizedText = struct.unpack(self._LocalizedText_fmt, data.read(self._LocalizedText_fmt_size))
            if self.Encoding & (1 << 4):
                self.AdditionalInfo = struct.unpack(self._AdditionalInfo_fmt, data.read(self._AdditionalInfo_fmt_size))
            if self.Encoding & (1 << 5):
                data = self.InnerStatusCode.from_binary(data)
            if self.Encoding & (1 << 6):
                data = self.InnerDiagnosticInfo.from_binary(data)
            return data
            
class QualifiedName(object):
    def __init__(self):
        self.NamespaceIndex = None
        self._NamespaceIndex_fmt = '!i'
        self._NamespaceIndex_fmt_size = 4
        self.Name = None
        self._Name_fmt = '!s'
        self._Name_fmt_size = 1
    
    def to_binary(self):
        packet = []
        tmp = packet
        tmp.append(struct.pack(self._NamespaceIndex_fmt, self.NamespaceIndex))
        tmp.append(struct.pack(self._Name_fmt, self.Name))
        return b''.join(packet)
        
        def from_binary(self, data):
            self.NamespaceIndex = struct.unpack(self._NamespaceIndex_fmt, data.read(self._NamespaceIndex_fmt_size))
            self.Name = struct.unpack(self._Name_fmt, data.read(self._Name_fmt_size))
            return data
            
class LocalizedText(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.Locale = None
        self._Locale_fmt = '!s'
        self._Locale_fmt_size = 1
        self.Text = None
        self._Text_fmt = '!s'
        self._Text_fmt_size = 1
    
    def to_binary(self):
        packet = []
        tmp = packet
        if self.Locale: self.Encoding |= (value << 0)
        if self.Text: self.Encoding |= (value << 1)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.Locale: 
            tmp.append(struct.pack(self._Locale_fmt, self.Locale))
        if self.Text: 
            tmp.append(struct.pack(self._Text_fmt, self.Text))
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                self.Locale = struct.unpack(self._Locale_fmt, data.read(self._Locale_fmt_size))
            if self.Encoding & (1 << 1):
                self.Text = struct.unpack(self._Text_fmt, data.read(self._Text_fmt_size))
            return data
            
class ExtensionObject(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
    
    def to_binary(self):
        packet = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
        tmp.append(struct.pack('!i', len(self.Body)))
        for i in Body:
            tmp.append(struct.pack(self._Body_fmt, self.Body))
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    self.Body = struct.unpack(self._Body_fmt, data.read(self._Body_fmt_size))
            return data
            
class Variant(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.ArrayLength = None
        self._ArrayLength_fmt = '!i'
        self._ArrayLength_fmt_size = 4
        self.Boolean = []
        self._Boolean_fmt = '!?'
        self._Boolean_fmt_size = 1
        self.SByte = []
        self._SByte_fmt = '!B'
        self._SByte_fmt_size = 1
        self.Byte = []
        self._Byte_fmt = '!c'
        self._Byte_fmt_size = 1
        self.Int16 = []
        self._Int16_fmt = '!h'
        self._Int16_fmt_size = 2
        self.UInt16 = []
        self._UInt16_fmt = '!H'
        self._UInt16_fmt_size = 2
        self.Int32 = []
        self._Int32_fmt = '!i'
        self._Int32_fmt_size = 4
        self.UInt32 = []
        self._UInt32_fmt = '!I'
        self._UInt32_fmt_size = 4
        self.Int64 = []
        self._Int64_fmt = '!q'
        self._Int64_fmt_size = 8
        self.UInt64 = []
        self._UInt64_fmt = '!Q'
        self._UInt64_fmt_size = 8
        self.Float = []
        self._Float_fmt = '!f'
        self._Float_fmt_size = 4
        self.Double = []
        self._Double_fmt = '!d'
        self._Double_fmt_size = 8
        self.String = []
        self.DateTime = []
        self._DateTime_fmt = '!d'
        self._DateTime_fmt_size = 8
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
        packet = []
        tmp = packet
        if self.ArrayLength: self.Encoding |= (value << 7)
        others = self.Encoding & 0b01111111
        if self.Boolean: self.Encoding = ( 1 | others )
        others = self.Encoding & 0b01111111
        if self.SByte: self.Encoding = ( 2 | others )
        others = self.Encoding & 0b01111111
        if self.Byte: self.Encoding = ( 3 | others )
        others = self.Encoding & 0b01111111
        if self.Int16: self.Encoding = ( 4 | others )
        others = self.Encoding & 0b01111111
        if self.UInt16: self.Encoding = ( 5 | others )
        others = self.Encoding & 0b01111111
        if self.Int32: self.Encoding = ( 6 | others )
        others = self.Encoding & 0b01111111
        if self.UInt32: self.Encoding = ( 7 | others )
        others = self.Encoding & 0b01111111
        if self.Int64: self.Encoding = ( 8 | others )
        others = self.Encoding & 0b01111111
        if self.UInt64: self.Encoding = ( 9 | others )
        others = self.Encoding & 0b01111111
        if self.Float: self.Encoding = ( 10 | others )
        others = self.Encoding & 0b01111111
        if self.Double: self.Encoding = ( 11 | others )
        others = self.Encoding & 0b01111111
        if self.String: self.Encoding = ( 12 | others )
        others = self.Encoding & 0b01111111
        if self.DateTime: self.Encoding = ( 13 | others )
        others = self.Encoding & 0b01111111
        if self.Guid: self.Encoding = ( 14 | others )
        others = self.Encoding & 0b01111111
        if self.ByteString: self.Encoding = ( 15 | others )
        others = self.Encoding & 0b01111111
        if self.XmlElement: self.Encoding = ( 16 | others )
        others = self.Encoding & 0b01111111
        if self.NodeId: self.Encoding = ( 17 | others )
        others = self.Encoding & 0b01111111
        if self.ExpandedNodeId: self.Encoding = ( 18 | others )
        others = self.Encoding & 0b01111111
        if self.StatusCode: self.Encoding = ( 19 | others )
        others = self.Encoding & 0b01111111
        if self.DiagnosticInfo: self.Encoding = ( 20 | others )
        others = self.Encoding & 0b01111111
        if self.QualifiedName: self.Encoding = ( 21 | others )
        others = self.Encoding & 0b01111111
        if self.LocalizedText: self.Encoding = ( 22 | others )
        others = self.Encoding & 0b01111111
        if self.ExtensionObject: self.Encoding = ( 23 | others )
        others = self.Encoding & 0b01111111
        if self.DataValue: self.Encoding = ( 24 | others )
        others = self.Encoding & 0b01111111
        if self.Variant: self.Encoding = ( 25 | others )
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.ArrayLength: 
            tmp.append(struct.pack(self._ArrayLength_fmt, self.ArrayLength))
        if self.Boolean: 
            tmp.append(struct.pack('!i', len(self.Boolean)))
            for i in Boolean:
                tmp.append(struct.pack(self._Boolean_fmt, self.Boolean))
        if self.SByte: 
            tmp.append(struct.pack('!i', len(self.SByte)))
            for i in SByte:
                tmp.append(struct.pack(self._SByte_fmt, self.SByte))
        if self.Byte: 
            tmp.append(struct.pack('!i', len(self.Byte)))
            for i in Byte:
                tmp.append(struct.pack(self._Byte_fmt, self.Byte))
        if self.Int16: 
            tmp.append(struct.pack('!i', len(self.Int16)))
            for i in Int16:
                tmp.append(struct.pack(self._Int16_fmt, self.Int16))
        if self.UInt16: 
            tmp.append(struct.pack('!i', len(self.UInt16)))
            for i in UInt16:
                tmp.append(struct.pack(self._UInt16_fmt, self.UInt16))
        if self.Int32: 
            tmp.append(struct.pack('!i', len(self.Int32)))
            for i in Int32:
                tmp.append(struct.pack(self._Int32_fmt, self.Int32))
        if self.UInt32: 
            tmp.append(struct.pack('!i', len(self.UInt32)))
            for i in UInt32:
                tmp.append(struct.pack(self._UInt32_fmt, self.UInt32))
        if self.Int64: 
            tmp.append(struct.pack('!i', len(self.Int64)))
            for i in Int64:
                tmp.append(struct.pack(self._Int64_fmt, self.Int64))
        if self.UInt64: 
            tmp.append(struct.pack('!i', len(self.UInt64)))
            for i in UInt64:
                tmp.append(struct.pack(self._UInt64_fmt, self.UInt64))
        if self.Float: 
            tmp.append(struct.pack('!i', len(self.Float)))
            for i in Float:
                tmp.append(struct.pack(self._Float_fmt, self.Float))
        if self.Double: 
            tmp.append(struct.pack('!i', len(self.Double)))
            for i in Double:
                tmp.append(struct.pack(self._Double_fmt, self.Double))
        if self.String: 
            tmp.append(struct.pack('!i', len(self.String)))
            for i in String:
                tmp.append(self.String.to_binary())
        if self.DateTime: 
            tmp.append(struct.pack('!i', len(self.DateTime)))
            for i in DateTime:
                tmp.append(struct.pack(self._DateTime_fmt, self.DateTime))
        if self.Guid: 
            tmp.append(struct.pack('!i', len(self.Guid)))
            for i in Guid:
                tmp.append(self.Guid.to_binary())
        if self.ByteString: 
            tmp.append(struct.pack('!i', len(self.ByteString)))
            for i in ByteString:
                tmp.append(self.ByteString.to_binary())
        if self.XmlElement: 
            tmp.append(struct.pack('!i', len(self.XmlElement)))
            for i in XmlElement:
                tmp.append(self.XmlElement.to_binary())
        if self.NodeId: 
            tmp.append(struct.pack('!i', len(self.NodeId)))
            for i in NodeId:
                tmp.append(self.NodeId.to_binary())
        if self.ExpandedNodeId: 
            tmp.append(struct.pack('!i', len(self.ExpandedNodeId)))
            for i in ExpandedNodeId:
                tmp.append(self.ExpandedNodeId.to_binary())
        if self.StatusCode: 
            tmp.append(struct.pack('!i', len(self.StatusCode)))
            for i in StatusCode:
                tmp.append(self.StatusCode.to_binary())
        if self.DiagnosticInfo: 
            tmp.append(struct.pack('!i', len(self.DiagnosticInfo)))
            for i in DiagnosticInfo:
                tmp.append(self.DiagnosticInfo.to_binary())
        if self.QualifiedName: 
            tmp.append(struct.pack('!i', len(self.QualifiedName)))
            for i in QualifiedName:
                tmp.append(self.QualifiedName.to_binary())
        if self.LocalizedText: 
            tmp.append(struct.pack('!i', len(self.LocalizedText)))
            for i in LocalizedText:
                tmp.append(self.LocalizedText.to_binary())
        if self.ExtensionObject: 
            tmp.append(struct.pack('!i', len(self.ExtensionObject)))
            for i in ExtensionObject:
                tmp.append(self.ExtensionObject.to_binary())
        if self.DataValue: 
            tmp.append(struct.pack('!i', len(self.DataValue)))
            for i in DataValue:
                tmp.append(self.DataValue.to_binary())
        if self.Variant: 
            tmp.append(struct.pack('!i', len(self.Variant)))
            for i in Variant:
                tmp.append(self.Variant.to_binary())
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 7):
                self.ArrayLength = struct.unpack(self._ArrayLength_fmt, data.read(self._ArrayLength_fmt_size))
            val = self.Encoding & 0b01111111
            if val == 0:
                length = struct.unpack('!i', data.read(4))
                if length != -1:
                    for i in range(0, length):
                        self.Boolean = struct.unpack(self._Boolean_fmt, data.read(self._Boolean_fmt_size))
            val = self.Encoding & 0b01111111
            if val == 0:
                length = struct.unpack('!i', data.read(4))
                if length != -1:
                    for i in range(0, length):
                        self.SByte = struct.unpack(self._SByte_fmt, data.read(self._SByte_fmt_size))
            val = self.Encoding & 0b01111111
            if val == 0:
                length = struct.unpack('!i', data.read(4))
                if length != -1:
                    for i in range(0, length):
                        self.Byte = struct.unpack(self._Byte_fmt, data.read(self._Byte_fmt_size))
            val = self.Encoding & 0b01111111
            if val == 0:
                length = struct.unpack('!i', data.read(4))
                if length != -1:
                    for i in range(0, length):
                        self.Int16 = struct.unpack(self._Int16_fmt, data.read(self._Int16_fmt_size))
            val = self.Encoding & 0b01111111
            if val == 0:
                length = struct.unpack('!i', data.read(4))
                if length != -1:
                    for i in range(0, length):
                        self.UInt16 = struct.unpack(self._UInt16_fmt, data.read(self._UInt16_fmt_size))
            val = self.Encoding & 0b01111111
            if val == 0:
                length = struct.unpack('!i', data.read(4))
                if length != -1:
                    for i in range(0, length):
                        self.Int32 = struct.unpack(self._Int32_fmt, data.read(self._Int32_fmt_size))
            val = self.Encoding & 0b01111111
            if val == 0:
                length = struct.unpack('!i', data.read(4))
                if length != -1:
                    for i in range(0, length):
                        self.UInt32 = struct.unpack(self._UInt32_fmt, data.read(self._UInt32_fmt_size))
            val = self.Encoding & 0b01111111
            if val == 0:
                length = struct.unpack('!i', data.read(4))
                if length != -1:
                    for i in range(0, length):
                        self.Int64 = struct.unpack(self._Int64_fmt, data.read(self._Int64_fmt_size))
            val = self.Encoding & 0b01111111
            if val == 0:
                length = struct.unpack('!i', data.read(4))
                if length != -1:
                    for i in range(0, length):
                        self.UInt64 = struct.unpack(self._UInt64_fmt, data.read(self._UInt64_fmt_size))
            val = self.Encoding & 0b01111111
            if val == 0:
                length = struct.unpack('!i', data.read(4))
                if length != -1:
                    for i in range(0, length):
                        self.Float = struct.unpack(self._Float_fmt, data.read(self._Float_fmt_size))
            val = self.Encoding & 0b01111111
            if val == 0:
                length = struct.unpack('!i', data.read(4))
                if length != -1:
                    for i in range(0, length):
                        self.Double = struct.unpack(self._Double_fmt, data.read(self._Double_fmt_size))
            val = self.Encoding & 0b01111111
            if val == 0:
                length = struct.unpack('!i', data.read(4))
                if length != -1:
                    for i in range(0, length):
                        data = self.String.from_binary(data)
            val = self.Encoding & 0b01111111
            if val == 0:
                length = struct.unpack('!i', data.read(4))
                if length != -1:
                    for i in range(0, length):
                        self.DateTime = struct.unpack(self._DateTime_fmt, data.read(self._DateTime_fmt_size))
            val = self.Encoding & 0b01111111
            if val == 0:
                length = struct.unpack('!i', data.read(4))
                if length != -1:
                    for i in range(0, length):
                        data = self.Guid.from_binary(data)
            val = self.Encoding & 0b01111111
            if val == 0:
                length = struct.unpack('!i', data.read(4))
                if length != -1:
                    for i in range(0, length):
                        data = self.ByteString.from_binary(data)
            val = self.Encoding & 0b01111111
            if val == 0:
                length = struct.unpack('!i', data.read(4))
                if length != -1:
                    for i in range(0, length):
                        data = self.XmlElement.from_binary(data)
            val = self.Encoding & 0b01111111
            if val == 0:
                length = struct.unpack('!i', data.read(4))
                if length != -1:
                    for i in range(0, length):
                        data = self.NodeId.from_binary(data)
            val = self.Encoding & 0b01111111
            if val == 0:
                length = struct.unpack('!i', data.read(4))
                if length != -1:
                    for i in range(0, length):
                        data = self.ExpandedNodeId.from_binary(data)
            val = self.Encoding & 0b01111111
            if val == 0:
                length = struct.unpack('!i', data.read(4))
                if length != -1:
                    for i in range(0, length):
                        data = self.StatusCode.from_binary(data)
            val = self.Encoding & 0b01111111
            if val == 0:
                length = struct.unpack('!i', data.read(4))
                if length != -1:
                    for i in range(0, length):
                        data = self.DiagnosticInfo.from_binary(data)
            val = self.Encoding & 0b01111111
            if val == 0:
                length = struct.unpack('!i', data.read(4))
                if length != -1:
                    for i in range(0, length):
                        data = self.QualifiedName.from_binary(data)
            val = self.Encoding & 0b01111111
            if val == 0:
                length = struct.unpack('!i', data.read(4))
                if length != -1:
                    for i in range(0, length):
                        data = self.LocalizedText.from_binary(data)
            val = self.Encoding & 0b01111111
            if val == 0:
                length = struct.unpack('!i', data.read(4))
                if length != -1:
                    for i in range(0, length):
                        data = self.ExtensionObject.from_binary(data)
            val = self.Encoding & 0b01111111
            if val == 0:
                length = struct.unpack('!i', data.read(4))
                if length != -1:
                    for i in range(0, length):
                        data = self.DataValue.from_binary(data)
            val = self.Encoding & 0b01111111
            if val == 0:
                length = struct.unpack('!i', data.read(4))
                if length != -1:
                    for i in range(0, length):
                        data = self.Variant.from_binary(data)
            return data
            
class DataValue(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.Value = None
        self.StatusCode = None
        self.SourceTimestamp = None
        self._SourceTimestamp_fmt = '!d'
        self._SourceTimestamp_fmt_size = 8
        self.SourcePicoseconds = None
        self._SourcePicoseconds_fmt = '!H'
        self._SourcePicoseconds_fmt_size = 2
        self.ServerTimestamp = None
        self._ServerTimestamp_fmt = '!d'
        self._ServerTimestamp_fmt_size = 8
        self.ServerPicoseconds = None
        self._ServerPicoseconds_fmt = '!H'
        self._ServerPicoseconds_fmt_size = 2
    
    def to_binary(self):
        packet = []
        tmp = packet
        if self.Value: self.Encoding |= (value << 0)
        if self.StatusCode: self.Encoding |= (value << 1)
        if self.SourceTimestamp: self.Encoding |= (value << 2)
        if self.SourcePicoseconds: self.Encoding |= (value << 3)
        if self.ServerTimestamp: self.Encoding |= (value << 4)
        if self.ServerPicoseconds: self.Encoding |= (value << 5)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.Value: 
            tmp.append(self.Value.to_binary())
        if self.StatusCode: 
            tmp.append(self.StatusCode.to_binary())
        if self.SourceTimestamp: 
            tmp.append(struct.pack(self._SourceTimestamp_fmt, self.SourceTimestamp))
        if self.SourcePicoseconds: 
            tmp.append(struct.pack(self._SourcePicoseconds_fmt, self.SourcePicoseconds))
        if self.ServerTimestamp: 
            tmp.append(struct.pack(self._ServerTimestamp_fmt, self.ServerTimestamp))
        if self.ServerPicoseconds: 
            tmp.append(struct.pack(self._ServerPicoseconds_fmt, self.ServerPicoseconds))
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.Value.from_binary(data)
            if self.Encoding & (1 << 1):
                data = self.StatusCode.from_binary(data)
            if self.Encoding & (1 << 2):
                self.SourceTimestamp = struct.unpack(self._SourceTimestamp_fmt, data.read(self._SourceTimestamp_fmt_size))
            if self.Encoding & (1 << 3):
                self.SourcePicoseconds = struct.unpack(self._SourcePicoseconds_fmt, data.read(self._SourcePicoseconds_fmt_size))
            if self.Encoding & (1 << 4):
                self.ServerTimestamp = struct.unpack(self._ServerTimestamp_fmt, data.read(self._ServerTimestamp_fmt_size))
            if self.Encoding & (1 << 5):
                self.ServerPicoseconds = struct.unpack(self._ServerPicoseconds_fmt, data.read(self._ServerPicoseconds_fmt_size))
            return data
            
class ReferenceNode(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.ReferenceTypeId = None
        self.IsInverse = None
        self._IsInverse_fmt = '!?'
        self._IsInverse_fmt_size = 1
        self.TargetId = None
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.ReferenceTypeId.to_binary())
        tmp.append(struct.pack(self._IsInverse_fmt, self.IsInverse))
        tmp.append(self.TargetId.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.ReferenceTypeId.from_binary(data)
            self.IsInverse = struct.unpack(self._IsInverse_fmt, data.read(self._IsInverse_fmt_size))
            data = self.TargetId.from_binary(data)
            return data
            
class Node(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.NodeId = None
        self.NodeClass = None
        self.BrowseName = None
        self.DisplayName = None
        self.Description = None
        self.WriteMask = None
        self._WriteMask_fmt = '!I'
        self._WriteMask_fmt_size = 4
        self.UserWriteMask = None
        self._UserWriteMask_fmt = '!I'
        self._UserWriteMask_fmt_size = 4
        self.References = []
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.NodeId.to_binary())
        tmp.append(self.NodeClass.to_binary())
        tmp.append(self.BrowseName.to_binary())
        tmp.append(self.DisplayName.to_binary())
        tmp.append(self.Description.to_binary())
        tmp.append(struct.pack(self._WriteMask_fmt, self.WriteMask))
        tmp.append(struct.pack(self._UserWriteMask_fmt, self.UserWriteMask))
        tmp.append(struct.pack('!i', len(self.References)))
        for i in References:
            tmp.append(self.References.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.NodeId.from_binary(data)
            data = self.NodeClass.from_binary(data)
            data = self.BrowseName.from_binary(data)
            data = self.DisplayName.from_binary(data)
            data = self.Description.from_binary(data)
            self.WriteMask = struct.unpack(self._WriteMask_fmt, data.read(self._WriteMask_fmt_size))
            self.UserWriteMask = struct.unpack(self._UserWriteMask_fmt, data.read(self._UserWriteMask_fmt_size))
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.References.from_binary(data)
            return data
            
class InstanceNode(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.NodeId = None
        self.NodeClass = None
        self.BrowseName = None
        self.DisplayName = None
        self.Description = None
        self.WriteMask = None
        self._WriteMask_fmt = '!I'
        self._WriteMask_fmt_size = 4
        self.UserWriteMask = None
        self._UserWriteMask_fmt = '!I'
        self._UserWriteMask_fmt_size = 4
        self.References = []
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.NodeId.to_binary())
        tmp.append(self.NodeClass.to_binary())
        tmp.append(self.BrowseName.to_binary())
        tmp.append(self.DisplayName.to_binary())
        tmp.append(self.Description.to_binary())
        tmp.append(struct.pack(self._WriteMask_fmt, self.WriteMask))
        tmp.append(struct.pack(self._UserWriteMask_fmt, self.UserWriteMask))
        tmp.append(struct.pack('!i', len(self.References)))
        for i in References:
            tmp.append(self.References.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.NodeId.from_binary(data)
            data = self.NodeClass.from_binary(data)
            data = self.BrowseName.from_binary(data)
            data = self.DisplayName.from_binary(data)
            data = self.Description.from_binary(data)
            self.WriteMask = struct.unpack(self._WriteMask_fmt, data.read(self._WriteMask_fmt_size))
            self.UserWriteMask = struct.unpack(self._UserWriteMask_fmt, data.read(self._UserWriteMask_fmt_size))
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.References.from_binary(data)
            return data
            
class TypeNode(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.NodeId = None
        self.NodeClass = None
        self.BrowseName = None
        self.DisplayName = None
        self.Description = None
        self.WriteMask = None
        self._WriteMask_fmt = '!I'
        self._WriteMask_fmt_size = 4
        self.UserWriteMask = None
        self._UserWriteMask_fmt = '!I'
        self._UserWriteMask_fmt_size = 4
        self.References = []
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.NodeId.to_binary())
        tmp.append(self.NodeClass.to_binary())
        tmp.append(self.BrowseName.to_binary())
        tmp.append(self.DisplayName.to_binary())
        tmp.append(self.Description.to_binary())
        tmp.append(struct.pack(self._WriteMask_fmt, self.WriteMask))
        tmp.append(struct.pack(self._UserWriteMask_fmt, self.UserWriteMask))
        tmp.append(struct.pack('!i', len(self.References)))
        for i in References:
            tmp.append(self.References.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.NodeId.from_binary(data)
            data = self.NodeClass.from_binary(data)
            data = self.BrowseName.from_binary(data)
            data = self.DisplayName.from_binary(data)
            data = self.Description.from_binary(data)
            self.WriteMask = struct.unpack(self._WriteMask_fmt, data.read(self._WriteMask_fmt_size))
            self.UserWriteMask = struct.unpack(self._UserWriteMask_fmt, data.read(self._UserWriteMask_fmt_size))
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.References.from_binary(data)
            return data
            
class ObjectNode(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.NodeId = None
        self.NodeClass = None
        self.BrowseName = None
        self.DisplayName = None
        self.Description = None
        self.WriteMask = None
        self._WriteMask_fmt = '!I'
        self._WriteMask_fmt_size = 4
        self.UserWriteMask = None
        self._UserWriteMask_fmt = '!I'
        self._UserWriteMask_fmt_size = 4
        self.References = []
        self.EventNotifier = None
        self._EventNotifier_fmt = '!c'
        self._EventNotifier_fmt_size = 1
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.NodeId.to_binary())
        tmp.append(self.NodeClass.to_binary())
        tmp.append(self.BrowseName.to_binary())
        tmp.append(self.DisplayName.to_binary())
        tmp.append(self.Description.to_binary())
        tmp.append(struct.pack(self._WriteMask_fmt, self.WriteMask))
        tmp.append(struct.pack(self._UserWriteMask_fmt, self.UserWriteMask))
        tmp.append(struct.pack('!i', len(self.References)))
        for i in References:
            tmp.append(self.References.to_binary())
        tmp.append(struct.pack(self._EventNotifier_fmt, self.EventNotifier))
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.NodeId.from_binary(data)
            data = self.NodeClass.from_binary(data)
            data = self.BrowseName.from_binary(data)
            data = self.DisplayName.from_binary(data)
            data = self.Description.from_binary(data)
            self.WriteMask = struct.unpack(self._WriteMask_fmt, data.read(self._WriteMask_fmt_size))
            self.UserWriteMask = struct.unpack(self._UserWriteMask_fmt, data.read(self._UserWriteMask_fmt_size))
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.References.from_binary(data)
            self.EventNotifier = struct.unpack(self._EventNotifier_fmt, data.read(self._EventNotifier_fmt_size))
            return data
            
class ObjectTypeNode(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.NodeId = None
        self.NodeClass = None
        self.BrowseName = None
        self.DisplayName = None
        self.Description = None
        self.WriteMask = None
        self._WriteMask_fmt = '!I'
        self._WriteMask_fmt_size = 4
        self.UserWriteMask = None
        self._UserWriteMask_fmt = '!I'
        self._UserWriteMask_fmt_size = 4
        self.References = []
        self.IsAbstract = None
        self._IsAbstract_fmt = '!?'
        self._IsAbstract_fmt_size = 1
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.NodeId.to_binary())
        tmp.append(self.NodeClass.to_binary())
        tmp.append(self.BrowseName.to_binary())
        tmp.append(self.DisplayName.to_binary())
        tmp.append(self.Description.to_binary())
        tmp.append(struct.pack(self._WriteMask_fmt, self.WriteMask))
        tmp.append(struct.pack(self._UserWriteMask_fmt, self.UserWriteMask))
        tmp.append(struct.pack('!i', len(self.References)))
        for i in References:
            tmp.append(self.References.to_binary())
        tmp.append(struct.pack(self._IsAbstract_fmt, self.IsAbstract))
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.NodeId.from_binary(data)
            data = self.NodeClass.from_binary(data)
            data = self.BrowseName.from_binary(data)
            data = self.DisplayName.from_binary(data)
            data = self.Description.from_binary(data)
            self.WriteMask = struct.unpack(self._WriteMask_fmt, data.read(self._WriteMask_fmt_size))
            self.UserWriteMask = struct.unpack(self._UserWriteMask_fmt, data.read(self._UserWriteMask_fmt_size))
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.References.from_binary(data)
            self.IsAbstract = struct.unpack(self._IsAbstract_fmt, data.read(self._IsAbstract_fmt_size))
            return data
            
class VariableNode(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.NodeId = None
        self.NodeClass = None
        self.BrowseName = None
        self.DisplayName = None
        self.Description = None
        self.WriteMask = None
        self._WriteMask_fmt = '!I'
        self._WriteMask_fmt_size = 4
        self.UserWriteMask = None
        self._UserWriteMask_fmt = '!I'
        self._UserWriteMask_fmt_size = 4
        self.References = []
        self.Value = None
        self.DataType = None
        self.ValueRank = None
        self._ValueRank_fmt = '!i'
        self._ValueRank_fmt_size = 4
        self.ArrayDimensions = []
        self._ArrayDimensions_fmt = '!I'
        self._ArrayDimensions_fmt_size = 4
        self.AccessLevel = None
        self._AccessLevel_fmt = '!c'
        self._AccessLevel_fmt_size = 1
        self.UserAccessLevel = None
        self._UserAccessLevel_fmt = '!c'
        self._UserAccessLevel_fmt_size = 1
        self.MinimumSamplingInterval = None
        self._MinimumSamplingInterval_fmt = '!d'
        self._MinimumSamplingInterval_fmt_size = 8
        self.Historizing = None
        self._Historizing_fmt = '!?'
        self._Historizing_fmt_size = 1
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.NodeId.to_binary())
        tmp.append(self.NodeClass.to_binary())
        tmp.append(self.BrowseName.to_binary())
        tmp.append(self.DisplayName.to_binary())
        tmp.append(self.Description.to_binary())
        tmp.append(struct.pack(self._WriteMask_fmt, self.WriteMask))
        tmp.append(struct.pack(self._UserWriteMask_fmt, self.UserWriteMask))
        tmp.append(struct.pack('!i', len(self.References)))
        for i in References:
            tmp.append(self.References.to_binary())
        tmp.append(self.Value.to_binary())
        tmp.append(self.DataType.to_binary())
        tmp.append(struct.pack(self._ValueRank_fmt, self.ValueRank))
        tmp.append(struct.pack('!i', len(self.ArrayDimensions)))
        for i in ArrayDimensions:
            tmp.append(struct.pack(self._ArrayDimensions_fmt, self.ArrayDimensions))
        tmp.append(struct.pack(self._AccessLevel_fmt, self.AccessLevel))
        tmp.append(struct.pack(self._UserAccessLevel_fmt, self.UserAccessLevel))
        tmp.append(struct.pack(self._MinimumSamplingInterval_fmt, self.MinimumSamplingInterval))
        tmp.append(struct.pack(self._Historizing_fmt, self.Historizing))
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.NodeId.from_binary(data)
            data = self.NodeClass.from_binary(data)
            data = self.BrowseName.from_binary(data)
            data = self.DisplayName.from_binary(data)
            data = self.Description.from_binary(data)
            self.WriteMask = struct.unpack(self._WriteMask_fmt, data.read(self._WriteMask_fmt_size))
            self.UserWriteMask = struct.unpack(self._UserWriteMask_fmt, data.read(self._UserWriteMask_fmt_size))
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.References.from_binary(data)
            data = self.Value.from_binary(data)
            data = self.DataType.from_binary(data)
            self.ValueRank = struct.unpack(self._ValueRank_fmt, data.read(self._ValueRank_fmt_size))
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    self.ArrayDimensions = struct.unpack(self._ArrayDimensions_fmt, data.read(self._ArrayDimensions_fmt_size))
            self.AccessLevel = struct.unpack(self._AccessLevel_fmt, data.read(self._AccessLevel_fmt_size))
            self.UserAccessLevel = struct.unpack(self._UserAccessLevel_fmt, data.read(self._UserAccessLevel_fmt_size))
            self.MinimumSamplingInterval = struct.unpack(self._MinimumSamplingInterval_fmt, data.read(self._MinimumSamplingInterval_fmt_size))
            self.Historizing = struct.unpack(self._Historizing_fmt, data.read(self._Historizing_fmt_size))
            return data
            
class VariableTypeNode(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.NodeId = None
        self.NodeClass = None
        self.BrowseName = None
        self.DisplayName = None
        self.Description = None
        self.WriteMask = None
        self._WriteMask_fmt = '!I'
        self._WriteMask_fmt_size = 4
        self.UserWriteMask = None
        self._UserWriteMask_fmt = '!I'
        self._UserWriteMask_fmt_size = 4
        self.References = []
        self.Value = None
        self.DataType = None
        self.ValueRank = None
        self._ValueRank_fmt = '!i'
        self._ValueRank_fmt_size = 4
        self.ArrayDimensions = []
        self._ArrayDimensions_fmt = '!I'
        self._ArrayDimensions_fmt_size = 4
        self.IsAbstract = None
        self._IsAbstract_fmt = '!?'
        self._IsAbstract_fmt_size = 1
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.NodeId.to_binary())
        tmp.append(self.NodeClass.to_binary())
        tmp.append(self.BrowseName.to_binary())
        tmp.append(self.DisplayName.to_binary())
        tmp.append(self.Description.to_binary())
        tmp.append(struct.pack(self._WriteMask_fmt, self.WriteMask))
        tmp.append(struct.pack(self._UserWriteMask_fmt, self.UserWriteMask))
        tmp.append(struct.pack('!i', len(self.References)))
        for i in References:
            tmp.append(self.References.to_binary())
        tmp.append(self.Value.to_binary())
        tmp.append(self.DataType.to_binary())
        tmp.append(struct.pack(self._ValueRank_fmt, self.ValueRank))
        tmp.append(struct.pack('!i', len(self.ArrayDimensions)))
        for i in ArrayDimensions:
            tmp.append(struct.pack(self._ArrayDimensions_fmt, self.ArrayDimensions))
        tmp.append(struct.pack(self._IsAbstract_fmt, self.IsAbstract))
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.NodeId.from_binary(data)
            data = self.NodeClass.from_binary(data)
            data = self.BrowseName.from_binary(data)
            data = self.DisplayName.from_binary(data)
            data = self.Description.from_binary(data)
            self.WriteMask = struct.unpack(self._WriteMask_fmt, data.read(self._WriteMask_fmt_size))
            self.UserWriteMask = struct.unpack(self._UserWriteMask_fmt, data.read(self._UserWriteMask_fmt_size))
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.References.from_binary(data)
            data = self.Value.from_binary(data)
            data = self.DataType.from_binary(data)
            self.ValueRank = struct.unpack(self._ValueRank_fmt, data.read(self._ValueRank_fmt_size))
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    self.ArrayDimensions = struct.unpack(self._ArrayDimensions_fmt, data.read(self._ArrayDimensions_fmt_size))
            self.IsAbstract = struct.unpack(self._IsAbstract_fmt, data.read(self._IsAbstract_fmt_size))
            return data
            
class ReferenceTypeNode(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.NodeId = None
        self.NodeClass = None
        self.BrowseName = None
        self.DisplayName = None
        self.Description = None
        self.WriteMask = None
        self._WriteMask_fmt = '!I'
        self._WriteMask_fmt_size = 4
        self.UserWriteMask = None
        self._UserWriteMask_fmt = '!I'
        self._UserWriteMask_fmt_size = 4
        self.References = []
        self.IsAbstract = None
        self._IsAbstract_fmt = '!?'
        self._IsAbstract_fmt_size = 1
        self.Symmetric = None
        self._Symmetric_fmt = '!?'
        self._Symmetric_fmt_size = 1
        self.InverseName = None
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.NodeId.to_binary())
        tmp.append(self.NodeClass.to_binary())
        tmp.append(self.BrowseName.to_binary())
        tmp.append(self.DisplayName.to_binary())
        tmp.append(self.Description.to_binary())
        tmp.append(struct.pack(self._WriteMask_fmt, self.WriteMask))
        tmp.append(struct.pack(self._UserWriteMask_fmt, self.UserWriteMask))
        tmp.append(struct.pack('!i', len(self.References)))
        for i in References:
            tmp.append(self.References.to_binary())
        tmp.append(struct.pack(self._IsAbstract_fmt, self.IsAbstract))
        tmp.append(struct.pack(self._Symmetric_fmt, self.Symmetric))
        tmp.append(self.InverseName.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.NodeId.from_binary(data)
            data = self.NodeClass.from_binary(data)
            data = self.BrowseName.from_binary(data)
            data = self.DisplayName.from_binary(data)
            data = self.Description.from_binary(data)
            self.WriteMask = struct.unpack(self._WriteMask_fmt, data.read(self._WriteMask_fmt_size))
            self.UserWriteMask = struct.unpack(self._UserWriteMask_fmt, data.read(self._UserWriteMask_fmt_size))
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.References.from_binary(data)
            self.IsAbstract = struct.unpack(self._IsAbstract_fmt, data.read(self._IsAbstract_fmt_size))
            self.Symmetric = struct.unpack(self._Symmetric_fmt, data.read(self._Symmetric_fmt_size))
            data = self.InverseName.from_binary(data)
            return data
            
class MethodNode(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.NodeId = None
        self.NodeClass = None
        self.BrowseName = None
        self.DisplayName = None
        self.Description = None
        self.WriteMask = None
        self._WriteMask_fmt = '!I'
        self._WriteMask_fmt_size = 4
        self.UserWriteMask = None
        self._UserWriteMask_fmt = '!I'
        self._UserWriteMask_fmt_size = 4
        self.References = []
        self.Executable = None
        self._Executable_fmt = '!?'
        self._Executable_fmt_size = 1
        self.UserExecutable = None
        self._UserExecutable_fmt = '!?'
        self._UserExecutable_fmt_size = 1
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.NodeId.to_binary())
        tmp.append(self.NodeClass.to_binary())
        tmp.append(self.BrowseName.to_binary())
        tmp.append(self.DisplayName.to_binary())
        tmp.append(self.Description.to_binary())
        tmp.append(struct.pack(self._WriteMask_fmt, self.WriteMask))
        tmp.append(struct.pack(self._UserWriteMask_fmt, self.UserWriteMask))
        tmp.append(struct.pack('!i', len(self.References)))
        for i in References:
            tmp.append(self.References.to_binary())
        tmp.append(struct.pack(self._Executable_fmt, self.Executable))
        tmp.append(struct.pack(self._UserExecutable_fmt, self.UserExecutable))
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.NodeId.from_binary(data)
            data = self.NodeClass.from_binary(data)
            data = self.BrowseName.from_binary(data)
            data = self.DisplayName.from_binary(data)
            data = self.Description.from_binary(data)
            self.WriteMask = struct.unpack(self._WriteMask_fmt, data.read(self._WriteMask_fmt_size))
            self.UserWriteMask = struct.unpack(self._UserWriteMask_fmt, data.read(self._UserWriteMask_fmt_size))
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.References.from_binary(data)
            self.Executable = struct.unpack(self._Executable_fmt, data.read(self._Executable_fmt_size))
            self.UserExecutable = struct.unpack(self._UserExecutable_fmt, data.read(self._UserExecutable_fmt_size))
            return data
            
class ViewNode(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.NodeId = None
        self.NodeClass = None
        self.BrowseName = None
        self.DisplayName = None
        self.Description = None
        self.WriteMask = None
        self._WriteMask_fmt = '!I'
        self._WriteMask_fmt_size = 4
        self.UserWriteMask = None
        self._UserWriteMask_fmt = '!I'
        self._UserWriteMask_fmt_size = 4
        self.References = []
        self.ContainsNoLoops = None
        self._ContainsNoLoops_fmt = '!?'
        self._ContainsNoLoops_fmt_size = 1
        self.EventNotifier = None
        self._EventNotifier_fmt = '!c'
        self._EventNotifier_fmt_size = 1
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.NodeId.to_binary())
        tmp.append(self.NodeClass.to_binary())
        tmp.append(self.BrowseName.to_binary())
        tmp.append(self.DisplayName.to_binary())
        tmp.append(self.Description.to_binary())
        tmp.append(struct.pack(self._WriteMask_fmt, self.WriteMask))
        tmp.append(struct.pack(self._UserWriteMask_fmt, self.UserWriteMask))
        tmp.append(struct.pack('!i', len(self.References)))
        for i in References:
            tmp.append(self.References.to_binary())
        tmp.append(struct.pack(self._ContainsNoLoops_fmt, self.ContainsNoLoops))
        tmp.append(struct.pack(self._EventNotifier_fmt, self.EventNotifier))
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.NodeId.from_binary(data)
            data = self.NodeClass.from_binary(data)
            data = self.BrowseName.from_binary(data)
            data = self.DisplayName.from_binary(data)
            data = self.Description.from_binary(data)
            self.WriteMask = struct.unpack(self._WriteMask_fmt, data.read(self._WriteMask_fmt_size))
            self.UserWriteMask = struct.unpack(self._UserWriteMask_fmt, data.read(self._UserWriteMask_fmt_size))
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.References.from_binary(data)
            self.ContainsNoLoops = struct.unpack(self._ContainsNoLoops_fmt, data.read(self._ContainsNoLoops_fmt_size))
            self.EventNotifier = struct.unpack(self._EventNotifier_fmt, data.read(self._EventNotifier_fmt_size))
            return data
            
class DataTypeNode(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.NodeId = None
        self.NodeClass = None
        self.BrowseName = None
        self.DisplayName = None
        self.Description = None
        self.WriteMask = None
        self._WriteMask_fmt = '!I'
        self._WriteMask_fmt_size = 4
        self.UserWriteMask = None
        self._UserWriteMask_fmt = '!I'
        self._UserWriteMask_fmt_size = 4
        self.References = []
        self.IsAbstract = None
        self._IsAbstract_fmt = '!?'
        self._IsAbstract_fmt_size = 1
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.NodeId.to_binary())
        tmp.append(self.NodeClass.to_binary())
        tmp.append(self.BrowseName.to_binary())
        tmp.append(self.DisplayName.to_binary())
        tmp.append(self.Description.to_binary())
        tmp.append(struct.pack(self._WriteMask_fmt, self.WriteMask))
        tmp.append(struct.pack(self._UserWriteMask_fmt, self.UserWriteMask))
        tmp.append(struct.pack('!i', len(self.References)))
        for i in References:
            tmp.append(self.References.to_binary())
        tmp.append(struct.pack(self._IsAbstract_fmt, self.IsAbstract))
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.NodeId.from_binary(data)
            data = self.NodeClass.from_binary(data)
            data = self.BrowseName.from_binary(data)
            data = self.DisplayName.from_binary(data)
            data = self.Description.from_binary(data)
            self.WriteMask = struct.unpack(self._WriteMask_fmt, data.read(self._WriteMask_fmt_size))
            self.UserWriteMask = struct.unpack(self._UserWriteMask_fmt, data.read(self._UserWriteMask_fmt_size))
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.References.from_binary(data)
            self.IsAbstract = struct.unpack(self._IsAbstract_fmt, data.read(self._IsAbstract_fmt_size))
            return data
            
class Argument(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.Name = None
        self.DataType = None
        self.ValueRank = None
        self._ValueRank_fmt = '!i'
        self._ValueRank_fmt_size = 4
        self.ArrayDimensions = []
        self._ArrayDimensions_fmt = '!I'
        self._ArrayDimensions_fmt_size = 4
        self.Description = None
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.Name.to_binary())
        tmp.append(self.DataType.to_binary())
        tmp.append(struct.pack(self._ValueRank_fmt, self.ValueRank))
        tmp.append(struct.pack('!i', len(self.ArrayDimensions)))
        for i in ArrayDimensions:
            tmp.append(struct.pack(self._ArrayDimensions_fmt, self.ArrayDimensions))
        tmp.append(self.Description.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.Name.from_binary(data)
            data = self.DataType.from_binary(data)
            self.ValueRank = struct.unpack(self._ValueRank_fmt, data.read(self._ValueRank_fmt_size))
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    self.ArrayDimensions = struct.unpack(self._ArrayDimensions_fmt, data.read(self._ArrayDimensions_fmt_size))
            data = self.Description.from_binary(data)
            return data
            
class EnumValueType(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.Value = None
        self._Value_fmt = '!q'
        self._Value_fmt_size = 8
        self.DisplayName = None
        self.Description = None
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(struct.pack(self._Value_fmt, self.Value))
        tmp.append(self.DisplayName.to_binary())
        tmp.append(self.Description.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            self.Value = struct.unpack(self._Value_fmt, data.read(self._Value_fmt_size))
            data = self.DisplayName.from_binary(data)
            data = self.Description.from_binary(data)
            return data
            
class TimeZoneDataType(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.Offset = None
        self._Offset_fmt = '!h'
        self._Offset_fmt_size = 2
        self.DaylightSavingInOffset = None
        self._DaylightSavingInOffset_fmt = '!?'
        self._DaylightSavingInOffset_fmt_size = 1
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(struct.pack(self._Offset_fmt, self.Offset))
        tmp.append(struct.pack(self._DaylightSavingInOffset_fmt, self.DaylightSavingInOffset))
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            self.Offset = struct.unpack(self._Offset_fmt, data.read(self._Offset_fmt_size))
            self.DaylightSavingInOffset = struct.unpack(self._DaylightSavingInOffset_fmt, data.read(self._DaylightSavingInOffset_fmt_size))
            return data
            
class ApplicationDescription(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.ApplicationUri = None
        self.ProductUri = None
        self.ApplicationName = None
        self.ApplicationType = None
        self.GatewayServerUri = None
        self.DiscoveryProfileUri = None
        self.DiscoveryUrls = []
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.ApplicationUri.to_binary())
        tmp.append(self.ProductUri.to_binary())
        tmp.append(self.ApplicationName.to_binary())
        tmp.append(self.ApplicationType.to_binary())
        tmp.append(self.GatewayServerUri.to_binary())
        tmp.append(self.DiscoveryProfileUri.to_binary())
        tmp.append(struct.pack('!i', len(self.DiscoveryUrls)))
        for i in DiscoveryUrls:
            tmp.append(self.DiscoveryUrls.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.ApplicationUri.from_binary(data)
            data = self.ProductUri.from_binary(data)
            data = self.ApplicationName.from_binary(data)
            data = self.ApplicationType.from_binary(data)
            data = self.GatewayServerUri.from_binary(data)
            data = self.DiscoveryProfileUri.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.DiscoveryUrls.from_binary(data)
            return data
            
class RequestHeader(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.AuthenticationToken = None
        self.Timestamp = None
        self._Timestamp_fmt = '!d'
        self._Timestamp_fmt_size = 8
        self.RequestHandle = None
        self._RequestHandle_fmt = '!I'
        self._RequestHandle_fmt_size = 4
        self.ReturnDiagnostics = None
        self._ReturnDiagnostics_fmt = '!I'
        self._ReturnDiagnostics_fmt_size = 4
        self.AuditEntryId = None
        self.TimeoutHint = None
        self._TimeoutHint_fmt = '!I'
        self._TimeoutHint_fmt_size = 4
        self.AdditionalHeader = None
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.AuthenticationToken.to_binary())
        tmp.append(struct.pack(self._Timestamp_fmt, self.Timestamp))
        tmp.append(struct.pack(self._RequestHandle_fmt, self.RequestHandle))
        tmp.append(struct.pack(self._ReturnDiagnostics_fmt, self.ReturnDiagnostics))
        tmp.append(self.AuditEntryId.to_binary())
        tmp.append(struct.pack(self._TimeoutHint_fmt, self.TimeoutHint))
        tmp.append(self.AdditionalHeader.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.AuthenticationToken.from_binary(data)
            self.Timestamp = struct.unpack(self._Timestamp_fmt, data.read(self._Timestamp_fmt_size))
            self.RequestHandle = struct.unpack(self._RequestHandle_fmt, data.read(self._RequestHandle_fmt_size))
            self.ReturnDiagnostics = struct.unpack(self._ReturnDiagnostics_fmt, data.read(self._ReturnDiagnostics_fmt_size))
            data = self.AuditEntryId.from_binary(data)
            self.TimeoutHint = struct.unpack(self._TimeoutHint_fmt, data.read(self._TimeoutHint_fmt_size))
            data = self.AdditionalHeader.from_binary(data)
            return data
            
class ResponseHeader(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.Timestamp = None
        self._Timestamp_fmt = '!d'
        self._Timestamp_fmt_size = 8
        self.RequestHandle = None
        self._RequestHandle_fmt = '!I'
        self._RequestHandle_fmt_size = 4
        self.ServiceResult = None
        self.ServiceDiagnostics = None
        self.StringTable = []
        self.AdditionalHeader = None
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(struct.pack(self._Timestamp_fmt, self.Timestamp))
        tmp.append(struct.pack(self._RequestHandle_fmt, self.RequestHandle))
        tmp.append(self.ServiceResult.to_binary())
        tmp.append(self.ServiceDiagnostics.to_binary())
        tmp.append(struct.pack('!i', len(self.StringTable)))
        for i in StringTable:
            tmp.append(self.StringTable.to_binary())
        tmp.append(self.AdditionalHeader.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            self.Timestamp = struct.unpack(self._Timestamp_fmt, data.read(self._Timestamp_fmt_size))
            self.RequestHandle = struct.unpack(self._RequestHandle_fmt, data.read(self._RequestHandle_fmt_size))
            data = self.ServiceResult.from_binary(data)
            data = self.ServiceDiagnostics.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.StringTable.from_binary(data)
            data = self.AdditionalHeader.from_binary(data)
            return data
            
class ServiceFault(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.ResponseHeader = None
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.ResponseHeader.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.ResponseHeader.from_binary(data)
            return data
            
class FindServersRequest(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.RequestHeader = None
        self.EndpointUrl = None
        self.LocaleIds = []
        self.ServerUris = []
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.RequestHeader.to_binary())
        tmp.append(self.EndpointUrl.to_binary())
        tmp.append(struct.pack('!i', len(self.LocaleIds)))
        for i in LocaleIds:
            tmp.append(self.LocaleIds.to_binary())
        tmp.append(struct.pack('!i', len(self.ServerUris)))
        for i in ServerUris:
            tmp.append(self.ServerUris.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.RequestHeader.from_binary(data)
            data = self.EndpointUrl.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.LocaleIds.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.ServerUris.from_binary(data)
            return data
            
class FindServersResponse(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.ResponseHeader = None
        self.Servers = []
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.ResponseHeader.to_binary())
        tmp.append(struct.pack('!i', len(self.Servers)))
        for i in Servers:
            tmp.append(self.Servers.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.ResponseHeader.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.Servers.from_binary(data)
            return data
            
class UserTokenPolicy(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.PolicyId = None
        self.TokenType = None
        self.IssuedTokenType = None
        self.IssuerEndpointUrl = None
        self.SecurityPolicyUri = None
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.PolicyId.to_binary())
        tmp.append(self.TokenType.to_binary())
        tmp.append(self.IssuedTokenType.to_binary())
        tmp.append(self.IssuerEndpointUrl.to_binary())
        tmp.append(self.SecurityPolicyUri.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.PolicyId.from_binary(data)
            data = self.TokenType.from_binary(data)
            data = self.IssuedTokenType.from_binary(data)
            data = self.IssuerEndpointUrl.from_binary(data)
            data = self.SecurityPolicyUri.from_binary(data)
            return data
            
class EndpointDescription(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.EndpointUrl = None
        self.Server = None
        self.ServerCertificate = None
        self.SecurityMode = None
        self.SecurityPolicyUri = None
        self.UserIdentityTokens = []
        self.TransportProfileUri = None
        self.SecurityLevel = None
        self._SecurityLevel_fmt = '!c'
        self._SecurityLevel_fmt_size = 1
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.EndpointUrl.to_binary())
        tmp.append(self.Server.to_binary())
        tmp.append(self.ServerCertificate.to_binary())
        tmp.append(self.SecurityMode.to_binary())
        tmp.append(self.SecurityPolicyUri.to_binary())
        tmp.append(struct.pack('!i', len(self.UserIdentityTokens)))
        for i in UserIdentityTokens:
            tmp.append(self.UserIdentityTokens.to_binary())
        tmp.append(self.TransportProfileUri.to_binary())
        tmp.append(struct.pack(self._SecurityLevel_fmt, self.SecurityLevel))
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.EndpointUrl.from_binary(data)
            data = self.Server.from_binary(data)
            data = self.ServerCertificate.from_binary(data)
            data = self.SecurityMode.from_binary(data)
            data = self.SecurityPolicyUri.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.UserIdentityTokens.from_binary(data)
            data = self.TransportProfileUri.from_binary(data)
            self.SecurityLevel = struct.unpack(self._SecurityLevel_fmt, data.read(self._SecurityLevel_fmt_size))
            return data
            
class GetEndpointsRequest(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.RequestHeader = None
        self.EndpointUrl = None
        self.LocaleIds = []
        self.ProfileUris = []
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.RequestHeader.to_binary())
        tmp.append(self.EndpointUrl.to_binary())
        tmp.append(struct.pack('!i', len(self.LocaleIds)))
        for i in LocaleIds:
            tmp.append(self.LocaleIds.to_binary())
        tmp.append(struct.pack('!i', len(self.ProfileUris)))
        for i in ProfileUris:
            tmp.append(self.ProfileUris.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.RequestHeader.from_binary(data)
            data = self.EndpointUrl.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.LocaleIds.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.ProfileUris.from_binary(data)
            return data
            
class GetEndpointsResponse(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.ResponseHeader = None
        self.Endpoints = []
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.ResponseHeader.to_binary())
        tmp.append(struct.pack('!i', len(self.Endpoints)))
        for i in Endpoints:
            tmp.append(self.Endpoints.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.ResponseHeader.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.Endpoints.from_binary(data)
            return data
            
class RegisteredServer(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.ServerUri = None
        self.ProductUri = None
        self.ServerNames = []
        self.ServerType = None
        self.GatewayServerUri = None
        self.DiscoveryUrls = []
        self.SemaphoreFilePath = None
        self.IsOnline = None
        self._IsOnline_fmt = '!?'
        self._IsOnline_fmt_size = 1
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.ServerUri.to_binary())
        tmp.append(self.ProductUri.to_binary())
        tmp.append(struct.pack('!i', len(self.ServerNames)))
        for i in ServerNames:
            tmp.append(self.ServerNames.to_binary())
        tmp.append(self.ServerType.to_binary())
        tmp.append(self.GatewayServerUri.to_binary())
        tmp.append(struct.pack('!i', len(self.DiscoveryUrls)))
        for i in DiscoveryUrls:
            tmp.append(self.DiscoveryUrls.to_binary())
        tmp.append(self.SemaphoreFilePath.to_binary())
        tmp.append(struct.pack(self._IsOnline_fmt, self.IsOnline))
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.ServerUri.from_binary(data)
            data = self.ProductUri.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.ServerNames.from_binary(data)
            data = self.ServerType.from_binary(data)
            data = self.GatewayServerUri.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.DiscoveryUrls.from_binary(data)
            data = self.SemaphoreFilePath.from_binary(data)
            self.IsOnline = struct.unpack(self._IsOnline_fmt, data.read(self._IsOnline_fmt_size))
            return data
            
class RegisterServerRequest(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.RequestHeader = None
        self.Server = None
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.RequestHeader.to_binary())
        tmp.append(self.Server.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.RequestHeader.from_binary(data)
            data = self.Server.from_binary(data)
            return data
            
class RegisterServerResponse(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.ResponseHeader = None
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.ResponseHeader.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.ResponseHeader.from_binary(data)
            return data
            
class ChannelSecurityToken(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.ChannelId = None
        self._ChannelId_fmt = '!I'
        self._ChannelId_fmt_size = 4
        self.TokenId = None
        self._TokenId_fmt = '!I'
        self._TokenId_fmt_size = 4
        self.CreatedAt = None
        self._CreatedAt_fmt = '!d'
        self._CreatedAt_fmt_size = 8
        self.RevisedLifetime = None
        self._RevisedLifetime_fmt = '!I'
        self._RevisedLifetime_fmt_size = 4
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(struct.pack(self._ChannelId_fmt, self.ChannelId))
        tmp.append(struct.pack(self._TokenId_fmt, self.TokenId))
        tmp.append(struct.pack(self._CreatedAt_fmt, self.CreatedAt))
        tmp.append(struct.pack(self._RevisedLifetime_fmt, self.RevisedLifetime))
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            self.ChannelId = struct.unpack(self._ChannelId_fmt, data.read(self._ChannelId_fmt_size))
            self.TokenId = struct.unpack(self._TokenId_fmt, data.read(self._TokenId_fmt_size))
            self.CreatedAt = struct.unpack(self._CreatedAt_fmt, data.read(self._CreatedAt_fmt_size))
            self.RevisedLifetime = struct.unpack(self._RevisedLifetime_fmt, data.read(self._RevisedLifetime_fmt_size))
            return data
            
class OpenSecureChannelRequest(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.RequestHeader = None
        self.ClientProtocolVersion = None
        self._ClientProtocolVersion_fmt = '!I'
        self._ClientProtocolVersion_fmt_size = 4
        self.RequestType = None
        self.SecurityMode = None
        self.ClientNonce = None
        self.RequestedLifetime = None
        self._RequestedLifetime_fmt = '!I'
        self._RequestedLifetime_fmt_size = 4
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.RequestHeader.to_binary())
        tmp.append(struct.pack(self._ClientProtocolVersion_fmt, self.ClientProtocolVersion))
        tmp.append(self.RequestType.to_binary())
        tmp.append(self.SecurityMode.to_binary())
        tmp.append(self.ClientNonce.to_binary())
        tmp.append(struct.pack(self._RequestedLifetime_fmt, self.RequestedLifetime))
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.RequestHeader.from_binary(data)
            self.ClientProtocolVersion = struct.unpack(self._ClientProtocolVersion_fmt, data.read(self._ClientProtocolVersion_fmt_size))
            data = self.RequestType.from_binary(data)
            data = self.SecurityMode.from_binary(data)
            data = self.ClientNonce.from_binary(data)
            self.RequestedLifetime = struct.unpack(self._RequestedLifetime_fmt, data.read(self._RequestedLifetime_fmt_size))
            return data
            
class OpenSecureChannelResponse(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.ResponseHeader = None
        self.ServerProtocolVersion = None
        self._ServerProtocolVersion_fmt = '!I'
        self._ServerProtocolVersion_fmt_size = 4
        self.SecurityToken = None
        self.ServerNonce = None
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.ResponseHeader.to_binary())
        tmp.append(struct.pack(self._ServerProtocolVersion_fmt, self.ServerProtocolVersion))
        tmp.append(self.SecurityToken.to_binary())
        tmp.append(self.ServerNonce.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.ResponseHeader.from_binary(data)
            self.ServerProtocolVersion = struct.unpack(self._ServerProtocolVersion_fmt, data.read(self._ServerProtocolVersion_fmt_size))
            data = self.SecurityToken.from_binary(data)
            data = self.ServerNonce.from_binary(data)
            return data
            
class CloseSecureChannelRequest(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.RequestHeader = None
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.RequestHeader.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.RequestHeader.from_binary(data)
            return data
            
class CloseSecureChannelResponse(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.ResponseHeader = None
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.ResponseHeader.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.ResponseHeader.from_binary(data)
            return data
            
class SignedSoftwareCertificate(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.CertificateData = None
        self.Signature = None
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.CertificateData.to_binary())
        tmp.append(self.Signature.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.CertificateData.from_binary(data)
            data = self.Signature.from_binary(data)
            return data
            
class SignatureData(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.Algorithm = None
        self.Signature = None
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.Algorithm.to_binary())
        tmp.append(self.Signature.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.Algorithm.from_binary(data)
            data = self.Signature.from_binary(data)
            return data
            
class CreateSessionRequest(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.RequestHeader = None
        self.ClientDescription = None
        self.ServerUri = None
        self.EndpointUrl = None
        self.SessionName = None
        self.ClientNonce = None
        self.ClientCertificate = None
        self.RequestedSessionTimeout = None
        self._RequestedSessionTimeout_fmt = '!d'
        self._RequestedSessionTimeout_fmt_size = 8
        self.MaxResponseMessageSize = None
        self._MaxResponseMessageSize_fmt = '!I'
        self._MaxResponseMessageSize_fmt_size = 4
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.RequestHeader.to_binary())
        tmp.append(self.ClientDescription.to_binary())
        tmp.append(self.ServerUri.to_binary())
        tmp.append(self.EndpointUrl.to_binary())
        tmp.append(self.SessionName.to_binary())
        tmp.append(self.ClientNonce.to_binary())
        tmp.append(self.ClientCertificate.to_binary())
        tmp.append(struct.pack(self._RequestedSessionTimeout_fmt, self.RequestedSessionTimeout))
        tmp.append(struct.pack(self._MaxResponseMessageSize_fmt, self.MaxResponseMessageSize))
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.RequestHeader.from_binary(data)
            data = self.ClientDescription.from_binary(data)
            data = self.ServerUri.from_binary(data)
            data = self.EndpointUrl.from_binary(data)
            data = self.SessionName.from_binary(data)
            data = self.ClientNonce.from_binary(data)
            data = self.ClientCertificate.from_binary(data)
            self.RequestedSessionTimeout = struct.unpack(self._RequestedSessionTimeout_fmt, data.read(self._RequestedSessionTimeout_fmt_size))
            self.MaxResponseMessageSize = struct.unpack(self._MaxResponseMessageSize_fmt, data.read(self._MaxResponseMessageSize_fmt_size))
            return data
            
class CreateSessionResponse(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.ResponseHeader = None
        self.SessionId = None
        self.AuthenticationToken = None
        self.RevisedSessionTimeout = None
        self._RevisedSessionTimeout_fmt = '!d'
        self._RevisedSessionTimeout_fmt_size = 8
        self.ServerNonce = None
        self.ServerCertificate = None
        self.ServerEndpoints = []
        self.ServerSoftwareCertificates = []
        self.ServerSignature = None
        self.MaxRequestMessageSize = None
        self._MaxRequestMessageSize_fmt = '!I'
        self._MaxRequestMessageSize_fmt_size = 4
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.ResponseHeader.to_binary())
        tmp.append(self.SessionId.to_binary())
        tmp.append(self.AuthenticationToken.to_binary())
        tmp.append(struct.pack(self._RevisedSessionTimeout_fmt, self.RevisedSessionTimeout))
        tmp.append(self.ServerNonce.to_binary())
        tmp.append(self.ServerCertificate.to_binary())
        tmp.append(struct.pack('!i', len(self.ServerEndpoints)))
        for i in ServerEndpoints:
            tmp.append(self.ServerEndpoints.to_binary())
        tmp.append(struct.pack('!i', len(self.ServerSoftwareCertificates)))
        for i in ServerSoftwareCertificates:
            tmp.append(self.ServerSoftwareCertificates.to_binary())
        tmp.append(self.ServerSignature.to_binary())
        tmp.append(struct.pack(self._MaxRequestMessageSize_fmt, self.MaxRequestMessageSize))
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.ResponseHeader.from_binary(data)
            data = self.SessionId.from_binary(data)
            data = self.AuthenticationToken.from_binary(data)
            self.RevisedSessionTimeout = struct.unpack(self._RevisedSessionTimeout_fmt, data.read(self._RevisedSessionTimeout_fmt_size))
            data = self.ServerNonce.from_binary(data)
            data = self.ServerCertificate.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.ServerEndpoints.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.ServerSoftwareCertificates.from_binary(data)
            data = self.ServerSignature.from_binary(data)
            self.MaxRequestMessageSize = struct.unpack(self._MaxRequestMessageSize_fmt, data.read(self._MaxRequestMessageSize_fmt_size))
            return data
            
class UserIdentityToken(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.PolicyId = None
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.PolicyId.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.PolicyId.from_binary(data)
            return data
            
class AnonymousIdentityToken(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.PolicyId = None
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.PolicyId.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.PolicyId.from_binary(data)
            return data
            
class UserNameIdentityToken(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.PolicyId = None
        self.UserName = None
        self.Password = None
        self.EncryptionAlgorithm = None
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.PolicyId.to_binary())
        tmp.append(self.UserName.to_binary())
        tmp.append(self.Password.to_binary())
        tmp.append(self.EncryptionAlgorithm.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.PolicyId.from_binary(data)
            data = self.UserName.from_binary(data)
            data = self.Password.from_binary(data)
            data = self.EncryptionAlgorithm.from_binary(data)
            return data
            
class X509IdentityToken(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.PolicyId = None
        self.CertificateData = None
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.PolicyId.to_binary())
        tmp.append(self.CertificateData.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.PolicyId.from_binary(data)
            data = self.CertificateData.from_binary(data)
            return data
            
class IssuedIdentityToken(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.PolicyId = None
        self.TokenData = None
        self.EncryptionAlgorithm = None
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.PolicyId.to_binary())
        tmp.append(self.TokenData.to_binary())
        tmp.append(self.EncryptionAlgorithm.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.PolicyId.from_binary(data)
            data = self.TokenData.from_binary(data)
            data = self.EncryptionAlgorithm.from_binary(data)
            return data
            
class ActivateSessionRequest(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.RequestHeader = None
        self.ClientSignature = None
        self.ClientSoftwareCertificates = []
        self.LocaleIds = []
        self.UserIdentityToken = None
        self.UserTokenSignature = None
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.RequestHeader.to_binary())
        tmp.append(self.ClientSignature.to_binary())
        tmp.append(struct.pack('!i', len(self.ClientSoftwareCertificates)))
        for i in ClientSoftwareCertificates:
            tmp.append(self.ClientSoftwareCertificates.to_binary())
        tmp.append(struct.pack('!i', len(self.LocaleIds)))
        for i in LocaleIds:
            tmp.append(self.LocaleIds.to_binary())
        tmp.append(self.UserIdentityToken.to_binary())
        tmp.append(self.UserTokenSignature.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.RequestHeader.from_binary(data)
            data = self.ClientSignature.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.ClientSoftwareCertificates.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.LocaleIds.from_binary(data)
            data = self.UserIdentityToken.from_binary(data)
            data = self.UserTokenSignature.from_binary(data)
            return data
            
class ActivateSessionResponse(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.ResponseHeader = None
        self.ServerNonce = None
        self.Results = []
        self.DiagnosticInfos = []
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.ResponseHeader.to_binary())
        tmp.append(self.ServerNonce.to_binary())
        tmp.append(struct.pack('!i', len(self.Results)))
        for i in Results:
            tmp.append(self.Results.to_binary())
        tmp.append(struct.pack('!i', len(self.DiagnosticInfos)))
        for i in DiagnosticInfos:
            tmp.append(self.DiagnosticInfos.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.ResponseHeader.from_binary(data)
            data = self.ServerNonce.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.Results.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.DiagnosticInfos.from_binary(data)
            return data
            
class CloseSessionRequest(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.RequestHeader = None
        self.DeleteSubscriptions = None
        self._DeleteSubscriptions_fmt = '!?'
        self._DeleteSubscriptions_fmt_size = 1
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.RequestHeader.to_binary())
        tmp.append(struct.pack(self._DeleteSubscriptions_fmt, self.DeleteSubscriptions))
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.RequestHeader.from_binary(data)
            self.DeleteSubscriptions = struct.unpack(self._DeleteSubscriptions_fmt, data.read(self._DeleteSubscriptions_fmt_size))
            return data
            
class CloseSessionResponse(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.ResponseHeader = None
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.ResponseHeader.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.ResponseHeader.from_binary(data)
            return data
            
class CancelRequest(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.RequestHeader = None
        self.RequestHandle = None
        self._RequestHandle_fmt = '!I'
        self._RequestHandle_fmt_size = 4
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.RequestHeader.to_binary())
        tmp.append(struct.pack(self._RequestHandle_fmt, self.RequestHandle))
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.RequestHeader.from_binary(data)
            self.RequestHandle = struct.unpack(self._RequestHandle_fmt, data.read(self._RequestHandle_fmt_size))
            return data
            
class CancelResponse(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.ResponseHeader = None
        self.CancelCount = None
        self._CancelCount_fmt = '!I'
        self._CancelCount_fmt_size = 4
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.ResponseHeader.to_binary())
        tmp.append(struct.pack(self._CancelCount_fmt, self.CancelCount))
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.ResponseHeader.from_binary(data)
            self.CancelCount = struct.unpack(self._CancelCount_fmt, data.read(self._CancelCount_fmt_size))
            return data
            
class NodeAttributes(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.SpecifiedAttributes = None
        self._SpecifiedAttributes_fmt = '!I'
        self._SpecifiedAttributes_fmt_size = 4
        self.DisplayName = None
        self.Description = None
        self.WriteMask = None
        self._WriteMask_fmt = '!I'
        self._WriteMask_fmt_size = 4
        self.UserWriteMask = None
        self._UserWriteMask_fmt = '!I'
        self._UserWriteMask_fmt_size = 4
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(struct.pack(self._SpecifiedAttributes_fmt, self.SpecifiedAttributes))
        tmp.append(self.DisplayName.to_binary())
        tmp.append(self.Description.to_binary())
        tmp.append(struct.pack(self._WriteMask_fmt, self.WriteMask))
        tmp.append(struct.pack(self._UserWriteMask_fmt, self.UserWriteMask))
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            self.SpecifiedAttributes = struct.unpack(self._SpecifiedAttributes_fmt, data.read(self._SpecifiedAttributes_fmt_size))
            data = self.DisplayName.from_binary(data)
            data = self.Description.from_binary(data)
            self.WriteMask = struct.unpack(self._WriteMask_fmt, data.read(self._WriteMask_fmt_size))
            self.UserWriteMask = struct.unpack(self._UserWriteMask_fmt, data.read(self._UserWriteMask_fmt_size))
            return data
            
class ObjectAttributes(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.SpecifiedAttributes = None
        self._SpecifiedAttributes_fmt = '!I'
        self._SpecifiedAttributes_fmt_size = 4
        self.DisplayName = None
        self.Description = None
        self.WriteMask = None
        self._WriteMask_fmt = '!I'
        self._WriteMask_fmt_size = 4
        self.UserWriteMask = None
        self._UserWriteMask_fmt = '!I'
        self._UserWriteMask_fmt_size = 4
        self.EventNotifier = None
        self._EventNotifier_fmt = '!c'
        self._EventNotifier_fmt_size = 1
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(struct.pack(self._SpecifiedAttributes_fmt, self.SpecifiedAttributes))
        tmp.append(self.DisplayName.to_binary())
        tmp.append(self.Description.to_binary())
        tmp.append(struct.pack(self._WriteMask_fmt, self.WriteMask))
        tmp.append(struct.pack(self._UserWriteMask_fmt, self.UserWriteMask))
        tmp.append(struct.pack(self._EventNotifier_fmt, self.EventNotifier))
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            self.SpecifiedAttributes = struct.unpack(self._SpecifiedAttributes_fmt, data.read(self._SpecifiedAttributes_fmt_size))
            data = self.DisplayName.from_binary(data)
            data = self.Description.from_binary(data)
            self.WriteMask = struct.unpack(self._WriteMask_fmt, data.read(self._WriteMask_fmt_size))
            self.UserWriteMask = struct.unpack(self._UserWriteMask_fmt, data.read(self._UserWriteMask_fmt_size))
            self.EventNotifier = struct.unpack(self._EventNotifier_fmt, data.read(self._EventNotifier_fmt_size))
            return data
            
class VariableAttributes(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.SpecifiedAttributes = None
        self._SpecifiedAttributes_fmt = '!I'
        self._SpecifiedAttributes_fmt_size = 4
        self.DisplayName = None
        self.Description = None
        self.WriteMask = None
        self._WriteMask_fmt = '!I'
        self._WriteMask_fmt_size = 4
        self.UserWriteMask = None
        self._UserWriteMask_fmt = '!I'
        self._UserWriteMask_fmt_size = 4
        self.Value = None
        self.DataType = None
        self.ValueRank = None
        self._ValueRank_fmt = '!i'
        self._ValueRank_fmt_size = 4
        self.ArrayDimensions = []
        self._ArrayDimensions_fmt = '!I'
        self._ArrayDimensions_fmt_size = 4
        self.AccessLevel = None
        self._AccessLevel_fmt = '!c'
        self._AccessLevel_fmt_size = 1
        self.UserAccessLevel = None
        self._UserAccessLevel_fmt = '!c'
        self._UserAccessLevel_fmt_size = 1
        self.MinimumSamplingInterval = None
        self._MinimumSamplingInterval_fmt = '!d'
        self._MinimumSamplingInterval_fmt_size = 8
        self.Historizing = None
        self._Historizing_fmt = '!?'
        self._Historizing_fmt_size = 1
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(struct.pack(self._SpecifiedAttributes_fmt, self.SpecifiedAttributes))
        tmp.append(self.DisplayName.to_binary())
        tmp.append(self.Description.to_binary())
        tmp.append(struct.pack(self._WriteMask_fmt, self.WriteMask))
        tmp.append(struct.pack(self._UserWriteMask_fmt, self.UserWriteMask))
        tmp.append(self.Value.to_binary())
        tmp.append(self.DataType.to_binary())
        tmp.append(struct.pack(self._ValueRank_fmt, self.ValueRank))
        tmp.append(struct.pack('!i', len(self.ArrayDimensions)))
        for i in ArrayDimensions:
            tmp.append(struct.pack(self._ArrayDimensions_fmt, self.ArrayDimensions))
        tmp.append(struct.pack(self._AccessLevel_fmt, self.AccessLevel))
        tmp.append(struct.pack(self._UserAccessLevel_fmt, self.UserAccessLevel))
        tmp.append(struct.pack(self._MinimumSamplingInterval_fmt, self.MinimumSamplingInterval))
        tmp.append(struct.pack(self._Historizing_fmt, self.Historizing))
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            self.SpecifiedAttributes = struct.unpack(self._SpecifiedAttributes_fmt, data.read(self._SpecifiedAttributes_fmt_size))
            data = self.DisplayName.from_binary(data)
            data = self.Description.from_binary(data)
            self.WriteMask = struct.unpack(self._WriteMask_fmt, data.read(self._WriteMask_fmt_size))
            self.UserWriteMask = struct.unpack(self._UserWriteMask_fmt, data.read(self._UserWriteMask_fmt_size))
            data = self.Value.from_binary(data)
            data = self.DataType.from_binary(data)
            self.ValueRank = struct.unpack(self._ValueRank_fmt, data.read(self._ValueRank_fmt_size))
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    self.ArrayDimensions = struct.unpack(self._ArrayDimensions_fmt, data.read(self._ArrayDimensions_fmt_size))
            self.AccessLevel = struct.unpack(self._AccessLevel_fmt, data.read(self._AccessLevel_fmt_size))
            self.UserAccessLevel = struct.unpack(self._UserAccessLevel_fmt, data.read(self._UserAccessLevel_fmt_size))
            self.MinimumSamplingInterval = struct.unpack(self._MinimumSamplingInterval_fmt, data.read(self._MinimumSamplingInterval_fmt_size))
            self.Historizing = struct.unpack(self._Historizing_fmt, data.read(self._Historizing_fmt_size))
            return data
            
class MethodAttributes(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.SpecifiedAttributes = None
        self._SpecifiedAttributes_fmt = '!I'
        self._SpecifiedAttributes_fmt_size = 4
        self.DisplayName = None
        self.Description = None
        self.WriteMask = None
        self._WriteMask_fmt = '!I'
        self._WriteMask_fmt_size = 4
        self.UserWriteMask = None
        self._UserWriteMask_fmt = '!I'
        self._UserWriteMask_fmt_size = 4
        self.Executable = None
        self._Executable_fmt = '!?'
        self._Executable_fmt_size = 1
        self.UserExecutable = None
        self._UserExecutable_fmt = '!?'
        self._UserExecutable_fmt_size = 1
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(struct.pack(self._SpecifiedAttributes_fmt, self.SpecifiedAttributes))
        tmp.append(self.DisplayName.to_binary())
        tmp.append(self.Description.to_binary())
        tmp.append(struct.pack(self._WriteMask_fmt, self.WriteMask))
        tmp.append(struct.pack(self._UserWriteMask_fmt, self.UserWriteMask))
        tmp.append(struct.pack(self._Executable_fmt, self.Executable))
        tmp.append(struct.pack(self._UserExecutable_fmt, self.UserExecutable))
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            self.SpecifiedAttributes = struct.unpack(self._SpecifiedAttributes_fmt, data.read(self._SpecifiedAttributes_fmt_size))
            data = self.DisplayName.from_binary(data)
            data = self.Description.from_binary(data)
            self.WriteMask = struct.unpack(self._WriteMask_fmt, data.read(self._WriteMask_fmt_size))
            self.UserWriteMask = struct.unpack(self._UserWriteMask_fmt, data.read(self._UserWriteMask_fmt_size))
            self.Executable = struct.unpack(self._Executable_fmt, data.read(self._Executable_fmt_size))
            self.UserExecutable = struct.unpack(self._UserExecutable_fmt, data.read(self._UserExecutable_fmt_size))
            return data
            
class ObjectTypeAttributes(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.SpecifiedAttributes = None
        self._SpecifiedAttributes_fmt = '!I'
        self._SpecifiedAttributes_fmt_size = 4
        self.DisplayName = None
        self.Description = None
        self.WriteMask = None
        self._WriteMask_fmt = '!I'
        self._WriteMask_fmt_size = 4
        self.UserWriteMask = None
        self._UserWriteMask_fmt = '!I'
        self._UserWriteMask_fmt_size = 4
        self.IsAbstract = None
        self._IsAbstract_fmt = '!?'
        self._IsAbstract_fmt_size = 1
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(struct.pack(self._SpecifiedAttributes_fmt, self.SpecifiedAttributes))
        tmp.append(self.DisplayName.to_binary())
        tmp.append(self.Description.to_binary())
        tmp.append(struct.pack(self._WriteMask_fmt, self.WriteMask))
        tmp.append(struct.pack(self._UserWriteMask_fmt, self.UserWriteMask))
        tmp.append(struct.pack(self._IsAbstract_fmt, self.IsAbstract))
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            self.SpecifiedAttributes = struct.unpack(self._SpecifiedAttributes_fmt, data.read(self._SpecifiedAttributes_fmt_size))
            data = self.DisplayName.from_binary(data)
            data = self.Description.from_binary(data)
            self.WriteMask = struct.unpack(self._WriteMask_fmt, data.read(self._WriteMask_fmt_size))
            self.UserWriteMask = struct.unpack(self._UserWriteMask_fmt, data.read(self._UserWriteMask_fmt_size))
            self.IsAbstract = struct.unpack(self._IsAbstract_fmt, data.read(self._IsAbstract_fmt_size))
            return data
            
class VariableTypeAttributes(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.SpecifiedAttributes = None
        self._SpecifiedAttributes_fmt = '!I'
        self._SpecifiedAttributes_fmt_size = 4
        self.DisplayName = None
        self.Description = None
        self.WriteMask = None
        self._WriteMask_fmt = '!I'
        self._WriteMask_fmt_size = 4
        self.UserWriteMask = None
        self._UserWriteMask_fmt = '!I'
        self._UserWriteMask_fmt_size = 4
        self.Value = None
        self.DataType = None
        self.ValueRank = None
        self._ValueRank_fmt = '!i'
        self._ValueRank_fmt_size = 4
        self.ArrayDimensions = []
        self._ArrayDimensions_fmt = '!I'
        self._ArrayDimensions_fmt_size = 4
        self.IsAbstract = None
        self._IsAbstract_fmt = '!?'
        self._IsAbstract_fmt_size = 1
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(struct.pack(self._SpecifiedAttributes_fmt, self.SpecifiedAttributes))
        tmp.append(self.DisplayName.to_binary())
        tmp.append(self.Description.to_binary())
        tmp.append(struct.pack(self._WriteMask_fmt, self.WriteMask))
        tmp.append(struct.pack(self._UserWriteMask_fmt, self.UserWriteMask))
        tmp.append(self.Value.to_binary())
        tmp.append(self.DataType.to_binary())
        tmp.append(struct.pack(self._ValueRank_fmt, self.ValueRank))
        tmp.append(struct.pack('!i', len(self.ArrayDimensions)))
        for i in ArrayDimensions:
            tmp.append(struct.pack(self._ArrayDimensions_fmt, self.ArrayDimensions))
        tmp.append(struct.pack(self._IsAbstract_fmt, self.IsAbstract))
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            self.SpecifiedAttributes = struct.unpack(self._SpecifiedAttributes_fmt, data.read(self._SpecifiedAttributes_fmt_size))
            data = self.DisplayName.from_binary(data)
            data = self.Description.from_binary(data)
            self.WriteMask = struct.unpack(self._WriteMask_fmt, data.read(self._WriteMask_fmt_size))
            self.UserWriteMask = struct.unpack(self._UserWriteMask_fmt, data.read(self._UserWriteMask_fmt_size))
            data = self.Value.from_binary(data)
            data = self.DataType.from_binary(data)
            self.ValueRank = struct.unpack(self._ValueRank_fmt, data.read(self._ValueRank_fmt_size))
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    self.ArrayDimensions = struct.unpack(self._ArrayDimensions_fmt, data.read(self._ArrayDimensions_fmt_size))
            self.IsAbstract = struct.unpack(self._IsAbstract_fmt, data.read(self._IsAbstract_fmt_size))
            return data
            
class ReferenceTypeAttributes(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.SpecifiedAttributes = None
        self._SpecifiedAttributes_fmt = '!I'
        self._SpecifiedAttributes_fmt_size = 4
        self.DisplayName = None
        self.Description = None
        self.WriteMask = None
        self._WriteMask_fmt = '!I'
        self._WriteMask_fmt_size = 4
        self.UserWriteMask = None
        self._UserWriteMask_fmt = '!I'
        self._UserWriteMask_fmt_size = 4
        self.IsAbstract = None
        self._IsAbstract_fmt = '!?'
        self._IsAbstract_fmt_size = 1
        self.Symmetric = None
        self._Symmetric_fmt = '!?'
        self._Symmetric_fmt_size = 1
        self.InverseName = None
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(struct.pack(self._SpecifiedAttributes_fmt, self.SpecifiedAttributes))
        tmp.append(self.DisplayName.to_binary())
        tmp.append(self.Description.to_binary())
        tmp.append(struct.pack(self._WriteMask_fmt, self.WriteMask))
        tmp.append(struct.pack(self._UserWriteMask_fmt, self.UserWriteMask))
        tmp.append(struct.pack(self._IsAbstract_fmt, self.IsAbstract))
        tmp.append(struct.pack(self._Symmetric_fmt, self.Symmetric))
        tmp.append(self.InverseName.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            self.SpecifiedAttributes = struct.unpack(self._SpecifiedAttributes_fmt, data.read(self._SpecifiedAttributes_fmt_size))
            data = self.DisplayName.from_binary(data)
            data = self.Description.from_binary(data)
            self.WriteMask = struct.unpack(self._WriteMask_fmt, data.read(self._WriteMask_fmt_size))
            self.UserWriteMask = struct.unpack(self._UserWriteMask_fmt, data.read(self._UserWriteMask_fmt_size))
            self.IsAbstract = struct.unpack(self._IsAbstract_fmt, data.read(self._IsAbstract_fmt_size))
            self.Symmetric = struct.unpack(self._Symmetric_fmt, data.read(self._Symmetric_fmt_size))
            data = self.InverseName.from_binary(data)
            return data
            
class DataTypeAttributes(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.SpecifiedAttributes = None
        self._SpecifiedAttributes_fmt = '!I'
        self._SpecifiedAttributes_fmt_size = 4
        self.DisplayName = None
        self.Description = None
        self.WriteMask = None
        self._WriteMask_fmt = '!I'
        self._WriteMask_fmt_size = 4
        self.UserWriteMask = None
        self._UserWriteMask_fmt = '!I'
        self._UserWriteMask_fmt_size = 4
        self.IsAbstract = None
        self._IsAbstract_fmt = '!?'
        self._IsAbstract_fmt_size = 1
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(struct.pack(self._SpecifiedAttributes_fmt, self.SpecifiedAttributes))
        tmp.append(self.DisplayName.to_binary())
        tmp.append(self.Description.to_binary())
        tmp.append(struct.pack(self._WriteMask_fmt, self.WriteMask))
        tmp.append(struct.pack(self._UserWriteMask_fmt, self.UserWriteMask))
        tmp.append(struct.pack(self._IsAbstract_fmt, self.IsAbstract))
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            self.SpecifiedAttributes = struct.unpack(self._SpecifiedAttributes_fmt, data.read(self._SpecifiedAttributes_fmt_size))
            data = self.DisplayName.from_binary(data)
            data = self.Description.from_binary(data)
            self.WriteMask = struct.unpack(self._WriteMask_fmt, data.read(self._WriteMask_fmt_size))
            self.UserWriteMask = struct.unpack(self._UserWriteMask_fmt, data.read(self._UserWriteMask_fmt_size))
            self.IsAbstract = struct.unpack(self._IsAbstract_fmt, data.read(self._IsAbstract_fmt_size))
            return data
            
class ViewAttributes(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.SpecifiedAttributes = None
        self._SpecifiedAttributes_fmt = '!I'
        self._SpecifiedAttributes_fmt_size = 4
        self.DisplayName = None
        self.Description = None
        self.WriteMask = None
        self._WriteMask_fmt = '!I'
        self._WriteMask_fmt_size = 4
        self.UserWriteMask = None
        self._UserWriteMask_fmt = '!I'
        self._UserWriteMask_fmt_size = 4
        self.ContainsNoLoops = None
        self._ContainsNoLoops_fmt = '!?'
        self._ContainsNoLoops_fmt_size = 1
        self.EventNotifier = None
        self._EventNotifier_fmt = '!c'
        self._EventNotifier_fmt_size = 1
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(struct.pack(self._SpecifiedAttributes_fmt, self.SpecifiedAttributes))
        tmp.append(self.DisplayName.to_binary())
        tmp.append(self.Description.to_binary())
        tmp.append(struct.pack(self._WriteMask_fmt, self.WriteMask))
        tmp.append(struct.pack(self._UserWriteMask_fmt, self.UserWriteMask))
        tmp.append(struct.pack(self._ContainsNoLoops_fmt, self.ContainsNoLoops))
        tmp.append(struct.pack(self._EventNotifier_fmt, self.EventNotifier))
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            self.SpecifiedAttributes = struct.unpack(self._SpecifiedAttributes_fmt, data.read(self._SpecifiedAttributes_fmt_size))
            data = self.DisplayName.from_binary(data)
            data = self.Description.from_binary(data)
            self.WriteMask = struct.unpack(self._WriteMask_fmt, data.read(self._WriteMask_fmt_size))
            self.UserWriteMask = struct.unpack(self._UserWriteMask_fmt, data.read(self._UserWriteMask_fmt_size))
            self.ContainsNoLoops = struct.unpack(self._ContainsNoLoops_fmt, data.read(self._ContainsNoLoops_fmt_size))
            self.EventNotifier = struct.unpack(self._EventNotifier_fmt, data.read(self._EventNotifier_fmt_size))
            return data
            
class AddNodesItem(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.ParentNodeId = None
        self.ReferenceTypeId = None
        self.RequestedNewNodeId = None
        self.BrowseName = None
        self.NodeClass = None
        self.NodeAttributes = None
        self.TypeDefinition = None
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.ParentNodeId.to_binary())
        tmp.append(self.ReferenceTypeId.to_binary())
        tmp.append(self.RequestedNewNodeId.to_binary())
        tmp.append(self.BrowseName.to_binary())
        tmp.append(self.NodeClass.to_binary())
        tmp.append(self.NodeAttributes.to_binary())
        tmp.append(self.TypeDefinition.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
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
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.StatusCode = None
        self.AddedNodeId = None
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.StatusCode.to_binary())
        tmp.append(self.AddedNodeId.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.StatusCode.from_binary(data)
            data = self.AddedNodeId.from_binary(data)
            return data
            
class AddNodesRequest(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.RequestHeader = None
        self.NodesToAdd = []
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.RequestHeader.to_binary())
        tmp.append(struct.pack('!i', len(self.NodesToAdd)))
        for i in NodesToAdd:
            tmp.append(self.NodesToAdd.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.RequestHeader.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.NodesToAdd.from_binary(data)
            return data
            
class AddNodesResponse(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.ResponseHeader = None
        self.Results = []
        self.DiagnosticInfos = []
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.ResponseHeader.to_binary())
        tmp.append(struct.pack('!i', len(self.Results)))
        for i in Results:
            tmp.append(self.Results.to_binary())
        tmp.append(struct.pack('!i', len(self.DiagnosticInfos)))
        for i in DiagnosticInfos:
            tmp.append(self.DiagnosticInfos.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.ResponseHeader.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.Results.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.DiagnosticInfos.from_binary(data)
            return data
            
class AddReferencesItem(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.SourceNodeId = None
        self.ReferenceTypeId = None
        self.IsForward = None
        self._IsForward_fmt = '!?'
        self._IsForward_fmt_size = 1
        self.TargetServerUri = None
        self.TargetNodeId = None
        self.TargetNodeClass = None
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.SourceNodeId.to_binary())
        tmp.append(self.ReferenceTypeId.to_binary())
        tmp.append(struct.pack(self._IsForward_fmt, self.IsForward))
        tmp.append(self.TargetServerUri.to_binary())
        tmp.append(self.TargetNodeId.to_binary())
        tmp.append(self.TargetNodeClass.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.SourceNodeId.from_binary(data)
            data = self.ReferenceTypeId.from_binary(data)
            self.IsForward = struct.unpack(self._IsForward_fmt, data.read(self._IsForward_fmt_size))
            data = self.TargetServerUri.from_binary(data)
            data = self.TargetNodeId.from_binary(data)
            data = self.TargetNodeClass.from_binary(data)
            return data
            
class AddReferencesRequest(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.RequestHeader = None
        self.ReferencesToAdd = []
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.RequestHeader.to_binary())
        tmp.append(struct.pack('!i', len(self.ReferencesToAdd)))
        for i in ReferencesToAdd:
            tmp.append(self.ReferencesToAdd.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.RequestHeader.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.ReferencesToAdd.from_binary(data)
            return data
            
class AddReferencesResponse(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.ResponseHeader = None
        self.Results = []
        self.DiagnosticInfos = []
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.ResponseHeader.to_binary())
        tmp.append(struct.pack('!i', len(self.Results)))
        for i in Results:
            tmp.append(self.Results.to_binary())
        tmp.append(struct.pack('!i', len(self.DiagnosticInfos)))
        for i in DiagnosticInfos:
            tmp.append(self.DiagnosticInfos.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.ResponseHeader.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.Results.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.DiagnosticInfos.from_binary(data)
            return data
            
class DeleteNodesItem(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.NodeId = None
        self.DeleteTargetReferences = None
        self._DeleteTargetReferences_fmt = '!?'
        self._DeleteTargetReferences_fmt_size = 1
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.NodeId.to_binary())
        tmp.append(struct.pack(self._DeleteTargetReferences_fmt, self.DeleteTargetReferences))
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.NodeId.from_binary(data)
            self.DeleteTargetReferences = struct.unpack(self._DeleteTargetReferences_fmt, data.read(self._DeleteTargetReferences_fmt_size))
            return data
            
class DeleteNodesRequest(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.RequestHeader = None
        self.NodesToDelete = []
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.RequestHeader.to_binary())
        tmp.append(struct.pack('!i', len(self.NodesToDelete)))
        for i in NodesToDelete:
            tmp.append(self.NodesToDelete.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.RequestHeader.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.NodesToDelete.from_binary(data)
            return data
            
class DeleteNodesResponse(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.ResponseHeader = None
        self.Results = []
        self.DiagnosticInfos = []
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.ResponseHeader.to_binary())
        tmp.append(struct.pack('!i', len(self.Results)))
        for i in Results:
            tmp.append(self.Results.to_binary())
        tmp.append(struct.pack('!i', len(self.DiagnosticInfos)))
        for i in DiagnosticInfos:
            tmp.append(self.DiagnosticInfos.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.ResponseHeader.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.Results.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.DiagnosticInfos.from_binary(data)
            return data
            
class DeleteReferencesItem(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.SourceNodeId = None
        self.ReferenceTypeId = None
        self.IsForward = None
        self._IsForward_fmt = '!?'
        self._IsForward_fmt_size = 1
        self.TargetNodeId = None
        self.DeleteBidirectional = None
        self._DeleteBidirectional_fmt = '!?'
        self._DeleteBidirectional_fmt_size = 1
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.SourceNodeId.to_binary())
        tmp.append(self.ReferenceTypeId.to_binary())
        tmp.append(struct.pack(self._IsForward_fmt, self.IsForward))
        tmp.append(self.TargetNodeId.to_binary())
        tmp.append(struct.pack(self._DeleteBidirectional_fmt, self.DeleteBidirectional))
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.SourceNodeId.from_binary(data)
            data = self.ReferenceTypeId.from_binary(data)
            self.IsForward = struct.unpack(self._IsForward_fmt, data.read(self._IsForward_fmt_size))
            data = self.TargetNodeId.from_binary(data)
            self.DeleteBidirectional = struct.unpack(self._DeleteBidirectional_fmt, data.read(self._DeleteBidirectional_fmt_size))
            return data
            
class DeleteReferencesRequest(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.RequestHeader = None
        self.ReferencesToDelete = []
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.RequestHeader.to_binary())
        tmp.append(struct.pack('!i', len(self.ReferencesToDelete)))
        for i in ReferencesToDelete:
            tmp.append(self.ReferencesToDelete.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.RequestHeader.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.ReferencesToDelete.from_binary(data)
            return data
            
class DeleteReferencesResponse(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.ResponseHeader = None
        self.Results = []
        self.DiagnosticInfos = []
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.ResponseHeader.to_binary())
        tmp.append(struct.pack('!i', len(self.Results)))
        for i in Results:
            tmp.append(self.Results.to_binary())
        tmp.append(struct.pack('!i', len(self.DiagnosticInfos)))
        for i in DiagnosticInfos:
            tmp.append(self.DiagnosticInfos.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.ResponseHeader.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.Results.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.DiagnosticInfos.from_binary(data)
            return data
            
class ViewDescription(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.ViewId = None
        self.Timestamp = None
        self._Timestamp_fmt = '!d'
        self._Timestamp_fmt_size = 8
        self.ViewVersion = None
        self._ViewVersion_fmt = '!I'
        self._ViewVersion_fmt_size = 4
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.ViewId.to_binary())
        tmp.append(struct.pack(self._Timestamp_fmt, self.Timestamp))
        tmp.append(struct.pack(self._ViewVersion_fmt, self.ViewVersion))
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.ViewId.from_binary(data)
            self.Timestamp = struct.unpack(self._Timestamp_fmt, data.read(self._Timestamp_fmt_size))
            self.ViewVersion = struct.unpack(self._ViewVersion_fmt, data.read(self._ViewVersion_fmt_size))
            return data
            
class BrowseDescription(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.NodeId = None
        self.BrowseDirection = None
        self.ReferenceTypeId = None
        self.IncludeSubtypes = None
        self._IncludeSubtypes_fmt = '!?'
        self._IncludeSubtypes_fmt_size = 1
        self.NodeClassMask = None
        self._NodeClassMask_fmt = '!I'
        self._NodeClassMask_fmt_size = 4
        self.ResultMask = None
        self._ResultMask_fmt = '!I'
        self._ResultMask_fmt_size = 4
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.NodeId.to_binary())
        tmp.append(self.BrowseDirection.to_binary())
        tmp.append(self.ReferenceTypeId.to_binary())
        tmp.append(struct.pack(self._IncludeSubtypes_fmt, self.IncludeSubtypes))
        tmp.append(struct.pack(self._NodeClassMask_fmt, self.NodeClassMask))
        tmp.append(struct.pack(self._ResultMask_fmt, self.ResultMask))
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.NodeId.from_binary(data)
            data = self.BrowseDirection.from_binary(data)
            data = self.ReferenceTypeId.from_binary(data)
            self.IncludeSubtypes = struct.unpack(self._IncludeSubtypes_fmt, data.read(self._IncludeSubtypes_fmt_size))
            self.NodeClassMask = struct.unpack(self._NodeClassMask_fmt, data.read(self._NodeClassMask_fmt_size))
            self.ResultMask = struct.unpack(self._ResultMask_fmt, data.read(self._ResultMask_fmt_size))
            return data
            
class ReferenceDescription(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.ReferenceTypeId = None
        self.IsForward = None
        self._IsForward_fmt = '!?'
        self._IsForward_fmt_size = 1
        self.NodeId = None
        self.BrowseName = None
        self.DisplayName = None
        self.NodeClass = None
        self.TypeDefinition = None
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.ReferenceTypeId.to_binary())
        tmp.append(struct.pack(self._IsForward_fmt, self.IsForward))
        tmp.append(self.NodeId.to_binary())
        tmp.append(self.BrowseName.to_binary())
        tmp.append(self.DisplayName.to_binary())
        tmp.append(self.NodeClass.to_binary())
        tmp.append(self.TypeDefinition.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.ReferenceTypeId.from_binary(data)
            self.IsForward = struct.unpack(self._IsForward_fmt, data.read(self._IsForward_fmt_size))
            data = self.NodeId.from_binary(data)
            data = self.BrowseName.from_binary(data)
            data = self.DisplayName.from_binary(data)
            data = self.NodeClass.from_binary(data)
            data = self.TypeDefinition.from_binary(data)
            return data
            
class BrowseResult(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.StatusCode = None
        self.ContinuationPoint = None
        self.References = []
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.StatusCode.to_binary())
        tmp.append(self.ContinuationPoint.to_binary())
        tmp.append(struct.pack('!i', len(self.References)))
        for i in References:
            tmp.append(self.References.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.StatusCode.from_binary(data)
            data = self.ContinuationPoint.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.References.from_binary(data)
            return data
            
class BrowseRequest(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.RequestHeader = None
        self.View = None
        self.RequestedMaxReferencesPerNode = None
        self._RequestedMaxReferencesPerNode_fmt = '!I'
        self._RequestedMaxReferencesPerNode_fmt_size = 4
        self.NodesToBrowse = []
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.RequestHeader.to_binary())
        tmp.append(self.View.to_binary())
        tmp.append(struct.pack(self._RequestedMaxReferencesPerNode_fmt, self.RequestedMaxReferencesPerNode))
        tmp.append(struct.pack('!i', len(self.NodesToBrowse)))
        for i in NodesToBrowse:
            tmp.append(self.NodesToBrowse.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.RequestHeader.from_binary(data)
            data = self.View.from_binary(data)
            self.RequestedMaxReferencesPerNode = struct.unpack(self._RequestedMaxReferencesPerNode_fmt, data.read(self._RequestedMaxReferencesPerNode_fmt_size))
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.NodesToBrowse.from_binary(data)
            return data
            
class BrowseResponse(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.ResponseHeader = None
        self.Results = []
        self.DiagnosticInfos = []
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.ResponseHeader.to_binary())
        tmp.append(struct.pack('!i', len(self.Results)))
        for i in Results:
            tmp.append(self.Results.to_binary())
        tmp.append(struct.pack('!i', len(self.DiagnosticInfos)))
        for i in DiagnosticInfos:
            tmp.append(self.DiagnosticInfos.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.ResponseHeader.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.Results.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.DiagnosticInfos.from_binary(data)
            return data
            
class BrowseNextRequest(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.RequestHeader = None
        self.ReleaseContinuationPoints = None
        self._ReleaseContinuationPoints_fmt = '!?'
        self._ReleaseContinuationPoints_fmt_size = 1
        self.ContinuationPoints = []
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.RequestHeader.to_binary())
        tmp.append(struct.pack(self._ReleaseContinuationPoints_fmt, self.ReleaseContinuationPoints))
        tmp.append(struct.pack('!i', len(self.ContinuationPoints)))
        for i in ContinuationPoints:
            tmp.append(self.ContinuationPoints.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.RequestHeader.from_binary(data)
            self.ReleaseContinuationPoints = struct.unpack(self._ReleaseContinuationPoints_fmt, data.read(self._ReleaseContinuationPoints_fmt_size))
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.ContinuationPoints.from_binary(data)
            return data
            
class BrowseNextResponse(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.ResponseHeader = None
        self.Results = []
        self.DiagnosticInfos = []
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.ResponseHeader.to_binary())
        tmp.append(struct.pack('!i', len(self.Results)))
        for i in Results:
            tmp.append(self.Results.to_binary())
        tmp.append(struct.pack('!i', len(self.DiagnosticInfos)))
        for i in DiagnosticInfos:
            tmp.append(self.DiagnosticInfos.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.ResponseHeader.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.Results.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.DiagnosticInfos.from_binary(data)
            return data
            
class RelativePathElement(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.ReferenceTypeId = None
        self.IsInverse = None
        self._IsInverse_fmt = '!?'
        self._IsInverse_fmt_size = 1
        self.IncludeSubtypes = None
        self._IncludeSubtypes_fmt = '!?'
        self._IncludeSubtypes_fmt_size = 1
        self.TargetName = None
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.ReferenceTypeId.to_binary())
        tmp.append(struct.pack(self._IsInverse_fmt, self.IsInverse))
        tmp.append(struct.pack(self._IncludeSubtypes_fmt, self.IncludeSubtypes))
        tmp.append(self.TargetName.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.ReferenceTypeId.from_binary(data)
            self.IsInverse = struct.unpack(self._IsInverse_fmt, data.read(self._IsInverse_fmt_size))
            self.IncludeSubtypes = struct.unpack(self._IncludeSubtypes_fmt, data.read(self._IncludeSubtypes_fmt_size))
            data = self.TargetName.from_binary(data)
            return data
            
class RelativePath(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.Elements = []
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(struct.pack('!i', len(self.Elements)))
        for i in Elements:
            tmp.append(self.Elements.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.Elements.from_binary(data)
            return data
            
class BrowsePath(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.StartingNode = None
        self.RelativePath = None
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.StartingNode.to_binary())
        tmp.append(self.RelativePath.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.StartingNode.from_binary(data)
            data = self.RelativePath.from_binary(data)
            return data
            
class BrowsePathTarget(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.TargetId = None
        self.RemainingPathIndex = None
        self._RemainingPathIndex_fmt = '!I'
        self._RemainingPathIndex_fmt_size = 4
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.TargetId.to_binary())
        tmp.append(struct.pack(self._RemainingPathIndex_fmt, self.RemainingPathIndex))
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.TargetId.from_binary(data)
            self.RemainingPathIndex = struct.unpack(self._RemainingPathIndex_fmt, data.read(self._RemainingPathIndex_fmt_size))
            return data
            
class BrowsePathResult(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.StatusCode = None
        self.Targets = []
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.StatusCode.to_binary())
        tmp.append(struct.pack('!i', len(self.Targets)))
        for i in Targets:
            tmp.append(self.Targets.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.StatusCode.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.Targets.from_binary(data)
            return data
            
class TranslateBrowsePathsToNodeIdsRequest(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.RequestHeader = None
        self.BrowsePaths = []
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.RequestHeader.to_binary())
        tmp.append(struct.pack('!i', len(self.BrowsePaths)))
        for i in BrowsePaths:
            tmp.append(self.BrowsePaths.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.RequestHeader.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.BrowsePaths.from_binary(data)
            return data
            
class TranslateBrowsePathsToNodeIdsResponse(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.ResponseHeader = None
        self.Results = []
        self.DiagnosticInfos = []
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.ResponseHeader.to_binary())
        tmp.append(struct.pack('!i', len(self.Results)))
        for i in Results:
            tmp.append(self.Results.to_binary())
        tmp.append(struct.pack('!i', len(self.DiagnosticInfos)))
        for i in DiagnosticInfos:
            tmp.append(self.DiagnosticInfos.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.ResponseHeader.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.Results.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.DiagnosticInfos.from_binary(data)
            return data
            
class RegisterNodesRequest(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.RequestHeader = None
        self.NodesToRegister = []
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.RequestHeader.to_binary())
        tmp.append(struct.pack('!i', len(self.NodesToRegister)))
        for i in NodesToRegister:
            tmp.append(self.NodesToRegister.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.RequestHeader.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.NodesToRegister.from_binary(data)
            return data
            
class RegisterNodesResponse(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.ResponseHeader = None
        self.RegisteredNodeIds = []
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.ResponseHeader.to_binary())
        tmp.append(struct.pack('!i', len(self.RegisteredNodeIds)))
        for i in RegisteredNodeIds:
            tmp.append(self.RegisteredNodeIds.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.ResponseHeader.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.RegisteredNodeIds.from_binary(data)
            return data
            
class UnregisterNodesRequest(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.RequestHeader = None
        self.NodesToUnregister = []
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.RequestHeader.to_binary())
        tmp.append(struct.pack('!i', len(self.NodesToUnregister)))
        for i in NodesToUnregister:
            tmp.append(self.NodesToUnregister.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.RequestHeader.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.NodesToUnregister.from_binary(data)
            return data
            
class UnregisterNodesResponse(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.ResponseHeader = None
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.ResponseHeader.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.ResponseHeader.from_binary(data)
            return data
            
class EndpointConfiguration(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.OperationTimeout = None
        self._OperationTimeout_fmt = '!i'
        self._OperationTimeout_fmt_size = 4
        self.UseBinaryEncoding = None
        self._UseBinaryEncoding_fmt = '!?'
        self._UseBinaryEncoding_fmt_size = 1
        self.MaxStringLength = None
        self._MaxStringLength_fmt = '!i'
        self._MaxStringLength_fmt_size = 4
        self.MaxByteStringLength = None
        self._MaxByteStringLength_fmt = '!i'
        self._MaxByteStringLength_fmt_size = 4
        self.MaxArrayLength = None
        self._MaxArrayLength_fmt = '!i'
        self._MaxArrayLength_fmt_size = 4
        self.MaxMessageSize = None
        self._MaxMessageSize_fmt = '!i'
        self._MaxMessageSize_fmt_size = 4
        self.MaxBufferSize = None
        self._MaxBufferSize_fmt = '!i'
        self._MaxBufferSize_fmt_size = 4
        self.ChannelLifetime = None
        self._ChannelLifetime_fmt = '!i'
        self._ChannelLifetime_fmt_size = 4
        self.SecurityTokenLifetime = None
        self._SecurityTokenLifetime_fmt = '!i'
        self._SecurityTokenLifetime_fmt_size = 4
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(struct.pack(self._OperationTimeout_fmt, self.OperationTimeout))
        tmp.append(struct.pack(self._UseBinaryEncoding_fmt, self.UseBinaryEncoding))
        tmp.append(struct.pack(self._MaxStringLength_fmt, self.MaxStringLength))
        tmp.append(struct.pack(self._MaxByteStringLength_fmt, self.MaxByteStringLength))
        tmp.append(struct.pack(self._MaxArrayLength_fmt, self.MaxArrayLength))
        tmp.append(struct.pack(self._MaxMessageSize_fmt, self.MaxMessageSize))
        tmp.append(struct.pack(self._MaxBufferSize_fmt, self.MaxBufferSize))
        tmp.append(struct.pack(self._ChannelLifetime_fmt, self.ChannelLifetime))
        tmp.append(struct.pack(self._SecurityTokenLifetime_fmt, self.SecurityTokenLifetime))
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            self.OperationTimeout = struct.unpack(self._OperationTimeout_fmt, data.read(self._OperationTimeout_fmt_size))
            self.UseBinaryEncoding = struct.unpack(self._UseBinaryEncoding_fmt, data.read(self._UseBinaryEncoding_fmt_size))
            self.MaxStringLength = struct.unpack(self._MaxStringLength_fmt, data.read(self._MaxStringLength_fmt_size))
            self.MaxByteStringLength = struct.unpack(self._MaxByteStringLength_fmt, data.read(self._MaxByteStringLength_fmt_size))
            self.MaxArrayLength = struct.unpack(self._MaxArrayLength_fmt, data.read(self._MaxArrayLength_fmt_size))
            self.MaxMessageSize = struct.unpack(self._MaxMessageSize_fmt, data.read(self._MaxMessageSize_fmt_size))
            self.MaxBufferSize = struct.unpack(self._MaxBufferSize_fmt, data.read(self._MaxBufferSize_fmt_size))
            self.ChannelLifetime = struct.unpack(self._ChannelLifetime_fmt, data.read(self._ChannelLifetime_fmt_size))
            self.SecurityTokenLifetime = struct.unpack(self._SecurityTokenLifetime_fmt, data.read(self._SecurityTokenLifetime_fmt_size))
            return data
            
class SupportedProfile(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.OrganizationUri = None
        self.ProfileId = None
        self.ComplianceTool = None
        self.ComplianceDate = None
        self._ComplianceDate_fmt = '!d'
        self._ComplianceDate_fmt_size = 8
        self.ComplianceLevel = None
        self.UnsupportedUnitIds = []
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.OrganizationUri.to_binary())
        tmp.append(self.ProfileId.to_binary())
        tmp.append(self.ComplianceTool.to_binary())
        tmp.append(struct.pack(self._ComplianceDate_fmt, self.ComplianceDate))
        tmp.append(self.ComplianceLevel.to_binary())
        tmp.append(struct.pack('!i', len(self.UnsupportedUnitIds)))
        for i in UnsupportedUnitIds:
            tmp.append(self.UnsupportedUnitIds.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.OrganizationUri.from_binary(data)
            data = self.ProfileId.from_binary(data)
            data = self.ComplianceTool.from_binary(data)
            self.ComplianceDate = struct.unpack(self._ComplianceDate_fmt, data.read(self._ComplianceDate_fmt_size))
            data = self.ComplianceLevel.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.UnsupportedUnitIds.from_binary(data)
            return data
            
class SoftwareCertificate(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.ProductName = None
        self.ProductUri = None
        self.VendorName = None
        self.VendorProductCertificate = None
        self.SoftwareVersion = None
        self.BuildNumber = None
        self.BuildDate = None
        self._BuildDate_fmt = '!d'
        self._BuildDate_fmt_size = 8
        self.IssuedBy = None
        self.IssueDate = None
        self._IssueDate_fmt = '!d'
        self._IssueDate_fmt_size = 8
        self.SupportedProfiles = []
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.ProductName.to_binary())
        tmp.append(self.ProductUri.to_binary())
        tmp.append(self.VendorName.to_binary())
        tmp.append(self.VendorProductCertificate.to_binary())
        tmp.append(self.SoftwareVersion.to_binary())
        tmp.append(self.BuildNumber.to_binary())
        tmp.append(struct.pack(self._BuildDate_fmt, self.BuildDate))
        tmp.append(self.IssuedBy.to_binary())
        tmp.append(struct.pack(self._IssueDate_fmt, self.IssueDate))
        tmp.append(struct.pack('!i', len(self.SupportedProfiles)))
        for i in SupportedProfiles:
            tmp.append(self.SupportedProfiles.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.ProductName.from_binary(data)
            data = self.ProductUri.from_binary(data)
            data = self.VendorName.from_binary(data)
            data = self.VendorProductCertificate.from_binary(data)
            data = self.SoftwareVersion.from_binary(data)
            data = self.BuildNumber.from_binary(data)
            self.BuildDate = struct.unpack(self._BuildDate_fmt, data.read(self._BuildDate_fmt_size))
            data = self.IssuedBy.from_binary(data)
            self.IssueDate = struct.unpack(self._IssueDate_fmt, data.read(self._IssueDate_fmt_size))
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.SupportedProfiles.from_binary(data)
            return data
            
class QueryDataDescription(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.RelativePath = None
        self.AttributeId = None
        self._AttributeId_fmt = '!I'
        self._AttributeId_fmt_size = 4
        self.IndexRange = None
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.RelativePath.to_binary())
        tmp.append(struct.pack(self._AttributeId_fmt, self.AttributeId))
        tmp.append(self.IndexRange.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.RelativePath.from_binary(data)
            self.AttributeId = struct.unpack(self._AttributeId_fmt, data.read(self._AttributeId_fmt_size))
            data = self.IndexRange.from_binary(data)
            return data
            
class NodeTypeDescription(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.TypeDefinitionNode = None
        self.IncludeSubTypes = None
        self._IncludeSubTypes_fmt = '!?'
        self._IncludeSubTypes_fmt_size = 1
        self.DataToReturn = []
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.TypeDefinitionNode.to_binary())
        tmp.append(struct.pack(self._IncludeSubTypes_fmt, self.IncludeSubTypes))
        tmp.append(struct.pack('!i', len(self.DataToReturn)))
        for i in DataToReturn:
            tmp.append(self.DataToReturn.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.TypeDefinitionNode.from_binary(data)
            self.IncludeSubTypes = struct.unpack(self._IncludeSubTypes_fmt, data.read(self._IncludeSubTypes_fmt_size))
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.DataToReturn.from_binary(data)
            return data
            
class QueryDataSet(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.NodeId = None
        self.TypeDefinitionNode = None
        self.Values = []
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.NodeId.to_binary())
        tmp.append(self.TypeDefinitionNode.to_binary())
        tmp.append(struct.pack('!i', len(self.Values)))
        for i in Values:
            tmp.append(self.Values.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.NodeId.from_binary(data)
            data = self.TypeDefinitionNode.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.Values.from_binary(data)
            return data
            
class NodeReference(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.NodeId = None
        self.ReferenceTypeId = None
        self.IsForward = None
        self._IsForward_fmt = '!?'
        self._IsForward_fmt_size = 1
        self.ReferencedNodeIds = []
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.NodeId.to_binary())
        tmp.append(self.ReferenceTypeId.to_binary())
        tmp.append(struct.pack(self._IsForward_fmt, self.IsForward))
        tmp.append(struct.pack('!i', len(self.ReferencedNodeIds)))
        for i in ReferencedNodeIds:
            tmp.append(self.ReferencedNodeIds.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.NodeId.from_binary(data)
            data = self.ReferenceTypeId.from_binary(data)
            self.IsForward = struct.unpack(self._IsForward_fmt, data.read(self._IsForward_fmt_size))
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.ReferencedNodeIds.from_binary(data)
            return data
            
class ContentFilterElement(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.FilterOperator = None
        self.FilterOperands = []
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.FilterOperator.to_binary())
        tmp.append(struct.pack('!i', len(self.FilterOperands)))
        for i in FilterOperands:
            tmp.append(self.FilterOperands.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.FilterOperator.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.FilterOperands.from_binary(data)
            return data
            
class ContentFilter(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.Elements = []
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(struct.pack('!i', len(self.Elements)))
        for i in Elements:
            tmp.append(self.Elements.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.Elements.from_binary(data)
            return data
            
class FilterOperand(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
        tmp.append(struct.pack('!i', len(self.Body)))
        for i in Body:
            tmp.append(struct.pack(self._Body_fmt, self.Body))
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    self.Body = struct.unpack(self._Body_fmt, data.read(self._Body_fmt_size))
            return data
            
class ElementOperand(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.Index = None
        self._Index_fmt = '!I'
        self._Index_fmt_size = 4
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(struct.pack(self._Index_fmt, self.Index))
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            self.Index = struct.unpack(self._Index_fmt, data.read(self._Index_fmt_size))
            return data
            
class LiteralOperand(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.Value = None
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.Value.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.Value.from_binary(data)
            return data
            
class AttributeOperand(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.NodeId = None
        self.Alias = None
        self.BrowsePath = None
        self.AttributeId = None
        self._AttributeId_fmt = '!I'
        self._AttributeId_fmt_size = 4
        self.IndexRange = None
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.NodeId.to_binary())
        tmp.append(self.Alias.to_binary())
        tmp.append(self.BrowsePath.to_binary())
        tmp.append(struct.pack(self._AttributeId_fmt, self.AttributeId))
        tmp.append(self.IndexRange.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.NodeId.from_binary(data)
            data = self.Alias.from_binary(data)
            data = self.BrowsePath.from_binary(data)
            self.AttributeId = struct.unpack(self._AttributeId_fmt, data.read(self._AttributeId_fmt_size))
            data = self.IndexRange.from_binary(data)
            return data
            
class SimpleAttributeOperand(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.TypeDefinitionId = None
        self.BrowsePath = []
        self.AttributeId = None
        self._AttributeId_fmt = '!I'
        self._AttributeId_fmt_size = 4
        self.IndexRange = None
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.TypeDefinitionId.to_binary())
        tmp.append(struct.pack('!i', len(self.BrowsePath)))
        for i in BrowsePath:
            tmp.append(self.BrowsePath.to_binary())
        tmp.append(struct.pack(self._AttributeId_fmt, self.AttributeId))
        tmp.append(self.IndexRange.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.TypeDefinitionId.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.BrowsePath.from_binary(data)
            self.AttributeId = struct.unpack(self._AttributeId_fmt, data.read(self._AttributeId_fmt_size))
            data = self.IndexRange.from_binary(data)
            return data
            
class ContentFilterElementResult(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.StatusCode = None
        self.OperandStatusCodes = []
        self.OperandDiagnosticInfos = []
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.StatusCode.to_binary())
        tmp.append(struct.pack('!i', len(self.OperandStatusCodes)))
        for i in OperandStatusCodes:
            tmp.append(self.OperandStatusCodes.to_binary())
        tmp.append(struct.pack('!i', len(self.OperandDiagnosticInfos)))
        for i in OperandDiagnosticInfos:
            tmp.append(self.OperandDiagnosticInfos.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.StatusCode.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.OperandStatusCodes.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.OperandDiagnosticInfos.from_binary(data)
            return data
            
class ContentFilterResult(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.ElementResults = []
        self.ElementDiagnosticInfos = []
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(struct.pack('!i', len(self.ElementResults)))
        for i in ElementResults:
            tmp.append(self.ElementResults.to_binary())
        tmp.append(struct.pack('!i', len(self.ElementDiagnosticInfos)))
        for i in ElementDiagnosticInfos:
            tmp.append(self.ElementDiagnosticInfos.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.ElementResults.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.ElementDiagnosticInfos.from_binary(data)
            return data
            
class ParsingResult(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.StatusCode = None
        self.DataStatusCodes = []
        self.DataDiagnosticInfos = []
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.StatusCode.to_binary())
        tmp.append(struct.pack('!i', len(self.DataStatusCodes)))
        for i in DataStatusCodes:
            tmp.append(self.DataStatusCodes.to_binary())
        tmp.append(struct.pack('!i', len(self.DataDiagnosticInfos)))
        for i in DataDiagnosticInfos:
            tmp.append(self.DataDiagnosticInfos.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.StatusCode.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.DataStatusCodes.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.DataDiagnosticInfos.from_binary(data)
            return data
            
class QueryFirstRequest(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.RequestHeader = None
        self.View = None
        self.NodeTypes = []
        self.Filter = None
        self.MaxDataSetsToReturn = None
        self._MaxDataSetsToReturn_fmt = '!I'
        self._MaxDataSetsToReturn_fmt_size = 4
        self.MaxReferencesToReturn = None
        self._MaxReferencesToReturn_fmt = '!I'
        self._MaxReferencesToReturn_fmt_size = 4
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.RequestHeader.to_binary())
        tmp.append(self.View.to_binary())
        tmp.append(struct.pack('!i', len(self.NodeTypes)))
        for i in NodeTypes:
            tmp.append(self.NodeTypes.to_binary())
        tmp.append(self.Filter.to_binary())
        tmp.append(struct.pack(self._MaxDataSetsToReturn_fmt, self.MaxDataSetsToReturn))
        tmp.append(struct.pack(self._MaxReferencesToReturn_fmt, self.MaxReferencesToReturn))
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.RequestHeader.from_binary(data)
            data = self.View.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.NodeTypes.from_binary(data)
            data = self.Filter.from_binary(data)
            self.MaxDataSetsToReturn = struct.unpack(self._MaxDataSetsToReturn_fmt, data.read(self._MaxDataSetsToReturn_fmt_size))
            self.MaxReferencesToReturn = struct.unpack(self._MaxReferencesToReturn_fmt, data.read(self._MaxReferencesToReturn_fmt_size))
            return data
            
class QueryFirstResponse(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.ResponseHeader = None
        self.QueryDataSets = []
        self.ContinuationPoint = None
        self.ParsingResults = []
        self.DiagnosticInfos = []
        self.FilterResult = None
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.ResponseHeader.to_binary())
        tmp.append(struct.pack('!i', len(self.QueryDataSets)))
        for i in QueryDataSets:
            tmp.append(self.QueryDataSets.to_binary())
        tmp.append(self.ContinuationPoint.to_binary())
        tmp.append(struct.pack('!i', len(self.ParsingResults)))
        for i in ParsingResults:
            tmp.append(self.ParsingResults.to_binary())
        tmp.append(struct.pack('!i', len(self.DiagnosticInfos)))
        for i in DiagnosticInfos:
            tmp.append(self.DiagnosticInfos.to_binary())
        tmp.append(self.FilterResult.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.ResponseHeader.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.QueryDataSets.from_binary(data)
            data = self.ContinuationPoint.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.ParsingResults.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.DiagnosticInfos.from_binary(data)
            data = self.FilterResult.from_binary(data)
            return data
            
class QueryNextRequest(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.RequestHeader = None
        self.ReleaseContinuationPoint = None
        self._ReleaseContinuationPoint_fmt = '!?'
        self._ReleaseContinuationPoint_fmt_size = 1
        self.ContinuationPoint = None
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.RequestHeader.to_binary())
        tmp.append(struct.pack(self._ReleaseContinuationPoint_fmt, self.ReleaseContinuationPoint))
        tmp.append(self.ContinuationPoint.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.RequestHeader.from_binary(data)
            self.ReleaseContinuationPoint = struct.unpack(self._ReleaseContinuationPoint_fmt, data.read(self._ReleaseContinuationPoint_fmt_size))
            data = self.ContinuationPoint.from_binary(data)
            return data
            
class QueryNextResponse(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.ResponseHeader = None
        self.QueryDataSets = []
        self.RevisedContinuationPoint = None
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.ResponseHeader.to_binary())
        tmp.append(struct.pack('!i', len(self.QueryDataSets)))
        for i in QueryDataSets:
            tmp.append(self.QueryDataSets.to_binary())
        tmp.append(self.RevisedContinuationPoint.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.ResponseHeader.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.QueryDataSets.from_binary(data)
            data = self.RevisedContinuationPoint.from_binary(data)
            return data
            
class ReadValueId(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.NodeId = None
        self.AttributeId = None
        self._AttributeId_fmt = '!I'
        self._AttributeId_fmt_size = 4
        self.IndexRange = None
        self.DataEncoding = None
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.NodeId.to_binary())
        tmp.append(struct.pack(self._AttributeId_fmt, self.AttributeId))
        tmp.append(self.IndexRange.to_binary())
        tmp.append(self.DataEncoding.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.NodeId.from_binary(data)
            self.AttributeId = struct.unpack(self._AttributeId_fmt, data.read(self._AttributeId_fmt_size))
            data = self.IndexRange.from_binary(data)
            data = self.DataEncoding.from_binary(data)
            return data
            
class ReadRequest(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.RequestHeader = None
        self.MaxAge = None
        self._MaxAge_fmt = '!d'
        self._MaxAge_fmt_size = 8
        self.TimestampsToReturn = None
        self.NodesToRead = []
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.RequestHeader.to_binary())
        tmp.append(struct.pack(self._MaxAge_fmt, self.MaxAge))
        tmp.append(self.TimestampsToReturn.to_binary())
        tmp.append(struct.pack('!i', len(self.NodesToRead)))
        for i in NodesToRead:
            tmp.append(self.NodesToRead.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.RequestHeader.from_binary(data)
            self.MaxAge = struct.unpack(self._MaxAge_fmt, data.read(self._MaxAge_fmt_size))
            data = self.TimestampsToReturn.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.NodesToRead.from_binary(data)
            return data
            
class ReadResponse(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.ResponseHeader = None
        self.Results = []
        self.DiagnosticInfos = []
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.ResponseHeader.to_binary())
        tmp.append(struct.pack('!i', len(self.Results)))
        for i in Results:
            tmp.append(self.Results.to_binary())
        tmp.append(struct.pack('!i', len(self.DiagnosticInfos)))
        for i in DiagnosticInfos:
            tmp.append(self.DiagnosticInfos.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.ResponseHeader.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.Results.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.DiagnosticInfos.from_binary(data)
            return data
            
class HistoryReadValueId(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.NodeId = None
        self.IndexRange = None
        self.DataEncoding = None
        self.ContinuationPoint = None
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.NodeId.to_binary())
        tmp.append(self.IndexRange.to_binary())
        tmp.append(self.DataEncoding.to_binary())
        tmp.append(self.ContinuationPoint.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.NodeId.from_binary(data)
            data = self.IndexRange.from_binary(data)
            data = self.DataEncoding.from_binary(data)
            data = self.ContinuationPoint.from_binary(data)
            return data
            
class HistoryReadResult(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.StatusCode = None
        self.ContinuationPoint = None
        self.HistoryData = None
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.StatusCode.to_binary())
        tmp.append(self.ContinuationPoint.to_binary())
        tmp.append(self.HistoryData.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.StatusCode.from_binary(data)
            data = self.ContinuationPoint.from_binary(data)
            data = self.HistoryData.from_binary(data)
            return data
            
class HistoryReadDetails(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
        tmp.append(struct.pack('!i', len(self.Body)))
        for i in Body:
            tmp.append(struct.pack(self._Body_fmt, self.Body))
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    self.Body = struct.unpack(self._Body_fmt, data.read(self._Body_fmt_size))
            return data
            
class ReadRawModifiedDetails(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.IsReadModified = None
        self._IsReadModified_fmt = '!?'
        self._IsReadModified_fmt_size = 1
        self.StartTime = None
        self._StartTime_fmt = '!d'
        self._StartTime_fmt_size = 8
        self.EndTime = None
        self._EndTime_fmt = '!d'
        self._EndTime_fmt_size = 8
        self.NumValuesPerNode = None
        self._NumValuesPerNode_fmt = '!I'
        self._NumValuesPerNode_fmt_size = 4
        self.ReturnBounds = None
        self._ReturnBounds_fmt = '!?'
        self._ReturnBounds_fmt_size = 1
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(struct.pack(self._IsReadModified_fmt, self.IsReadModified))
        tmp.append(struct.pack(self._StartTime_fmt, self.StartTime))
        tmp.append(struct.pack(self._EndTime_fmt, self.EndTime))
        tmp.append(struct.pack(self._NumValuesPerNode_fmt, self.NumValuesPerNode))
        tmp.append(struct.pack(self._ReturnBounds_fmt, self.ReturnBounds))
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            self.IsReadModified = struct.unpack(self._IsReadModified_fmt, data.read(self._IsReadModified_fmt_size))
            self.StartTime = struct.unpack(self._StartTime_fmt, data.read(self._StartTime_fmt_size))
            self.EndTime = struct.unpack(self._EndTime_fmt, data.read(self._EndTime_fmt_size))
            self.NumValuesPerNode = struct.unpack(self._NumValuesPerNode_fmt, data.read(self._NumValuesPerNode_fmt_size))
            self.ReturnBounds = struct.unpack(self._ReturnBounds_fmt, data.read(self._ReturnBounds_fmt_size))
            return data
            
class ReadAtTimeDetails(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.ReqTimes = []
        self._ReqTimes_fmt = '!d'
        self._ReqTimes_fmt_size = 8
        self.UseSimpleBounds = None
        self._UseSimpleBounds_fmt = '!?'
        self._UseSimpleBounds_fmt_size = 1
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(struct.pack('!i', len(self.ReqTimes)))
        for i in ReqTimes:
            tmp.append(struct.pack(self._ReqTimes_fmt, self.ReqTimes))
        tmp.append(struct.pack(self._UseSimpleBounds_fmt, self.UseSimpleBounds))
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    self.ReqTimes = struct.unpack(self._ReqTimes_fmt, data.read(self._ReqTimes_fmt_size))
            self.UseSimpleBounds = struct.unpack(self._UseSimpleBounds_fmt, data.read(self._UseSimpleBounds_fmt_size))
            return data
            
class HistoryData(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.DataValues = []
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(struct.pack('!i', len(self.DataValues)))
        for i in DataValues:
            tmp.append(self.DataValues.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.DataValues.from_binary(data)
            return data
            
class ModificationInfo(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.ModificationTime = None
        self._ModificationTime_fmt = '!d'
        self._ModificationTime_fmt_size = 8
        self.UpdateType = None
        self.UserName = None
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(struct.pack(self._ModificationTime_fmt, self.ModificationTime))
        tmp.append(self.UpdateType.to_binary())
        tmp.append(self.UserName.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            self.ModificationTime = struct.unpack(self._ModificationTime_fmt, data.read(self._ModificationTime_fmt_size))
            data = self.UpdateType.from_binary(data)
            data = self.UserName.from_binary(data)
            return data
            
class HistoryModifiedData(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.DataValues = []
        self.ModificationInfos = []
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(struct.pack('!i', len(self.DataValues)))
        for i in DataValues:
            tmp.append(self.DataValues.to_binary())
        tmp.append(struct.pack('!i', len(self.ModificationInfos)))
        for i in ModificationInfos:
            tmp.append(self.ModificationInfos.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.DataValues.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.ModificationInfos.from_binary(data)
            return data
            
class HistoryReadRequest(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.RequestHeader = None
        self.HistoryReadDetails = None
        self.TimestampsToReturn = None
        self.ReleaseContinuationPoints = None
        self._ReleaseContinuationPoints_fmt = '!?'
        self._ReleaseContinuationPoints_fmt_size = 1
        self.NodesToRead = []
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.RequestHeader.to_binary())
        tmp.append(self.HistoryReadDetails.to_binary())
        tmp.append(self.TimestampsToReturn.to_binary())
        tmp.append(struct.pack(self._ReleaseContinuationPoints_fmt, self.ReleaseContinuationPoints))
        tmp.append(struct.pack('!i', len(self.NodesToRead)))
        for i in NodesToRead:
            tmp.append(self.NodesToRead.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.RequestHeader.from_binary(data)
            data = self.HistoryReadDetails.from_binary(data)
            data = self.TimestampsToReturn.from_binary(data)
            self.ReleaseContinuationPoints = struct.unpack(self._ReleaseContinuationPoints_fmt, data.read(self._ReleaseContinuationPoints_fmt_size))
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.NodesToRead.from_binary(data)
            return data
            
class HistoryReadResponse(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.ResponseHeader = None
        self.Results = []
        self.DiagnosticInfos = []
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.ResponseHeader.to_binary())
        tmp.append(struct.pack('!i', len(self.Results)))
        for i in Results:
            tmp.append(self.Results.to_binary())
        tmp.append(struct.pack('!i', len(self.DiagnosticInfos)))
        for i in DiagnosticInfos:
            tmp.append(self.DiagnosticInfos.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.ResponseHeader.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.Results.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.DiagnosticInfos.from_binary(data)
            return data
            
class WriteValue(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.NodeId = None
        self.AttributeId = None
        self._AttributeId_fmt = '!I'
        self._AttributeId_fmt_size = 4
        self.IndexRange = None
        self.Value = None
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.NodeId.to_binary())
        tmp.append(struct.pack(self._AttributeId_fmt, self.AttributeId))
        tmp.append(self.IndexRange.to_binary())
        tmp.append(self.Value.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.NodeId.from_binary(data)
            self.AttributeId = struct.unpack(self._AttributeId_fmt, data.read(self._AttributeId_fmt_size))
            data = self.IndexRange.from_binary(data)
            data = self.Value.from_binary(data)
            return data
            
class WriteRequest(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.RequestHeader = None
        self.NodesToWrite = []
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.RequestHeader.to_binary())
        tmp.append(struct.pack('!i', len(self.NodesToWrite)))
        for i in NodesToWrite:
            tmp.append(self.NodesToWrite.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.RequestHeader.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.NodesToWrite.from_binary(data)
            return data
            
class WriteResponse(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.ResponseHeader = None
        self.Results = []
        self.DiagnosticInfos = []
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.ResponseHeader.to_binary())
        tmp.append(struct.pack('!i', len(self.Results)))
        for i in Results:
            tmp.append(self.Results.to_binary())
        tmp.append(struct.pack('!i', len(self.DiagnosticInfos)))
        for i in DiagnosticInfos:
            tmp.append(self.DiagnosticInfos.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.ResponseHeader.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.Results.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.DiagnosticInfos.from_binary(data)
            return data
            
class HistoryUpdateDetails(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.NodeId = None
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.NodeId.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.NodeId.from_binary(data)
            return data
            
class UpdateDataDetails(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.NodeId = None
        self.PerformInsertReplace = None
        self.UpdateValues = []
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.NodeId.to_binary())
        tmp.append(self.PerformInsertReplace.to_binary())
        tmp.append(struct.pack('!i', len(self.UpdateValues)))
        for i in UpdateValues:
            tmp.append(self.UpdateValues.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.NodeId.from_binary(data)
            data = self.PerformInsertReplace.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.UpdateValues.from_binary(data)
            return data
            
class UpdateStructureDataDetails(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.NodeId = None
        self.PerformInsertReplace = None
        self.UpdateValues = []
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.NodeId.to_binary())
        tmp.append(self.PerformInsertReplace.to_binary())
        tmp.append(struct.pack('!i', len(self.UpdateValues)))
        for i in UpdateValues:
            tmp.append(self.UpdateValues.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.NodeId.from_binary(data)
            data = self.PerformInsertReplace.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.UpdateValues.from_binary(data)
            return data
            
class DeleteRawModifiedDetails(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.NodeId = None
        self.IsDeleteModified = None
        self._IsDeleteModified_fmt = '!?'
        self._IsDeleteModified_fmt_size = 1
        self.StartTime = None
        self._StartTime_fmt = '!d'
        self._StartTime_fmt_size = 8
        self.EndTime = None
        self._EndTime_fmt = '!d'
        self._EndTime_fmt_size = 8
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.NodeId.to_binary())
        tmp.append(struct.pack(self._IsDeleteModified_fmt, self.IsDeleteModified))
        tmp.append(struct.pack(self._StartTime_fmt, self.StartTime))
        tmp.append(struct.pack(self._EndTime_fmt, self.EndTime))
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.NodeId.from_binary(data)
            self.IsDeleteModified = struct.unpack(self._IsDeleteModified_fmt, data.read(self._IsDeleteModified_fmt_size))
            self.StartTime = struct.unpack(self._StartTime_fmt, data.read(self._StartTime_fmt_size))
            self.EndTime = struct.unpack(self._EndTime_fmt, data.read(self._EndTime_fmt_size))
            return data
            
class DeleteAtTimeDetails(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.NodeId = None
        self.ReqTimes = []
        self._ReqTimes_fmt = '!d'
        self._ReqTimes_fmt_size = 8
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.NodeId.to_binary())
        tmp.append(struct.pack('!i', len(self.ReqTimes)))
        for i in ReqTimes:
            tmp.append(struct.pack(self._ReqTimes_fmt, self.ReqTimes))
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.NodeId.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    self.ReqTimes = struct.unpack(self._ReqTimes_fmt, data.read(self._ReqTimes_fmt_size))
            return data
            
class DeleteEventDetails(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.NodeId = None
        self.EventIds = []
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.NodeId.to_binary())
        tmp.append(struct.pack('!i', len(self.EventIds)))
        for i in EventIds:
            tmp.append(self.EventIds.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.NodeId.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.EventIds.from_binary(data)
            return data
            
class HistoryUpdateResult(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.StatusCode = None
        self.OperationResults = []
        self.DiagnosticInfos = []
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.StatusCode.to_binary())
        tmp.append(struct.pack('!i', len(self.OperationResults)))
        for i in OperationResults:
            tmp.append(self.OperationResults.to_binary())
        tmp.append(struct.pack('!i', len(self.DiagnosticInfos)))
        for i in DiagnosticInfos:
            tmp.append(self.DiagnosticInfos.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.StatusCode.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.OperationResults.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.DiagnosticInfos.from_binary(data)
            return data
            
class HistoryUpdateRequest(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.RequestHeader = None
        self.HistoryUpdateDetails = []
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.RequestHeader.to_binary())
        tmp.append(struct.pack('!i', len(self.HistoryUpdateDetails)))
        for i in HistoryUpdateDetails:
            tmp.append(self.HistoryUpdateDetails.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.RequestHeader.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.HistoryUpdateDetails.from_binary(data)
            return data
            
class HistoryUpdateResponse(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.ResponseHeader = None
        self.Results = []
        self.DiagnosticInfos = []
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.ResponseHeader.to_binary())
        tmp.append(struct.pack('!i', len(self.Results)))
        for i in Results:
            tmp.append(self.Results.to_binary())
        tmp.append(struct.pack('!i', len(self.DiagnosticInfos)))
        for i in DiagnosticInfos:
            tmp.append(self.DiagnosticInfos.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.ResponseHeader.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.Results.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.DiagnosticInfos.from_binary(data)
            return data
            
class CallMethodRequest(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.ObjectId = None
        self.MethodId = None
        self.InputArguments = []
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.ObjectId.to_binary())
        tmp.append(self.MethodId.to_binary())
        tmp.append(struct.pack('!i', len(self.InputArguments)))
        for i in InputArguments:
            tmp.append(self.InputArguments.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.ObjectId.from_binary(data)
            data = self.MethodId.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.InputArguments.from_binary(data)
            return data
            
class CallMethodResult(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.StatusCode = None
        self.InputArgumentResults = []
        self.InputArgumentDiagnosticInfos = []
        self.OutputArguments = []
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.StatusCode.to_binary())
        tmp.append(struct.pack('!i', len(self.InputArgumentResults)))
        for i in InputArgumentResults:
            tmp.append(self.InputArgumentResults.to_binary())
        tmp.append(struct.pack('!i', len(self.InputArgumentDiagnosticInfos)))
        for i in InputArgumentDiagnosticInfos:
            tmp.append(self.InputArgumentDiagnosticInfos.to_binary())
        tmp.append(struct.pack('!i', len(self.OutputArguments)))
        for i in OutputArguments:
            tmp.append(self.OutputArguments.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.StatusCode.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.InputArgumentResults.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.InputArgumentDiagnosticInfos.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.OutputArguments.from_binary(data)
            return data
            
class CallRequest(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.RequestHeader = None
        self.MethodsToCall = []
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.RequestHeader.to_binary())
        tmp.append(struct.pack('!i', len(self.MethodsToCall)))
        for i in MethodsToCall:
            tmp.append(self.MethodsToCall.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.RequestHeader.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.MethodsToCall.from_binary(data)
            return data
            
class CallResponse(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.ResponseHeader = None
        self.Results = []
        self.DiagnosticInfos = []
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.ResponseHeader.to_binary())
        tmp.append(struct.pack('!i', len(self.Results)))
        for i in Results:
            tmp.append(self.Results.to_binary())
        tmp.append(struct.pack('!i', len(self.DiagnosticInfos)))
        for i in DiagnosticInfos:
            tmp.append(self.DiagnosticInfos.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.ResponseHeader.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.Results.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.DiagnosticInfos.from_binary(data)
            return data
            
class MonitoringFilter(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
        tmp.append(struct.pack('!i', len(self.Body)))
        for i in Body:
            tmp.append(struct.pack(self._Body_fmt, self.Body))
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    self.Body = struct.unpack(self._Body_fmt, data.read(self._Body_fmt_size))
            return data
            
class DataChangeFilter(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.Trigger = None
        self.DeadbandType = None
        self._DeadbandType_fmt = '!I'
        self._DeadbandType_fmt_size = 4
        self.DeadbandValue = None
        self._DeadbandValue_fmt = '!d'
        self._DeadbandValue_fmt_size = 8
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.Trigger.to_binary())
        tmp.append(struct.pack(self._DeadbandType_fmt, self.DeadbandType))
        tmp.append(struct.pack(self._DeadbandValue_fmt, self.DeadbandValue))
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.Trigger.from_binary(data)
            self.DeadbandType = struct.unpack(self._DeadbandType_fmt, data.read(self._DeadbandType_fmt_size))
            self.DeadbandValue = struct.unpack(self._DeadbandValue_fmt, data.read(self._DeadbandValue_fmt_size))
            return data
            
class EventFilter(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.SelectClauses = []
        self.WhereClause = None
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(struct.pack('!i', len(self.SelectClauses)))
        for i in SelectClauses:
            tmp.append(self.SelectClauses.to_binary())
        tmp.append(self.WhereClause.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.SelectClauses.from_binary(data)
            data = self.WhereClause.from_binary(data)
            return data
            
class ReadEventDetails(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.NumValuesPerNode = None
        self._NumValuesPerNode_fmt = '!I'
        self._NumValuesPerNode_fmt_size = 4
        self.StartTime = None
        self._StartTime_fmt = '!d'
        self._StartTime_fmt_size = 8
        self.EndTime = None
        self._EndTime_fmt = '!d'
        self._EndTime_fmt_size = 8
        self.Filter = None
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(struct.pack(self._NumValuesPerNode_fmt, self.NumValuesPerNode))
        tmp.append(struct.pack(self._StartTime_fmt, self.StartTime))
        tmp.append(struct.pack(self._EndTime_fmt, self.EndTime))
        tmp.append(self.Filter.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            self.NumValuesPerNode = struct.unpack(self._NumValuesPerNode_fmt, data.read(self._NumValuesPerNode_fmt_size))
            self.StartTime = struct.unpack(self._StartTime_fmt, data.read(self._StartTime_fmt_size))
            self.EndTime = struct.unpack(self._EndTime_fmt, data.read(self._EndTime_fmt_size))
            data = self.Filter.from_binary(data)
            return data
            
class AggregateConfiguration(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.UseServerCapabilitiesDefaults = None
        self._UseServerCapabilitiesDefaults_fmt = '!?'
        self._UseServerCapabilitiesDefaults_fmt_size = 1
        self.TreatUncertainAsBad = None
        self._TreatUncertainAsBad_fmt = '!?'
        self._TreatUncertainAsBad_fmt_size = 1
        self.PercentDataBad = None
        self._PercentDataBad_fmt = '!c'
        self._PercentDataBad_fmt_size = 1
        self.PercentDataGood = None
        self._PercentDataGood_fmt = '!c'
        self._PercentDataGood_fmt_size = 1
        self.UseSlopedExtrapolation = None
        self._UseSlopedExtrapolation_fmt = '!?'
        self._UseSlopedExtrapolation_fmt_size = 1
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(struct.pack(self._UseServerCapabilitiesDefaults_fmt, self.UseServerCapabilitiesDefaults))
        tmp.append(struct.pack(self._TreatUncertainAsBad_fmt, self.TreatUncertainAsBad))
        tmp.append(struct.pack(self._PercentDataBad_fmt, self.PercentDataBad))
        tmp.append(struct.pack(self._PercentDataGood_fmt, self.PercentDataGood))
        tmp.append(struct.pack(self._UseSlopedExtrapolation_fmt, self.UseSlopedExtrapolation))
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            self.UseServerCapabilitiesDefaults = struct.unpack(self._UseServerCapabilitiesDefaults_fmt, data.read(self._UseServerCapabilitiesDefaults_fmt_size))
            self.TreatUncertainAsBad = struct.unpack(self._TreatUncertainAsBad_fmt, data.read(self._TreatUncertainAsBad_fmt_size))
            self.PercentDataBad = struct.unpack(self._PercentDataBad_fmt, data.read(self._PercentDataBad_fmt_size))
            self.PercentDataGood = struct.unpack(self._PercentDataGood_fmt, data.read(self._PercentDataGood_fmt_size))
            self.UseSlopedExtrapolation = struct.unpack(self._UseSlopedExtrapolation_fmt, data.read(self._UseSlopedExtrapolation_fmt_size))
            return data
            
class ReadProcessedDetails(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.StartTime = None
        self._StartTime_fmt = '!d'
        self._StartTime_fmt_size = 8
        self.EndTime = None
        self._EndTime_fmt = '!d'
        self._EndTime_fmt_size = 8
        self.ProcessingInterval = None
        self._ProcessingInterval_fmt = '!d'
        self._ProcessingInterval_fmt_size = 8
        self.AggregateType = []
        self.AggregateConfiguration = None
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(struct.pack(self._StartTime_fmt, self.StartTime))
        tmp.append(struct.pack(self._EndTime_fmt, self.EndTime))
        tmp.append(struct.pack(self._ProcessingInterval_fmt, self.ProcessingInterval))
        tmp.append(struct.pack('!i', len(self.AggregateType)))
        for i in AggregateType:
            tmp.append(self.AggregateType.to_binary())
        tmp.append(self.AggregateConfiguration.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            self.StartTime = struct.unpack(self._StartTime_fmt, data.read(self._StartTime_fmt_size))
            self.EndTime = struct.unpack(self._EndTime_fmt, data.read(self._EndTime_fmt_size))
            self.ProcessingInterval = struct.unpack(self._ProcessingInterval_fmt, data.read(self._ProcessingInterval_fmt_size))
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.AggregateType.from_binary(data)
            data = self.AggregateConfiguration.from_binary(data)
            return data
            
class AggregateFilter(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.StartTime = None
        self._StartTime_fmt = '!d'
        self._StartTime_fmt_size = 8
        self.AggregateType = None
        self.ProcessingInterval = None
        self._ProcessingInterval_fmt = '!d'
        self._ProcessingInterval_fmt_size = 8
        self.AggregateConfiguration = None
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(struct.pack(self._StartTime_fmt, self.StartTime))
        tmp.append(self.AggregateType.to_binary())
        tmp.append(struct.pack(self._ProcessingInterval_fmt, self.ProcessingInterval))
        tmp.append(self.AggregateConfiguration.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            self.StartTime = struct.unpack(self._StartTime_fmt, data.read(self._StartTime_fmt_size))
            data = self.AggregateType.from_binary(data)
            self.ProcessingInterval = struct.unpack(self._ProcessingInterval_fmt, data.read(self._ProcessingInterval_fmt_size))
            data = self.AggregateConfiguration.from_binary(data)
            return data
            
class MonitoringFilterResult(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
        tmp.append(struct.pack('!i', len(self.Body)))
        for i in Body:
            tmp.append(struct.pack(self._Body_fmt, self.Body))
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    self.Body = struct.unpack(self._Body_fmt, data.read(self._Body_fmt_size))
            return data
            
class EventFilterResult(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.SelectClauseResults = []
        self.SelectClauseDiagnosticInfos = []
        self.WhereClauseResult = None
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(struct.pack('!i', len(self.SelectClauseResults)))
        for i in SelectClauseResults:
            tmp.append(self.SelectClauseResults.to_binary())
        tmp.append(struct.pack('!i', len(self.SelectClauseDiagnosticInfos)))
        for i in SelectClauseDiagnosticInfos:
            tmp.append(self.SelectClauseDiagnosticInfos.to_binary())
        tmp.append(self.WhereClauseResult.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.SelectClauseResults.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.SelectClauseDiagnosticInfos.from_binary(data)
            data = self.WhereClauseResult.from_binary(data)
            return data
            
class HistoryUpdateEventResult(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.StatusCode = None
        self.EventFilterResult = None
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.StatusCode.to_binary())
        tmp.append(self.EventFilterResult.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.StatusCode.from_binary(data)
            data = self.EventFilterResult.from_binary(data)
            return data
            
class AggregateFilterResult(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.RevisedStartTime = None
        self._RevisedStartTime_fmt = '!d'
        self._RevisedStartTime_fmt_size = 8
        self.RevisedProcessingInterval = None
        self._RevisedProcessingInterval_fmt = '!d'
        self._RevisedProcessingInterval_fmt_size = 8
        self.RevisedAggregateConfiguration = None
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(struct.pack(self._RevisedStartTime_fmt, self.RevisedStartTime))
        tmp.append(struct.pack(self._RevisedProcessingInterval_fmt, self.RevisedProcessingInterval))
        tmp.append(self.RevisedAggregateConfiguration.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            self.RevisedStartTime = struct.unpack(self._RevisedStartTime_fmt, data.read(self._RevisedStartTime_fmt_size))
            self.RevisedProcessingInterval = struct.unpack(self._RevisedProcessingInterval_fmt, data.read(self._RevisedProcessingInterval_fmt_size))
            data = self.RevisedAggregateConfiguration.from_binary(data)
            return data
            
class MonitoringParameters(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.ClientHandle = None
        self._ClientHandle_fmt = '!I'
        self._ClientHandle_fmt_size = 4
        self.SamplingInterval = None
        self._SamplingInterval_fmt = '!d'
        self._SamplingInterval_fmt_size = 8
        self.Filter = None
        self.QueueSize = None
        self._QueueSize_fmt = '!I'
        self._QueueSize_fmt_size = 4
        self.DiscardOldest = None
        self._DiscardOldest_fmt = '!?'
        self._DiscardOldest_fmt_size = 1
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(struct.pack(self._ClientHandle_fmt, self.ClientHandle))
        tmp.append(struct.pack(self._SamplingInterval_fmt, self.SamplingInterval))
        tmp.append(self.Filter.to_binary())
        tmp.append(struct.pack(self._QueueSize_fmt, self.QueueSize))
        tmp.append(struct.pack(self._DiscardOldest_fmt, self.DiscardOldest))
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            self.ClientHandle = struct.unpack(self._ClientHandle_fmt, data.read(self._ClientHandle_fmt_size))
            self.SamplingInterval = struct.unpack(self._SamplingInterval_fmt, data.read(self._SamplingInterval_fmt_size))
            data = self.Filter.from_binary(data)
            self.QueueSize = struct.unpack(self._QueueSize_fmt, data.read(self._QueueSize_fmt_size))
            self.DiscardOldest = struct.unpack(self._DiscardOldest_fmt, data.read(self._DiscardOldest_fmt_size))
            return data
            
class MonitoredItemCreateRequest(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.ItemToMonitor = None
        self.MonitoringMode = None
        self.RequestedParameters = None
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.ItemToMonitor.to_binary())
        tmp.append(self.MonitoringMode.to_binary())
        tmp.append(self.RequestedParameters.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.ItemToMonitor.from_binary(data)
            data = self.MonitoringMode.from_binary(data)
            data = self.RequestedParameters.from_binary(data)
            return data
            
class MonitoredItemCreateResult(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.StatusCode = None
        self.MonitoredItemId = None
        self._MonitoredItemId_fmt = '!I'
        self._MonitoredItemId_fmt_size = 4
        self.RevisedSamplingInterval = None
        self._RevisedSamplingInterval_fmt = '!d'
        self._RevisedSamplingInterval_fmt_size = 8
        self.RevisedQueueSize = None
        self._RevisedQueueSize_fmt = '!I'
        self._RevisedQueueSize_fmt_size = 4
        self.FilterResult = None
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.StatusCode.to_binary())
        tmp.append(struct.pack(self._MonitoredItemId_fmt, self.MonitoredItemId))
        tmp.append(struct.pack(self._RevisedSamplingInterval_fmt, self.RevisedSamplingInterval))
        tmp.append(struct.pack(self._RevisedQueueSize_fmt, self.RevisedQueueSize))
        tmp.append(self.FilterResult.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.StatusCode.from_binary(data)
            self.MonitoredItemId = struct.unpack(self._MonitoredItemId_fmt, data.read(self._MonitoredItemId_fmt_size))
            self.RevisedSamplingInterval = struct.unpack(self._RevisedSamplingInterval_fmt, data.read(self._RevisedSamplingInterval_fmt_size))
            self.RevisedQueueSize = struct.unpack(self._RevisedQueueSize_fmt, data.read(self._RevisedQueueSize_fmt_size))
            data = self.FilterResult.from_binary(data)
            return data
            
class CreateMonitoredItemsRequest(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.RequestHeader = None
        self.SubscriptionId = None
        self._SubscriptionId_fmt = '!I'
        self._SubscriptionId_fmt_size = 4
        self.TimestampsToReturn = None
        self.ItemsToCreate = []
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.RequestHeader.to_binary())
        tmp.append(struct.pack(self._SubscriptionId_fmt, self.SubscriptionId))
        tmp.append(self.TimestampsToReturn.to_binary())
        tmp.append(struct.pack('!i', len(self.ItemsToCreate)))
        for i in ItemsToCreate:
            tmp.append(self.ItemsToCreate.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.RequestHeader.from_binary(data)
            self.SubscriptionId = struct.unpack(self._SubscriptionId_fmt, data.read(self._SubscriptionId_fmt_size))
            data = self.TimestampsToReturn.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.ItemsToCreate.from_binary(data)
            return data
            
class CreateMonitoredItemsResponse(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.ResponseHeader = None
        self.Results = []
        self.DiagnosticInfos = []
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.ResponseHeader.to_binary())
        tmp.append(struct.pack('!i', len(self.Results)))
        for i in Results:
            tmp.append(self.Results.to_binary())
        tmp.append(struct.pack('!i', len(self.DiagnosticInfos)))
        for i in DiagnosticInfos:
            tmp.append(self.DiagnosticInfos.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.ResponseHeader.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.Results.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.DiagnosticInfos.from_binary(data)
            return data
            
class MonitoredItemModifyRequest(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.MonitoredItemId = None
        self._MonitoredItemId_fmt = '!I'
        self._MonitoredItemId_fmt_size = 4
        self.RequestedParameters = None
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(struct.pack(self._MonitoredItemId_fmt, self.MonitoredItemId))
        tmp.append(self.RequestedParameters.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            self.MonitoredItemId = struct.unpack(self._MonitoredItemId_fmt, data.read(self._MonitoredItemId_fmt_size))
            data = self.RequestedParameters.from_binary(data)
            return data
            
class MonitoredItemModifyResult(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.StatusCode = None
        self.RevisedSamplingInterval = None
        self._RevisedSamplingInterval_fmt = '!d'
        self._RevisedSamplingInterval_fmt_size = 8
        self.RevisedQueueSize = None
        self._RevisedQueueSize_fmt = '!I'
        self._RevisedQueueSize_fmt_size = 4
        self.FilterResult = None
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.StatusCode.to_binary())
        tmp.append(struct.pack(self._RevisedSamplingInterval_fmt, self.RevisedSamplingInterval))
        tmp.append(struct.pack(self._RevisedQueueSize_fmt, self.RevisedQueueSize))
        tmp.append(self.FilterResult.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.StatusCode.from_binary(data)
            self.RevisedSamplingInterval = struct.unpack(self._RevisedSamplingInterval_fmt, data.read(self._RevisedSamplingInterval_fmt_size))
            self.RevisedQueueSize = struct.unpack(self._RevisedQueueSize_fmt, data.read(self._RevisedQueueSize_fmt_size))
            data = self.FilterResult.from_binary(data)
            return data
            
class ModifyMonitoredItemsRequest(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.RequestHeader = None
        self.SubscriptionId = None
        self._SubscriptionId_fmt = '!I'
        self._SubscriptionId_fmt_size = 4
        self.TimestampsToReturn = None
        self.ItemsToModify = []
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.RequestHeader.to_binary())
        tmp.append(struct.pack(self._SubscriptionId_fmt, self.SubscriptionId))
        tmp.append(self.TimestampsToReturn.to_binary())
        tmp.append(struct.pack('!i', len(self.ItemsToModify)))
        for i in ItemsToModify:
            tmp.append(self.ItemsToModify.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.RequestHeader.from_binary(data)
            self.SubscriptionId = struct.unpack(self._SubscriptionId_fmt, data.read(self._SubscriptionId_fmt_size))
            data = self.TimestampsToReturn.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.ItemsToModify.from_binary(data)
            return data
            
class ModifyMonitoredItemsResponse(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.ResponseHeader = None
        self.Results = []
        self.DiagnosticInfos = []
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.ResponseHeader.to_binary())
        tmp.append(struct.pack('!i', len(self.Results)))
        for i in Results:
            tmp.append(self.Results.to_binary())
        tmp.append(struct.pack('!i', len(self.DiagnosticInfos)))
        for i in DiagnosticInfos:
            tmp.append(self.DiagnosticInfos.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.ResponseHeader.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.Results.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.DiagnosticInfos.from_binary(data)
            return data
            
class SetMonitoringModeRequest(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.RequestHeader = None
        self.SubscriptionId = None
        self._SubscriptionId_fmt = '!I'
        self._SubscriptionId_fmt_size = 4
        self.MonitoringMode = None
        self.MonitoredItemIds = []
        self._MonitoredItemIds_fmt = '!I'
        self._MonitoredItemIds_fmt_size = 4
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.RequestHeader.to_binary())
        tmp.append(struct.pack(self._SubscriptionId_fmt, self.SubscriptionId))
        tmp.append(self.MonitoringMode.to_binary())
        tmp.append(struct.pack('!i', len(self.MonitoredItemIds)))
        for i in MonitoredItemIds:
            tmp.append(struct.pack(self._MonitoredItemIds_fmt, self.MonitoredItemIds))
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.RequestHeader.from_binary(data)
            self.SubscriptionId = struct.unpack(self._SubscriptionId_fmt, data.read(self._SubscriptionId_fmt_size))
            data = self.MonitoringMode.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    self.MonitoredItemIds = struct.unpack(self._MonitoredItemIds_fmt, data.read(self._MonitoredItemIds_fmt_size))
            return data
            
class SetMonitoringModeResponse(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.ResponseHeader = None
        self.Results = []
        self.DiagnosticInfos = []
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.ResponseHeader.to_binary())
        tmp.append(struct.pack('!i', len(self.Results)))
        for i in Results:
            tmp.append(self.Results.to_binary())
        tmp.append(struct.pack('!i', len(self.DiagnosticInfos)))
        for i in DiagnosticInfos:
            tmp.append(self.DiagnosticInfos.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.ResponseHeader.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.Results.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.DiagnosticInfos.from_binary(data)
            return data
            
class SetTriggeringRequest(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.RequestHeader = None
        self.SubscriptionId = None
        self._SubscriptionId_fmt = '!I'
        self._SubscriptionId_fmt_size = 4
        self.TriggeringItemId = None
        self._TriggeringItemId_fmt = '!I'
        self._TriggeringItemId_fmt_size = 4
        self.LinksToAdd = []
        self._LinksToAdd_fmt = '!I'
        self._LinksToAdd_fmt_size = 4
        self.LinksToRemove = []
        self._LinksToRemove_fmt = '!I'
        self._LinksToRemove_fmt_size = 4
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.RequestHeader.to_binary())
        tmp.append(struct.pack(self._SubscriptionId_fmt, self.SubscriptionId))
        tmp.append(struct.pack(self._TriggeringItemId_fmt, self.TriggeringItemId))
        tmp.append(struct.pack('!i', len(self.LinksToAdd)))
        for i in LinksToAdd:
            tmp.append(struct.pack(self._LinksToAdd_fmt, self.LinksToAdd))
        tmp.append(struct.pack('!i', len(self.LinksToRemove)))
        for i in LinksToRemove:
            tmp.append(struct.pack(self._LinksToRemove_fmt, self.LinksToRemove))
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.RequestHeader.from_binary(data)
            self.SubscriptionId = struct.unpack(self._SubscriptionId_fmt, data.read(self._SubscriptionId_fmt_size))
            self.TriggeringItemId = struct.unpack(self._TriggeringItemId_fmt, data.read(self._TriggeringItemId_fmt_size))
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    self.LinksToAdd = struct.unpack(self._LinksToAdd_fmt, data.read(self._LinksToAdd_fmt_size))
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    self.LinksToRemove = struct.unpack(self._LinksToRemove_fmt, data.read(self._LinksToRemove_fmt_size))
            return data
            
class SetTriggeringResponse(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.ResponseHeader = None
        self.AddResults = []
        self.AddDiagnosticInfos = []
        self.RemoveResults = []
        self.RemoveDiagnosticInfos = []
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.ResponseHeader.to_binary())
        tmp.append(struct.pack('!i', len(self.AddResults)))
        for i in AddResults:
            tmp.append(self.AddResults.to_binary())
        tmp.append(struct.pack('!i', len(self.AddDiagnosticInfos)))
        for i in AddDiagnosticInfos:
            tmp.append(self.AddDiagnosticInfos.to_binary())
        tmp.append(struct.pack('!i', len(self.RemoveResults)))
        for i in RemoveResults:
            tmp.append(self.RemoveResults.to_binary())
        tmp.append(struct.pack('!i', len(self.RemoveDiagnosticInfos)))
        for i in RemoveDiagnosticInfos:
            tmp.append(self.RemoveDiagnosticInfos.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.ResponseHeader.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.AddResults.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.AddDiagnosticInfos.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.RemoveResults.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.RemoveDiagnosticInfos.from_binary(data)
            return data
            
class DeleteMonitoredItemsRequest(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.RequestHeader = None
        self.SubscriptionId = None
        self._SubscriptionId_fmt = '!I'
        self._SubscriptionId_fmt_size = 4
        self.MonitoredItemIds = []
        self._MonitoredItemIds_fmt = '!I'
        self._MonitoredItemIds_fmt_size = 4
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.RequestHeader.to_binary())
        tmp.append(struct.pack(self._SubscriptionId_fmt, self.SubscriptionId))
        tmp.append(struct.pack('!i', len(self.MonitoredItemIds)))
        for i in MonitoredItemIds:
            tmp.append(struct.pack(self._MonitoredItemIds_fmt, self.MonitoredItemIds))
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.RequestHeader.from_binary(data)
            self.SubscriptionId = struct.unpack(self._SubscriptionId_fmt, data.read(self._SubscriptionId_fmt_size))
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    self.MonitoredItemIds = struct.unpack(self._MonitoredItemIds_fmt, data.read(self._MonitoredItemIds_fmt_size))
            return data
            
class DeleteMonitoredItemsResponse(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.ResponseHeader = None
        self.Results = []
        self.DiagnosticInfos = []
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.ResponseHeader.to_binary())
        tmp.append(struct.pack('!i', len(self.Results)))
        for i in Results:
            tmp.append(self.Results.to_binary())
        tmp.append(struct.pack('!i', len(self.DiagnosticInfos)))
        for i in DiagnosticInfos:
            tmp.append(self.DiagnosticInfos.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.ResponseHeader.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.Results.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.DiagnosticInfos.from_binary(data)
            return data
            
class CreateSubscriptionRequest(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.RequestHeader = None
        self.RequestedPublishingInterval = None
        self._RequestedPublishingInterval_fmt = '!d'
        self._RequestedPublishingInterval_fmt_size = 8
        self.RequestedLifetimeCount = None
        self._RequestedLifetimeCount_fmt = '!I'
        self._RequestedLifetimeCount_fmt_size = 4
        self.RequestedMaxKeepAliveCount = None
        self._RequestedMaxKeepAliveCount_fmt = '!I'
        self._RequestedMaxKeepAliveCount_fmt_size = 4
        self.MaxNotificationsPerPublish = None
        self._MaxNotificationsPerPublish_fmt = '!I'
        self._MaxNotificationsPerPublish_fmt_size = 4
        self.PublishingEnabled = None
        self._PublishingEnabled_fmt = '!?'
        self._PublishingEnabled_fmt_size = 1
        self.Priority = None
        self._Priority_fmt = '!c'
        self._Priority_fmt_size = 1
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.RequestHeader.to_binary())
        tmp.append(struct.pack(self._RequestedPublishingInterval_fmt, self.RequestedPublishingInterval))
        tmp.append(struct.pack(self._RequestedLifetimeCount_fmt, self.RequestedLifetimeCount))
        tmp.append(struct.pack(self._RequestedMaxKeepAliveCount_fmt, self.RequestedMaxKeepAliveCount))
        tmp.append(struct.pack(self._MaxNotificationsPerPublish_fmt, self.MaxNotificationsPerPublish))
        tmp.append(struct.pack(self._PublishingEnabled_fmt, self.PublishingEnabled))
        tmp.append(struct.pack(self._Priority_fmt, self.Priority))
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.RequestHeader.from_binary(data)
            self.RequestedPublishingInterval = struct.unpack(self._RequestedPublishingInterval_fmt, data.read(self._RequestedPublishingInterval_fmt_size))
            self.RequestedLifetimeCount = struct.unpack(self._RequestedLifetimeCount_fmt, data.read(self._RequestedLifetimeCount_fmt_size))
            self.RequestedMaxKeepAliveCount = struct.unpack(self._RequestedMaxKeepAliveCount_fmt, data.read(self._RequestedMaxKeepAliveCount_fmt_size))
            self.MaxNotificationsPerPublish = struct.unpack(self._MaxNotificationsPerPublish_fmt, data.read(self._MaxNotificationsPerPublish_fmt_size))
            self.PublishingEnabled = struct.unpack(self._PublishingEnabled_fmt, data.read(self._PublishingEnabled_fmt_size))
            self.Priority = struct.unpack(self._Priority_fmt, data.read(self._Priority_fmt_size))
            return data
            
class CreateSubscriptionResponse(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.ResponseHeader = None
        self.SubscriptionId = None
        self._SubscriptionId_fmt = '!I'
        self._SubscriptionId_fmt_size = 4
        self.RevisedPublishingInterval = None
        self._RevisedPublishingInterval_fmt = '!d'
        self._RevisedPublishingInterval_fmt_size = 8
        self.RevisedLifetimeCount = None
        self._RevisedLifetimeCount_fmt = '!I'
        self._RevisedLifetimeCount_fmt_size = 4
        self.RevisedMaxKeepAliveCount = None
        self._RevisedMaxKeepAliveCount_fmt = '!I'
        self._RevisedMaxKeepAliveCount_fmt_size = 4
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.ResponseHeader.to_binary())
        tmp.append(struct.pack(self._SubscriptionId_fmt, self.SubscriptionId))
        tmp.append(struct.pack(self._RevisedPublishingInterval_fmt, self.RevisedPublishingInterval))
        tmp.append(struct.pack(self._RevisedLifetimeCount_fmt, self.RevisedLifetimeCount))
        tmp.append(struct.pack(self._RevisedMaxKeepAliveCount_fmt, self.RevisedMaxKeepAliveCount))
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.ResponseHeader.from_binary(data)
            self.SubscriptionId = struct.unpack(self._SubscriptionId_fmt, data.read(self._SubscriptionId_fmt_size))
            self.RevisedPublishingInterval = struct.unpack(self._RevisedPublishingInterval_fmt, data.read(self._RevisedPublishingInterval_fmt_size))
            self.RevisedLifetimeCount = struct.unpack(self._RevisedLifetimeCount_fmt, data.read(self._RevisedLifetimeCount_fmt_size))
            self.RevisedMaxKeepAliveCount = struct.unpack(self._RevisedMaxKeepAliveCount_fmt, data.read(self._RevisedMaxKeepAliveCount_fmt_size))
            return data
            
class ModifySubscriptionRequest(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.RequestHeader = None
        self.SubscriptionId = None
        self._SubscriptionId_fmt = '!I'
        self._SubscriptionId_fmt_size = 4
        self.RequestedPublishingInterval = None
        self._RequestedPublishingInterval_fmt = '!d'
        self._RequestedPublishingInterval_fmt_size = 8
        self.RequestedLifetimeCount = None
        self._RequestedLifetimeCount_fmt = '!I'
        self._RequestedLifetimeCount_fmt_size = 4
        self.RequestedMaxKeepAliveCount = None
        self._RequestedMaxKeepAliveCount_fmt = '!I'
        self._RequestedMaxKeepAliveCount_fmt_size = 4
        self.MaxNotificationsPerPublish = None
        self._MaxNotificationsPerPublish_fmt = '!I'
        self._MaxNotificationsPerPublish_fmt_size = 4
        self.Priority = None
        self._Priority_fmt = '!c'
        self._Priority_fmt_size = 1
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.RequestHeader.to_binary())
        tmp.append(struct.pack(self._SubscriptionId_fmt, self.SubscriptionId))
        tmp.append(struct.pack(self._RequestedPublishingInterval_fmt, self.RequestedPublishingInterval))
        tmp.append(struct.pack(self._RequestedLifetimeCount_fmt, self.RequestedLifetimeCount))
        tmp.append(struct.pack(self._RequestedMaxKeepAliveCount_fmt, self.RequestedMaxKeepAliveCount))
        tmp.append(struct.pack(self._MaxNotificationsPerPublish_fmt, self.MaxNotificationsPerPublish))
        tmp.append(struct.pack(self._Priority_fmt, self.Priority))
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.RequestHeader.from_binary(data)
            self.SubscriptionId = struct.unpack(self._SubscriptionId_fmt, data.read(self._SubscriptionId_fmt_size))
            self.RequestedPublishingInterval = struct.unpack(self._RequestedPublishingInterval_fmt, data.read(self._RequestedPublishingInterval_fmt_size))
            self.RequestedLifetimeCount = struct.unpack(self._RequestedLifetimeCount_fmt, data.read(self._RequestedLifetimeCount_fmt_size))
            self.RequestedMaxKeepAliveCount = struct.unpack(self._RequestedMaxKeepAliveCount_fmt, data.read(self._RequestedMaxKeepAliveCount_fmt_size))
            self.MaxNotificationsPerPublish = struct.unpack(self._MaxNotificationsPerPublish_fmt, data.read(self._MaxNotificationsPerPublish_fmt_size))
            self.Priority = struct.unpack(self._Priority_fmt, data.read(self._Priority_fmt_size))
            return data
            
class ModifySubscriptionResponse(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.ResponseHeader = None
        self.RevisedPublishingInterval = None
        self._RevisedPublishingInterval_fmt = '!d'
        self._RevisedPublishingInterval_fmt_size = 8
        self.RevisedLifetimeCount = None
        self._RevisedLifetimeCount_fmt = '!I'
        self._RevisedLifetimeCount_fmt_size = 4
        self.RevisedMaxKeepAliveCount = None
        self._RevisedMaxKeepAliveCount_fmt = '!I'
        self._RevisedMaxKeepAliveCount_fmt_size = 4
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.ResponseHeader.to_binary())
        tmp.append(struct.pack(self._RevisedPublishingInterval_fmt, self.RevisedPublishingInterval))
        tmp.append(struct.pack(self._RevisedLifetimeCount_fmt, self.RevisedLifetimeCount))
        tmp.append(struct.pack(self._RevisedMaxKeepAliveCount_fmt, self.RevisedMaxKeepAliveCount))
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.ResponseHeader.from_binary(data)
            self.RevisedPublishingInterval = struct.unpack(self._RevisedPublishingInterval_fmt, data.read(self._RevisedPublishingInterval_fmt_size))
            self.RevisedLifetimeCount = struct.unpack(self._RevisedLifetimeCount_fmt, data.read(self._RevisedLifetimeCount_fmt_size))
            self.RevisedMaxKeepAliveCount = struct.unpack(self._RevisedMaxKeepAliveCount_fmt, data.read(self._RevisedMaxKeepAliveCount_fmt_size))
            return data
            
class SetPublishingModeRequest(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.RequestHeader = None
        self.PublishingEnabled = None
        self._PublishingEnabled_fmt = '!?'
        self._PublishingEnabled_fmt_size = 1
        self.SubscriptionIds = []
        self._SubscriptionIds_fmt = '!I'
        self._SubscriptionIds_fmt_size = 4
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.RequestHeader.to_binary())
        tmp.append(struct.pack(self._PublishingEnabled_fmt, self.PublishingEnabled))
        tmp.append(struct.pack('!i', len(self.SubscriptionIds)))
        for i in SubscriptionIds:
            tmp.append(struct.pack(self._SubscriptionIds_fmt, self.SubscriptionIds))
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.RequestHeader.from_binary(data)
            self.PublishingEnabled = struct.unpack(self._PublishingEnabled_fmt, data.read(self._PublishingEnabled_fmt_size))
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    self.SubscriptionIds = struct.unpack(self._SubscriptionIds_fmt, data.read(self._SubscriptionIds_fmt_size))
            return data
            
class SetPublishingModeResponse(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.ResponseHeader = None
        self.Results = []
        self.DiagnosticInfos = []
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.ResponseHeader.to_binary())
        tmp.append(struct.pack('!i', len(self.Results)))
        for i in Results:
            tmp.append(self.Results.to_binary())
        tmp.append(struct.pack('!i', len(self.DiagnosticInfos)))
        for i in DiagnosticInfos:
            tmp.append(self.DiagnosticInfos.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.ResponseHeader.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.Results.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.DiagnosticInfos.from_binary(data)
            return data
            
class NotificationMessage(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.SequenceNumber = None
        self._SequenceNumber_fmt = '!I'
        self._SequenceNumber_fmt_size = 4
        self.PublishTime = None
        self._PublishTime_fmt = '!d'
        self._PublishTime_fmt_size = 8
        self.NotificationData = []
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(struct.pack(self._SequenceNumber_fmt, self.SequenceNumber))
        tmp.append(struct.pack(self._PublishTime_fmt, self.PublishTime))
        tmp.append(struct.pack('!i', len(self.NotificationData)))
        for i in NotificationData:
            tmp.append(self.NotificationData.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            self.SequenceNumber = struct.unpack(self._SequenceNumber_fmt, data.read(self._SequenceNumber_fmt_size))
            self.PublishTime = struct.unpack(self._PublishTime_fmt, data.read(self._PublishTime_fmt_size))
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.NotificationData.from_binary(data)
            return data
            
class NotificationData(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
        tmp.append(struct.pack('!i', len(self.Body)))
        for i in Body:
            tmp.append(struct.pack(self._Body_fmt, self.Body))
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    self.Body = struct.unpack(self._Body_fmt, data.read(self._Body_fmt_size))
            return data
            
class MonitoredItemNotification(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.ClientHandle = None
        self._ClientHandle_fmt = '!I'
        self._ClientHandle_fmt_size = 4
        self.Value = None
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(struct.pack(self._ClientHandle_fmt, self.ClientHandle))
        tmp.append(self.Value.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            self.ClientHandle = struct.unpack(self._ClientHandle_fmt, data.read(self._ClientHandle_fmt_size))
            data = self.Value.from_binary(data)
            return data
            
class DataChangeNotification(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.MonitoredItems = []
        self.DiagnosticInfos = []
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(struct.pack('!i', len(self.MonitoredItems)))
        for i in MonitoredItems:
            tmp.append(self.MonitoredItems.to_binary())
        tmp.append(struct.pack('!i', len(self.DiagnosticInfos)))
        for i in DiagnosticInfos:
            tmp.append(self.DiagnosticInfos.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.MonitoredItems.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.DiagnosticInfos.from_binary(data)
            return data
            
class EventFieldList(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.ClientHandle = None
        self._ClientHandle_fmt = '!I'
        self._ClientHandle_fmt_size = 4
        self.EventFields = []
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(struct.pack(self._ClientHandle_fmt, self.ClientHandle))
        tmp.append(struct.pack('!i', len(self.EventFields)))
        for i in EventFields:
            tmp.append(self.EventFields.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            self.ClientHandle = struct.unpack(self._ClientHandle_fmt, data.read(self._ClientHandle_fmt_size))
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.EventFields.from_binary(data)
            return data
            
class EventNotificationList(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.Events = []
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(struct.pack('!i', len(self.Events)))
        for i in Events:
            tmp.append(self.Events.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.Events.from_binary(data)
            return data
            
class HistoryEventFieldList(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.EventFields = []
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(struct.pack('!i', len(self.EventFields)))
        for i in EventFields:
            tmp.append(self.EventFields.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.EventFields.from_binary(data)
            return data
            
class HistoryEvent(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.Events = []
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(struct.pack('!i', len(self.Events)))
        for i in Events:
            tmp.append(self.Events.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.Events.from_binary(data)
            return data
            
class UpdateEventDetails(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.NodeId = None
        self.PerformInsertReplace = None
        self.Filter = None
        self.EventData = []
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.NodeId.to_binary())
        tmp.append(self.PerformInsertReplace.to_binary())
        tmp.append(self.Filter.to_binary())
        tmp.append(struct.pack('!i', len(self.EventData)))
        for i in EventData:
            tmp.append(self.EventData.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.NodeId.from_binary(data)
            data = self.PerformInsertReplace.from_binary(data)
            data = self.Filter.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.EventData.from_binary(data)
            return data
            
class StatusChangeNotification(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.Status = None
        self.DiagnosticInfo = None
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.Status.to_binary())
        tmp.append(self.DiagnosticInfo.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.Status.from_binary(data)
            data = self.DiagnosticInfo.from_binary(data)
            return data
            
class SubscriptionAcknowledgement(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.SubscriptionId = None
        self._SubscriptionId_fmt = '!I'
        self._SubscriptionId_fmt_size = 4
        self.SequenceNumber = None
        self._SequenceNumber_fmt = '!I'
        self._SequenceNumber_fmt_size = 4
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(struct.pack(self._SubscriptionId_fmt, self.SubscriptionId))
        tmp.append(struct.pack(self._SequenceNumber_fmt, self.SequenceNumber))
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            self.SubscriptionId = struct.unpack(self._SubscriptionId_fmt, data.read(self._SubscriptionId_fmt_size))
            self.SequenceNumber = struct.unpack(self._SequenceNumber_fmt, data.read(self._SequenceNumber_fmt_size))
            return data
            
class PublishRequest(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.RequestHeader = None
        self.SubscriptionAcknowledgements = []
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.RequestHeader.to_binary())
        tmp.append(struct.pack('!i', len(self.SubscriptionAcknowledgements)))
        for i in SubscriptionAcknowledgements:
            tmp.append(self.SubscriptionAcknowledgements.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.RequestHeader.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.SubscriptionAcknowledgements.from_binary(data)
            return data
            
class PublishResponse(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.ResponseHeader = None
        self.SubscriptionId = None
        self._SubscriptionId_fmt = '!I'
        self._SubscriptionId_fmt_size = 4
        self.AvailableSequenceNumbers = []
        self._AvailableSequenceNumbers_fmt = '!I'
        self._AvailableSequenceNumbers_fmt_size = 4
        self.MoreNotifications = None
        self._MoreNotifications_fmt = '!?'
        self._MoreNotifications_fmt_size = 1
        self.NotificationMessage = None
        self.Results = []
        self.DiagnosticInfos = []
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.ResponseHeader.to_binary())
        tmp.append(struct.pack(self._SubscriptionId_fmt, self.SubscriptionId))
        tmp.append(struct.pack('!i', len(self.AvailableSequenceNumbers)))
        for i in AvailableSequenceNumbers:
            tmp.append(struct.pack(self._AvailableSequenceNumbers_fmt, self.AvailableSequenceNumbers))
        tmp.append(struct.pack(self._MoreNotifications_fmt, self.MoreNotifications))
        tmp.append(self.NotificationMessage.to_binary())
        tmp.append(struct.pack('!i', len(self.Results)))
        for i in Results:
            tmp.append(self.Results.to_binary())
        tmp.append(struct.pack('!i', len(self.DiagnosticInfos)))
        for i in DiagnosticInfos:
            tmp.append(self.DiagnosticInfos.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.ResponseHeader.from_binary(data)
            self.SubscriptionId = struct.unpack(self._SubscriptionId_fmt, data.read(self._SubscriptionId_fmt_size))
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    self.AvailableSequenceNumbers = struct.unpack(self._AvailableSequenceNumbers_fmt, data.read(self._AvailableSequenceNumbers_fmt_size))
            self.MoreNotifications = struct.unpack(self._MoreNotifications_fmt, data.read(self._MoreNotifications_fmt_size))
            data = self.NotificationMessage.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.Results.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.DiagnosticInfos.from_binary(data)
            return data
            
class RepublishRequest(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.RequestHeader = None
        self.SubscriptionId = None
        self._SubscriptionId_fmt = '!I'
        self._SubscriptionId_fmt_size = 4
        self.RetransmitSequenceNumber = None
        self._RetransmitSequenceNumber_fmt = '!I'
        self._RetransmitSequenceNumber_fmt_size = 4
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.RequestHeader.to_binary())
        tmp.append(struct.pack(self._SubscriptionId_fmt, self.SubscriptionId))
        tmp.append(struct.pack(self._RetransmitSequenceNumber_fmt, self.RetransmitSequenceNumber))
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.RequestHeader.from_binary(data)
            self.SubscriptionId = struct.unpack(self._SubscriptionId_fmt, data.read(self._SubscriptionId_fmt_size))
            self.RetransmitSequenceNumber = struct.unpack(self._RetransmitSequenceNumber_fmt, data.read(self._RetransmitSequenceNumber_fmt_size))
            return data
            
class RepublishResponse(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.ResponseHeader = None
        self.NotificationMessage = None
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.ResponseHeader.to_binary())
        tmp.append(self.NotificationMessage.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.ResponseHeader.from_binary(data)
            data = self.NotificationMessage.from_binary(data)
            return data
            
class TransferResult(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.StatusCode = None
        self.AvailableSequenceNumbers = []
        self._AvailableSequenceNumbers_fmt = '!I'
        self._AvailableSequenceNumbers_fmt_size = 4
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.StatusCode.to_binary())
        tmp.append(struct.pack('!i', len(self.AvailableSequenceNumbers)))
        for i in AvailableSequenceNumbers:
            tmp.append(struct.pack(self._AvailableSequenceNumbers_fmt, self.AvailableSequenceNumbers))
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.StatusCode.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    self.AvailableSequenceNumbers = struct.unpack(self._AvailableSequenceNumbers_fmt, data.read(self._AvailableSequenceNumbers_fmt_size))
            return data
            
class TransferSubscriptionsRequest(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.RequestHeader = None
        self.SubscriptionIds = []
        self._SubscriptionIds_fmt = '!I'
        self._SubscriptionIds_fmt_size = 4
        self.SendInitialValues = None
        self._SendInitialValues_fmt = '!?'
        self._SendInitialValues_fmt_size = 1
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.RequestHeader.to_binary())
        tmp.append(struct.pack('!i', len(self.SubscriptionIds)))
        for i in SubscriptionIds:
            tmp.append(struct.pack(self._SubscriptionIds_fmt, self.SubscriptionIds))
        tmp.append(struct.pack(self._SendInitialValues_fmt, self.SendInitialValues))
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.RequestHeader.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    self.SubscriptionIds = struct.unpack(self._SubscriptionIds_fmt, data.read(self._SubscriptionIds_fmt_size))
            self.SendInitialValues = struct.unpack(self._SendInitialValues_fmt, data.read(self._SendInitialValues_fmt_size))
            return data
            
class TransferSubscriptionsResponse(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.ResponseHeader = None
        self.Results = []
        self.DiagnosticInfos = []
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.ResponseHeader.to_binary())
        tmp.append(struct.pack('!i', len(self.Results)))
        for i in Results:
            tmp.append(self.Results.to_binary())
        tmp.append(struct.pack('!i', len(self.DiagnosticInfos)))
        for i in DiagnosticInfos:
            tmp.append(self.DiagnosticInfos.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.ResponseHeader.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.Results.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.DiagnosticInfos.from_binary(data)
            return data
            
class DeleteSubscriptionsRequest(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.RequestHeader = None
        self.SubscriptionIds = []
        self._SubscriptionIds_fmt = '!I'
        self._SubscriptionIds_fmt_size = 4
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.RequestHeader.to_binary())
        tmp.append(struct.pack('!i', len(self.SubscriptionIds)))
        for i in SubscriptionIds:
            tmp.append(struct.pack(self._SubscriptionIds_fmt, self.SubscriptionIds))
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.RequestHeader.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    self.SubscriptionIds = struct.unpack(self._SubscriptionIds_fmt, data.read(self._SubscriptionIds_fmt_size))
            return data
            
class DeleteSubscriptionsResponse(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.ResponseHeader = None
        self.Results = []
        self.DiagnosticInfos = []
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.ResponseHeader.to_binary())
        tmp.append(struct.pack('!i', len(self.Results)))
        for i in Results:
            tmp.append(self.Results.to_binary())
        tmp.append(struct.pack('!i', len(self.DiagnosticInfos)))
        for i in DiagnosticInfos:
            tmp.append(self.DiagnosticInfos.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.ResponseHeader.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.Results.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.DiagnosticInfos.from_binary(data)
            return data
            
class ScalarTestType(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.Boolean = None
        self._Boolean_fmt = '!?'
        self._Boolean_fmt_size = 1
        self.SByte = None
        self._SByte_fmt = '!B'
        self._SByte_fmt_size = 1
        self.Byte = None
        self._Byte_fmt = '!c'
        self._Byte_fmt_size = 1
        self.Int16 = None
        self._Int16_fmt = '!h'
        self._Int16_fmt_size = 2
        self.UInt16 = None
        self._UInt16_fmt = '!H'
        self._UInt16_fmt_size = 2
        self.Int32 = None
        self._Int32_fmt = '!i'
        self._Int32_fmt_size = 4
        self.UInt32 = None
        self._UInt32_fmt = '!I'
        self._UInt32_fmt_size = 4
        self.Int64 = None
        self._Int64_fmt = '!q'
        self._Int64_fmt_size = 8
        self.UInt64 = None
        self._UInt64_fmt = '!Q'
        self._UInt64_fmt_size = 8
        self.Float = None
        self._Float_fmt = '!f'
        self._Float_fmt_size = 4
        self.Double = None
        self._Double_fmt = '!d'
        self._Double_fmt_size = 8
        self.String = None
        self.DateTime = None
        self._DateTime_fmt = '!d'
        self._DateTime_fmt_size = 8
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
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(struct.pack(self._Boolean_fmt, self.Boolean))
        tmp.append(struct.pack(self._SByte_fmt, self.SByte))
        tmp.append(struct.pack(self._Byte_fmt, self.Byte))
        tmp.append(struct.pack(self._Int16_fmt, self.Int16))
        tmp.append(struct.pack(self._UInt16_fmt, self.UInt16))
        tmp.append(struct.pack(self._Int32_fmt, self.Int32))
        tmp.append(struct.pack(self._UInt32_fmt, self.UInt32))
        tmp.append(struct.pack(self._Int64_fmt, self.Int64))
        tmp.append(struct.pack(self._UInt64_fmt, self.UInt64))
        tmp.append(struct.pack(self._Float_fmt, self.Float))
        tmp.append(struct.pack(self._Double_fmt, self.Double))
        tmp.append(self.String.to_binary())
        tmp.append(struct.pack(self._DateTime_fmt, self.DateTime))
        tmp.append(self.Guid.to_binary())
        tmp.append(self.ByteString.to_binary())
        tmp.append(self.XmlElement.to_binary())
        tmp.append(self.NodeId.to_binary())
        tmp.append(self.ExpandedNodeId.to_binary())
        tmp.append(self.StatusCode.to_binary())
        tmp.append(self.DiagnosticInfo.to_binary())
        tmp.append(self.QualifiedName.to_binary())
        tmp.append(self.LocalizedText.to_binary())
        tmp.append(self.ExtensionObject.to_binary())
        tmp.append(self.DataValue.to_binary())
        tmp.append(self.EnumeratedValue.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            self.Boolean = struct.unpack(self._Boolean_fmt, data.read(self._Boolean_fmt_size))
            self.SByte = struct.unpack(self._SByte_fmt, data.read(self._SByte_fmt_size))
            self.Byte = struct.unpack(self._Byte_fmt, data.read(self._Byte_fmt_size))
            self.Int16 = struct.unpack(self._Int16_fmt, data.read(self._Int16_fmt_size))
            self.UInt16 = struct.unpack(self._UInt16_fmt, data.read(self._UInt16_fmt_size))
            self.Int32 = struct.unpack(self._Int32_fmt, data.read(self._Int32_fmt_size))
            self.UInt32 = struct.unpack(self._UInt32_fmt, data.read(self._UInt32_fmt_size))
            self.Int64 = struct.unpack(self._Int64_fmt, data.read(self._Int64_fmt_size))
            self.UInt64 = struct.unpack(self._UInt64_fmt, data.read(self._UInt64_fmt_size))
            self.Float = struct.unpack(self._Float_fmt, data.read(self._Float_fmt_size))
            self.Double = struct.unpack(self._Double_fmt, data.read(self._Double_fmt_size))
            data = self.String.from_binary(data)
            self.DateTime = struct.unpack(self._DateTime_fmt, data.read(self._DateTime_fmt_size))
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
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.Booleans = []
        self._Booleans_fmt = '!?'
        self._Booleans_fmt_size = 1
        self.SBytes = []
        self._SBytes_fmt = '!B'
        self._SBytes_fmt_size = 1
        self.Int16s = []
        self._Int16s_fmt = '!h'
        self._Int16s_fmt_size = 2
        self.UInt16s = []
        self._UInt16s_fmt = '!H'
        self._UInt16s_fmt_size = 2
        self.Int32s = []
        self._Int32s_fmt = '!i'
        self._Int32s_fmt_size = 4
        self.UInt32s = []
        self._UInt32s_fmt = '!I'
        self._UInt32s_fmt_size = 4
        self.Int64s = []
        self._Int64s_fmt = '!q'
        self._Int64s_fmt_size = 8
        self.UInt64s = []
        self._UInt64s_fmt = '!Q'
        self._UInt64s_fmt_size = 8
        self.Floats = []
        self._Floats_fmt = '!f'
        self._Floats_fmt_size = 4
        self.Doubles = []
        self._Doubles_fmt = '!d'
        self._Doubles_fmt_size = 8
        self.Strings = []
        self.DateTimes = []
        self._DateTimes_fmt = '!d'
        self._DateTimes_fmt_size = 8
        self.Guids = []
        self.ByteStrings = []
        self.XmlElements = []
        self.NodeIds = []
        self.ExpandedNodeIds = []
        self.StatusCodes = []
        self.DiagnosticInfos = []
        self.QualifiedNames = []
        self.LocalizedTexts = []
        self.ExtensionObjects = []
        self.DataValues = []
        self.Variants = []
        self.EnumeratedValues = []
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(struct.pack('!i', len(self.Booleans)))
        for i in Booleans:
            tmp.append(struct.pack(self._Booleans_fmt, self.Booleans))
        tmp.append(struct.pack('!i', len(self.SBytes)))
        for i in SBytes:
            tmp.append(struct.pack(self._SBytes_fmt, self.SBytes))
        tmp.append(struct.pack('!i', len(self.Int16s)))
        for i in Int16s:
            tmp.append(struct.pack(self._Int16s_fmt, self.Int16s))
        tmp.append(struct.pack('!i', len(self.UInt16s)))
        for i in UInt16s:
            tmp.append(struct.pack(self._UInt16s_fmt, self.UInt16s))
        tmp.append(struct.pack('!i', len(self.Int32s)))
        for i in Int32s:
            tmp.append(struct.pack(self._Int32s_fmt, self.Int32s))
        tmp.append(struct.pack('!i', len(self.UInt32s)))
        for i in UInt32s:
            tmp.append(struct.pack(self._UInt32s_fmt, self.UInt32s))
        tmp.append(struct.pack('!i', len(self.Int64s)))
        for i in Int64s:
            tmp.append(struct.pack(self._Int64s_fmt, self.Int64s))
        tmp.append(struct.pack('!i', len(self.UInt64s)))
        for i in UInt64s:
            tmp.append(struct.pack(self._UInt64s_fmt, self.UInt64s))
        tmp.append(struct.pack('!i', len(self.Floats)))
        for i in Floats:
            tmp.append(struct.pack(self._Floats_fmt, self.Floats))
        tmp.append(struct.pack('!i', len(self.Doubles)))
        for i in Doubles:
            tmp.append(struct.pack(self._Doubles_fmt, self.Doubles))
        tmp.append(struct.pack('!i', len(self.Strings)))
        for i in Strings:
            tmp.append(self.Strings.to_binary())
        tmp.append(struct.pack('!i', len(self.DateTimes)))
        for i in DateTimes:
            tmp.append(struct.pack(self._DateTimes_fmt, self.DateTimes))
        tmp.append(struct.pack('!i', len(self.Guids)))
        for i in Guids:
            tmp.append(self.Guids.to_binary())
        tmp.append(struct.pack('!i', len(self.ByteStrings)))
        for i in ByteStrings:
            tmp.append(self.ByteStrings.to_binary())
        tmp.append(struct.pack('!i', len(self.XmlElements)))
        for i in XmlElements:
            tmp.append(self.XmlElements.to_binary())
        tmp.append(struct.pack('!i', len(self.NodeIds)))
        for i in NodeIds:
            tmp.append(self.NodeIds.to_binary())
        tmp.append(struct.pack('!i', len(self.ExpandedNodeIds)))
        for i in ExpandedNodeIds:
            tmp.append(self.ExpandedNodeIds.to_binary())
        tmp.append(struct.pack('!i', len(self.StatusCodes)))
        for i in StatusCodes:
            tmp.append(self.StatusCodes.to_binary())
        tmp.append(struct.pack('!i', len(self.DiagnosticInfos)))
        for i in DiagnosticInfos:
            tmp.append(self.DiagnosticInfos.to_binary())
        tmp.append(struct.pack('!i', len(self.QualifiedNames)))
        for i in QualifiedNames:
            tmp.append(self.QualifiedNames.to_binary())
        tmp.append(struct.pack('!i', len(self.LocalizedTexts)))
        for i in LocalizedTexts:
            tmp.append(self.LocalizedTexts.to_binary())
        tmp.append(struct.pack('!i', len(self.ExtensionObjects)))
        for i in ExtensionObjects:
            tmp.append(self.ExtensionObjects.to_binary())
        tmp.append(struct.pack('!i', len(self.DataValues)))
        for i in DataValues:
            tmp.append(self.DataValues.to_binary())
        tmp.append(struct.pack('!i', len(self.Variants)))
        for i in Variants:
            tmp.append(self.Variants.to_binary())
        tmp.append(struct.pack('!i', len(self.EnumeratedValues)))
        for i in EnumeratedValues:
            tmp.append(self.EnumeratedValues.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    self.Booleans = struct.unpack(self._Booleans_fmt, data.read(self._Booleans_fmt_size))
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    self.SBytes = struct.unpack(self._SBytes_fmt, data.read(self._SBytes_fmt_size))
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    self.Int16s = struct.unpack(self._Int16s_fmt, data.read(self._Int16s_fmt_size))
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    self.UInt16s = struct.unpack(self._UInt16s_fmt, data.read(self._UInt16s_fmt_size))
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    self.Int32s = struct.unpack(self._Int32s_fmt, data.read(self._Int32s_fmt_size))
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    self.UInt32s = struct.unpack(self._UInt32s_fmt, data.read(self._UInt32s_fmt_size))
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    self.Int64s = struct.unpack(self._Int64s_fmt, data.read(self._Int64s_fmt_size))
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    self.UInt64s = struct.unpack(self._UInt64s_fmt, data.read(self._UInt64s_fmt_size))
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    self.Floats = struct.unpack(self._Floats_fmt, data.read(self._Floats_fmt_size))
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    self.Doubles = struct.unpack(self._Doubles_fmt, data.read(self._Doubles_fmt_size))
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.Strings.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    self.DateTimes = struct.unpack(self._DateTimes_fmt, data.read(self._DateTimes_fmt_size))
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.Guids.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.ByteStrings.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.XmlElements.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.NodeIds.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.ExpandedNodeIds.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.StatusCodes.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.DiagnosticInfos.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.QualifiedNames.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.LocalizedTexts.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.ExtensionObjects.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.DataValues.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.Variants.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.EnumeratedValues.from_binary(data)
            return data
            
class CompositeTestType(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.Field1 = None
        self.Field2 = None
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.Field1.to_binary())
        tmp.append(self.Field2.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.Field1.from_binary(data)
            data = self.Field2.from_binary(data)
            return data
            
class TestStackRequest(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.RequestHeader = None
        self.TestId = None
        self._TestId_fmt = '!I'
        self._TestId_fmt_size = 4
        self.Iteration = None
        self._Iteration_fmt = '!i'
        self._Iteration_fmt_size = 4
        self.Input = None
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.RequestHeader.to_binary())
        tmp.append(struct.pack(self._TestId_fmt, self.TestId))
        tmp.append(struct.pack(self._Iteration_fmt, self.Iteration))
        tmp.append(self.Input.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.RequestHeader.from_binary(data)
            self.TestId = struct.unpack(self._TestId_fmt, data.read(self._TestId_fmt_size))
            self.Iteration = struct.unpack(self._Iteration_fmt, data.read(self._Iteration_fmt_size))
            data = self.Input.from_binary(data)
            return data
            
class TestStackResponse(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.ResponseHeader = None
        self.Output = None
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.ResponseHeader.to_binary())
        tmp.append(self.Output.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.ResponseHeader.from_binary(data)
            data = self.Output.from_binary(data)
            return data
            
class TestStackExRequest(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.RequestHeader = None
        self.TestId = None
        self._TestId_fmt = '!I'
        self._TestId_fmt_size = 4
        self.Iteration = None
        self._Iteration_fmt = '!i'
        self._Iteration_fmt_size = 4
        self.Input = None
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.RequestHeader.to_binary())
        tmp.append(struct.pack(self._TestId_fmt, self.TestId))
        tmp.append(struct.pack(self._Iteration_fmt, self.Iteration))
        tmp.append(self.Input.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.RequestHeader.from_binary(data)
            self.TestId = struct.unpack(self._TestId_fmt, data.read(self._TestId_fmt_size))
            self.Iteration = struct.unpack(self._Iteration_fmt, data.read(self._Iteration_fmt_size))
            data = self.Input.from_binary(data)
            return data
            
class TestStackExResponse(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.ResponseHeader = None
        self.Output = None
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.ResponseHeader.to_binary())
        tmp.append(self.Output.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.ResponseHeader.from_binary(data)
            data = self.Output.from_binary(data)
            return data
            
class BuildInfo(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.ProductUri = None
        self.ManufacturerName = None
        self.ProductName = None
        self.SoftwareVersion = None
        self.BuildNumber = None
        self.BuildDate = None
        self._BuildDate_fmt = '!d'
        self._BuildDate_fmt_size = 8
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.ProductUri.to_binary())
        tmp.append(self.ManufacturerName.to_binary())
        tmp.append(self.ProductName.to_binary())
        tmp.append(self.SoftwareVersion.to_binary())
        tmp.append(self.BuildNumber.to_binary())
        tmp.append(struct.pack(self._BuildDate_fmt, self.BuildDate))
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.ProductUri.from_binary(data)
            data = self.ManufacturerName.from_binary(data)
            data = self.ProductName.from_binary(data)
            data = self.SoftwareVersion.from_binary(data)
            data = self.BuildNumber.from_binary(data)
            self.BuildDate = struct.unpack(self._BuildDate_fmt, data.read(self._BuildDate_fmt_size))
            return data
            
class RedundantServerDataType(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.ServerId = None
        self.ServiceLevel = None
        self._ServiceLevel_fmt = '!c'
        self._ServiceLevel_fmt_size = 1
        self.ServerState = None
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.ServerId.to_binary())
        tmp.append(struct.pack(self._ServiceLevel_fmt, self.ServiceLevel))
        tmp.append(self.ServerState.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.ServerId.from_binary(data)
            self.ServiceLevel = struct.unpack(self._ServiceLevel_fmt, data.read(self._ServiceLevel_fmt_size))
            data = self.ServerState.from_binary(data)
            return data
            
class EndpointUrlListDataType(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.EndpointUrlList = []
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(struct.pack('!i', len(self.EndpointUrlList)))
        for i in EndpointUrlList:
            tmp.append(self.EndpointUrlList.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.EndpointUrlList.from_binary(data)
            return data
            
class NetworkGroupDataType(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.ServerUri = None
        self.NetworkPaths = []
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.ServerUri.to_binary())
        tmp.append(struct.pack('!i', len(self.NetworkPaths)))
        for i in NetworkPaths:
            tmp.append(self.NetworkPaths.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.ServerUri.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.NetworkPaths.from_binary(data)
            return data
            
class SamplingIntervalDiagnosticsDataType(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.SamplingInterval = None
        self._SamplingInterval_fmt = '!d'
        self._SamplingInterval_fmt_size = 8
        self.MonitoredItemCount = None
        self._MonitoredItemCount_fmt = '!I'
        self._MonitoredItemCount_fmt_size = 4
        self.MaxMonitoredItemCount = None
        self._MaxMonitoredItemCount_fmt = '!I'
        self._MaxMonitoredItemCount_fmt_size = 4
        self.DisabledMonitoredItemCount = None
        self._DisabledMonitoredItemCount_fmt = '!I'
        self._DisabledMonitoredItemCount_fmt_size = 4
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(struct.pack(self._SamplingInterval_fmt, self.SamplingInterval))
        tmp.append(struct.pack(self._MonitoredItemCount_fmt, self.MonitoredItemCount))
        tmp.append(struct.pack(self._MaxMonitoredItemCount_fmt, self.MaxMonitoredItemCount))
        tmp.append(struct.pack(self._DisabledMonitoredItemCount_fmt, self.DisabledMonitoredItemCount))
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            self.SamplingInterval = struct.unpack(self._SamplingInterval_fmt, data.read(self._SamplingInterval_fmt_size))
            self.MonitoredItemCount = struct.unpack(self._MonitoredItemCount_fmt, data.read(self._MonitoredItemCount_fmt_size))
            self.MaxMonitoredItemCount = struct.unpack(self._MaxMonitoredItemCount_fmt, data.read(self._MaxMonitoredItemCount_fmt_size))
            self.DisabledMonitoredItemCount = struct.unpack(self._DisabledMonitoredItemCount_fmt, data.read(self._DisabledMonitoredItemCount_fmt_size))
            return data
            
class ServerDiagnosticsSummaryDataType(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.ServerViewCount = None
        self._ServerViewCount_fmt = '!I'
        self._ServerViewCount_fmt_size = 4
        self.CurrentSessionCount = None
        self._CurrentSessionCount_fmt = '!I'
        self._CurrentSessionCount_fmt_size = 4
        self.CumulatedSessionCount = None
        self._CumulatedSessionCount_fmt = '!I'
        self._CumulatedSessionCount_fmt_size = 4
        self.SecurityRejectedSessionCount = None
        self._SecurityRejectedSessionCount_fmt = '!I'
        self._SecurityRejectedSessionCount_fmt_size = 4
        self.RejectedSessionCount = None
        self._RejectedSessionCount_fmt = '!I'
        self._RejectedSessionCount_fmt_size = 4
        self.SessionTimeoutCount = None
        self._SessionTimeoutCount_fmt = '!I'
        self._SessionTimeoutCount_fmt_size = 4
        self.SessionAbortCount = None
        self._SessionAbortCount_fmt = '!I'
        self._SessionAbortCount_fmt_size = 4
        self.CurrentSubscriptionCount = None
        self._CurrentSubscriptionCount_fmt = '!I'
        self._CurrentSubscriptionCount_fmt_size = 4
        self.CumulatedSubscriptionCount = None
        self._CumulatedSubscriptionCount_fmt = '!I'
        self._CumulatedSubscriptionCount_fmt_size = 4
        self.PublishingIntervalCount = None
        self._PublishingIntervalCount_fmt = '!I'
        self._PublishingIntervalCount_fmt_size = 4
        self.SecurityRejectedRequestsCount = None
        self._SecurityRejectedRequestsCount_fmt = '!I'
        self._SecurityRejectedRequestsCount_fmt_size = 4
        self.RejectedRequestsCount = None
        self._RejectedRequestsCount_fmt = '!I'
        self._RejectedRequestsCount_fmt_size = 4
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(struct.pack(self._ServerViewCount_fmt, self.ServerViewCount))
        tmp.append(struct.pack(self._CurrentSessionCount_fmt, self.CurrentSessionCount))
        tmp.append(struct.pack(self._CumulatedSessionCount_fmt, self.CumulatedSessionCount))
        tmp.append(struct.pack(self._SecurityRejectedSessionCount_fmt, self.SecurityRejectedSessionCount))
        tmp.append(struct.pack(self._RejectedSessionCount_fmt, self.RejectedSessionCount))
        tmp.append(struct.pack(self._SessionTimeoutCount_fmt, self.SessionTimeoutCount))
        tmp.append(struct.pack(self._SessionAbortCount_fmt, self.SessionAbortCount))
        tmp.append(struct.pack(self._CurrentSubscriptionCount_fmt, self.CurrentSubscriptionCount))
        tmp.append(struct.pack(self._CumulatedSubscriptionCount_fmt, self.CumulatedSubscriptionCount))
        tmp.append(struct.pack(self._PublishingIntervalCount_fmt, self.PublishingIntervalCount))
        tmp.append(struct.pack(self._SecurityRejectedRequestsCount_fmt, self.SecurityRejectedRequestsCount))
        tmp.append(struct.pack(self._RejectedRequestsCount_fmt, self.RejectedRequestsCount))
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            self.ServerViewCount = struct.unpack(self._ServerViewCount_fmt, data.read(self._ServerViewCount_fmt_size))
            self.CurrentSessionCount = struct.unpack(self._CurrentSessionCount_fmt, data.read(self._CurrentSessionCount_fmt_size))
            self.CumulatedSessionCount = struct.unpack(self._CumulatedSessionCount_fmt, data.read(self._CumulatedSessionCount_fmt_size))
            self.SecurityRejectedSessionCount = struct.unpack(self._SecurityRejectedSessionCount_fmt, data.read(self._SecurityRejectedSessionCount_fmt_size))
            self.RejectedSessionCount = struct.unpack(self._RejectedSessionCount_fmt, data.read(self._RejectedSessionCount_fmt_size))
            self.SessionTimeoutCount = struct.unpack(self._SessionTimeoutCount_fmt, data.read(self._SessionTimeoutCount_fmt_size))
            self.SessionAbortCount = struct.unpack(self._SessionAbortCount_fmt, data.read(self._SessionAbortCount_fmt_size))
            self.CurrentSubscriptionCount = struct.unpack(self._CurrentSubscriptionCount_fmt, data.read(self._CurrentSubscriptionCount_fmt_size))
            self.CumulatedSubscriptionCount = struct.unpack(self._CumulatedSubscriptionCount_fmt, data.read(self._CumulatedSubscriptionCount_fmt_size))
            self.PublishingIntervalCount = struct.unpack(self._PublishingIntervalCount_fmt, data.read(self._PublishingIntervalCount_fmt_size))
            self.SecurityRejectedRequestsCount = struct.unpack(self._SecurityRejectedRequestsCount_fmt, data.read(self._SecurityRejectedRequestsCount_fmt_size))
            self.RejectedRequestsCount = struct.unpack(self._RejectedRequestsCount_fmt, data.read(self._RejectedRequestsCount_fmt_size))
            return data
            
class ServerStatusDataType(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.StartTime = None
        self._StartTime_fmt = '!d'
        self._StartTime_fmt_size = 8
        self.CurrentTime = None
        self._CurrentTime_fmt = '!d'
        self._CurrentTime_fmt_size = 8
        self.State = None
        self.BuildInfo = None
        self.SecondsTillShutdown = None
        self._SecondsTillShutdown_fmt = '!I'
        self._SecondsTillShutdown_fmt_size = 4
        self.ShutdownReason = None
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(struct.pack(self._StartTime_fmt, self.StartTime))
        tmp.append(struct.pack(self._CurrentTime_fmt, self.CurrentTime))
        tmp.append(self.State.to_binary())
        tmp.append(self.BuildInfo.to_binary())
        tmp.append(struct.pack(self._SecondsTillShutdown_fmt, self.SecondsTillShutdown))
        tmp.append(self.ShutdownReason.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            self.StartTime = struct.unpack(self._StartTime_fmt, data.read(self._StartTime_fmt_size))
            self.CurrentTime = struct.unpack(self._CurrentTime_fmt, data.read(self._CurrentTime_fmt_size))
            data = self.State.from_binary(data)
            data = self.BuildInfo.from_binary(data)
            self.SecondsTillShutdown = struct.unpack(self._SecondsTillShutdown_fmt, data.read(self._SecondsTillShutdown_fmt_size))
            data = self.ShutdownReason.from_binary(data)
            return data
            
class SessionSecurityDiagnosticsDataType(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.SessionId = None
        self.ClientUserIdOfSession = None
        self.ClientUserIdHistory = []
        self.AuthenticationMechanism = None
        self.TransportProtocol = None
        self.SecurityMode = None
        self.SecurityPolicyUri = None
        self.ClientCertificate = None
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.SessionId.to_binary())
        tmp.append(self.ClientUserIdOfSession.to_binary())
        tmp.append(struct.pack('!i', len(self.ClientUserIdHistory)))
        for i in ClientUserIdHistory:
            tmp.append(self.ClientUserIdHistory.to_binary())
        tmp.append(self.AuthenticationMechanism.to_binary())
        tmp.append(self.TransportProtocol.to_binary())
        tmp.append(self.SecurityMode.to_binary())
        tmp.append(self.SecurityPolicyUri.to_binary())
        tmp.append(self.ClientCertificate.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.SessionId.from_binary(data)
            data = self.ClientUserIdOfSession.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.ClientUserIdHistory.from_binary(data)
            data = self.AuthenticationMechanism.from_binary(data)
            data = self.TransportProtocol.from_binary(data)
            data = self.SecurityMode.from_binary(data)
            data = self.SecurityPolicyUri.from_binary(data)
            data = self.ClientCertificate.from_binary(data)
            return data
            
class ServiceCounterDataType(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.TotalCount = None
        self._TotalCount_fmt = '!I'
        self._TotalCount_fmt_size = 4
        self.ErrorCount = None
        self._ErrorCount_fmt = '!I'
        self._ErrorCount_fmt_size = 4
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(struct.pack(self._TotalCount_fmt, self.TotalCount))
        tmp.append(struct.pack(self._ErrorCount_fmt, self.ErrorCount))
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            self.TotalCount = struct.unpack(self._TotalCount_fmt, data.read(self._TotalCount_fmt_size))
            self.ErrorCount = struct.unpack(self._ErrorCount_fmt, data.read(self._ErrorCount_fmt_size))
            return data
            
class SessionDiagnosticsDataType(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.SessionId = None
        self.SessionName = None
        self.ClientDescription = None
        self.ServerUri = None
        self.EndpointUrl = None
        self.LocaleIds = []
        self.ActualSessionTimeout = None
        self._ActualSessionTimeout_fmt = '!d'
        self._ActualSessionTimeout_fmt_size = 8
        self.MaxResponseMessageSize = None
        self._MaxResponseMessageSize_fmt = '!I'
        self._MaxResponseMessageSize_fmt_size = 4
        self.ClientConnectionTime = None
        self._ClientConnectionTime_fmt = '!d'
        self._ClientConnectionTime_fmt_size = 8
        self.ClientLastContactTime = None
        self._ClientLastContactTime_fmt = '!d'
        self._ClientLastContactTime_fmt_size = 8
        self.CurrentSubscriptionsCount = None
        self._CurrentSubscriptionsCount_fmt = '!I'
        self._CurrentSubscriptionsCount_fmt_size = 4
        self.CurrentMonitoredItemsCount = None
        self._CurrentMonitoredItemsCount_fmt = '!I'
        self._CurrentMonitoredItemsCount_fmt_size = 4
        self.CurrentPublishRequestsInQueue = None
        self._CurrentPublishRequestsInQueue_fmt = '!I'
        self._CurrentPublishRequestsInQueue_fmt_size = 4
        self.TotalRequestCount = None
        self.UnauthorizedRequestCount = None
        self._UnauthorizedRequestCount_fmt = '!I'
        self._UnauthorizedRequestCount_fmt_size = 4
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
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.SessionId.to_binary())
        tmp.append(self.SessionName.to_binary())
        tmp.append(self.ClientDescription.to_binary())
        tmp.append(self.ServerUri.to_binary())
        tmp.append(self.EndpointUrl.to_binary())
        tmp.append(struct.pack('!i', len(self.LocaleIds)))
        for i in LocaleIds:
            tmp.append(self.LocaleIds.to_binary())
        tmp.append(struct.pack(self._ActualSessionTimeout_fmt, self.ActualSessionTimeout))
        tmp.append(struct.pack(self._MaxResponseMessageSize_fmt, self.MaxResponseMessageSize))
        tmp.append(struct.pack(self._ClientConnectionTime_fmt, self.ClientConnectionTime))
        tmp.append(struct.pack(self._ClientLastContactTime_fmt, self.ClientLastContactTime))
        tmp.append(struct.pack(self._CurrentSubscriptionsCount_fmt, self.CurrentSubscriptionsCount))
        tmp.append(struct.pack(self._CurrentMonitoredItemsCount_fmt, self.CurrentMonitoredItemsCount))
        tmp.append(struct.pack(self._CurrentPublishRequestsInQueue_fmt, self.CurrentPublishRequestsInQueue))
        tmp.append(self.TotalRequestCount.to_binary())
        tmp.append(struct.pack(self._UnauthorizedRequestCount_fmt, self.UnauthorizedRequestCount))
        tmp.append(self.ReadCount.to_binary())
        tmp.append(self.HistoryReadCount.to_binary())
        tmp.append(self.WriteCount.to_binary())
        tmp.append(self.HistoryUpdateCount.to_binary())
        tmp.append(self.CallCount.to_binary())
        tmp.append(self.CreateMonitoredItemsCount.to_binary())
        tmp.append(self.ModifyMonitoredItemsCount.to_binary())
        tmp.append(self.SetMonitoringModeCount.to_binary())
        tmp.append(self.SetTriggeringCount.to_binary())
        tmp.append(self.DeleteMonitoredItemsCount.to_binary())
        tmp.append(self.CreateSubscriptionCount.to_binary())
        tmp.append(self.ModifySubscriptionCount.to_binary())
        tmp.append(self.SetPublishingModeCount.to_binary())
        tmp.append(self.PublishCount.to_binary())
        tmp.append(self.RepublishCount.to_binary())
        tmp.append(self.TransferSubscriptionsCount.to_binary())
        tmp.append(self.DeleteSubscriptionsCount.to_binary())
        tmp.append(self.AddNodesCount.to_binary())
        tmp.append(self.AddReferencesCount.to_binary())
        tmp.append(self.DeleteNodesCount.to_binary())
        tmp.append(self.DeleteReferencesCount.to_binary())
        tmp.append(self.BrowseCount.to_binary())
        tmp.append(self.BrowseNextCount.to_binary())
        tmp.append(self.TranslateBrowsePathsToNodeIdsCount.to_binary())
        tmp.append(self.QueryFirstCount.to_binary())
        tmp.append(self.QueryNextCount.to_binary())
        tmp.append(self.RegisterNodesCount.to_binary())
        tmp.append(self.UnregisterNodesCount.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.SessionId.from_binary(data)
            data = self.SessionName.from_binary(data)
            data = self.ClientDescription.from_binary(data)
            data = self.ServerUri.from_binary(data)
            data = self.EndpointUrl.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.LocaleIds.from_binary(data)
            self.ActualSessionTimeout = struct.unpack(self._ActualSessionTimeout_fmt, data.read(self._ActualSessionTimeout_fmt_size))
            self.MaxResponseMessageSize = struct.unpack(self._MaxResponseMessageSize_fmt, data.read(self._MaxResponseMessageSize_fmt_size))
            self.ClientConnectionTime = struct.unpack(self._ClientConnectionTime_fmt, data.read(self._ClientConnectionTime_fmt_size))
            self.ClientLastContactTime = struct.unpack(self._ClientLastContactTime_fmt, data.read(self._ClientLastContactTime_fmt_size))
            self.CurrentSubscriptionsCount = struct.unpack(self._CurrentSubscriptionsCount_fmt, data.read(self._CurrentSubscriptionsCount_fmt_size))
            self.CurrentMonitoredItemsCount = struct.unpack(self._CurrentMonitoredItemsCount_fmt, data.read(self._CurrentMonitoredItemsCount_fmt_size))
            self.CurrentPublishRequestsInQueue = struct.unpack(self._CurrentPublishRequestsInQueue_fmt, data.read(self._CurrentPublishRequestsInQueue_fmt_size))
            data = self.TotalRequestCount.from_binary(data)
            self.UnauthorizedRequestCount = struct.unpack(self._UnauthorizedRequestCount_fmt, data.read(self._UnauthorizedRequestCount_fmt_size))
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
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.StatusCode = None
        self.DiagnosticInfo = None
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.StatusCode.to_binary())
        tmp.append(self.DiagnosticInfo.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.StatusCode.from_binary(data)
            data = self.DiagnosticInfo.from_binary(data)
            return data
            
class SubscriptionDiagnosticsDataType(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.SessionId = None
        self.SubscriptionId = None
        self._SubscriptionId_fmt = '!I'
        self._SubscriptionId_fmt_size = 4
        self.Priority = None
        self._Priority_fmt = '!c'
        self._Priority_fmt_size = 1
        self.PublishingInterval = None
        self._PublishingInterval_fmt = '!d'
        self._PublishingInterval_fmt_size = 8
        self.MaxKeepAliveCount = None
        self._MaxKeepAliveCount_fmt = '!I'
        self._MaxKeepAliveCount_fmt_size = 4
        self.MaxLifetimeCount = None
        self._MaxLifetimeCount_fmt = '!I'
        self._MaxLifetimeCount_fmt_size = 4
        self.MaxNotificationsPerPublish = None
        self._MaxNotificationsPerPublish_fmt = '!I'
        self._MaxNotificationsPerPublish_fmt_size = 4
        self.PublishingEnabled = None
        self._PublishingEnabled_fmt = '!?'
        self._PublishingEnabled_fmt_size = 1
        self.ModifyCount = None
        self._ModifyCount_fmt = '!I'
        self._ModifyCount_fmt_size = 4
        self.EnableCount = None
        self._EnableCount_fmt = '!I'
        self._EnableCount_fmt_size = 4
        self.DisableCount = None
        self._DisableCount_fmt = '!I'
        self._DisableCount_fmt_size = 4
        self.RepublishRequestCount = None
        self._RepublishRequestCount_fmt = '!I'
        self._RepublishRequestCount_fmt_size = 4
        self.RepublishMessageRequestCount = None
        self._RepublishMessageRequestCount_fmt = '!I'
        self._RepublishMessageRequestCount_fmt_size = 4
        self.RepublishMessageCount = None
        self._RepublishMessageCount_fmt = '!I'
        self._RepublishMessageCount_fmt_size = 4
        self.TransferRequestCount = None
        self._TransferRequestCount_fmt = '!I'
        self._TransferRequestCount_fmt_size = 4
        self.TransferredToAltClientCount = None
        self._TransferredToAltClientCount_fmt = '!I'
        self._TransferredToAltClientCount_fmt_size = 4
        self.TransferredToSameClientCount = None
        self._TransferredToSameClientCount_fmt = '!I'
        self._TransferredToSameClientCount_fmt_size = 4
        self.PublishRequestCount = None
        self._PublishRequestCount_fmt = '!I'
        self._PublishRequestCount_fmt_size = 4
        self.DataChangeNotificationsCount = None
        self._DataChangeNotificationsCount_fmt = '!I'
        self._DataChangeNotificationsCount_fmt_size = 4
        self.EventNotificationsCount = None
        self._EventNotificationsCount_fmt = '!I'
        self._EventNotificationsCount_fmt_size = 4
        self.NotificationsCount = None
        self._NotificationsCount_fmt = '!I'
        self._NotificationsCount_fmt_size = 4
        self.LatePublishRequestCount = None
        self._LatePublishRequestCount_fmt = '!I'
        self._LatePublishRequestCount_fmt_size = 4
        self.CurrentKeepAliveCount = None
        self._CurrentKeepAliveCount_fmt = '!I'
        self._CurrentKeepAliveCount_fmt_size = 4
        self.CurrentLifetimeCount = None
        self._CurrentLifetimeCount_fmt = '!I'
        self._CurrentLifetimeCount_fmt_size = 4
        self.UnacknowledgedMessageCount = None
        self._UnacknowledgedMessageCount_fmt = '!I'
        self._UnacknowledgedMessageCount_fmt_size = 4
        self.DiscardedMessageCount = None
        self._DiscardedMessageCount_fmt = '!I'
        self._DiscardedMessageCount_fmt_size = 4
        self.MonitoredItemCount = None
        self._MonitoredItemCount_fmt = '!I'
        self._MonitoredItemCount_fmt_size = 4
        self.DisabledMonitoredItemCount = None
        self._DisabledMonitoredItemCount_fmt = '!I'
        self._DisabledMonitoredItemCount_fmt_size = 4
        self.MonitoringQueueOverflowCount = None
        self._MonitoringQueueOverflowCount_fmt = '!I'
        self._MonitoringQueueOverflowCount_fmt_size = 4
        self.NextSequenceNumber = None
        self._NextSequenceNumber_fmt = '!I'
        self._NextSequenceNumber_fmt_size = 4
        self.EventQueueOverFlowCount = None
        self._EventQueueOverFlowCount_fmt = '!I'
        self._EventQueueOverFlowCount_fmt_size = 4
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.SessionId.to_binary())
        tmp.append(struct.pack(self._SubscriptionId_fmt, self.SubscriptionId))
        tmp.append(struct.pack(self._Priority_fmt, self.Priority))
        tmp.append(struct.pack(self._PublishingInterval_fmt, self.PublishingInterval))
        tmp.append(struct.pack(self._MaxKeepAliveCount_fmt, self.MaxKeepAliveCount))
        tmp.append(struct.pack(self._MaxLifetimeCount_fmt, self.MaxLifetimeCount))
        tmp.append(struct.pack(self._MaxNotificationsPerPublish_fmt, self.MaxNotificationsPerPublish))
        tmp.append(struct.pack(self._PublishingEnabled_fmt, self.PublishingEnabled))
        tmp.append(struct.pack(self._ModifyCount_fmt, self.ModifyCount))
        tmp.append(struct.pack(self._EnableCount_fmt, self.EnableCount))
        tmp.append(struct.pack(self._DisableCount_fmt, self.DisableCount))
        tmp.append(struct.pack(self._RepublishRequestCount_fmt, self.RepublishRequestCount))
        tmp.append(struct.pack(self._RepublishMessageRequestCount_fmt, self.RepublishMessageRequestCount))
        tmp.append(struct.pack(self._RepublishMessageCount_fmt, self.RepublishMessageCount))
        tmp.append(struct.pack(self._TransferRequestCount_fmt, self.TransferRequestCount))
        tmp.append(struct.pack(self._TransferredToAltClientCount_fmt, self.TransferredToAltClientCount))
        tmp.append(struct.pack(self._TransferredToSameClientCount_fmt, self.TransferredToSameClientCount))
        tmp.append(struct.pack(self._PublishRequestCount_fmt, self.PublishRequestCount))
        tmp.append(struct.pack(self._DataChangeNotificationsCount_fmt, self.DataChangeNotificationsCount))
        tmp.append(struct.pack(self._EventNotificationsCount_fmt, self.EventNotificationsCount))
        tmp.append(struct.pack(self._NotificationsCount_fmt, self.NotificationsCount))
        tmp.append(struct.pack(self._LatePublishRequestCount_fmt, self.LatePublishRequestCount))
        tmp.append(struct.pack(self._CurrentKeepAliveCount_fmt, self.CurrentKeepAliveCount))
        tmp.append(struct.pack(self._CurrentLifetimeCount_fmt, self.CurrentLifetimeCount))
        tmp.append(struct.pack(self._UnacknowledgedMessageCount_fmt, self.UnacknowledgedMessageCount))
        tmp.append(struct.pack(self._DiscardedMessageCount_fmt, self.DiscardedMessageCount))
        tmp.append(struct.pack(self._MonitoredItemCount_fmt, self.MonitoredItemCount))
        tmp.append(struct.pack(self._DisabledMonitoredItemCount_fmt, self.DisabledMonitoredItemCount))
        tmp.append(struct.pack(self._MonitoringQueueOverflowCount_fmt, self.MonitoringQueueOverflowCount))
        tmp.append(struct.pack(self._NextSequenceNumber_fmt, self.NextSequenceNumber))
        tmp.append(struct.pack(self._EventQueueOverFlowCount_fmt, self.EventQueueOverFlowCount))
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.SessionId.from_binary(data)
            self.SubscriptionId = struct.unpack(self._SubscriptionId_fmt, data.read(self._SubscriptionId_fmt_size))
            self.Priority = struct.unpack(self._Priority_fmt, data.read(self._Priority_fmt_size))
            self.PublishingInterval = struct.unpack(self._PublishingInterval_fmt, data.read(self._PublishingInterval_fmt_size))
            self.MaxKeepAliveCount = struct.unpack(self._MaxKeepAliveCount_fmt, data.read(self._MaxKeepAliveCount_fmt_size))
            self.MaxLifetimeCount = struct.unpack(self._MaxLifetimeCount_fmt, data.read(self._MaxLifetimeCount_fmt_size))
            self.MaxNotificationsPerPublish = struct.unpack(self._MaxNotificationsPerPublish_fmt, data.read(self._MaxNotificationsPerPublish_fmt_size))
            self.PublishingEnabled = struct.unpack(self._PublishingEnabled_fmt, data.read(self._PublishingEnabled_fmt_size))
            self.ModifyCount = struct.unpack(self._ModifyCount_fmt, data.read(self._ModifyCount_fmt_size))
            self.EnableCount = struct.unpack(self._EnableCount_fmt, data.read(self._EnableCount_fmt_size))
            self.DisableCount = struct.unpack(self._DisableCount_fmt, data.read(self._DisableCount_fmt_size))
            self.RepublishRequestCount = struct.unpack(self._RepublishRequestCount_fmt, data.read(self._RepublishRequestCount_fmt_size))
            self.RepublishMessageRequestCount = struct.unpack(self._RepublishMessageRequestCount_fmt, data.read(self._RepublishMessageRequestCount_fmt_size))
            self.RepublishMessageCount = struct.unpack(self._RepublishMessageCount_fmt, data.read(self._RepublishMessageCount_fmt_size))
            self.TransferRequestCount = struct.unpack(self._TransferRequestCount_fmt, data.read(self._TransferRequestCount_fmt_size))
            self.TransferredToAltClientCount = struct.unpack(self._TransferredToAltClientCount_fmt, data.read(self._TransferredToAltClientCount_fmt_size))
            self.TransferredToSameClientCount = struct.unpack(self._TransferredToSameClientCount_fmt, data.read(self._TransferredToSameClientCount_fmt_size))
            self.PublishRequestCount = struct.unpack(self._PublishRequestCount_fmt, data.read(self._PublishRequestCount_fmt_size))
            self.DataChangeNotificationsCount = struct.unpack(self._DataChangeNotificationsCount_fmt, data.read(self._DataChangeNotificationsCount_fmt_size))
            self.EventNotificationsCount = struct.unpack(self._EventNotificationsCount_fmt, data.read(self._EventNotificationsCount_fmt_size))
            self.NotificationsCount = struct.unpack(self._NotificationsCount_fmt, data.read(self._NotificationsCount_fmt_size))
            self.LatePublishRequestCount = struct.unpack(self._LatePublishRequestCount_fmt, data.read(self._LatePublishRequestCount_fmt_size))
            self.CurrentKeepAliveCount = struct.unpack(self._CurrentKeepAliveCount_fmt, data.read(self._CurrentKeepAliveCount_fmt_size))
            self.CurrentLifetimeCount = struct.unpack(self._CurrentLifetimeCount_fmt, data.read(self._CurrentLifetimeCount_fmt_size))
            self.UnacknowledgedMessageCount = struct.unpack(self._UnacknowledgedMessageCount_fmt, data.read(self._UnacknowledgedMessageCount_fmt_size))
            self.DiscardedMessageCount = struct.unpack(self._DiscardedMessageCount_fmt, data.read(self._DiscardedMessageCount_fmt_size))
            self.MonitoredItemCount = struct.unpack(self._MonitoredItemCount_fmt, data.read(self._MonitoredItemCount_fmt_size))
            self.DisabledMonitoredItemCount = struct.unpack(self._DisabledMonitoredItemCount_fmt, data.read(self._DisabledMonitoredItemCount_fmt_size))
            self.MonitoringQueueOverflowCount = struct.unpack(self._MonitoringQueueOverflowCount_fmt, data.read(self._MonitoringQueueOverflowCount_fmt_size))
            self.NextSequenceNumber = struct.unpack(self._NextSequenceNumber_fmt, data.read(self._NextSequenceNumber_fmt_size))
            self.EventQueueOverFlowCount = struct.unpack(self._EventQueueOverFlowCount_fmt, data.read(self._EventQueueOverFlowCount_fmt_size))
            return data
            
class ModelChangeStructureDataType(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.Affected = None
        self.AffectedType = None
        self.Verb = None
        self._Verb_fmt = '!c'
        self._Verb_fmt_size = 1
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.Affected.to_binary())
        tmp.append(self.AffectedType.to_binary())
        tmp.append(struct.pack(self._Verb_fmt, self.Verb))
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.Affected.from_binary(data)
            data = self.AffectedType.from_binary(data)
            self.Verb = struct.unpack(self._Verb_fmt, data.read(self._Verb_fmt_size))
            return data
            
class SemanticChangeStructureDataType(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.Affected = None
        self.AffectedType = None
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.Affected.to_binary())
        tmp.append(self.AffectedType.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.Affected.from_binary(data)
            data = self.AffectedType.from_binary(data)
            return data
            
class Range(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.Low = None
        self._Low_fmt = '!d'
        self._Low_fmt_size = 8
        self.High = None
        self._High_fmt = '!d'
        self._High_fmt_size = 8
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(struct.pack(self._Low_fmt, self.Low))
        tmp.append(struct.pack(self._High_fmt, self.High))
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            self.Low = struct.unpack(self._Low_fmt, data.read(self._Low_fmt_size))
            self.High = struct.unpack(self._High_fmt, data.read(self._High_fmt_size))
            return data
            
class EUInformation(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.NamespaceUri = None
        self.UnitId = None
        self._UnitId_fmt = '!i'
        self._UnitId_fmt_size = 4
        self.DisplayName = None
        self.Description = None
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.NamespaceUri.to_binary())
        tmp.append(struct.pack(self._UnitId_fmt, self.UnitId))
        tmp.append(self.DisplayName.to_binary())
        tmp.append(self.Description.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.NamespaceUri.from_binary(data)
            self.UnitId = struct.unpack(self._UnitId_fmt, data.read(self._UnitId_fmt_size))
            data = self.DisplayName.from_binary(data)
            data = self.Description.from_binary(data)
            return data
            
class ComplexNumberType(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.Real = None
        self._Real_fmt = '!f'
        self._Real_fmt_size = 4
        self.Imaginary = None
        self._Imaginary_fmt = '!f'
        self._Imaginary_fmt_size = 4
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(struct.pack(self._Real_fmt, self.Real))
        tmp.append(struct.pack(self._Imaginary_fmt, self.Imaginary))
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            self.Real = struct.unpack(self._Real_fmt, data.read(self._Real_fmt_size))
            self.Imaginary = struct.unpack(self._Imaginary_fmt, data.read(self._Imaginary_fmt_size))
            return data
            
class DoubleComplexNumberType(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.Real = None
        self._Real_fmt = '!d'
        self._Real_fmt_size = 8
        self.Imaginary = None
        self._Imaginary_fmt = '!d'
        self._Imaginary_fmt_size = 8
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(struct.pack(self._Real_fmt, self.Real))
        tmp.append(struct.pack(self._Imaginary_fmt, self.Imaginary))
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            self.Real = struct.unpack(self._Real_fmt, data.read(self._Real_fmt_size))
            self.Imaginary = struct.unpack(self._Imaginary_fmt, data.read(self._Imaginary_fmt_size))
            return data
            
class AxisInformation(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.EngineeringUnits = None
        self.EURange = None
        self.Title = None
        self.AxisScaleType = None
        self.AxisSteps = []
        self._AxisSteps_fmt = '!d'
        self._AxisSteps_fmt_size = 8
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.EngineeringUnits.to_binary())
        tmp.append(self.EURange.to_binary())
        tmp.append(self.Title.to_binary())
        tmp.append(self.AxisScaleType.to_binary())
        tmp.append(struct.pack('!i', len(self.AxisSteps)))
        for i in AxisSteps:
            tmp.append(struct.pack(self._AxisSteps_fmt, self.AxisSteps))
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.EngineeringUnits.from_binary(data)
            data = self.EURange.from_binary(data)
            data = self.Title.from_binary(data)
            data = self.AxisScaleType.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    self.AxisSteps = struct.unpack(self._AxisSteps_fmt, data.read(self._AxisSteps_fmt_size))
            return data
            
class XVType(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.X = None
        self._X_fmt = '!d'
        self._X_fmt_size = 8
        self.Value = None
        self._Value_fmt = '!f'
        self._Value_fmt_size = 4
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(struct.pack(self._X_fmt, self.X))
        tmp.append(struct.pack(self._Value_fmt, self.Value))
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            self.X = struct.unpack(self._X_fmt, data.read(self._X_fmt_size))
            self.Value = struct.unpack(self._Value_fmt, data.read(self._Value_fmt_size))
            return data
            
class ProgramDiagnosticDataType(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.CreateSessionId = None
        self.CreateClientName = None
        self.InvocationCreationTime = None
        self._InvocationCreationTime_fmt = '!d'
        self._InvocationCreationTime_fmt_size = 8
        self.LastTransitionTime = None
        self._LastTransitionTime_fmt = '!d'
        self._LastTransitionTime_fmt_size = 8
        self.LastMethodCall = None
        self.LastMethodSessionId = None
        self.LastMethodInputArguments = []
        self.LastMethodOutputArguments = []
        self.LastMethodCallTime = None
        self._LastMethodCallTime_fmt = '!d'
        self._LastMethodCallTime_fmt_size = 8
        self.LastMethodReturnStatus = None
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.CreateSessionId.to_binary())
        tmp.append(self.CreateClientName.to_binary())
        tmp.append(struct.pack(self._InvocationCreationTime_fmt, self.InvocationCreationTime))
        tmp.append(struct.pack(self._LastTransitionTime_fmt, self.LastTransitionTime))
        tmp.append(self.LastMethodCall.to_binary())
        tmp.append(self.LastMethodSessionId.to_binary())
        tmp.append(struct.pack('!i', len(self.LastMethodInputArguments)))
        for i in LastMethodInputArguments:
            tmp.append(self.LastMethodInputArguments.to_binary())
        tmp.append(struct.pack('!i', len(self.LastMethodOutputArguments)))
        for i in LastMethodOutputArguments:
            tmp.append(self.LastMethodOutputArguments.to_binary())
        tmp.append(struct.pack(self._LastMethodCallTime_fmt, self.LastMethodCallTime))
        tmp.append(self.LastMethodReturnStatus.to_binary())
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.CreateSessionId.from_binary(data)
            data = self.CreateClientName.from_binary(data)
            self.InvocationCreationTime = struct.unpack(self._InvocationCreationTime_fmt, data.read(self._InvocationCreationTime_fmt_size))
            self.LastTransitionTime = struct.unpack(self._LastTransitionTime_fmt, data.read(self._LastTransitionTime_fmt_size))
            data = self.LastMethodCall.from_binary(data)
            data = self.LastMethodSessionId.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.LastMethodInputArguments.from_binary(data)
            length = struct.unpack('!i', data.read(4))
            if length != -1:
                for i in range(0, length):
                    data = self.LastMethodOutputArguments.from_binary(data)
            self.LastMethodCallTime = struct.unpack(self._LastMethodCallTime_fmt, data.read(self._LastMethodCallTime_fmt_size))
            data = self.LastMethodReturnStatus.from_binary(data)
            return data
            
class Annotation(object):
    def __init__(self):
        self.Encoding = None
        self._Encoding_fmt = '!B'
        self._Encoding_fmt_size = 1
        self.TypeId = None
        self.Body = []
        self._Body_fmt = '!c'
        self._Body_fmt_size = 1
        self.Message = None
        self.UserName = None
        self.AnnotationTime = None
        self._AnnotationTime_fmt = '!d'
        self._AnnotationTime_fmt_size = 8
    
    def to_binary(self):
        packet = []
        body = []
        tmp = packet
        if self.TypeId: self.Encoding |= (value << 0)
        tmp.append(struct.pack(self._Encoding_fmt, self.Encoding))
        if self.TypeId: 
            tmp.append(self.TypeId.to_binary())
            tmp = packet
        tmp.append(self.Message.to_binary())
        tmp.append(self.UserName.to_binary())
        tmp.append(struct.pack(self._AnnotationTime_fmt, self.AnnotationTime))
        body = b''.join(tmp)
        packet.append(struct.pack('!i', struct.calcsize(body)))
        packet.append(body)
        return b''.join(packet)
        
        def from_binary(self, data):
            self.Encoding = struct.unpack(self._Encoding_fmt, data.read(self._Encoding_fmt_size))
            if self.Encoding & (1 << 0):
                data = self.TypeId.from_binary(data)
            bodylength = struct.unpack('!i', data.read(4))
            data = self.Message.from_binary(data)
            data = self.UserName.from_binary(data)
            self.AnnotationTime = struct.unpack(self._AnnotationTime_fmt, data.read(self._AnnotationTime_fmt_size))
            return data
