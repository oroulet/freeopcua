
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
    std::size_t RawSize(const XmlElement& data)
    {
        return RawSize(data.Length) + RawSizeContainer(data.Value);
    }


    template<>
    void DataSerializer::Serialize<XmlElement>(const XmlElement& data)
    {
        *this << data.Length;
        SerializeContainer(*this, data.Value);
    }


    template<>
    std::size_t RawSize(const DiagnosticInfo& data)
    {
        return RawSize(data.Encoding) + RawSize(data.SymbolicId) + RawSize(data.NamespaceURI) + RawSize(data.LocalizedText) + RawSize(data.AdditionalInfo) + RawSize(data.InnerStatusCode) + RawSize(data.InnerDiagnosticInfo);
    }


    template<>
    void DataSerializer::Serialize<DiagnosticInfo>(const DiagnosticInfo& data)
    {
        *this << data.Encoding;
        if (data.Encoding) & (1<<(0)) *this << data.SymbolicId;
        if (data.Encoding) & (1<<(1)) *this << data.NamespaceURI;
        if (data.Encoding) & (1<<(2)) *this << data.LocalizedText;
        if (data.Encoding) & (1<<(4)) *this << data.AdditionalInfo;
        if (data.Encoding) & (1<<(5)) *this << data.InnerStatusCode;
        if (data.Encoding) & (1<<(6)) *this << data.InnerDiagnosticInfo;
    }


    template<>
    std::size_t RawSize(const ExtensionObject& data)
    {
        return RawSize(data.Encoding) + RawSize(data.TypeId) + RawSize(data.BodyLength) + RawSizeContainer(data.Body);
    }


    template<>
    void DataSerializer::Serialize<ExtensionObject>(const ExtensionObject& data)
    {
        *this << data.Encoding;
        if (data.Encoding) & (1<<(0)) *this << data.TypeId;
        *this << data.BodyLength;
        SerializeContainer(*this, data.Body);
    }


    template<>
    std::size_t RawSize(const Argument& data)
    {
        return RawSize(data.Name) + RawSize(data.DataType) + RawSize(data.ValueRank) + RawSizeContainer(data.ArrayDimensions) + RawSize(data.Description);
    }


    template<>
    void DataSerializer::Serialize<Argument>(const Argument& data)
    {
        *this << data.Name;
        *this << data.DataType;
        *this << data.ValueRank;
        SerializeContainer(*this, data.ArrayDimensions);
        *this << data.Description;
    }


    template<>
    std::size_t RawSize(const EnumValueType& data)
    {
        return RawSize(data.Value) + RawSize(data.DisplayName) + RawSize(data.Description);
    }


    template<>
    void DataSerializer::Serialize<EnumValueType>(const EnumValueType& data)
    {
        *this << data.Value;
        *this << data.DisplayName;
        *this << data.Description;
    }


    template<>
    std::size_t RawSize(const TimeZoneDataType& data)
    {
        return RawSize(data.Offset) + RawSize(data.DaylightSavingInOffset);
    }


    template<>
    void DataSerializer::Serialize<TimeZoneDataType>(const TimeZoneDataType& data)
    {
        *this << data.Offset;
        *this << data.DaylightSavingInOffset;
    }


    template<>
    std::size_t RawSize(const ApplicationDescription& data)
    {
        return RawSize(data.ApplicationUri) + RawSize(data.ProductUri) + RawSize(data.ApplicationName) + RawSize(data.ApplicationType) + RawSize(data.GatewayServerUri) + RawSize(data.DiscoveryProfileUri) + RawSizeContainer(data.DiscoveryUrls);
    }


    template<>
    void DataSerializer::Serialize<ApplicationDescription>(const ApplicationDescription& data)
    {
        *this << data.ApplicationUri;
        *this << data.ProductUri;
        *this << data.ApplicationName;
        *this << data.ApplicationType;
        *this << data.GatewayServerUri;
        *this << data.DiscoveryProfileUri;
        SerializeContainer(*this, data.DiscoveryUrls);
    }


    template<>
    std::size_t RawSize(const RequestHeader& data)
    {
        return RawSize(data.AuthenticationToken) + RawSize(data.Timestamp) + RawSize(data.RequestHandle) + RawSize(data.ReturnDiagnostics) + RawSize(data.AuditEntryId) + RawSize(data.TimeoutHint) + RawSize(data.AdditionalHeader);
    }


    template<>
    void DataSerializer::Serialize<RequestHeader>(const RequestHeader& data)
    {
        *this << data.AuthenticationToken;
        *this << data.Timestamp;
        *this << data.RequestHandle;
        *this << data.ReturnDiagnostics;
        *this << data.AuditEntryId;
        *this << data.TimeoutHint;
        *this << data.AdditionalHeader;
    }


    template<>
    std::size_t RawSize(const ResponseHeader& data)
    {
        return RawSize(data.Timestamp) + RawSize(data.RequestHandle) + RawSize(data.ServiceResult) + RawSize(data.ServiceDiagnostics) + RawSizeContainer(data.StringTable) + RawSize(data.AdditionalHeader);
    }


    template<>
    void DataSerializer::Serialize<ResponseHeader>(const ResponseHeader& data)
    {
        *this << data.Timestamp;
        *this << data.RequestHandle;
        *this << data.ServiceResult;
        *this << data.ServiceDiagnostics;
        SerializeContainer(*this, data.StringTable);
        *this << data.AdditionalHeader;
    }


    template<>
    std::size_t RawSize(const ServiceFault& data)
    {
        return RawSize(data.ResponseHeader);
    }


    template<>
    void DataSerializer::Serialize<ServiceFault>(const ServiceFault& data)
    {
        *this << data.ResponseHeader;
    }


    template<>
    std::size_t RawSize(const FindServersParameters& data)
    {
        return RawSize(data.EndpointUrl) + RawSizeContainer(data.LocaleIds) + RawSizeContainer(data.ServerUris);
    }


    template<>
    void DataSerializer::Serialize<FindServersParameters>(const FindServersParameters& data)
    {
        *this << data.EndpointUrl;
        SerializeContainer(*this, data.LocaleIds);
        SerializeContainer(*this, data.ServerUris);
    }


    template<>
    std::size_t RawSize(const FindServersRequest& data)
    {
        return RawSize(data.TypeId) + RawSize(data.RequestHeader) + RawSize(data.Parameters);
    }


    template<>
    void DataSerializer::Serialize<FindServersRequest>(const FindServersRequest& data)
    {
        *this << data.TypeId;
        *this << data.RequestHeader;
        *this << data.Parameters;
    }


    template<>
    std::size_t RawSize(const FindServersData& data)
    {
        return RawSizeContainer(data.Servers);
    }


    template<>
    void DataSerializer::Serialize<FindServersData>(const FindServersData& data)
    {
        SerializeContainer(*this, data.Servers);
    }


    template<>
    std::size_t RawSize(const FindServersResponse& data)
    {
        return RawSize(data.TypeId) + RawSize(data.ResponseHeader) + RawSize(data.Parameters);
    }


    template<>
    void DataSerializer::Serialize<FindServersResponse>(const FindServersResponse& data)
    {
        *this << data.TypeId;
        *this << data.ResponseHeader;
        *this << data.Parameters;
    }


    template<>
    std::size_t RawSize(const UserTokenPolicy& data)
    {
        return RawSize(data.PolicyId) + RawSize(data.TokenType) + RawSize(data.IssuedTokenType) + RawSize(data.IssuerEndpointUrl) + RawSize(data.SecurityPolicyUri);
    }


    template<>
    void DataSerializer::Serialize<UserTokenPolicy>(const UserTokenPolicy& data)
    {
        *this << data.PolicyId;
        *this << data.TokenType;
        *this << data.IssuedTokenType;
        *this << data.IssuerEndpointUrl;
        *this << data.SecurityPolicyUri;
    }


    template<>
    std::size_t RawSize(const EndpointDescription& data)
    {
        return RawSize(data.EndpointUrl) + RawSize(data.Server) + RawSize(data.ServerCertificate) + RawSize(data.SecurityMode) + RawSize(data.SecurityPolicyUri) + RawSizeContainer(data.UserIdentityTokens) + RawSize(data.TransportProfileUri) + RawSize(data.SecurityLevel);
    }


    template<>
    void DataSerializer::Serialize<EndpointDescription>(const EndpointDescription& data)
    {
        *this << data.EndpointUrl;
        *this << data.Server;
        *this << data.ServerCertificate;
        *this << data.SecurityMode;
        *this << data.SecurityPolicyUri;
        SerializeContainer(*this, data.UserIdentityTokens);
        *this << data.TransportProfileUri;
        *this << data.SecurityLevel;
    }


    template<>
    std::size_t RawSize(const GetEndpointsParameters& data)
    {
        return RawSize(data.EndpointUrl) + RawSizeContainer(data.LocaleIds) + RawSizeContainer(data.ProfileUris);
    }


    template<>
    void DataSerializer::Serialize<GetEndpointsParameters>(const GetEndpointsParameters& data)
    {
        *this << data.EndpointUrl;
        SerializeContainer(*this, data.LocaleIds);
        SerializeContainer(*this, data.ProfileUris);
    }


    template<>
    std::size_t RawSize(const GetEndpointsRequest& data)
    {
        return RawSize(data.TypeId) + RawSize(data.RequestHeader) + RawSize(data.Parameters);
    }


    template<>
    void DataSerializer::Serialize<GetEndpointsRequest>(const GetEndpointsRequest& data)
    {
        *this << data.TypeId;
        *this << data.RequestHeader;
        *this << data.Parameters;
    }


    template<>
    std::size_t RawSize(const GetEndpointsResponse& data)
    {
        return RawSize(data.ResponseHeader) + RawSizeContainer(data.Endpoints);
    }


    template<>
    void DataSerializer::Serialize<GetEndpointsResponse>(const GetEndpointsResponse& data)
    {
        *this << data.ResponseHeader;
        SerializeContainer(*this, data.Endpoints);
    }


    template<>
    std::size_t RawSize(const RegisteredServer& data)
    {
        return RawSize(data.ServerUri) + RawSize(data.ProductUri) + RawSizeContainer(data.ServerNames) + RawSize(data.ServerType) + RawSize(data.GatewayServerUri) + RawSizeContainer(data.DiscoveryUrls) + RawSize(data.SemaphoreFilePath) + RawSize(data.IsOnline);
    }


    template<>
    void DataSerializer::Serialize<RegisteredServer>(const RegisteredServer& data)
    {
        *this << data.ServerUri;
        *this << data.ProductUri;
        SerializeContainer(*this, data.ServerNames);
        *this << data.ServerType;
        *this << data.GatewayServerUri;
        SerializeContainer(*this, data.DiscoveryUrls);
        *this << data.SemaphoreFilePath;
        *this << data.IsOnline;
    }


    template<>
    std::size_t RawSize(const RegisterServerParameters& data)
    {
        return RawSize(data.Server);
    }


    template<>
    void DataSerializer::Serialize<RegisterServerParameters>(const RegisterServerParameters& data)
    {
        *this << data.Server;
    }


    template<>
    std::size_t RawSize(const RegisterServerRequest& data)
    {
        return RawSize(data.TypeId) + RawSize(data.RequestHeader) + RawSize(data.Parameters);
    }


    template<>
    void DataSerializer::Serialize<RegisterServerRequest>(const RegisterServerRequest& data)
    {
        *this << data.TypeId;
        *this << data.RequestHeader;
        *this << data.Parameters;
    }


    template<>
    std::size_t RawSize(const RegisterServerData& data)
    {
        return ;
    }


    template<>
    void DataSerializer::Serialize<RegisterServerData>(const RegisterServerData& data)
    {
    }


    template<>
    std::size_t RawSize(const RegisterServerResponse& data)
    {
        return RawSize(data.TypeId) + RawSize(data.ResponseHeader) + RawSize(data.Parameters);
    }


    template<>
    void DataSerializer::Serialize<RegisterServerResponse>(const RegisterServerResponse& data)
    {
        *this << data.TypeId;
        *this << data.ResponseHeader;
        *this << data.Parameters;
    }


    template<>
    std::size_t RawSize(const ChannelSecurityToken& data)
    {
        return RawSize(data.ChannelId) + RawSize(data.TokenId) + RawSize(data.CreatedAt) + RawSize(data.RevisedLifetime);
    }


    template<>
    void DataSerializer::Serialize<ChannelSecurityToken>(const ChannelSecurityToken& data)
    {
        *this << data.ChannelId;
        *this << data.TokenId;
        *this << data.CreatedAt;
        *this << data.RevisedLifetime;
    }


    template<>
    std::size_t RawSize(const OpenSecureChannelParameters& data)
    {
        return RawSize(data.ClientProtocolVersion) + RawSize(data.RequestType) + RawSize(data.SecurityMode) + RawSize(data.ClientNonce) + RawSize(data.RequestedLifetime);
    }


    template<>
    void DataSerializer::Serialize<OpenSecureChannelParameters>(const OpenSecureChannelParameters& data)
    {
        *this << data.ClientProtocolVersion;
        *this << data.RequestType;
        *this << data.SecurityMode;
        *this << data.ClientNonce;
        *this << data.RequestedLifetime;
    }


    template<>
    std::size_t RawSize(const OpenSecureChannelRequest& data)
    {
        return RawSize(data.TypeId) + RawSize(data.RequestHeader) + RawSize(data.Parameters);
    }


    template<>
    void DataSerializer::Serialize<OpenSecureChannelRequest>(const OpenSecureChannelRequest& data)
    {
        *this << data.TypeId;
        *this << data.RequestHeader;
        *this << data.Parameters;
    }


    template<>
    std::size_t RawSize(const OpenSecureChannelData& data)
    {
        return RawSize(data.ServerProtocolVersion) + RawSize(data.SecurityToken) + RawSize(data.ServerNonce);
    }


    template<>
    void DataSerializer::Serialize<OpenSecureChannelData>(const OpenSecureChannelData& data)
    {
        *this << data.ServerProtocolVersion;
        *this << data.SecurityToken;
        *this << data.ServerNonce;
    }


    template<>
    std::size_t RawSize(const OpenSecureChannelResponse& data)
    {
        return RawSize(data.TypeId) + RawSize(data.ResponseHeader) + RawSize(data.Parameters);
    }


    template<>
    void DataSerializer::Serialize<OpenSecureChannelResponse>(const OpenSecureChannelResponse& data)
    {
        *this << data.TypeId;
        *this << data.ResponseHeader;
        *this << data.Parameters;
    }


    template<>
    std::size_t RawSize(const CloseSecureChannelParameters& data)
    {
        return ;
    }


    template<>
    void DataSerializer::Serialize<CloseSecureChannelParameters>(const CloseSecureChannelParameters& data)
    {
    }


    template<>
    std::size_t RawSize(const CloseSecureChannelRequest& data)
    {
        return RawSize(data.TypeId) + RawSize(data.RequestHeader) + RawSize(data.Parameters);
    }


    template<>
    void DataSerializer::Serialize<CloseSecureChannelRequest>(const CloseSecureChannelRequest& data)
    {
        *this << data.TypeId;
        *this << data.RequestHeader;
        *this << data.Parameters;
    }


    template<>
    std::size_t RawSize(const CloseSecureChannelData& data)
    {
        return ;
    }


    template<>
    void DataSerializer::Serialize<CloseSecureChannelData>(const CloseSecureChannelData& data)
    {
    }


    template<>
    std::size_t RawSize(const CloseSecureChannelResponse& data)
    {
        return RawSize(data.TypeId) + RawSize(data.ResponseHeader) + RawSize(data.Parameters);
    }


    template<>
    void DataSerializer::Serialize<CloseSecureChannelResponse>(const CloseSecureChannelResponse& data)
    {
        *this << data.TypeId;
        *this << data.ResponseHeader;
        *this << data.Parameters;
    }


    template<>
    std::size_t RawSize(const SignedSoftwareCertificate& data)
    {
        return RawSize(data.CertificateData) + RawSize(data.Signature);
    }


    template<>
    void DataSerializer::Serialize<SignedSoftwareCertificate>(const SignedSoftwareCertificate& data)
    {
        *this << data.CertificateData;
        *this << data.Signature;
    }


    template<>
    std::size_t RawSize(const SignatureData& data)
    {
        return RawSize(data.Algorithm) + RawSize(data.Signature);
    }


    template<>
    void DataSerializer::Serialize<SignatureData>(const SignatureData& data)
    {
        *this << data.Algorithm;
        *this << data.Signature;
    }


    template<>
    std::size_t RawSize(const CreateSessionParameters& data)
    {
        return RawSize(data.ClientDescription) + RawSize(data.ServerUri) + RawSize(data.EndpointUrl) + RawSize(data.SessionName) + RawSize(data.ClientNonce) + RawSize(data.ClientCertificate) + RawSize(data.RequestedSessionTimeout) + RawSize(data.MaxResponseMessageSize);
    }


    template<>
    void DataSerializer::Serialize<CreateSessionParameters>(const CreateSessionParameters& data)
    {
        *this << data.ClientDescription;
        *this << data.ServerUri;
        *this << data.EndpointUrl;
        *this << data.SessionName;
        *this << data.ClientNonce;
        *this << data.ClientCertificate;
        *this << data.RequestedSessionTimeout;
        *this << data.MaxResponseMessageSize;
    }


    template<>
    std::size_t RawSize(const CreateSessionRequest& data)
    {
        return RawSize(data.TypeId) + RawSize(data.RequestHeader) + RawSize(data.Parameters);
    }


    template<>
    void DataSerializer::Serialize<CreateSessionRequest>(const CreateSessionRequest& data)
    {
        *this << data.TypeId;
        *this << data.RequestHeader;
        *this << data.Parameters;
    }


    template<>
    std::size_t RawSize(const CreateSessionData& data)
    {
        return RawSize(data.SessionId) + RawSize(data.AuthenticationToken) + RawSize(data.RevisedSessionTimeout) + RawSize(data.ServerNonce) + RawSize(data.ServerCertificate) + RawSizeContainer(data.ServerEndpoints) + RawSizeContainer(data.ServerSoftwareCertificates) + RawSize(data.ServerSignature) + RawSize(data.MaxRequestMessageSize);
    }


    template<>
    void DataSerializer::Serialize<CreateSessionData>(const CreateSessionData& data)
    {
        *this << data.SessionId;
        *this << data.AuthenticationToken;
        *this << data.RevisedSessionTimeout;
        *this << data.ServerNonce;
        *this << data.ServerCertificate;
        SerializeContainer(*this, data.ServerEndpoints);
        SerializeContainer(*this, data.ServerSoftwareCertificates);
        *this << data.ServerSignature;
        *this << data.MaxRequestMessageSize;
    }


    template<>
    std::size_t RawSize(const CreateSessionResponse& data)
    {
        return RawSize(data.TypeId) + RawSize(data.ResponseHeader) + RawSize(data.Parameters);
    }


    template<>
    void DataSerializer::Serialize<CreateSessionResponse>(const CreateSessionResponse& data)
    {
        *this << data.TypeId;
        *this << data.ResponseHeader;
        *this << data.Parameters;
    }


    template<>
    std::size_t RawSize(const UserIdentityToken& data)
    {
        return RawSize(data.PolicyId);
    }


    template<>
    void DataSerializer::Serialize<UserIdentityToken>(const UserIdentityToken& data)
    {
        *this << data.PolicyId;
    }


    template<>
    std::size_t RawSize(const AnonymousIdentityToken& data)
    {
        return RawSize(data.PolicyId);
    }


    template<>
    void DataSerializer::Serialize<AnonymousIdentityToken>(const AnonymousIdentityToken& data)
    {
        *this << data.PolicyId;
    }


    template<>
    std::size_t RawSize(const UserNameIdentityToken& data)
    {
        return RawSize(data.PolicyId) + RawSize(data.UserName) + RawSize(data.Password) + RawSize(data.EncryptionAlgorithm);
    }


    template<>
    void DataSerializer::Serialize<UserNameIdentityToken>(const UserNameIdentityToken& data)
    {
        *this << data.PolicyId;
        *this << data.UserName;
        *this << data.Password;
        *this << data.EncryptionAlgorithm;
    }


    template<>
    std::size_t RawSize(const X509IdentityToken& data)
    {
        return RawSize(data.PolicyId) + RawSize(data.CertificateData);
    }


    template<>
    void DataSerializer::Serialize<X509IdentityToken>(const X509IdentityToken& data)
    {
        *this << data.PolicyId;
        *this << data.CertificateData;
    }


    template<>
    std::size_t RawSize(const IssuedIdentityToken& data)
    {
        return RawSize(data.PolicyId) + RawSize(data.TokenData) + RawSize(data.EncryptionAlgorithm);
    }


    template<>
    void DataSerializer::Serialize<IssuedIdentityToken>(const IssuedIdentityToken& data)
    {
        *this << data.PolicyId;
        *this << data.TokenData;
        *this << data.EncryptionAlgorithm;
    }


    template<>
    std::size_t RawSize(const ActivateSessionParameters& data)
    {
        return RawSize(data.ClientSignature) + RawSizeContainer(data.ClientSoftwareCertificates) + RawSizeContainer(data.LocaleIds) + RawSize(data.UserIdentityToken) + RawSize(data.UserTokenSignature);
    }


    template<>
    void DataSerializer::Serialize<ActivateSessionParameters>(const ActivateSessionParameters& data)
    {
        *this << data.ClientSignature;
        SerializeContainer(*this, data.ClientSoftwareCertificates);
        SerializeContainer(*this, data.LocaleIds);
        *this << data.UserIdentityToken;
        *this << data.UserTokenSignature;
    }


    template<>
    std::size_t RawSize(const ActivateSessionRequest& data)
    {
        return RawSize(data.TypeId) + RawSize(data.RequestHeader) + RawSize(data.Parameters);
    }


    template<>
    void DataSerializer::Serialize<ActivateSessionRequest>(const ActivateSessionRequest& data)
    {
        *this << data.TypeId;
        *this << data.RequestHeader;
        *this << data.Parameters;
    }


    template<>
    std::size_t RawSize(const ActivateSessionData& data)
    {
        return RawSize(data.ServerNonce) + RawSizeContainer(data.Results) + RawSizeContainer(data.DiagnosticInfos);
    }


    template<>
    void DataSerializer::Serialize<ActivateSessionData>(const ActivateSessionData& data)
    {
        *this << data.ServerNonce;
        SerializeContainer(*this, data.Results);
        SerializeContainer(*this, data.DiagnosticInfos);
    }


    template<>
    std::size_t RawSize(const ActivateSessionResponse& data)
    {
        return RawSize(data.TypeId) + RawSize(data.ResponseHeader) + RawSize(data.Parameters);
    }


    template<>
    void DataSerializer::Serialize<ActivateSessionResponse>(const ActivateSessionResponse& data)
    {
        *this << data.TypeId;
        *this << data.ResponseHeader;
        *this << data.Parameters;
    }


    template<>
    std::size_t RawSize(const CloseSessionParameters& data)
    {
        return RawSize(data.DeleteSubscriptions);
    }


    template<>
    void DataSerializer::Serialize<CloseSessionParameters>(const CloseSessionParameters& data)
    {
        *this << data.DeleteSubscriptions;
    }


    template<>
    std::size_t RawSize(const CloseSessionRequest& data)
    {
        return RawSize(data.TypeId) + RawSize(data.RequestHeader) + RawSize(data.Parameters);
    }


    template<>
    void DataSerializer::Serialize<CloseSessionRequest>(const CloseSessionRequest& data)
    {
        *this << data.TypeId;
        *this << data.RequestHeader;
        *this << data.Parameters;
    }


    template<>
    std::size_t RawSize(const CloseSessionData& data)
    {
        return ;
    }


    template<>
    void DataSerializer::Serialize<CloseSessionData>(const CloseSessionData& data)
    {
    }


    template<>
    std::size_t RawSize(const CloseSessionResponse& data)
    {
        return RawSize(data.TypeId) + RawSize(data.ResponseHeader) + RawSize(data.Parameters);
    }


    template<>
    void DataSerializer::Serialize<CloseSessionResponse>(const CloseSessionResponse& data)
    {
        *this << data.TypeId;
        *this << data.ResponseHeader;
        *this << data.Parameters;
    }


    template<>
    std::size_t RawSize(const CancelParameters& data)
    {
        return RawSize(data.RequestHandle);
    }


    template<>
    void DataSerializer::Serialize<CancelParameters>(const CancelParameters& data)
    {
        *this << data.RequestHandle;
    }


    template<>
    std::size_t RawSize(const CancelRequest& data)
    {
        return RawSize(data.TypeId) + RawSize(data.RequestHeader) + RawSize(data.Parameters);
    }


    template<>
    void DataSerializer::Serialize<CancelRequest>(const CancelRequest& data)
    {
        *this << data.TypeId;
        *this << data.RequestHeader;
        *this << data.Parameters;
    }


    template<>
    std::size_t RawSize(const CancelData& data)
    {
        return RawSize(data.CancelCount);
    }


    template<>
    void DataSerializer::Serialize<CancelData>(const CancelData& data)
    {
        *this << data.CancelCount;
    }


    template<>
    std::size_t RawSize(const CancelResponse& data)
    {
        return RawSize(data.TypeId) + RawSize(data.ResponseHeader) + RawSize(data.Parameters);
    }


    template<>
    void DataSerializer::Serialize<CancelResponse>(const CancelResponse& data)
    {
        *this << data.TypeId;
        *this << data.ResponseHeader;
        *this << data.Parameters;
    }


    template<>
    std::size_t RawSize(const NodeAttributes& data)
    {
        return RawSize(data.SpecifiedAttributes) + RawSize(data.DisplayName) + RawSize(data.Description) + RawSize(data.WriteMask) + RawSize(data.UserWriteMask);
    }


    template<>
    void DataSerializer::Serialize<NodeAttributes>(const NodeAttributes& data)
    {
        *this << data.SpecifiedAttributes;
        *this << data.DisplayName;
        *this << data.Description;
        *this << data.WriteMask;
        *this << data.UserWriteMask;
    }


    template<>
    std::size_t RawSize(const ObjectAttributes& data)
    {
        return RawSize(data.SpecifiedAttributes) + RawSize(data.DisplayName) + RawSize(data.Description) + RawSize(data.WriteMask) + RawSize(data.UserWriteMask) + RawSize(data.EventNotifier);
    }


    template<>
    void DataSerializer::Serialize<ObjectAttributes>(const ObjectAttributes& data)
    {
        *this << data.SpecifiedAttributes;
        *this << data.DisplayName;
        *this << data.Description;
        *this << data.WriteMask;
        *this << data.UserWriteMask;
        *this << data.EventNotifier;
    }


    template<>
    std::size_t RawSize(const VariableAttributes& data)
    {
        return RawSize(data.SpecifiedAttributes) + RawSize(data.DisplayName) + RawSize(data.Description) + RawSize(data.WriteMask) + RawSize(data.UserWriteMask) + RawSize(data.Value) + RawSize(data.DataType) + RawSize(data.ValueRank) + RawSizeContainer(data.ArrayDimensions) + RawSize(data.AccessLevel) + RawSize(data.UserAccessLevel) + RawSize(data.MinimumSamplingInterval) + RawSize(data.Historizing);
    }


    template<>
    void DataSerializer::Serialize<VariableAttributes>(const VariableAttributes& data)
    {
        *this << data.SpecifiedAttributes;
        *this << data.DisplayName;
        *this << data.Description;
        *this << data.WriteMask;
        *this << data.UserWriteMask;
        *this << data.Value;
        *this << data.DataType;
        *this << data.ValueRank;
        SerializeContainer(*this, data.ArrayDimensions);
        *this << data.AccessLevel;
        *this << data.UserAccessLevel;
        *this << data.MinimumSamplingInterval;
        *this << data.Historizing;
    }


    template<>
    std::size_t RawSize(const MethodAttributes& data)
    {
        return RawSize(data.SpecifiedAttributes) + RawSize(data.DisplayName) + RawSize(data.Description) + RawSize(data.WriteMask) + RawSize(data.UserWriteMask) + RawSize(data.Executable) + RawSize(data.UserExecutable);
    }


    template<>
    void DataSerializer::Serialize<MethodAttributes>(const MethodAttributes& data)
    {
        *this << data.SpecifiedAttributes;
        *this << data.DisplayName;
        *this << data.Description;
        *this << data.WriteMask;
        *this << data.UserWriteMask;
        *this << data.Executable;
        *this << data.UserExecutable;
    }


    template<>
    std::size_t RawSize(const ObjectTypeAttributes& data)
    {
        return RawSize(data.SpecifiedAttributes) + RawSize(data.DisplayName) + RawSize(data.Description) + RawSize(data.WriteMask) + RawSize(data.UserWriteMask) + RawSize(data.IsAbstract);
    }


    template<>
    void DataSerializer::Serialize<ObjectTypeAttributes>(const ObjectTypeAttributes& data)
    {
        *this << data.SpecifiedAttributes;
        *this << data.DisplayName;
        *this << data.Description;
        *this << data.WriteMask;
        *this << data.UserWriteMask;
        *this << data.IsAbstract;
    }


    template<>
    std::size_t RawSize(const VariableTypeAttributes& data)
    {
        return RawSize(data.SpecifiedAttributes) + RawSize(data.DisplayName) + RawSize(data.Description) + RawSize(data.WriteMask) + RawSize(data.UserWriteMask) + RawSize(data.Value) + RawSize(data.DataType) + RawSize(data.ValueRank) + RawSizeContainer(data.ArrayDimensions) + RawSize(data.IsAbstract);
    }


    template<>
    void DataSerializer::Serialize<VariableTypeAttributes>(const VariableTypeAttributes& data)
    {
        *this << data.SpecifiedAttributes;
        *this << data.DisplayName;
        *this << data.Description;
        *this << data.WriteMask;
        *this << data.UserWriteMask;
        *this << data.Value;
        *this << data.DataType;
        *this << data.ValueRank;
        SerializeContainer(*this, data.ArrayDimensions);
        *this << data.IsAbstract;
    }


    template<>
    std::size_t RawSize(const ReferenceTypeAttributes& data)
    {
        return RawSize(data.SpecifiedAttributes) + RawSize(data.DisplayName) + RawSize(data.Description) + RawSize(data.WriteMask) + RawSize(data.UserWriteMask) + RawSize(data.IsAbstract) + RawSize(data.Symmetric) + RawSize(data.InverseName);
    }


    template<>
    void DataSerializer::Serialize<ReferenceTypeAttributes>(const ReferenceTypeAttributes& data)
    {
        *this << data.SpecifiedAttributes;
        *this << data.DisplayName;
        *this << data.Description;
        *this << data.WriteMask;
        *this << data.UserWriteMask;
        *this << data.IsAbstract;
        *this << data.Symmetric;
        *this << data.InverseName;
    }


    template<>
    std::size_t RawSize(const DataTypeAttributes& data)
    {
        return RawSize(data.SpecifiedAttributes) + RawSize(data.DisplayName) + RawSize(data.Description) + RawSize(data.WriteMask) + RawSize(data.UserWriteMask) + RawSize(data.IsAbstract);
    }


    template<>
    void DataSerializer::Serialize<DataTypeAttributes>(const DataTypeAttributes& data)
    {
        *this << data.SpecifiedAttributes;
        *this << data.DisplayName;
        *this << data.Description;
        *this << data.WriteMask;
        *this << data.UserWriteMask;
        *this << data.IsAbstract;
    }


    template<>
    std::size_t RawSize(const ViewAttributes& data)
    {
        return RawSize(data.SpecifiedAttributes) + RawSize(data.DisplayName) + RawSize(data.Description) + RawSize(data.WriteMask) + RawSize(data.UserWriteMask) + RawSize(data.ContainsNoLoops) + RawSize(data.EventNotifier);
    }


    template<>
    void DataSerializer::Serialize<ViewAttributes>(const ViewAttributes& data)
    {
        *this << data.SpecifiedAttributes;
        *this << data.DisplayName;
        *this << data.Description;
        *this << data.WriteMask;
        *this << data.UserWriteMask;
        *this << data.ContainsNoLoops;
        *this << data.EventNotifier;
    }


    template<>
    std::size_t RawSize(const AddNodesItem& data)
    {
        return RawSize(data.ParentNodeId) + RawSize(data.ReferenceTypeId) + RawSize(data.RequestedNewNodeId) + RawSize(data.BrowseName) + RawSize(data.NodeClass) + RawSize(data.NodeAttributes) + RawSize(data.TypeDefinition);
    }


    template<>
    void DataSerializer::Serialize<AddNodesItem>(const AddNodesItem& data)
    {
        *this << data.ParentNodeId;
        *this << data.ReferenceTypeId;
        *this << data.RequestedNewNodeId;
        *this << data.BrowseName;
        *this << data.NodeClass;
        *this << data.NodeAttributes;
        *this << data.TypeDefinition;
    }


    template<>
    std::size_t RawSize(const AddNodesResult& data)
    {
        return RawSize(data.StatusCode) + RawSize(data.AddedNodeId);
    }


    template<>
    void DataSerializer::Serialize<AddNodesResult>(const AddNodesResult& data)
    {
        *this << data.StatusCode;
        *this << data.AddedNodeId;
    }


    template<>
    std::size_t RawSize(const AddNodesParameters& data)
    {
        return RawSizeContainer(data.NodesToAdd);
    }


    template<>
    void DataSerializer::Serialize<AddNodesParameters>(const AddNodesParameters& data)
    {
        SerializeContainer(*this, data.NodesToAdd);
    }


    template<>
    std::size_t RawSize(const AddNodesRequest& data)
    {
        return RawSize(data.TypeId) + RawSize(data.RequestHeader) + RawSize(data.Parameters);
    }


    template<>
    void DataSerializer::Serialize<AddNodesRequest>(const AddNodesRequest& data)
    {
        *this << data.TypeId;
        *this << data.RequestHeader;
        *this << data.Parameters;
    }


    template<>
    std::size_t RawSize(const AddNodesData& data)
    {
        return RawSizeContainer(data.Results) + RawSizeContainer(data.DiagnosticInfos);
    }


    template<>
    void DataSerializer::Serialize<AddNodesData>(const AddNodesData& data)
    {
        SerializeContainer(*this, data.Results);
        SerializeContainer(*this, data.DiagnosticInfos);
    }


    template<>
    std::size_t RawSize(const AddNodesResponse& data)
    {
        return RawSize(data.TypeId) + RawSize(data.ResponseHeader) + RawSize(data.Parameters);
    }


    template<>
    void DataSerializer::Serialize<AddNodesResponse>(const AddNodesResponse& data)
    {
        *this << data.TypeId;
        *this << data.ResponseHeader;
        *this << data.Parameters;
    }


    template<>
    std::size_t RawSize(const AddReferencesItem& data)
    {
        return RawSize(data.SourceNodeId) + RawSize(data.ReferenceTypeId) + RawSize(data.IsForward) + RawSize(data.TargetServerUri) + RawSize(data.TargetNodeId) + RawSize(data.TargetNodeClass);
    }


    template<>
    void DataSerializer::Serialize<AddReferencesItem>(const AddReferencesItem& data)
    {
        *this << data.SourceNodeId;
        *this << data.ReferenceTypeId;
        *this << data.IsForward;
        *this << data.TargetServerUri;
        *this << data.TargetNodeId;
        *this << data.TargetNodeClass;
    }


    template<>
    std::size_t RawSize(const AddReferencesParameters& data)
    {
        return RawSizeContainer(data.ReferencesToAdd);
    }


    template<>
    void DataSerializer::Serialize<AddReferencesParameters>(const AddReferencesParameters& data)
    {
        SerializeContainer(*this, data.ReferencesToAdd);
    }


    template<>
    std::size_t RawSize(const AddReferencesRequest& data)
    {
        return RawSize(data.TypeId) + RawSize(data.RequestHeader) + RawSize(data.Parameters);
    }


    template<>
    void DataSerializer::Serialize<AddReferencesRequest>(const AddReferencesRequest& data)
    {
        *this << data.TypeId;
        *this << data.RequestHeader;
        *this << data.Parameters;
    }


    template<>
    std::size_t RawSize(const AddReferencesData& data)
    {
        return RawSizeContainer(data.Results) + RawSizeContainer(data.DiagnosticInfos);
    }


    template<>
    void DataSerializer::Serialize<AddReferencesData>(const AddReferencesData& data)
    {
        SerializeContainer(*this, data.Results);
        SerializeContainer(*this, data.DiagnosticInfos);
    }


    template<>
    std::size_t RawSize(const AddReferencesResponse& data)
    {
        return RawSize(data.TypeId) + RawSize(data.ResponseHeader) + RawSize(data.Parameters);
    }


    template<>
    void DataSerializer::Serialize<AddReferencesResponse>(const AddReferencesResponse& data)
    {
        *this << data.TypeId;
        *this << data.ResponseHeader;
        *this << data.Parameters;
    }


    template<>
    std::size_t RawSize(const DeleteNodesItem& data)
    {
        return RawSize(data.NodeId) + RawSize(data.DeleteTargetReferences);
    }


    template<>
    void DataSerializer::Serialize<DeleteNodesItem>(const DeleteNodesItem& data)
    {
        *this << data.NodeId;
        *this << data.DeleteTargetReferences;
    }


    template<>
    std::size_t RawSize(const DeleteNodesParameters& data)
    {
        return RawSizeContainer(data.NodesToDelete);
    }


    template<>
    void DataSerializer::Serialize<DeleteNodesParameters>(const DeleteNodesParameters& data)
    {
        SerializeContainer(*this, data.NodesToDelete);
    }


    template<>
    std::size_t RawSize(const DeleteNodesRequest& data)
    {
        return RawSize(data.TypeId) + RawSize(data.RequestHeader) + RawSize(data.Parameters);
    }


    template<>
    void DataSerializer::Serialize<DeleteNodesRequest>(const DeleteNodesRequest& data)
    {
        *this << data.TypeId;
        *this << data.RequestHeader;
        *this << data.Parameters;
    }


    template<>
    std::size_t RawSize(const DeleteNodesData& data)
    {
        return RawSizeContainer(data.Results) + RawSizeContainer(data.DiagnosticInfos);
    }


    template<>
    void DataSerializer::Serialize<DeleteNodesData>(const DeleteNodesData& data)
    {
        SerializeContainer(*this, data.Results);
        SerializeContainer(*this, data.DiagnosticInfos);
    }


    template<>
    std::size_t RawSize(const DeleteNodesResponse& data)
    {
        return RawSize(data.TypeId) + RawSize(data.ResponseHeader) + RawSize(data.Parameters);
    }


    template<>
    void DataSerializer::Serialize<DeleteNodesResponse>(const DeleteNodesResponse& data)
    {
        *this << data.TypeId;
        *this << data.ResponseHeader;
        *this << data.Parameters;
    }


    template<>
    std::size_t RawSize(const DeleteReferencesItem& data)
    {
        return RawSize(data.SourceNodeId) + RawSize(data.ReferenceTypeId) + RawSize(data.IsForward) + RawSize(data.TargetNodeId) + RawSize(data.DeleteBidirectional);
    }


    template<>
    void DataSerializer::Serialize<DeleteReferencesItem>(const DeleteReferencesItem& data)
    {
        *this << data.SourceNodeId;
        *this << data.ReferenceTypeId;
        *this << data.IsForward;
        *this << data.TargetNodeId;
        *this << data.DeleteBidirectional;
    }


    template<>
    std::size_t RawSize(const DeleteReferencesParameters& data)
    {
        return RawSizeContainer(data.ReferencesToDelete);
    }


    template<>
    void DataSerializer::Serialize<DeleteReferencesParameters>(const DeleteReferencesParameters& data)
    {
        SerializeContainer(*this, data.ReferencesToDelete);
    }


    template<>
    std::size_t RawSize(const DeleteReferencesRequest& data)
    {
        return RawSize(data.TypeId) + RawSize(data.RequestHeader) + RawSize(data.Parameters);
    }


    template<>
    void DataSerializer::Serialize<DeleteReferencesRequest>(const DeleteReferencesRequest& data)
    {
        *this << data.TypeId;
        *this << data.RequestHeader;
        *this << data.Parameters;
    }


    template<>
    std::size_t RawSize(const DeleteReferencesData& data)
    {
        return RawSizeContainer(data.Results) + RawSizeContainer(data.DiagnosticInfos);
    }


    template<>
    void DataSerializer::Serialize<DeleteReferencesData>(const DeleteReferencesData& data)
    {
        SerializeContainer(*this, data.Results);
        SerializeContainer(*this, data.DiagnosticInfos);
    }


    template<>
    std::size_t RawSize(const DeleteReferencesResponse& data)
    {
        return RawSize(data.TypeId) + RawSize(data.ResponseHeader) + RawSize(data.Parameters);
    }


    template<>
    void DataSerializer::Serialize<DeleteReferencesResponse>(const DeleteReferencesResponse& data)
    {
        *this << data.TypeId;
        *this << data.ResponseHeader;
        *this << data.Parameters;
    }


    template<>
    std::size_t RawSize(const ViewDescription& data)
    {
        return RawSize(data.ViewId) + RawSize(data.Timestamp) + RawSize(data.ViewVersion);
    }


    template<>
    void DataSerializer::Serialize<ViewDescription>(const ViewDescription& data)
    {
        *this << data.ViewId;
        *this << data.Timestamp;
        *this << data.ViewVersion;
    }


    template<>
    std::size_t RawSize(const BrowseDescription& data)
    {
        return RawSize(data.NodeId) + RawSize(data.BrowseDirection) + RawSize(data.ReferenceTypeId) + RawSize(data.IncludeSubtypes) + RawSize(data.NodeClassMask) + RawSize(data.ResultMask);
    }


    template<>
    void DataSerializer::Serialize<BrowseDescription>(const BrowseDescription& data)
    {
        *this << data.NodeId;
        *this << data.BrowseDirection;
        *this << data.ReferenceTypeId;
        *this << data.IncludeSubtypes;
        *this << data.NodeClassMask;
        *this << data.ResultMask;
    }


    template<>
    std::size_t RawSize(const ReferenceDescription& data)
    {
        return RawSize(data.ReferenceTypeId) + RawSize(data.IsForward) + RawSize(data.NodeId) + RawSize(data.BrowseName) + RawSize(data.DisplayName) + RawSize(data.NodeClass) + RawSize(data.TypeDefinition);
    }


    template<>
    void DataSerializer::Serialize<ReferenceDescription>(const ReferenceDescription& data)
    {
        *this << data.ReferenceTypeId;
        *this << data.IsForward;
        *this << data.NodeId;
        *this << data.BrowseName;
        *this << data.DisplayName;
        *this << data.NodeClass;
        *this << data.TypeDefinition;
    }


    template<>
    std::size_t RawSize(const BrowseResult& data)
    {
        return RawSize(data.StatusCode) + RawSize(data.ContinuationPoint) + RawSizeContainer(data.References);
    }


    template<>
    void DataSerializer::Serialize<BrowseResult>(const BrowseResult& data)
    {
        *this << data.StatusCode;
        *this << data.ContinuationPoint;
        SerializeContainer(*this, data.References);
    }


    template<>
    std::size_t RawSize(const BrowseParameters& data)
    {
        return RawSize(data.View) + RawSize(data.RequestedMaxReferencesPerNode) + RawSizeContainer(data.NodesToBrowse);
    }


    template<>
    void DataSerializer::Serialize<BrowseParameters>(const BrowseParameters& data)
    {
        *this << data.View;
        *this << data.RequestedMaxReferencesPerNode;
        SerializeContainer(*this, data.NodesToBrowse);
    }


    template<>
    std::size_t RawSize(const BrowseRequest& data)
    {
        return RawSize(data.TypeId) + RawSize(data.RequestHeader) + RawSize(data.Parameters);
    }


    template<>
    void DataSerializer::Serialize<BrowseRequest>(const BrowseRequest& data)
    {
        *this << data.TypeId;
        *this << data.RequestHeader;
        *this << data.Parameters;
    }


    template<>
    std::size_t RawSize(const BrowseData& data)
    {
        return RawSizeContainer(data.Results) + RawSizeContainer(data.DiagnosticInfos);
    }


    template<>
    void DataSerializer::Serialize<BrowseData>(const BrowseData& data)
    {
        SerializeContainer(*this, data.Results);
        SerializeContainer(*this, data.DiagnosticInfos);
    }


    template<>
    std::size_t RawSize(const BrowseResponse& data)
    {
        return RawSize(data.TypeId) + RawSize(data.ResponseHeader) + RawSize(data.Parameters);
    }


    template<>
    void DataSerializer::Serialize<BrowseResponse>(const BrowseResponse& data)
    {
        *this << data.TypeId;
        *this << data.ResponseHeader;
        *this << data.Parameters;
    }


    template<>
    std::size_t RawSize(const BrowseNextParameters& data)
    {
        return RawSize(data.ReleaseContinuationPoints) + RawSizeContainer(data.ContinuationPoints);
    }


    template<>
    void DataSerializer::Serialize<BrowseNextParameters>(const BrowseNextParameters& data)
    {
        *this << data.ReleaseContinuationPoints;
        SerializeContainer(*this, data.ContinuationPoints);
    }


    template<>
    std::size_t RawSize(const BrowseNextRequest& data)
    {
        return RawSize(data.TypeId) + RawSize(data.RequestHeader) + RawSize(data.Parameters);
    }


    template<>
    void DataSerializer::Serialize<BrowseNextRequest>(const BrowseNextRequest& data)
    {
        *this << data.TypeId;
        *this << data.RequestHeader;
        *this << data.Parameters;
    }


    template<>
    std::size_t RawSize(const BrowseNextData& data)
    {
        return RawSizeContainer(data.Results) + RawSizeContainer(data.DiagnosticInfos);
    }


    template<>
    void DataSerializer::Serialize<BrowseNextData>(const BrowseNextData& data)
    {
        SerializeContainer(*this, data.Results);
        SerializeContainer(*this, data.DiagnosticInfos);
    }


    template<>
    std::size_t RawSize(const BrowseNextResponse& data)
    {
        return RawSize(data.TypeId) + RawSize(data.ResponseHeader) + RawSize(data.Parameters);
    }


    template<>
    void DataSerializer::Serialize<BrowseNextResponse>(const BrowseNextResponse& data)
    {
        *this << data.TypeId;
        *this << data.ResponseHeader;
        *this << data.Parameters;
    }


    template<>
    std::size_t RawSize(const RelativePathElement& data)
    {
        return RawSize(data.ReferenceTypeId) + RawSize(data.IsInverse) + RawSize(data.IncludeSubtypes) + RawSize(data.TargetName);
    }


    template<>
    void DataSerializer::Serialize<RelativePathElement>(const RelativePathElement& data)
    {
        *this << data.ReferenceTypeId;
        *this << data.IsInverse;
        *this << data.IncludeSubtypes;
        *this << data.TargetName;
    }


    template<>
    std::size_t RawSize(const RelativePath& data)
    {
        return RawSizeContainer(data.Elements);
    }


    template<>
    void DataSerializer::Serialize<RelativePath>(const RelativePath& data)
    {
        SerializeContainer(*this, data.Elements);
    }


    template<>
    std::size_t RawSize(const BrowsePath& data)
    {
        return RawSize(data.StartingNode) + RawSize(data.RelativePath);
    }


    template<>
    void DataSerializer::Serialize<BrowsePath>(const BrowsePath& data)
    {
        *this << data.StartingNode;
        *this << data.RelativePath;
    }


    template<>
    std::size_t RawSize(const BrowsePathTarget& data)
    {
        return RawSize(data.TargetId) + RawSize(data.RemainingPathIndex);
    }


    template<>
    void DataSerializer::Serialize<BrowsePathTarget>(const BrowsePathTarget& data)
    {
        *this << data.TargetId;
        *this << data.RemainingPathIndex;
    }


    template<>
    std::size_t RawSize(const BrowsePathResult& data)
    {
        return RawSize(data.StatusCode) + RawSizeContainer(data.Targets);
    }


    template<>
    void DataSerializer::Serialize<BrowsePathResult>(const BrowsePathResult& data)
    {
        *this << data.StatusCode;
        SerializeContainer(*this, data.Targets);
    }


    template<>
    std::size_t RawSize(const TranslateBrowsePathsToNodeIdsParameters& data)
    {
        return RawSizeContainer(data.BrowsePaths);
    }


    template<>
    void DataSerializer::Serialize<TranslateBrowsePathsToNodeIdsParameters>(const TranslateBrowsePathsToNodeIdsParameters& data)
    {
        SerializeContainer(*this, data.BrowsePaths);
    }


    template<>
    std::size_t RawSize(const TranslateBrowsePathsToNodeIdsRequest& data)
    {
        return RawSize(data.TypeId) + RawSize(data.RequestHeader) + RawSize(data.Parameters);
    }


    template<>
    void DataSerializer::Serialize<TranslateBrowsePathsToNodeIdsRequest>(const TranslateBrowsePathsToNodeIdsRequest& data)
    {
        *this << data.TypeId;
        *this << data.RequestHeader;
        *this << data.Parameters;
    }


    template<>
    std::size_t RawSize(const TranslateBrowsePathsToNodeIdsData& data)
    {
        return RawSizeContainer(data.Results) + RawSizeContainer(data.DiagnosticInfos);
    }


    template<>
    void DataSerializer::Serialize<TranslateBrowsePathsToNodeIdsData>(const TranslateBrowsePathsToNodeIdsData& data)
    {
        SerializeContainer(*this, data.Results);
        SerializeContainer(*this, data.DiagnosticInfos);
    }


    template<>
    std::size_t RawSize(const TranslateBrowsePathsToNodeIdsResponse& data)
    {
        return RawSize(data.TypeId) + RawSize(data.ResponseHeader) + RawSize(data.Parameters);
    }


    template<>
    void DataSerializer::Serialize<TranslateBrowsePathsToNodeIdsResponse>(const TranslateBrowsePathsToNodeIdsResponse& data)
    {
        *this << data.TypeId;
        *this << data.ResponseHeader;
        *this << data.Parameters;
    }


    template<>
    std::size_t RawSize(const RegisterNodesParameters& data)
    {
        return RawSizeContainer(data.NodesToRegister);
    }


    template<>
    void DataSerializer::Serialize<RegisterNodesParameters>(const RegisterNodesParameters& data)
    {
        SerializeContainer(*this, data.NodesToRegister);
    }


    template<>
    std::size_t RawSize(const RegisterNodesRequest& data)
    {
        return RawSize(data.TypeId) + RawSize(data.RequestHeader) + RawSize(data.Parameters);
    }


    template<>
    void DataSerializer::Serialize<RegisterNodesRequest>(const RegisterNodesRequest& data)
    {
        *this << data.TypeId;
        *this << data.RequestHeader;
        *this << data.Parameters;
    }


    template<>
    std::size_t RawSize(const RegisterNodesData& data)
    {
        return RawSizeContainer(data.RegisteredNodeIds);
    }


    template<>
    void DataSerializer::Serialize<RegisterNodesData>(const RegisterNodesData& data)
    {
        SerializeContainer(*this, data.RegisteredNodeIds);
    }


    template<>
    std::size_t RawSize(const RegisterNodesResponse& data)
    {
        return RawSize(data.TypeId) + RawSize(data.ResponseHeader) + RawSize(data.Parameters);
    }


    template<>
    void DataSerializer::Serialize<RegisterNodesResponse>(const RegisterNodesResponse& data)
    {
        *this << data.TypeId;
        *this << data.ResponseHeader;
        *this << data.Parameters;
    }


    template<>
    std::size_t RawSize(const UnregisterNodesParameters& data)
    {
        return RawSizeContainer(data.NodesToUnregister);
    }


    template<>
    void DataSerializer::Serialize<UnregisterNodesParameters>(const UnregisterNodesParameters& data)
    {
        SerializeContainer(*this, data.NodesToUnregister);
    }


    template<>
    std::size_t RawSize(const UnregisterNodesRequest& data)
    {
        return RawSize(data.TypeId) + RawSize(data.RequestHeader) + RawSize(data.Parameters);
    }


    template<>
    void DataSerializer::Serialize<UnregisterNodesRequest>(const UnregisterNodesRequest& data)
    {
        *this << data.TypeId;
        *this << data.RequestHeader;
        *this << data.Parameters;
    }


    template<>
    std::size_t RawSize(const UnregisterNodesData& data)
    {
        return ;
    }


    template<>
    void DataSerializer::Serialize<UnregisterNodesData>(const UnregisterNodesData& data)
    {
    }


    template<>
    std::size_t RawSize(const UnregisterNodesResponse& data)
    {
        return RawSize(data.TypeId) + RawSize(data.ResponseHeader) + RawSize(data.Parameters);
    }


    template<>
    void DataSerializer::Serialize<UnregisterNodesResponse>(const UnregisterNodesResponse& data)
    {
        *this << data.TypeId;
        *this << data.ResponseHeader;
        *this << data.Parameters;
    }


    template<>
    std::size_t RawSize(const EndpointConfiguration& data)
    {
        return RawSize(data.OperationTimeout) + RawSize(data.UseBinaryEncoding) + RawSize(data.MaxStringLength) + RawSize(data.MaxByteStringLength) + RawSize(data.MaxArrayLength) + RawSize(data.MaxMessageSize) + RawSize(data.MaxBufferSize) + RawSize(data.ChannelLifetime) + RawSize(data.SecurityTokenLifetime);
    }


    template<>
    void DataSerializer::Serialize<EndpointConfiguration>(const EndpointConfiguration& data)
    {
        *this << data.OperationTimeout;
        *this << data.UseBinaryEncoding;
        *this << data.MaxStringLength;
        *this << data.MaxByteStringLength;
        *this << data.MaxArrayLength;
        *this << data.MaxMessageSize;
        *this << data.MaxBufferSize;
        *this << data.ChannelLifetime;
        *this << data.SecurityTokenLifetime;
    }


    template<>
    std::size_t RawSize(const SupportedProfile& data)
    {
        return RawSize(data.OrganizationUri) + RawSize(data.ProfileId) + RawSize(data.ComplianceTool) + RawSize(data.ComplianceDate) + RawSize(data.ComplianceLevel) + RawSizeContainer(data.UnsupportedUnitIds);
    }


    template<>
    void DataSerializer::Serialize<SupportedProfile>(const SupportedProfile& data)
    {
        *this << data.OrganizationUri;
        *this << data.ProfileId;
        *this << data.ComplianceTool;
        *this << data.ComplianceDate;
        *this << data.ComplianceLevel;
        SerializeContainer(*this, data.UnsupportedUnitIds);
    }


    template<>
    std::size_t RawSize(const SoftwareCertificate& data)
    {
        return RawSize(data.ProductName) + RawSize(data.ProductUri) + RawSize(data.VendorName) + RawSize(data.VendorProductCertificate) + RawSize(data.SoftwareVersion) + RawSize(data.BuildNumber) + RawSize(data.BuildDate) + RawSize(data.IssuedBy) + RawSize(data.IssueDate) + RawSizeContainer(data.SupportedProfiles);
    }


    template<>
    void DataSerializer::Serialize<SoftwareCertificate>(const SoftwareCertificate& data)
    {
        *this << data.ProductName;
        *this << data.ProductUri;
        *this << data.VendorName;
        *this << data.VendorProductCertificate;
        *this << data.SoftwareVersion;
        *this << data.BuildNumber;
        *this << data.BuildDate;
        *this << data.IssuedBy;
        *this << data.IssueDate;
        SerializeContainer(*this, data.SupportedProfiles);
    }


    template<>
    std::size_t RawSize(const QueryDataDescription& data)
    {
        return RawSize(data.RelativePath) + RawSize(data.AttributeId) + RawSize(data.IndexRange);
    }


    template<>
    void DataSerializer::Serialize<QueryDataDescription>(const QueryDataDescription& data)
    {
        *this << data.RelativePath;
        *this << data.AttributeId;
        *this << data.IndexRange;
    }


    template<>
    std::size_t RawSize(const NodeTypeDescription& data)
    {
        return RawSize(data.TypeDefinitionNode) + RawSize(data.IncludeSubTypes) + RawSizeContainer(data.DataToReturn);
    }


    template<>
    void DataSerializer::Serialize<NodeTypeDescription>(const NodeTypeDescription& data)
    {
        *this << data.TypeDefinitionNode;
        *this << data.IncludeSubTypes;
        SerializeContainer(*this, data.DataToReturn);
    }


    template<>
    std::size_t RawSize(const QueryDataSet& data)
    {
        return RawSize(data.NodeId) + RawSize(data.TypeDefinitionNode) + RawSizeContainer(data.Values);
    }


    template<>
    void DataSerializer::Serialize<QueryDataSet>(const QueryDataSet& data)
    {
        *this << data.NodeId;
        *this << data.TypeDefinitionNode;
        SerializeContainer(*this, data.Values);
    }


    template<>
    std::size_t RawSize(const NodeReference& data)
    {
        return RawSize(data.NodeId) + RawSize(data.ReferenceTypeId) + RawSize(data.IsForward) + RawSizeContainer(data.ReferencedNodeIds);
    }


    template<>
    void DataSerializer::Serialize<NodeReference>(const NodeReference& data)
    {
        *this << data.NodeId;
        *this << data.ReferenceTypeId;
        *this << data.IsForward;
        SerializeContainer(*this, data.ReferencedNodeIds);
    }


    template<>
    std::size_t RawSize(const ContentFilterElement& data)
    {
        return RawSize(data.FilterOperator) + RawSizeContainer(data.FilterOperands);
    }


    template<>
    void DataSerializer::Serialize<ContentFilterElement>(const ContentFilterElement& data)
    {
        *this << data.FilterOperator;
        SerializeContainer(*this, data.FilterOperands);
    }


    template<>
    std::size_t RawSize(const ContentFilter& data)
    {
        return RawSizeContainer(data.Elements);
    }


    template<>
    void DataSerializer::Serialize<ContentFilter>(const ContentFilter& data)
    {
        SerializeContainer(*this, data.Elements);
    }


    template<>
    std::size_t RawSize(const FilterOperand& data)
    {
        return ;
    }


    template<>
    void DataSerializer::Serialize<FilterOperand>(const FilterOperand& data)
    {
    }


    template<>
    std::size_t RawSize(const ElementOperand& data)
    {
        return RawSize(data.Index);
    }


    template<>
    void DataSerializer::Serialize<ElementOperand>(const ElementOperand& data)
    {
        *this << data.Index;
    }


    template<>
    std::size_t RawSize(const LiteralOperand& data)
    {
        return RawSize(data.Value);
    }


    template<>
    void DataSerializer::Serialize<LiteralOperand>(const LiteralOperand& data)
    {
        *this << data.Value;
    }


    template<>
    std::size_t RawSize(const AttributeOperand& data)
    {
        return RawSize(data.NodeId) + RawSize(data.Alias) + RawSize(data.BrowsePath) + RawSize(data.AttributeId) + RawSize(data.IndexRange);
    }


    template<>
    void DataSerializer::Serialize<AttributeOperand>(const AttributeOperand& data)
    {
        *this << data.NodeId;
        *this << data.Alias;
        *this << data.BrowsePath;
        *this << data.AttributeId;
        *this << data.IndexRange;
    }


    template<>
    std::size_t RawSize(const SimpleAttributeOperand& data)
    {
        return RawSize(data.TypeDefinitionId) + RawSizeContainer(data.BrowsePath) + RawSize(data.AttributeId) + RawSize(data.IndexRange);
    }


    template<>
    void DataSerializer::Serialize<SimpleAttributeOperand>(const SimpleAttributeOperand& data)
    {
        *this << data.TypeDefinitionId;
        SerializeContainer(*this, data.BrowsePath);
        *this << data.AttributeId;
        *this << data.IndexRange;
    }


    template<>
    std::size_t RawSize(const ContentFilterElementResult& data)
    {
        return RawSize(data.StatusCode) + RawSizeContainer(data.OperandStatusCodes) + RawSizeContainer(data.OperandDiagnosticInfos);
    }


    template<>
    void DataSerializer::Serialize<ContentFilterElementResult>(const ContentFilterElementResult& data)
    {
        *this << data.StatusCode;
        SerializeContainer(*this, data.OperandStatusCodes);
        SerializeContainer(*this, data.OperandDiagnosticInfos);
    }


    template<>
    std::size_t RawSize(const ContentFilterResult& data)
    {
        return RawSizeContainer(data.ElementResults) + RawSizeContainer(data.ElementDiagnosticInfos);
    }


    template<>
    void DataSerializer::Serialize<ContentFilterResult>(const ContentFilterResult& data)
    {
        SerializeContainer(*this, data.ElementResults);
        SerializeContainer(*this, data.ElementDiagnosticInfos);
    }


    template<>
    std::size_t RawSize(const ParsingResult& data)
    {
        return RawSize(data.StatusCode) + RawSizeContainer(data.DataStatusCodes) + RawSizeContainer(data.DataDiagnosticInfos);
    }


    template<>
    void DataSerializer::Serialize<ParsingResult>(const ParsingResult& data)
    {
        *this << data.StatusCode;
        SerializeContainer(*this, data.DataStatusCodes);
        SerializeContainer(*this, data.DataDiagnosticInfos);
    }


    template<>
    std::size_t RawSize(const QueryFirstParameters& data)
    {
        return RawSize(data.View) + RawSizeContainer(data.NodeTypes) + RawSize(data.Filter) + RawSize(data.MaxDataSetsToReturn) + RawSize(data.MaxReferencesToReturn);
    }


    template<>
    void DataSerializer::Serialize<QueryFirstParameters>(const QueryFirstParameters& data)
    {
        *this << data.View;
        SerializeContainer(*this, data.NodeTypes);
        *this << data.Filter;
        *this << data.MaxDataSetsToReturn;
        *this << data.MaxReferencesToReturn;
    }


    template<>
    std::size_t RawSize(const QueryFirstRequest& data)
    {
        return RawSize(data.TypeId) + RawSize(data.RequestHeader) + RawSize(data.Parameters);
    }


    template<>
    void DataSerializer::Serialize<QueryFirstRequest>(const QueryFirstRequest& data)
    {
        *this << data.TypeId;
        *this << data.RequestHeader;
        *this << data.Parameters;
    }


    template<>
    std::size_t RawSize(const QueryFirstData& data)
    {
        return RawSizeContainer(data.QueryDataSets) + RawSize(data.ContinuationPoint) + RawSizeContainer(data.ParsingResults) + RawSizeContainer(data.DiagnosticInfos) + RawSize(data.FilterResult);
    }


    template<>
    void DataSerializer::Serialize<QueryFirstData>(const QueryFirstData& data)
    {
        SerializeContainer(*this, data.QueryDataSets);
        *this << data.ContinuationPoint;
        SerializeContainer(*this, data.ParsingResults);
        SerializeContainer(*this, data.DiagnosticInfos);
        *this << data.FilterResult;
    }


    template<>
    std::size_t RawSize(const QueryFirstResponse& data)
    {
        return RawSize(data.TypeId) + RawSize(data.ResponseHeader) + RawSize(data.Parameters);
    }


    template<>
    void DataSerializer::Serialize<QueryFirstResponse>(const QueryFirstResponse& data)
    {
        *this << data.TypeId;
        *this << data.ResponseHeader;
        *this << data.Parameters;
    }


    template<>
    std::size_t RawSize(const QueryNextParameters& data)
    {
        return RawSize(data.ReleaseContinuationPoint) + RawSize(data.ContinuationPoint);
    }


    template<>
    void DataSerializer::Serialize<QueryNextParameters>(const QueryNextParameters& data)
    {
        *this << data.ReleaseContinuationPoint;
        *this << data.ContinuationPoint;
    }


    template<>
    std::size_t RawSize(const QueryNextRequest& data)
    {
        return RawSize(data.TypeId) + RawSize(data.RequestHeader) + RawSize(data.Parameters);
    }


    template<>
    void DataSerializer::Serialize<QueryNextRequest>(const QueryNextRequest& data)
    {
        *this << data.TypeId;
        *this << data.RequestHeader;
        *this << data.Parameters;
    }


    template<>
    std::size_t RawSize(const QueryNextData& data)
    {
        return RawSizeContainer(data.QueryDataSets) + RawSize(data.RevisedContinuationPoint);
    }


    template<>
    void DataSerializer::Serialize<QueryNextData>(const QueryNextData& data)
    {
        SerializeContainer(*this, data.QueryDataSets);
        *this << data.RevisedContinuationPoint;
    }


    template<>
    std::size_t RawSize(const QueryNextResponse& data)
    {
        return RawSize(data.TypeId) + RawSize(data.ResponseHeader) + RawSize(data.Parameters);
    }


    template<>
    void DataSerializer::Serialize<QueryNextResponse>(const QueryNextResponse& data)
    {
        *this << data.TypeId;
        *this << data.ResponseHeader;
        *this << data.Parameters;
    }


    template<>
    std::size_t RawSize(const ReadValueId& data)
    {
        return RawSize(data.NodeId) + RawSize(data.AttributeId) + RawSize(data.IndexRange) + RawSize(data.DataEncoding);
    }


    template<>
    void DataSerializer::Serialize<ReadValueId>(const ReadValueId& data)
    {
        *this << data.NodeId;
        *this << data.AttributeId;
        *this << data.IndexRange;
        *this << data.DataEncoding;
    }


    template<>
    std::size_t RawSize(const ReadParameters& data)
    {
        return RawSize(data.MaxAge) + RawSize(data.TimestampsToReturn) + RawSizeContainer(data.NodesToRead);
    }


    template<>
    void DataSerializer::Serialize<ReadParameters>(const ReadParameters& data)
    {
        *this << data.MaxAge;
        *this << data.TimestampsToReturn;
        SerializeContainer(*this, data.NodesToRead);
    }


    template<>
    std::size_t RawSize(const ReadRequest& data)
    {
        return RawSize(data.TypeId) + RawSize(data.RequestHeader) + RawSize(data.Parameters);
    }


    template<>
    void DataSerializer::Serialize<ReadRequest>(const ReadRequest& data)
    {
        *this << data.TypeId;
        *this << data.RequestHeader;
        *this << data.Parameters;
    }


    template<>
    std::size_t RawSize(const ReadData& data)
    {
        return RawSizeContainer(data.Results) + RawSizeContainer(data.DiagnosticInfos);
    }


    template<>
    void DataSerializer::Serialize<ReadData>(const ReadData& data)
    {
        SerializeContainer(*this, data.Results);
        SerializeContainer(*this, data.DiagnosticInfos);
    }


    template<>
    std::size_t RawSize(const ReadResponse& data)
    {
        return RawSize(data.TypeId) + RawSize(data.ResponseHeader) + RawSize(data.Parameters);
    }


    template<>
    void DataSerializer::Serialize<ReadResponse>(const ReadResponse& data)
    {
        *this << data.TypeId;
        *this << data.ResponseHeader;
        *this << data.Parameters;
    }


    template<>
    std::size_t RawSize(const HistoryReadValueId& data)
    {
        return RawSize(data.NodeId) + RawSize(data.IndexRange) + RawSize(data.DataEncoding) + RawSize(data.ContinuationPoint);
    }


    template<>
    void DataSerializer::Serialize<HistoryReadValueId>(const HistoryReadValueId& data)
    {
        *this << data.NodeId;
        *this << data.IndexRange;
        *this << data.DataEncoding;
        *this << data.ContinuationPoint;
    }


    template<>
    std::size_t RawSize(const HistoryReadResult& data)
    {
        return RawSize(data.StatusCode) + RawSize(data.ContinuationPoint) + RawSize(data.HistoryData);
    }


    template<>
    void DataSerializer::Serialize<HistoryReadResult>(const HistoryReadResult& data)
    {
        *this << data.StatusCode;
        *this << data.ContinuationPoint;
        *this << data.HistoryData;
    }


    template<>
    std::size_t RawSize(const HistoryReadDetails& data)
    {
        return ;
    }


    template<>
    void DataSerializer::Serialize<HistoryReadDetails>(const HistoryReadDetails& data)
    {
    }


    template<>
    std::size_t RawSize(const ReadEventDetails& data)
    {
        return RawSize(data.NumValuesPerNode) + RawSize(data.StartTime) + RawSize(data.EndTime) + RawSize(data.Filter);
    }


    template<>
    void DataSerializer::Serialize<ReadEventDetails>(const ReadEventDetails& data)
    {
        *this << data.NumValuesPerNode;
        *this << data.StartTime;
        *this << data.EndTime;
        *this << data.Filter;
    }


    template<>
    std::size_t RawSize(const ReadRawModifiedDetails& data)
    {
        return RawSize(data.IsReadModified) + RawSize(data.StartTime) + RawSize(data.EndTime) + RawSize(data.NumValuesPerNode) + RawSize(data.ReturnBounds);
    }


    template<>
    void DataSerializer::Serialize<ReadRawModifiedDetails>(const ReadRawModifiedDetails& data)
    {
        *this << data.IsReadModified;
        *this << data.StartTime;
        *this << data.EndTime;
        *this << data.NumValuesPerNode;
        *this << data.ReturnBounds;
    }


    template<>
    std::size_t RawSize(const ReadProcessedDetails& data)
    {
        return RawSize(data.StartTime) + RawSize(data.EndTime) + RawSize(data.ProcessingInterval) + RawSizeContainer(data.AggregateType) + RawSize(data.AggregateConfiguration);
    }


    template<>
    void DataSerializer::Serialize<ReadProcessedDetails>(const ReadProcessedDetails& data)
    {
        *this << data.StartTime;
        *this << data.EndTime;
        *this << data.ProcessingInterval;
        SerializeContainer(*this, data.AggregateType);
        *this << data.AggregateConfiguration;
    }


    template<>
    std::size_t RawSize(const ReadAtTimeDetails& data)
    {
        return RawSizeContainer(data.ReqTimes) + RawSize(data.UseSimpleBounds);
    }


    template<>
    void DataSerializer::Serialize<ReadAtTimeDetails>(const ReadAtTimeDetails& data)
    {
        SerializeContainer(*this, data.ReqTimes);
        *this << data.UseSimpleBounds;
    }


    template<>
    std::size_t RawSize(const HistoryData& data)
    {
        return RawSizeContainer(data.DataValues);
    }


    template<>
    void DataSerializer::Serialize<HistoryData>(const HistoryData& data)
    {
        SerializeContainer(*this, data.DataValues);
    }


    template<>
    std::size_t RawSize(const ModificationInfo& data)
    {
        return RawSize(data.ModificationTime) + RawSize(data.UpdateType) + RawSize(data.UserName);
    }


    template<>
    void DataSerializer::Serialize<ModificationInfo>(const ModificationInfo& data)
    {
        *this << data.ModificationTime;
        *this << data.UpdateType;
        *this << data.UserName;
    }


    template<>
    std::size_t RawSize(const HistoryModifiedData& data)
    {
        return RawSizeContainer(data.DataValues) + RawSizeContainer(data.ModificationInfos);
    }


    template<>
    void DataSerializer::Serialize<HistoryModifiedData>(const HistoryModifiedData& data)
    {
        SerializeContainer(*this, data.DataValues);
        SerializeContainer(*this, data.ModificationInfos);
    }


    template<>
    std::size_t RawSize(const HistoryEvent& data)
    {
        return RawSizeContainer(data.Events);
    }


    template<>
    void DataSerializer::Serialize<HistoryEvent>(const HistoryEvent& data)
    {
        SerializeContainer(*this, data.Events);
    }


    template<>
    std::size_t RawSize(const HistoryReadParameters& data)
    {
        return RawSize(data.HistoryReadDetails) + RawSize(data.TimestampsToReturn) + RawSize(data.ReleaseContinuationPoints) + RawSizeContainer(data.NodesToRead);
    }


    template<>
    void DataSerializer::Serialize<HistoryReadParameters>(const HistoryReadParameters& data)
    {
        *this << data.HistoryReadDetails;
        *this << data.TimestampsToReturn;
        *this << data.ReleaseContinuationPoints;
        SerializeContainer(*this, data.NodesToRead);
    }


    template<>
    std::size_t RawSize(const HistoryReadRequest& data)
    {
        return RawSize(data.TypeId) + RawSize(data.RequestHeader) + RawSize(data.Parameters);
    }


    template<>
    void DataSerializer::Serialize<HistoryReadRequest>(const HistoryReadRequest& data)
    {
        *this << data.TypeId;
        *this << data.RequestHeader;
        *this << data.Parameters;
    }


    template<>
    std::size_t RawSize(const HistoryReadData& data)
    {
        return RawSizeContainer(data.Results) + RawSizeContainer(data.DiagnosticInfos);
    }


    template<>
    void DataSerializer::Serialize<HistoryReadData>(const HistoryReadData& data)
    {
        SerializeContainer(*this, data.Results);
        SerializeContainer(*this, data.DiagnosticInfos);
    }


    template<>
    std::size_t RawSize(const HistoryReadResponse& data)
    {
        return RawSize(data.TypeId) + RawSize(data.ResponseHeader) + RawSize(data.Parameters);
    }


    template<>
    void DataSerializer::Serialize<HistoryReadResponse>(const HistoryReadResponse& data)
    {
        *this << data.TypeId;
        *this << data.ResponseHeader;
        *this << data.Parameters;
    }


    template<>
    std::size_t RawSize(const WriteValue& data)
    {
        return RawSize(data.NodeId) + RawSize(data.AttributeId) + RawSize(data.IndexRange) + RawSize(data.Value);
    }


    template<>
    void DataSerializer::Serialize<WriteValue>(const WriteValue& data)
    {
        *this << data.NodeId;
        *this << data.AttributeId;
        *this << data.IndexRange;
        *this << data.Value;
    }


    template<>
    std::size_t RawSize(const WriteParameters& data)
    {
        return RawSizeContainer(data.NodesToWrite);
    }


    template<>
    void DataSerializer::Serialize<WriteParameters>(const WriteParameters& data)
    {
        SerializeContainer(*this, data.NodesToWrite);
    }


    template<>
    std::size_t RawSize(const WriteRequest& data)
    {
        return RawSize(data.TypeId) + RawSize(data.RequestHeader) + RawSize(data.Parameters);
    }


    template<>
    void DataSerializer::Serialize<WriteRequest>(const WriteRequest& data)
    {
        *this << data.TypeId;
        *this << data.RequestHeader;
        *this << data.Parameters;
    }


    template<>
    std::size_t RawSize(const WriteData& data)
    {
        return RawSizeContainer(data.Results) + RawSizeContainer(data.DiagnosticInfos);
    }


    template<>
    void DataSerializer::Serialize<WriteData>(const WriteData& data)
    {
        SerializeContainer(*this, data.Results);
        SerializeContainer(*this, data.DiagnosticInfos);
    }


    template<>
    std::size_t RawSize(const WriteResponse& data)
    {
        return RawSize(data.TypeId) + RawSize(data.ResponseHeader) + RawSize(data.Parameters);
    }


    template<>
    void DataSerializer::Serialize<WriteResponse>(const WriteResponse& data)
    {
        *this << data.TypeId;
        *this << data.ResponseHeader;
        *this << data.Parameters;
    }


    template<>
    std::size_t RawSize(const HistoryUpdateDetails& data)
    {
        return RawSize(data.NodeId);
    }


    template<>
    void DataSerializer::Serialize<HistoryUpdateDetails>(const HistoryUpdateDetails& data)
    {
        *this << data.NodeId;
    }


    template<>
    std::size_t RawSize(const UpdateDataDetails& data)
    {
        return RawSize(data.NodeId) + RawSize(data.PerformInsertReplace) + RawSizeContainer(data.UpdateValues);
    }


    template<>
    void DataSerializer::Serialize<UpdateDataDetails>(const UpdateDataDetails& data)
    {
        *this << data.NodeId;
        *this << data.PerformInsertReplace;
        SerializeContainer(*this, data.UpdateValues);
    }


    template<>
    std::size_t RawSize(const UpdateStructureDataDetails& data)
    {
        return RawSize(data.NodeId) + RawSize(data.PerformInsertReplace) + RawSizeContainer(data.UpdateValues);
    }


    template<>
    void DataSerializer::Serialize<UpdateStructureDataDetails>(const UpdateStructureDataDetails& data)
    {
        *this << data.NodeId;
        *this << data.PerformInsertReplace;
        SerializeContainer(*this, data.UpdateValues);
    }


    template<>
    std::size_t RawSize(const UpdateEventDetails& data)
    {
        return RawSize(data.NodeId) + RawSize(data.PerformInsertReplace) + RawSize(data.Filter) + RawSizeContainer(data.EventData);
    }


    template<>
    void DataSerializer::Serialize<UpdateEventDetails>(const UpdateEventDetails& data)
    {
        *this << data.NodeId;
        *this << data.PerformInsertReplace;
        *this << data.Filter;
        SerializeContainer(*this, data.EventData);
    }


    template<>
    std::size_t RawSize(const DeleteRawModifiedDetails& data)
    {
        return RawSize(data.NodeId) + RawSize(data.IsDeleteModified) + RawSize(data.StartTime) + RawSize(data.EndTime);
    }


    template<>
    void DataSerializer::Serialize<DeleteRawModifiedDetails>(const DeleteRawModifiedDetails& data)
    {
        *this << data.NodeId;
        *this << data.IsDeleteModified;
        *this << data.StartTime;
        *this << data.EndTime;
    }


    template<>
    std::size_t RawSize(const DeleteAtTimeDetails& data)
    {
        return RawSize(data.NodeId) + RawSizeContainer(data.ReqTimes);
    }


    template<>
    void DataSerializer::Serialize<DeleteAtTimeDetails>(const DeleteAtTimeDetails& data)
    {
        *this << data.NodeId;
        SerializeContainer(*this, data.ReqTimes);
    }


    template<>
    std::size_t RawSize(const DeleteEventDetails& data)
    {
        return RawSize(data.NodeId) + RawSizeContainer(data.EventIds);
    }


    template<>
    void DataSerializer::Serialize<DeleteEventDetails>(const DeleteEventDetails& data)
    {
        *this << data.NodeId;
        SerializeContainer(*this, data.EventIds);
    }


    template<>
    std::size_t RawSize(const HistoryUpdateResult& data)
    {
        return RawSize(data.StatusCode) + RawSizeContainer(data.OperationResults) + RawSizeContainer(data.DiagnosticInfos);
    }


    template<>
    void DataSerializer::Serialize<HistoryUpdateResult>(const HistoryUpdateResult& data)
    {
        *this << data.StatusCode;
        SerializeContainer(*this, data.OperationResults);
        SerializeContainer(*this, data.DiagnosticInfos);
    }


    template<>
    std::size_t RawSize(const HistoryUpdateEventResult& data)
    {
        return RawSize(data.StatusCode) + RawSize(data.EventFilterResult);
    }


    template<>
    void DataSerializer::Serialize<HistoryUpdateEventResult>(const HistoryUpdateEventResult& data)
    {
        *this << data.StatusCode;
        *this << data.EventFilterResult;
    }


    template<>
    std::size_t RawSize(const HistoryUpdateParameters& data)
    {
        return RawSizeContainer(data.HistoryUpdateDetails);
    }


    template<>
    void DataSerializer::Serialize<HistoryUpdateParameters>(const HistoryUpdateParameters& data)
    {
        SerializeContainer(*this, data.HistoryUpdateDetails);
    }


    template<>
    std::size_t RawSize(const HistoryUpdateRequest& data)
    {
        return RawSize(data.TypeId) + RawSize(data.RequestHeader) + RawSize(data.Parameters);
    }


    template<>
    void DataSerializer::Serialize<HistoryUpdateRequest>(const HistoryUpdateRequest& data)
    {
        *this << data.TypeId;
        *this << data.RequestHeader;
        *this << data.Parameters;
    }


    template<>
    std::size_t RawSize(const HistoryUpdateData& data)
    {
        return RawSizeContainer(data.Results) + RawSizeContainer(data.DiagnosticInfos);
    }


    template<>
    void DataSerializer::Serialize<HistoryUpdateData>(const HistoryUpdateData& data)
    {
        SerializeContainer(*this, data.Results);
        SerializeContainer(*this, data.DiagnosticInfos);
    }


    template<>
    std::size_t RawSize(const HistoryUpdateResponse& data)
    {
        return RawSize(data.TypeId) + RawSize(data.ResponseHeader) + RawSize(data.Parameters);
    }


    template<>
    void DataSerializer::Serialize<HistoryUpdateResponse>(const HistoryUpdateResponse& data)
    {
        *this << data.TypeId;
        *this << data.ResponseHeader;
        *this << data.Parameters;
    }


    template<>
    std::size_t RawSize(const CallMethodParameters& data)
    {
        return RawSize(data.MethodId) + RawSizeContainer(data.InputArguments);
    }


    template<>
    void DataSerializer::Serialize<CallMethodParameters>(const CallMethodParameters& data)
    {
        *this << data.MethodId;
        SerializeContainer(*this, data.InputArguments);
    }


    template<>
    std::size_t RawSize(const CallMethodRequest& data)
    {
        return RawSize(data.TypeId) + RawSize(data.ObjectId) + RawSize(data.Parameters);
    }


    template<>
    void DataSerializer::Serialize<CallMethodRequest>(const CallMethodRequest& data)
    {
        *this << data.TypeId;
        *this << data.ObjectId;
        *this << data.Parameters;
    }


    template<>
    std::size_t RawSize(const CallMethodResult& data)
    {
        return RawSize(data.StatusCode) + RawSizeContainer(data.InputArgumentResults) + RawSizeContainer(data.InputArgumentDiagnosticInfos) + RawSizeContainer(data.OutputArguments);
    }


    template<>
    void DataSerializer::Serialize<CallMethodResult>(const CallMethodResult& data)
    {
        *this << data.StatusCode;
        SerializeContainer(*this, data.InputArgumentResults);
        SerializeContainer(*this, data.InputArgumentDiagnosticInfos);
        SerializeContainer(*this, data.OutputArguments);
    }


    template<>
    std::size_t RawSize(const CallParameters& data)
    {
        return RawSizeContainer(data.MethodsToCall);
    }


    template<>
    void DataSerializer::Serialize<CallParameters>(const CallParameters& data)
    {
        SerializeContainer(*this, data.MethodsToCall);
    }


    template<>
    std::size_t RawSize(const CallRequest& data)
    {
        return RawSize(data.TypeId) + RawSize(data.RequestHeader) + RawSize(data.Parameters);
    }


    template<>
    void DataSerializer::Serialize<CallRequest>(const CallRequest& data)
    {
        *this << data.TypeId;
        *this << data.RequestHeader;
        *this << data.Parameters;
    }


    template<>
    std::size_t RawSize(const CallData& data)
    {
        return RawSizeContainer(data.Results) + RawSizeContainer(data.DiagnosticInfos);
    }


    template<>
    void DataSerializer::Serialize<CallData>(const CallData& data)
    {
        SerializeContainer(*this, data.Results);
        SerializeContainer(*this, data.DiagnosticInfos);
    }


    template<>
    std::size_t RawSize(const CallResponse& data)
    {
        return RawSize(data.TypeId) + RawSize(data.ResponseHeader) + RawSize(data.Parameters);
    }


    template<>
    void DataSerializer::Serialize<CallResponse>(const CallResponse& data)
    {
        *this << data.TypeId;
        *this << data.ResponseHeader;
        *this << data.Parameters;
    }


    template<>
    std::size_t RawSize(const MonitoringFilter& data)
    {
        return ;
    }


    template<>
    void DataSerializer::Serialize<MonitoringFilter>(const MonitoringFilter& data)
    {
    }


    template<>
    std::size_t RawSize(const DataChangeFilter& data)
    {
        return RawSize(data.Trigger) + RawSize(data.DeadbandType) + RawSize(data.DeadbandValue);
    }


    template<>
    void DataSerializer::Serialize<DataChangeFilter>(const DataChangeFilter& data)
    {
        *this << data.Trigger;
        *this << data.DeadbandType;
        *this << data.DeadbandValue;
    }


    template<>
    std::size_t RawSize(const EventFilter& data)
    {
        return RawSizeContainer(data.SelectClauses) + RawSize(data.WhereClause);
    }


    template<>
    void DataSerializer::Serialize<EventFilter>(const EventFilter& data)
    {
        SerializeContainer(*this, data.SelectClauses);
        *this << data.WhereClause;
    }


    template<>
    std::size_t RawSize(const AggregateConfiguration& data)
    {
        return RawSize(data.UseServerCapabilitiesDefaults) + RawSize(data.TreatUncertainAsBad) + RawSize(data.PercentDataBad) + RawSize(data.PercentDataGood) + RawSize(data.UseSlopedExtrapolation);
    }


    template<>
    void DataSerializer::Serialize<AggregateConfiguration>(const AggregateConfiguration& data)
    {
        *this << data.UseServerCapabilitiesDefaults;
        *this << data.TreatUncertainAsBad;
        *this << data.PercentDataBad;
        *this << data.PercentDataGood;
        *this << data.UseSlopedExtrapolation;
    }


    template<>
    std::size_t RawSize(const AggregateFilter& data)
    {
        return RawSize(data.StartTime) + RawSize(data.AggregateType) + RawSize(data.ProcessingInterval) + RawSize(data.AggregateConfiguration);
    }


    template<>
    void DataSerializer::Serialize<AggregateFilter>(const AggregateFilter& data)
    {
        *this << data.StartTime;
        *this << data.AggregateType;
        *this << data.ProcessingInterval;
        *this << data.AggregateConfiguration;
    }


    template<>
    std::size_t RawSize(const MonitoringFilterResult& data)
    {
        return ;
    }


    template<>
    void DataSerializer::Serialize<MonitoringFilterResult>(const MonitoringFilterResult& data)
    {
    }


    template<>
    std::size_t RawSize(const EventFilterResult& data)
    {
        return RawSizeContainer(data.SelectClauseResults) + RawSizeContainer(data.SelectClauseDiagnosticInfos) + RawSize(data.WhereClauseResult);
    }


    template<>
    void DataSerializer::Serialize<EventFilterResult>(const EventFilterResult& data)
    {
        SerializeContainer(*this, data.SelectClauseResults);
        SerializeContainer(*this, data.SelectClauseDiagnosticInfos);
        *this << data.WhereClauseResult;
    }


    template<>
    std::size_t RawSize(const AggregateFilterResult& data)
    {
        return RawSize(data.RevisedStartTime) + RawSize(data.RevisedProcessingInterval) + RawSize(data.RevisedAggregateConfiguration);
    }


    template<>
    void DataSerializer::Serialize<AggregateFilterResult>(const AggregateFilterResult& data)
    {
        *this << data.RevisedStartTime;
        *this << data.RevisedProcessingInterval;
        *this << data.RevisedAggregateConfiguration;
    }


    template<>
    std::size_t RawSize(const MonitoringParameters& data)
    {
        return RawSize(data.ClientHandle) + RawSize(data.SamplingInterval) + RawSize(data.Filter) + RawSize(data.QueueSize) + RawSize(data.DiscardOldest);
    }


    template<>
    void DataSerializer::Serialize<MonitoringParameters>(const MonitoringParameters& data)
    {
        *this << data.ClientHandle;
        *this << data.SamplingInterval;
        *this << data.Filter;
        *this << data.QueueSize;
        *this << data.DiscardOldest;
    }


    template<>
    std::size_t RawSize(const MonitoredItemCreateParameters& data)
    {
        return RawSize(data.MonitoringMode) + RawSize(data.RequestedParameters);
    }


    template<>
    void DataSerializer::Serialize<MonitoredItemCreateParameters>(const MonitoredItemCreateParameters& data)
    {
        *this << data.MonitoringMode;
        *this << data.RequestedParameters;
    }


    template<>
    std::size_t RawSize(const MonitoredItemCreateRequest& data)
    {
        return RawSize(data.TypeId) + RawSize(data.ItemToMonitor) + RawSize(data.Parameters);
    }


    template<>
    void DataSerializer::Serialize<MonitoredItemCreateRequest>(const MonitoredItemCreateRequest& data)
    {
        *this << data.TypeId;
        *this << data.ItemToMonitor;
        *this << data.Parameters;
    }


    template<>
    std::size_t RawSize(const MonitoredItemCreateResult& data)
    {
        return RawSize(data.StatusCode) + RawSize(data.MonitoredItemId) + RawSize(data.RevisedSamplingInterval) + RawSize(data.RevisedQueueSize) + RawSize(data.FilterResult);
    }


    template<>
    void DataSerializer::Serialize<MonitoredItemCreateResult>(const MonitoredItemCreateResult& data)
    {
        *this << data.StatusCode;
        *this << data.MonitoredItemId;
        *this << data.RevisedSamplingInterval;
        *this << data.RevisedQueueSize;
        *this << data.FilterResult;
    }


    template<>
    std::size_t RawSize(const CreateMonitoredItemsParameters& data)
    {
        return RawSize(data.SubscriptionId) + RawSize(data.TimestampsToReturn) + RawSizeContainer(data.ItemsToCreate);
    }


    template<>
    void DataSerializer::Serialize<CreateMonitoredItemsParameters>(const CreateMonitoredItemsParameters& data)
    {
        *this << data.SubscriptionId;
        *this << data.TimestampsToReturn;
        SerializeContainer(*this, data.ItemsToCreate);
    }


    template<>
    std::size_t RawSize(const CreateMonitoredItemsRequest& data)
    {
        return RawSize(data.TypeId) + RawSize(data.RequestHeader) + RawSize(data.Parameters);
    }


    template<>
    void DataSerializer::Serialize<CreateMonitoredItemsRequest>(const CreateMonitoredItemsRequest& data)
    {
        *this << data.TypeId;
        *this << data.RequestHeader;
        *this << data.Parameters;
    }


    template<>
    std::size_t RawSize(const CreateMonitoredItemsData& data)
    {
        return RawSizeContainer(data.Results) + RawSizeContainer(data.DiagnosticInfos);
    }


    template<>
    void DataSerializer::Serialize<CreateMonitoredItemsData>(const CreateMonitoredItemsData& data)
    {
        SerializeContainer(*this, data.Results);
        SerializeContainer(*this, data.DiagnosticInfos);
    }


    template<>
    std::size_t RawSize(const CreateMonitoredItemsResponse& data)
    {
        return RawSize(data.TypeId) + RawSize(data.ResponseHeader) + RawSize(data.Parameters);
    }


    template<>
    void DataSerializer::Serialize<CreateMonitoredItemsResponse>(const CreateMonitoredItemsResponse& data)
    {
        *this << data.TypeId;
        *this << data.ResponseHeader;
        *this << data.Parameters;
    }


    template<>
    std::size_t RawSize(const MonitoredItemModifyParameters& data)
    {
        return RawSize(data.RequestedParameters);
    }


    template<>
    void DataSerializer::Serialize<MonitoredItemModifyParameters>(const MonitoredItemModifyParameters& data)
    {
        *this << data.RequestedParameters;
    }


    template<>
    std::size_t RawSize(const MonitoredItemModifyRequest& data)
    {
        return RawSize(data.TypeId) + RawSize(data.MonitoredItemId) + RawSize(data.Parameters);
    }


    template<>
    void DataSerializer::Serialize<MonitoredItemModifyRequest>(const MonitoredItemModifyRequest& data)
    {
        *this << data.TypeId;
        *this << data.MonitoredItemId;
        *this << data.Parameters;
    }


    template<>
    std::size_t RawSize(const MonitoredItemModifyResult& data)
    {
        return RawSize(data.StatusCode) + RawSize(data.RevisedSamplingInterval) + RawSize(data.RevisedQueueSize) + RawSize(data.FilterResult);
    }


    template<>
    void DataSerializer::Serialize<MonitoredItemModifyResult>(const MonitoredItemModifyResult& data)
    {
        *this << data.StatusCode;
        *this << data.RevisedSamplingInterval;
        *this << data.RevisedQueueSize;
        *this << data.FilterResult;
    }


    template<>
    std::size_t RawSize(const ModifyMonitoredItemsParameters& data)
    {
        return RawSize(data.SubscriptionId) + RawSize(data.TimestampsToReturn) + RawSizeContainer(data.ItemsToModify);
    }


    template<>
    void DataSerializer::Serialize<ModifyMonitoredItemsParameters>(const ModifyMonitoredItemsParameters& data)
    {
        *this << data.SubscriptionId;
        *this << data.TimestampsToReturn;
        SerializeContainer(*this, data.ItemsToModify);
    }


    template<>
    std::size_t RawSize(const ModifyMonitoredItemsRequest& data)
    {
        return RawSize(data.TypeId) + RawSize(data.RequestHeader) + RawSize(data.Parameters);
    }


    template<>
    void DataSerializer::Serialize<ModifyMonitoredItemsRequest>(const ModifyMonitoredItemsRequest& data)
    {
        *this << data.TypeId;
        *this << data.RequestHeader;
        *this << data.Parameters;
    }


    template<>
    std::size_t RawSize(const ModifyMonitoredItemsData& data)
    {
        return RawSizeContainer(data.Results) + RawSizeContainer(data.DiagnosticInfos);
    }


    template<>
    void DataSerializer::Serialize<ModifyMonitoredItemsData>(const ModifyMonitoredItemsData& data)
    {
        SerializeContainer(*this, data.Results);
        SerializeContainer(*this, data.DiagnosticInfos);
    }


    template<>
    std::size_t RawSize(const ModifyMonitoredItemsResponse& data)
    {
        return RawSize(data.TypeId) + RawSize(data.ResponseHeader) + RawSize(data.Parameters);
    }


    template<>
    void DataSerializer::Serialize<ModifyMonitoredItemsResponse>(const ModifyMonitoredItemsResponse& data)
    {
        *this << data.TypeId;
        *this << data.ResponseHeader;
        *this << data.Parameters;
    }


    template<>
    std::size_t RawSize(const SetMonitoringModeParameters& data)
    {
        return RawSize(data.SubscriptionId) + RawSize(data.MonitoringMode) + RawSizeContainer(data.MonitoredItemIds);
    }


    template<>
    void DataSerializer::Serialize<SetMonitoringModeParameters>(const SetMonitoringModeParameters& data)
    {
        *this << data.SubscriptionId;
        *this << data.MonitoringMode;
        SerializeContainer(*this, data.MonitoredItemIds);
    }


    template<>
    std::size_t RawSize(const SetMonitoringModeRequest& data)
    {
        return RawSize(data.TypeId) + RawSize(data.RequestHeader) + RawSize(data.Parameters);
    }


    template<>
    void DataSerializer::Serialize<SetMonitoringModeRequest>(const SetMonitoringModeRequest& data)
    {
        *this << data.TypeId;
        *this << data.RequestHeader;
        *this << data.Parameters;
    }


    template<>
    std::size_t RawSize(const SetMonitoringModeData& data)
    {
        return RawSizeContainer(data.Results) + RawSizeContainer(data.DiagnosticInfos);
    }


    template<>
    void DataSerializer::Serialize<SetMonitoringModeData>(const SetMonitoringModeData& data)
    {
        SerializeContainer(*this, data.Results);
        SerializeContainer(*this, data.DiagnosticInfos);
    }


    template<>
    std::size_t RawSize(const SetMonitoringModeResponse& data)
    {
        return RawSize(data.TypeId) + RawSize(data.ResponseHeader) + RawSize(data.Parameters);
    }


    template<>
    void DataSerializer::Serialize<SetMonitoringModeResponse>(const SetMonitoringModeResponse& data)
    {
        *this << data.TypeId;
        *this << data.ResponseHeader;
        *this << data.Parameters;
    }


    template<>
    std::size_t RawSize(const SetTriggeringParameters& data)
    {
        return RawSize(data.SubscriptionId) + RawSize(data.TriggeringItemId) + RawSizeContainer(data.LinksToAdd) + RawSizeContainer(data.LinksToRemove);
    }


    template<>
    void DataSerializer::Serialize<SetTriggeringParameters>(const SetTriggeringParameters& data)
    {
        *this << data.SubscriptionId;
        *this << data.TriggeringItemId;
        SerializeContainer(*this, data.LinksToAdd);
        SerializeContainer(*this, data.LinksToRemove);
    }


    template<>
    std::size_t RawSize(const SetTriggeringRequest& data)
    {
        return RawSize(data.TypeId) + RawSize(data.RequestHeader) + RawSize(data.Parameters);
    }


    template<>
    void DataSerializer::Serialize<SetTriggeringRequest>(const SetTriggeringRequest& data)
    {
        *this << data.TypeId;
        *this << data.RequestHeader;
        *this << data.Parameters;
    }


    template<>
    std::size_t RawSize(const SetTriggeringData& data)
    {
        return RawSizeContainer(data.AddResults) + RawSizeContainer(data.AddDiagnosticInfos) + RawSizeContainer(data.RemoveResults) + RawSizeContainer(data.RemoveDiagnosticInfos);
    }


    template<>
    void DataSerializer::Serialize<SetTriggeringData>(const SetTriggeringData& data)
    {
        SerializeContainer(*this, data.AddResults);
        SerializeContainer(*this, data.AddDiagnosticInfos);
        SerializeContainer(*this, data.RemoveResults);
        SerializeContainer(*this, data.RemoveDiagnosticInfos);
    }


    template<>
    std::size_t RawSize(const SetTriggeringResponse& data)
    {
        return RawSize(data.TypeId) + RawSize(data.ResponseHeader) + RawSize(data.Parameters);
    }


    template<>
    void DataSerializer::Serialize<SetTriggeringResponse>(const SetTriggeringResponse& data)
    {
        *this << data.TypeId;
        *this << data.ResponseHeader;
        *this << data.Parameters;
    }


    template<>
    std::size_t RawSize(const DeleteMonitoredItemsParameters& data)
    {
        return RawSize(data.SubscriptionId) + RawSizeContainer(data.MonitoredItemIds);
    }


    template<>
    void DataSerializer::Serialize<DeleteMonitoredItemsParameters>(const DeleteMonitoredItemsParameters& data)
    {
        *this << data.SubscriptionId;
        SerializeContainer(*this, data.MonitoredItemIds);
    }


    template<>
    std::size_t RawSize(const DeleteMonitoredItemsRequest& data)
    {
        return RawSize(data.TypeId) + RawSize(data.RequestHeader) + RawSize(data.Parameters);
    }


    template<>
    void DataSerializer::Serialize<DeleteMonitoredItemsRequest>(const DeleteMonitoredItemsRequest& data)
    {
        *this << data.TypeId;
        *this << data.RequestHeader;
        *this << data.Parameters;
    }


    template<>
    std::size_t RawSize(const DeleteMonitoredItemsData& data)
    {
        return RawSizeContainer(data.Results) + RawSizeContainer(data.DiagnosticInfos);
    }


    template<>
    void DataSerializer::Serialize<DeleteMonitoredItemsData>(const DeleteMonitoredItemsData& data)
    {
        SerializeContainer(*this, data.Results);
        SerializeContainer(*this, data.DiagnosticInfos);
    }


    template<>
    std::size_t RawSize(const DeleteMonitoredItemsResponse& data)
    {
        return RawSize(data.TypeId) + RawSize(data.ResponseHeader) + RawSize(data.Parameters);
    }


    template<>
    void DataSerializer::Serialize<DeleteMonitoredItemsResponse>(const DeleteMonitoredItemsResponse& data)
    {
        *this << data.TypeId;
        *this << data.ResponseHeader;
        *this << data.Parameters;
    }


    template<>
    std::size_t RawSize(const CreateSubscriptionParameters& data)
    {
        return RawSize(data.RequestedPublishingInterval) + RawSize(data.RequestedLifetimeCount) + RawSize(data.RequestedMaxKeepAliveCount) + RawSize(data.MaxNotificationsPerPublish) + RawSize(data.PublishingEnabled) + RawSize(data.Priority);
    }


    template<>
    void DataSerializer::Serialize<CreateSubscriptionParameters>(const CreateSubscriptionParameters& data)
    {
        *this << data.RequestedPublishingInterval;
        *this << data.RequestedLifetimeCount;
        *this << data.RequestedMaxKeepAliveCount;
        *this << data.MaxNotificationsPerPublish;
        *this << data.PublishingEnabled;
        *this << data.Priority;
    }


    template<>
    std::size_t RawSize(const CreateSubscriptionRequest& data)
    {
        return RawSize(data.TypeId) + RawSize(data.RequestHeader) + RawSize(data.Parameters);
    }


    template<>
    void DataSerializer::Serialize<CreateSubscriptionRequest>(const CreateSubscriptionRequest& data)
    {
        *this << data.TypeId;
        *this << data.RequestHeader;
        *this << data.Parameters;
    }


    template<>
    std::size_t RawSize(const CreateSubscriptionData& data)
    {
        return RawSize(data.SubscriptionId) + RawSize(data.RevisedPublishingInterval) + RawSize(data.RevisedLifetimeCount) + RawSize(data.RevisedMaxKeepAliveCount);
    }


    template<>
    void DataSerializer::Serialize<CreateSubscriptionData>(const CreateSubscriptionData& data)
    {
        *this << data.SubscriptionId;
        *this << data.RevisedPublishingInterval;
        *this << data.RevisedLifetimeCount;
        *this << data.RevisedMaxKeepAliveCount;
    }


    template<>
    std::size_t RawSize(const CreateSubscriptionResponse& data)
    {
        return RawSize(data.TypeId) + RawSize(data.ResponseHeader) + RawSize(data.Parameters);
    }


    template<>
    void DataSerializer::Serialize<CreateSubscriptionResponse>(const CreateSubscriptionResponse& data)
    {
        *this << data.TypeId;
        *this << data.ResponseHeader;
        *this << data.Parameters;
    }


    template<>
    std::size_t RawSize(const ModifySubscriptionParameters& data)
    {
        return RawSize(data.SubscriptionId) + RawSize(data.RequestedPublishingInterval) + RawSize(data.RequestedLifetimeCount) + RawSize(data.RequestedMaxKeepAliveCount) + RawSize(data.MaxNotificationsPerPublish) + RawSize(data.Priority);
    }


    template<>
    void DataSerializer::Serialize<ModifySubscriptionParameters>(const ModifySubscriptionParameters& data)
    {
        *this << data.SubscriptionId;
        *this << data.RequestedPublishingInterval;
        *this << data.RequestedLifetimeCount;
        *this << data.RequestedMaxKeepAliveCount;
        *this << data.MaxNotificationsPerPublish;
        *this << data.Priority;
    }


    template<>
    std::size_t RawSize(const ModifySubscriptionRequest& data)
    {
        return RawSize(data.TypeId) + RawSize(data.RequestHeader) + RawSize(data.Parameters);
    }


    template<>
    void DataSerializer::Serialize<ModifySubscriptionRequest>(const ModifySubscriptionRequest& data)
    {
        *this << data.TypeId;
        *this << data.RequestHeader;
        *this << data.Parameters;
    }


    template<>
    std::size_t RawSize(const ModifySubscriptionData& data)
    {
        return RawSize(data.RevisedPublishingInterval) + RawSize(data.RevisedLifetimeCount) + RawSize(data.RevisedMaxKeepAliveCount);
    }


    template<>
    void DataSerializer::Serialize<ModifySubscriptionData>(const ModifySubscriptionData& data)
    {
        *this << data.RevisedPublishingInterval;
        *this << data.RevisedLifetimeCount;
        *this << data.RevisedMaxKeepAliveCount;
    }


    template<>
    std::size_t RawSize(const ModifySubscriptionResponse& data)
    {
        return RawSize(data.TypeId) + RawSize(data.ResponseHeader) + RawSize(data.Parameters);
    }


    template<>
    void DataSerializer::Serialize<ModifySubscriptionResponse>(const ModifySubscriptionResponse& data)
    {
        *this << data.TypeId;
        *this << data.ResponseHeader;
        *this << data.Parameters;
    }


    template<>
    std::size_t RawSize(const SetPublishingModeParameters& data)
    {
        return RawSize(data.PublishingEnabled) + RawSizeContainer(data.SubscriptionIds);
    }


    template<>
    void DataSerializer::Serialize<SetPublishingModeParameters>(const SetPublishingModeParameters& data)
    {
        *this << data.PublishingEnabled;
        SerializeContainer(*this, data.SubscriptionIds);
    }


    template<>
    std::size_t RawSize(const SetPublishingModeRequest& data)
    {
        return RawSize(data.TypeId) + RawSize(data.RequestHeader) + RawSize(data.Parameters);
    }


    template<>
    void DataSerializer::Serialize<SetPublishingModeRequest>(const SetPublishingModeRequest& data)
    {
        *this << data.TypeId;
        *this << data.RequestHeader;
        *this << data.Parameters;
    }


    template<>
    std::size_t RawSize(const SetPublishingModeData& data)
    {
        return RawSizeContainer(data.Results) + RawSizeContainer(data.DiagnosticInfos);
    }


    template<>
    void DataSerializer::Serialize<SetPublishingModeData>(const SetPublishingModeData& data)
    {
        SerializeContainer(*this, data.Results);
        SerializeContainer(*this, data.DiagnosticInfos);
    }


    template<>
    std::size_t RawSize(const SetPublishingModeResponse& data)
    {
        return RawSize(data.TypeId) + RawSize(data.ResponseHeader) + RawSize(data.Parameters);
    }


    template<>
    void DataSerializer::Serialize<SetPublishingModeResponse>(const SetPublishingModeResponse& data)
    {
        *this << data.TypeId;
        *this << data.ResponseHeader;
        *this << data.Parameters;
    }


    template<>
    std::size_t RawSize(const NotificationMessage& data)
    {
        return RawSize(data.SequenceNumber) + RawSize(data.PublishTime) + RawSizeContainer(data.NotificationData);
    }


    template<>
    void DataSerializer::Serialize<NotificationMessage>(const NotificationMessage& data)
    {
        *this << data.SequenceNumber;
        *this << data.PublishTime;
        SerializeContainer(*this, data.NotificationData);
    }


    template<>
    std::size_t RawSize(const NotificationData& data)
    {
        return ;
    }


    template<>
    void DataSerializer::Serialize<NotificationData>(const NotificationData& data)
    {
    }


    template<>
    std::size_t RawSize(const DataChangeNotification& data)
    {
        return RawSizeContainer(data.MonitoredItems) + RawSizeContainer(data.DiagnosticInfos);
    }


    template<>
    void DataSerializer::Serialize<DataChangeNotification>(const DataChangeNotification& data)
    {
        SerializeContainer(*this, data.MonitoredItems);
        SerializeContainer(*this, data.DiagnosticInfos);
    }


    template<>
    std::size_t RawSize(const MonitoredItemNotification& data)
    {
        return RawSize(data.ClientHandle) + RawSize(data.Value);
    }


    template<>
    void DataSerializer::Serialize<MonitoredItemNotification>(const MonitoredItemNotification& data)
    {
        *this << data.ClientHandle;
        *this << data.Value;
    }


    template<>
    std::size_t RawSize(const EventNotificationList& data)
    {
        return RawSizeContainer(data.Events);
    }


    template<>
    void DataSerializer::Serialize<EventNotificationList>(const EventNotificationList& data)
    {
        SerializeContainer(*this, data.Events);
    }


    template<>
    std::size_t RawSize(const EventFieldList& data)
    {
        return RawSize(data.ClientHandle) + RawSizeContainer(data.EventFields);
    }


    template<>
    void DataSerializer::Serialize<EventFieldList>(const EventFieldList& data)
    {
        *this << data.ClientHandle;
        SerializeContainer(*this, data.EventFields);
    }


    template<>
    std::size_t RawSize(const HistoryEventFieldList& data)
    {
        return RawSizeContainer(data.EventFields);
    }


    template<>
    void DataSerializer::Serialize<HistoryEventFieldList>(const HistoryEventFieldList& data)
    {
        SerializeContainer(*this, data.EventFields);
    }


    template<>
    std::size_t RawSize(const StatusChangeNotification& data)
    {
        return RawSize(data.Status) + RawSize(data.DiagnosticInfo);
    }


    template<>
    void DataSerializer::Serialize<StatusChangeNotification>(const StatusChangeNotification& data)
    {
        *this << data.Status;
        *this << data.DiagnosticInfo;
    }


    template<>
    std::size_t RawSize(const SubscriptionAcknowledgement& data)
    {
        return RawSize(data.SubscriptionId) + RawSize(data.SequenceNumber);
    }


    template<>
    void DataSerializer::Serialize<SubscriptionAcknowledgement>(const SubscriptionAcknowledgement& data)
    {
        *this << data.SubscriptionId;
        *this << data.SequenceNumber;
    }


    template<>
    std::size_t RawSize(const PublishParameters& data)
    {
        return RawSizeContainer(data.SubscriptionAcknowledgements);
    }


    template<>
    void DataSerializer::Serialize<PublishParameters>(const PublishParameters& data)
    {
        SerializeContainer(*this, data.SubscriptionAcknowledgements);
    }


    template<>
    std::size_t RawSize(const PublishRequest& data)
    {
        return RawSize(data.TypeId) + RawSize(data.RequestHeader) + RawSize(data.Parameters);
    }


    template<>
    void DataSerializer::Serialize<PublishRequest>(const PublishRequest& data)
    {
        *this << data.TypeId;
        *this << data.RequestHeader;
        *this << data.Parameters;
    }


    template<>
    std::size_t RawSize(const PublishData& data)
    {
        return RawSize(data.SubscriptionId) + RawSizeContainer(data.AvailableSequenceNumbers) + RawSize(data.MoreNotifications) + RawSize(data.NotificationMessage) + RawSizeContainer(data.Results) + RawSizeContainer(data.DiagnosticInfos);
    }


    template<>
    void DataSerializer::Serialize<PublishData>(const PublishData& data)
    {
        *this << data.SubscriptionId;
        SerializeContainer(*this, data.AvailableSequenceNumbers);
        *this << data.MoreNotifications;
        *this << data.NotificationMessage;
        SerializeContainer(*this, data.Results);
        SerializeContainer(*this, data.DiagnosticInfos);
    }


    template<>
    std::size_t RawSize(const PublishResponse& data)
    {
        return RawSize(data.TypeId) + RawSize(data.ResponseHeader) + RawSize(data.Parameters);
    }


    template<>
    void DataSerializer::Serialize<PublishResponse>(const PublishResponse& data)
    {
        *this << data.TypeId;
        *this << data.ResponseHeader;
        *this << data.Parameters;
    }


    template<>
    std::size_t RawSize(const RepublishParameters& data)
    {
        return RawSize(data.SubscriptionId) + RawSize(data.RetransmitSequenceNumber);
    }


    template<>
    void DataSerializer::Serialize<RepublishParameters>(const RepublishParameters& data)
    {
        *this << data.SubscriptionId;
        *this << data.RetransmitSequenceNumber;
    }


    template<>
    std::size_t RawSize(const RepublishRequest& data)
    {
        return RawSize(data.TypeId) + RawSize(data.RequestHeader) + RawSize(data.Parameters);
    }


    template<>
    void DataSerializer::Serialize<RepublishRequest>(const RepublishRequest& data)
    {
        *this << data.TypeId;
        *this << data.RequestHeader;
        *this << data.Parameters;
    }


    template<>
    std::size_t RawSize(const RepublishData& data)
    {
        return RawSize(data.NotificationMessage);
    }


    template<>
    void DataSerializer::Serialize<RepublishData>(const RepublishData& data)
    {
        *this << data.NotificationMessage;
    }


    template<>
    std::size_t RawSize(const RepublishResponse& data)
    {
        return RawSize(data.TypeId) + RawSize(data.ResponseHeader) + RawSize(data.Parameters);
    }


    template<>
    void DataSerializer::Serialize<RepublishResponse>(const RepublishResponse& data)
    {
        *this << data.TypeId;
        *this << data.ResponseHeader;
        *this << data.Parameters;
    }


    template<>
    std::size_t RawSize(const TransferResult& data)
    {
        return RawSize(data.StatusCode) + RawSizeContainer(data.AvailableSequenceNumbers);
    }


    template<>
    void DataSerializer::Serialize<TransferResult>(const TransferResult& data)
    {
        *this << data.StatusCode;
        SerializeContainer(*this, data.AvailableSequenceNumbers);
    }


    template<>
    std::size_t RawSize(const TransferSubscriptionsParameters& data)
    {
        return RawSizeContainer(data.SubscriptionIds) + RawSize(data.SendInitialValues);
    }


    template<>
    void DataSerializer::Serialize<TransferSubscriptionsParameters>(const TransferSubscriptionsParameters& data)
    {
        SerializeContainer(*this, data.SubscriptionIds);
        *this << data.SendInitialValues;
    }


    template<>
    std::size_t RawSize(const TransferSubscriptionsRequest& data)
    {
        return RawSize(data.TypeId) + RawSize(data.RequestHeader) + RawSize(data.Parameters);
    }


    template<>
    void DataSerializer::Serialize<TransferSubscriptionsRequest>(const TransferSubscriptionsRequest& data)
    {
        *this << data.TypeId;
        *this << data.RequestHeader;
        *this << data.Parameters;
    }


    template<>
    std::size_t RawSize(const TransferSubscriptionsData& data)
    {
        return RawSizeContainer(data.Results) + RawSizeContainer(data.DiagnosticInfos);
    }


    template<>
    void DataSerializer::Serialize<TransferSubscriptionsData>(const TransferSubscriptionsData& data)
    {
        SerializeContainer(*this, data.Results);
        SerializeContainer(*this, data.DiagnosticInfos);
    }


    template<>
    std::size_t RawSize(const TransferSubscriptionsResponse& data)
    {
        return RawSize(data.TypeId) + RawSize(data.ResponseHeader) + RawSize(data.Parameters);
    }


    template<>
    void DataSerializer::Serialize<TransferSubscriptionsResponse>(const TransferSubscriptionsResponse& data)
    {
        *this << data.TypeId;
        *this << data.ResponseHeader;
        *this << data.Parameters;
    }


    template<>
    std::size_t RawSize(const DeleteSubscriptionsParameters& data)
    {
        return RawSizeContainer(data.SubscriptionIds);
    }


    template<>
    void DataSerializer::Serialize<DeleteSubscriptionsParameters>(const DeleteSubscriptionsParameters& data)
    {
        SerializeContainer(*this, data.SubscriptionIds);
    }


    template<>
    std::size_t RawSize(const DeleteSubscriptionsRequest& data)
    {
        return RawSize(data.TypeId) + RawSize(data.RequestHeader) + RawSize(data.Parameters);
    }


    template<>
    void DataSerializer::Serialize<DeleteSubscriptionsRequest>(const DeleteSubscriptionsRequest& data)
    {
        *this << data.TypeId;
        *this << data.RequestHeader;
        *this << data.Parameters;
    }


    template<>
    std::size_t RawSize(const DeleteSubscriptionsData& data)
    {
        return RawSizeContainer(data.Results) + RawSizeContainer(data.DiagnosticInfos);
    }


    template<>
    void DataSerializer::Serialize<DeleteSubscriptionsData>(const DeleteSubscriptionsData& data)
    {
        SerializeContainer(*this, data.Results);
        SerializeContainer(*this, data.DiagnosticInfos);
    }


    template<>
    std::size_t RawSize(const DeleteSubscriptionsResponse& data)
    {
        return RawSize(data.TypeId) + RawSize(data.ResponseHeader) + RawSize(data.Parameters);
    }


    template<>
    void DataSerializer::Serialize<DeleteSubscriptionsResponse>(const DeleteSubscriptionsResponse& data)
    {
        *this << data.TypeId;
        *this << data.ResponseHeader;
        *this << data.Parameters;
    }


    template<>
    std::size_t RawSize(const ScalarTestType& data)
    {
        return RawSize(data.Boolean) + RawSize(data.SByte) + RawSize(data.Byte) + RawSize(data.Int16) + RawSize(data.UInt16) + RawSize(data.Int32) + RawSize(data.UInt32) + RawSize(data.Int64) + RawSize(data.UInt64) + RawSize(data.Float) + RawSize(data.Double) + RawSize(data.String) + RawSize(data.DateTime) + RawSize(data.Guid) + RawSize(data.ByteString) + RawSize(data.XmlElement) + RawSize(data.NodeId) + RawSize(data.ExpandedNodeId) + RawSize(data.StatusCode) + RawSize(data.DiagnosticInfo) + RawSize(data.QualifiedName) + RawSize(data.LocalizedText) + RawSize(data.ExtensionObject) + RawSize(data.DataValue) + RawSize(data.EnumeratedValue);
    }


    template<>
    void DataSerializer::Serialize<ScalarTestType>(const ScalarTestType& data)
    {
        *this << data.Boolean;
        *this << data.SByte;
        *this << data.Byte;
        *this << data.Int16;
        *this << data.UInt16;
        *this << data.Int32;
        *this << data.UInt32;
        *this << data.Int64;
        *this << data.UInt64;
        *this << data.Float;
        *this << data.Double;
        *this << data.String;
        *this << data.DateTime;
        *this << data.Guid;
        *this << data.ByteString;
        *this << data.XmlElement;
        *this << data.NodeId;
        *this << data.ExpandedNodeId;
        *this << data.StatusCode;
        *this << data.DiagnosticInfo;
        *this << data.QualifiedName;
        *this << data.LocalizedText;
        *this << data.ExtensionObject;
        *this << data.DataValue;
        *this << data.EnumeratedValue;
    }


    template<>
    std::size_t RawSize(const ArrayTestType& data)
    {
        return RawSizeContainer(data.Booleans) + RawSizeContainer(data.SBytes) + RawSizeContainer(data.Int16s) + RawSizeContainer(data.UInt16s) + RawSizeContainer(data.Int32s) + RawSizeContainer(data.UInt32s) + RawSizeContainer(data.Int64s) + RawSizeContainer(data.UInt64s) + RawSizeContainer(data.Floats) + RawSizeContainer(data.Doubles) + RawSizeContainer(data.Strings) + RawSizeContainer(data.DateTimes) + RawSizeContainer(data.Guids) + RawSizeContainer(data.ByteStrings) + RawSizeContainer(data.XmlElements) + RawSizeContainer(data.NodeIds) + RawSizeContainer(data.ExpandedNodeIds) + RawSizeContainer(data.StatusCodes) + RawSizeContainer(data.DiagnosticInfos) + RawSizeContainer(data.QualifiedNames) + RawSizeContainer(data.LocalizedTexts) + RawSizeContainer(data.ExtensionObjects) + RawSizeContainer(data.DataValues) + RawSizeContainer(data.Variants) + RawSizeContainer(data.EnumeratedValues);
    }


    template<>
    void DataSerializer::Serialize<ArrayTestType>(const ArrayTestType& data)
    {
        SerializeContainer(*this, data.Booleans);
        SerializeContainer(*this, data.SBytes);
        SerializeContainer(*this, data.Int16s);
        SerializeContainer(*this, data.UInt16s);
        SerializeContainer(*this, data.Int32s);
        SerializeContainer(*this, data.UInt32s);
        SerializeContainer(*this, data.Int64s);
        SerializeContainer(*this, data.UInt64s);
        SerializeContainer(*this, data.Floats);
        SerializeContainer(*this, data.Doubles);
        SerializeContainer(*this, data.Strings);
        SerializeContainer(*this, data.DateTimes);
        SerializeContainer(*this, data.Guids);
        SerializeContainer(*this, data.ByteStrings);
        SerializeContainer(*this, data.XmlElements);
        SerializeContainer(*this, data.NodeIds);
        SerializeContainer(*this, data.ExpandedNodeIds);
        SerializeContainer(*this, data.StatusCodes);
        SerializeContainer(*this, data.DiagnosticInfos);
        SerializeContainer(*this, data.QualifiedNames);
        SerializeContainer(*this, data.LocalizedTexts);
        SerializeContainer(*this, data.ExtensionObjects);
        SerializeContainer(*this, data.DataValues);
        SerializeContainer(*this, data.Variants);
        SerializeContainer(*this, data.EnumeratedValues);
    }


    template<>
    std::size_t RawSize(const CompositeTestType& data)
    {
        return RawSize(data.Field1) + RawSize(data.Field2);
    }


    template<>
    void DataSerializer::Serialize<CompositeTestType>(const CompositeTestType& data)
    {
        *this << data.Field1;
        *this << data.Field2;
    }


    template<>
    std::size_t RawSize(const TestStackParameters& data)
    {
        return RawSize(data.TestId) + RawSize(data.Iteration) + RawSize(data.Input);
    }


    template<>
    void DataSerializer::Serialize<TestStackParameters>(const TestStackParameters& data)
    {
        *this << data.TestId;
        *this << data.Iteration;
        *this << data.Input;
    }


    template<>
    std::size_t RawSize(const TestStackRequest& data)
    {
        return RawSize(data.TypeId) + RawSize(data.RequestHeader) + RawSize(data.Parameters);
    }


    template<>
    void DataSerializer::Serialize<TestStackRequest>(const TestStackRequest& data)
    {
        *this << data.TypeId;
        *this << data.RequestHeader;
        *this << data.Parameters;
    }


    template<>
    std::size_t RawSize(const TestStackData& data)
    {
        return RawSize(data.Output);
    }


    template<>
    void DataSerializer::Serialize<TestStackData>(const TestStackData& data)
    {
        *this << data.Output;
    }


    template<>
    std::size_t RawSize(const TestStackResponse& data)
    {
        return RawSize(data.TypeId) + RawSize(data.ResponseHeader) + RawSize(data.Parameters);
    }


    template<>
    void DataSerializer::Serialize<TestStackResponse>(const TestStackResponse& data)
    {
        *this << data.TypeId;
        *this << data.ResponseHeader;
        *this << data.Parameters;
    }


    template<>
    std::size_t RawSize(const TestStackExParameters& data)
    {
        return RawSize(data.TestId) + RawSize(data.Iteration) + RawSize(data.Input);
    }


    template<>
    void DataSerializer::Serialize<TestStackExParameters>(const TestStackExParameters& data)
    {
        *this << data.TestId;
        *this << data.Iteration;
        *this << data.Input;
    }


    template<>
    std::size_t RawSize(const TestStackExRequest& data)
    {
        return RawSize(data.TypeId) + RawSize(data.RequestHeader) + RawSize(data.Parameters);
    }


    template<>
    void DataSerializer::Serialize<TestStackExRequest>(const TestStackExRequest& data)
    {
        *this << data.TypeId;
        *this << data.RequestHeader;
        *this << data.Parameters;
    }


    template<>
    std::size_t RawSize(const TestStackExData& data)
    {
        return RawSize(data.Output);
    }


    template<>
    void DataSerializer::Serialize<TestStackExData>(const TestStackExData& data)
    {
        *this << data.Output;
    }


    template<>
    std::size_t RawSize(const TestStackExResponse& data)
    {
        return RawSize(data.TypeId) + RawSize(data.ResponseHeader) + RawSize(data.Parameters);
    }


    template<>
    void DataSerializer::Serialize<TestStackExResponse>(const TestStackExResponse& data)
    {
        *this << data.TypeId;
        *this << data.ResponseHeader;
        *this << data.Parameters;
    }


    template<>
    std::size_t RawSize(const BuildInfo& data)
    {
        return RawSize(data.ProductUri) + RawSize(data.ManufacturerName) + RawSize(data.ProductName) + RawSize(data.SoftwareVersion) + RawSize(data.BuildNumber) + RawSize(data.BuildDate);
    }


    template<>
    void DataSerializer::Serialize<BuildInfo>(const BuildInfo& data)
    {
        *this << data.ProductUri;
        *this << data.ManufacturerName;
        *this << data.ProductName;
        *this << data.SoftwareVersion;
        *this << data.BuildNumber;
        *this << data.BuildDate;
    }


    template<>
    std::size_t RawSize(const RedundantServerDataType& data)
    {
        return RawSize(data.ServerId) + RawSize(data.ServiceLevel) + RawSize(data.ServerState);
    }


    template<>
    void DataSerializer::Serialize<RedundantServerDataType>(const RedundantServerDataType& data)
    {
        *this << data.ServerId;
        *this << data.ServiceLevel;
        *this << data.ServerState;
    }


    template<>
    std::size_t RawSize(const EndpointUrlListDataType& data)
    {
        return RawSizeContainer(data.EndpointUrlList);
    }


    template<>
    void DataSerializer::Serialize<EndpointUrlListDataType>(const EndpointUrlListDataType& data)
    {
        SerializeContainer(*this, data.EndpointUrlList);
    }


    template<>
    std::size_t RawSize(const NetworkGroupDataType& data)
    {
        return RawSize(data.ServerUri) + RawSizeContainer(data.NetworkPaths);
    }


    template<>
    void DataSerializer::Serialize<NetworkGroupDataType>(const NetworkGroupDataType& data)
    {
        *this << data.ServerUri;
        SerializeContainer(*this, data.NetworkPaths);
    }


    template<>
    std::size_t RawSize(const SamplingIntervalDiagnosticsDataType& data)
    {
        return RawSize(data.SamplingInterval) + RawSize(data.MonitoredItemCount) + RawSize(data.MaxMonitoredItemCount) + RawSize(data.DisabledMonitoredItemCount);
    }


    template<>
    void DataSerializer::Serialize<SamplingIntervalDiagnosticsDataType>(const SamplingIntervalDiagnosticsDataType& data)
    {
        *this << data.SamplingInterval;
        *this << data.MonitoredItemCount;
        *this << data.MaxMonitoredItemCount;
        *this << data.DisabledMonitoredItemCount;
    }


    template<>
    std::size_t RawSize(const ServerDiagnosticsSummaryDataType& data)
    {
        return RawSize(data.ServerViewCount) + RawSize(data.CurrentSessionCount) + RawSize(data.CumulatedSessionCount) + RawSize(data.SecurityRejectedSessionCount) + RawSize(data.RejectedSessionCount) + RawSize(data.SessionTimeoutCount) + RawSize(data.SessionAbortCount) + RawSize(data.CurrentSubscriptionCount) + RawSize(data.CumulatedSubscriptionCount) + RawSize(data.PublishingIntervalCount) + RawSize(data.SecurityRejectedRequestsCount) + RawSize(data.RejectedRequestsCount);
    }


    template<>
    void DataSerializer::Serialize<ServerDiagnosticsSummaryDataType>(const ServerDiagnosticsSummaryDataType& data)
    {
        *this << data.ServerViewCount;
        *this << data.CurrentSessionCount;
        *this << data.CumulatedSessionCount;
        *this << data.SecurityRejectedSessionCount;
        *this << data.RejectedSessionCount;
        *this << data.SessionTimeoutCount;
        *this << data.SessionAbortCount;
        *this << data.CurrentSubscriptionCount;
        *this << data.CumulatedSubscriptionCount;
        *this << data.PublishingIntervalCount;
        *this << data.SecurityRejectedRequestsCount;
        *this << data.RejectedRequestsCount;
    }


    template<>
    std::size_t RawSize(const ServerStatusDataType& data)
    {
        return RawSize(data.StartTime) + RawSize(data.CurrentTime) + RawSize(data.State) + RawSize(data.BuildInfo) + RawSize(data.SecondsTillShutdown) + RawSize(data.ShutdownReason);
    }


    template<>
    void DataSerializer::Serialize<ServerStatusDataType>(const ServerStatusDataType& data)
    {
        *this << data.StartTime;
        *this << data.CurrentTime;
        *this << data.State;
        *this << data.BuildInfo;
        *this << data.SecondsTillShutdown;
        *this << data.ShutdownReason;
    }


    template<>
    std::size_t RawSize(const SessionDiagnosticsDataType& data)
    {
        return RawSize(data.SessionId) + RawSize(data.SessionName) + RawSize(data.ClientDescription) + RawSize(data.ServerUri) + RawSize(data.EndpointUrl) + RawSizeContainer(data.LocaleIds) + RawSize(data.ActualSessionTimeout) + RawSize(data.MaxResponseMessageSize) + RawSize(data.ClientConnectionTime) + RawSize(data.ClientLastContactTime) + RawSize(data.CurrentSubscriptionsCount) + RawSize(data.CurrentMonitoredItemsCount) + RawSize(data.CurrentPublishRequestsInQueue) + RawSize(data.TotalRequestCount) + RawSize(data.UnauthorizedRequestCount) + RawSize(data.ReadCount) + RawSize(data.HistoryReadCount) + RawSize(data.WriteCount) + RawSize(data.HistoryUpdateCount) + RawSize(data.CallCount) + RawSize(data.CreateMonitoredItemsCount) + RawSize(data.ModifyMonitoredItemsCount) + RawSize(data.SetMonitoringModeCount) + RawSize(data.SetTriggeringCount) + RawSize(data.DeleteMonitoredItemsCount) + RawSize(data.CreateSubscriptionCount) + RawSize(data.ModifySubscriptionCount) + RawSize(data.SetPublishingModeCount) + RawSize(data.PublishCount) + RawSize(data.RepublishCount) + RawSize(data.TransferSubscriptionsCount) + RawSize(data.DeleteSubscriptionsCount) + RawSize(data.AddNodesCount) + RawSize(data.AddReferencesCount) + RawSize(data.DeleteNodesCount) + RawSize(data.DeleteReferencesCount) + RawSize(data.BrowseCount) + RawSize(data.BrowseNextCount) + RawSize(data.TranslateBrowsePathsToNodeIdsCount) + RawSize(data.QueryFirstCount) + RawSize(data.QueryNextCount) + RawSize(data.RegisterNodesCount) + RawSize(data.UnregisterNodesCount);
    }


    template<>
    void DataSerializer::Serialize<SessionDiagnosticsDataType>(const SessionDiagnosticsDataType& data)
    {
        *this << data.SessionId;
        *this << data.SessionName;
        *this << data.ClientDescription;
        *this << data.ServerUri;
        *this << data.EndpointUrl;
        SerializeContainer(*this, data.LocaleIds);
        *this << data.ActualSessionTimeout;
        *this << data.MaxResponseMessageSize;
        *this << data.ClientConnectionTime;
        *this << data.ClientLastContactTime;
        *this << data.CurrentSubscriptionsCount;
        *this << data.CurrentMonitoredItemsCount;
        *this << data.CurrentPublishRequestsInQueue;
        *this << data.TotalRequestCount;
        *this << data.UnauthorizedRequestCount;
        *this << data.ReadCount;
        *this << data.HistoryReadCount;
        *this << data.WriteCount;
        *this << data.HistoryUpdateCount;
        *this << data.CallCount;
        *this << data.CreateMonitoredItemsCount;
        *this << data.ModifyMonitoredItemsCount;
        *this << data.SetMonitoringModeCount;
        *this << data.SetTriggeringCount;
        *this << data.DeleteMonitoredItemsCount;
        *this << data.CreateSubscriptionCount;
        *this << data.ModifySubscriptionCount;
        *this << data.SetPublishingModeCount;
        *this << data.PublishCount;
        *this << data.RepublishCount;
        *this << data.TransferSubscriptionsCount;
        *this << data.DeleteSubscriptionsCount;
        *this << data.AddNodesCount;
        *this << data.AddReferencesCount;
        *this << data.DeleteNodesCount;
        *this << data.DeleteReferencesCount;
        *this << data.BrowseCount;
        *this << data.BrowseNextCount;
        *this << data.TranslateBrowsePathsToNodeIdsCount;
        *this << data.QueryFirstCount;
        *this << data.QueryNextCount;
        *this << data.RegisterNodesCount;
        *this << data.UnregisterNodesCount;
    }


    template<>
    std::size_t RawSize(const SessionSecurityDiagnosticsDataType& data)
    {
        return RawSize(data.SessionId) + RawSize(data.ClientUserIdOfSession) + RawSizeContainer(data.ClientUserIdHistory) + RawSize(data.AuthenticationMechanism) + RawSize(data.Encoding) + RawSize(data.TransportProtocol) + RawSize(data.SecurityMode) + RawSize(data.SecurityPolicyUri) + RawSize(data.ClientCertificate);
    }


    template<>
    void DataSerializer::Serialize<SessionSecurityDiagnosticsDataType>(const SessionSecurityDiagnosticsDataType& data)
    {
        *this << data.SessionId;
        *this << data.ClientUserIdOfSession;
        SerializeContainer(*this, data.ClientUserIdHistory);
        *this << data.AuthenticationMechanism;
        *this << data.Encoding;
        *this << data.TransportProtocol;
        *this << data.SecurityMode;
        *this << data.SecurityPolicyUri;
        *this << data.ClientCertificate;
    }


    template<>
    std::size_t RawSize(const ServiceCounterDataType& data)
    {
        return RawSize(data.TotalCount) + RawSize(data.ErrorCount);
    }


    template<>
    void DataSerializer::Serialize<ServiceCounterDataType>(const ServiceCounterDataType& data)
    {
        *this << data.TotalCount;
        *this << data.ErrorCount;
    }


    template<>
    std::size_t RawSize(const StatusResult& data)
    {
        return RawSize(data.StatusCode) + RawSize(data.DiagnosticInfo);
    }


    template<>
    void DataSerializer::Serialize<StatusResult>(const StatusResult& data)
    {
        *this << data.StatusCode;
        *this << data.DiagnosticInfo;
    }


    template<>
    std::size_t RawSize(const SubscriptionDiagnosticsDataType& data)
    {
        return RawSize(data.SessionId) + RawSize(data.SubscriptionId) + RawSize(data.Priority) + RawSize(data.PublishingInterval) + RawSize(data.MaxKeepAliveCount) + RawSize(data.MaxLifetimeCount) + RawSize(data.MaxNotificationsPerPublish) + RawSize(data.PublishingEnabled) + RawSize(data.ModifyCount) + RawSize(data.EnableCount) + RawSize(data.DisableCount) + RawSize(data.RepublishRequestCount) + RawSize(data.RepublishMessageRequestCount) + RawSize(data.RepublishMessageCount) + RawSize(data.TransferRequestCount) + RawSize(data.TransferredToAltClientCount) + RawSize(data.TransferredToSameClientCount) + RawSize(data.PublishRequestCount) + RawSize(data.DataChangeNotificationsCount) + RawSize(data.EventNotificationsCount) + RawSize(data.NotificationsCount) + RawSize(data.LatePublishRequestCount) + RawSize(data.CurrentKeepAliveCount) + RawSize(data.CurrentLifetimeCount) + RawSize(data.UnacknowledgedMessageCount) + RawSize(data.DiscardedMessageCount) + RawSize(data.MonitoredItemCount) + RawSize(data.DisabledMonitoredItemCount) + RawSize(data.MonitoringQueueOverflowCount) + RawSize(data.NextSequenceNumber) + RawSize(data.EventQueueOverFlowCount);
    }


    template<>
    void DataSerializer::Serialize<SubscriptionDiagnosticsDataType>(const SubscriptionDiagnosticsDataType& data)
    {
        *this << data.SessionId;
        *this << data.SubscriptionId;
        *this << data.Priority;
        *this << data.PublishingInterval;
        *this << data.MaxKeepAliveCount;
        *this << data.MaxLifetimeCount;
        *this << data.MaxNotificationsPerPublish;
        *this << data.PublishingEnabled;
        *this << data.ModifyCount;
        *this << data.EnableCount;
        *this << data.DisableCount;
        *this << data.RepublishRequestCount;
        *this << data.RepublishMessageRequestCount;
        *this << data.RepublishMessageCount;
        *this << data.TransferRequestCount;
        *this << data.TransferredToAltClientCount;
        *this << data.TransferredToSameClientCount;
        *this << data.PublishRequestCount;
        *this << data.DataChangeNotificationsCount;
        *this << data.EventNotificationsCount;
        *this << data.NotificationsCount;
        *this << data.LatePublishRequestCount;
        *this << data.CurrentKeepAliveCount;
        *this << data.CurrentLifetimeCount;
        *this << data.UnacknowledgedMessageCount;
        *this << data.DiscardedMessageCount;
        *this << data.MonitoredItemCount;
        *this << data.DisabledMonitoredItemCount;
        *this << data.MonitoringQueueOverflowCount;
        *this << data.NextSequenceNumber;
        *this << data.EventQueueOverFlowCount;
    }


    template<>
    std::size_t RawSize(const ModelChangeStructureDataType& data)
    {
        return RawSize(data.Affected) + RawSize(data.AffectedType) + RawSize(data.Verb);
    }


    template<>
    void DataSerializer::Serialize<ModelChangeStructureDataType>(const ModelChangeStructureDataType& data)
    {
        *this << data.Affected;
        *this << data.AffectedType;
        *this << data.Verb;
    }


    template<>
    std::size_t RawSize(const SemanticChangeStructureDataType& data)
    {
        return RawSize(data.Affected) + RawSize(data.AffectedType);
    }


    template<>
    void DataSerializer::Serialize<SemanticChangeStructureDataType>(const SemanticChangeStructureDataType& data)
    {
        *this << data.Affected;
        *this << data.AffectedType;
    }


    template<>
    std::size_t RawSize(const Range& data)
    {
        return RawSize(data.Low) + RawSize(data.High);
    }


    template<>
    void DataSerializer::Serialize<Range>(const Range& data)
    {
        *this << data.Low;
        *this << data.High;
    }


    template<>
    std::size_t RawSize(const EUInformation& data)
    {
        return RawSize(data.NamespaceUri) + RawSize(data.UnitId) + RawSize(data.DisplayName) + RawSize(data.Description);
    }


    template<>
    void DataSerializer::Serialize<EUInformation>(const EUInformation& data)
    {
        *this << data.NamespaceUri;
        *this << data.UnitId;
        *this << data.DisplayName;
        *this << data.Description;
    }


    template<>
    std::size_t RawSize(const ComplexNumberType& data)
    {
        return RawSize(data.Real) + RawSize(data.Imaginary);
    }


    template<>
    void DataSerializer::Serialize<ComplexNumberType>(const ComplexNumberType& data)
    {
        *this << data.Real;
        *this << data.Imaginary;
    }


    template<>
    std::size_t RawSize(const DoubleComplexNumberType& data)
    {
        return RawSize(data.Real) + RawSize(data.Imaginary);
    }


    template<>
    void DataSerializer::Serialize<DoubleComplexNumberType>(const DoubleComplexNumberType& data)
    {
        *this << data.Real;
        *this << data.Imaginary;
    }


    template<>
    std::size_t RawSize(const AxisInformation& data)
    {
        return RawSize(data.EngineeringUnits) + RawSize(data.EURange) + RawSize(data.Title) + RawSize(data.AxisScaleType) + RawSizeContainer(data.AxisSteps);
    }


    template<>
    void DataSerializer::Serialize<AxisInformation>(const AxisInformation& data)
    {
        *this << data.EngineeringUnits;
        *this << data.EURange;
        *this << data.Title;
        *this << data.AxisScaleType;
        SerializeContainer(*this, data.AxisSteps);
    }


    template<>
    std::size_t RawSize(const XVType& data)
    {
        return RawSize(data.X) + RawSize(data.Value);
    }


    template<>
    void DataSerializer::Serialize<XVType>(const XVType& data)
    {
        *this << data.X;
        *this << data.Value;
    }


    template<>
    std::size_t RawSize(const ProgramDiagnosticDataType& data)
    {
        return RawSize(data.CreateSessionId) + RawSize(data.CreateClientName) + RawSize(data.InvocationCreationTime) + RawSize(data.LastTransitionTime) + RawSize(data.LastMethodCall) + RawSize(data.LastMethodSessionId) + RawSizeContainer(data.LastMethodInputArguments) + RawSizeContainer(data.LastMethodOutputArguments) + RawSize(data.LastMethodCallTime) + RawSize(data.LastMethodReturnStatus);
    }


    template<>
    void DataSerializer::Serialize<ProgramDiagnosticDataType>(const ProgramDiagnosticDataType& data)
    {
        *this << data.CreateSessionId;
        *this << data.CreateClientName;
        *this << data.InvocationCreationTime;
        *this << data.LastTransitionTime;
        *this << data.LastMethodCall;
        *this << data.LastMethodSessionId;
        SerializeContainer(*this, data.LastMethodInputArguments);
        SerializeContainer(*this, data.LastMethodOutputArguments);
        *this << data.LastMethodCallTime;
        *this << data.LastMethodReturnStatus;
    }


    template<>
    std::size_t RawSize(const Annotation& data)
    {
        return RawSize(data.Message) + RawSize(data.UserName) + RawSize(data.AnnotationTime);
    }


    template<>
    void DataSerializer::Serialize<Annotation>(const Annotation& data)
    {
        *this << data.Message;
        *this << data.UserName;
        *this << data.AnnotationTime;
    }


   }

} // namespace
    
