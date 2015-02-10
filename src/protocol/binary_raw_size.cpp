/// @author Alexander Rykovanov 2012
/// @email rykovanov.as@gmail.com
/// @brief Sizes of structures serialized form.
/// @license GNU LGPL
///
/// Distributed under the GNU LGPL License
/// (See accompanying file LICENSE or copy at
/// http://www.gnu.org/licenses/lgpl.html)
///

#include <opc/ua/protocol/binary/stream.h>
#include <opc/ua/protocol/protocol.h>

#include <algorithm>
#include <stdexcept>

namespace OpcUa
{
  namespace Binary
  {
    template<>
    std::size_t RawSize<bool>(const bool&)
    {
      return 1;
    }

    template<>
    std::size_t RawSize<uint8_t>(const uint8_t&)
    {
      return 1;
    }

    template<>
    std::size_t RawSize<int8_t>(const int8_t&)
    {
      return 1;
    }

    template<>
    std::size_t RawSize<uint16_t>(const uint16_t&)
    {
      return 2;
    }

    template<>
    std::size_t RawSize<int16_t>(const int16_t&)
    {
      return 2;
    }

    template<>
    std::size_t RawSize<uint32_t>(const uint32_t&)
    {
      return 4;
    }

    template<>
    std::size_t RawSize<int32_t>(const int32_t&)
    {
      return 4;
    }


    template<>
    std::size_t RawSize<uint64_t>(const uint64_t&)
    {
      return 8;
    }

    template<>
    std::size_t RawSize<int64_t>(const int64_t&)
    {
      return 8;
    }

    template<>
    std::size_t RawSize<float>(const float&)
    {
      return 4;
    }

    template<>
    std::size_t RawSize<double>(const double&)
    {
      return 8;
    }

    template<>
    std::size_t RawSize<Guid>(const Guid&)
    {
      return 16;
    }

    template<>
    std::size_t RawSize<StatusCode>(const StatusCode&)
    {
      return 4;
    }

    template<>
    std::size_t RawSize<std::string>(const std::string& str)
    {
      const std::size_t headerSize = 4;
      return headerSize + str.size();
    }

    template<>
    std::size_t RawSize<ByteString>(const ByteString& str)
    {
      const std::size_t headerSize = 4;
      return headerSize + str.Data.size();
    }

    template<>
    std::size_t RawSize<DateTime>(const DateTime& date)
    {
      return RawSize(date.Value);
    }

    template<>
    std::size_t RawSize<std::vector<uint8_t>>(const std::vector<uint8_t>& vec)
    {
      const std::size_t headerSize = 4;
      return headerSize + vec.size();
    }

    template<>
    std::size_t RawSize<std::vector<std::vector<uint8_t>>>(const std::vector<std::vector<uint8_t>>& vec)
    {
      const std::size_t headerSize = 4;
      std::size_t totalSize = headerSize;
      std::for_each(vec.begin(), vec.end(), [&] (const std::vector<uint8_t>& v) {totalSize += RawSize(v);});
      return totalSize;
    }


    template<>
    std::size_t RawSize<std::vector<std::string>>(const std::vector<std::string>& vec)
    {
      const std::size_t headerSize = 4;
      std::size_t totalSize = headerSize;
      std::for_each(vec.begin(), vec.end(), [&] (const std::string& str) {totalSize += RawSize(str);});
      return totalSize;
    }


    template<>
    std::size_t RawSize<Header>(const Header&)
    {
      const std::size_t sizeofType = 3;  // 'H', 'E', 'L'
      const std::size_t sizeofChunk = 1; // 'F'
      const std::size_t sizeofSize = 4;
      return sizeofType + sizeofChunk + sizeofSize;
    }

    template<>
    std::size_t RawSize<SecureHeader>(const SecureHeader&)
    {
      const std::size_t sizeofType = 3;  // 'H', 'E', 'L'
      const std::size_t sizeofChunk = 1; // 'F'
      const std::size_t sizeofSize = 4;
      const std::size_t sizeofChannelID = 4;
      return sizeofType + sizeofChunk + sizeofSize + sizeofChannelID;
    }

    template<>
    std::size_t RawSize<Hello>(const Hello& hello)
    {
      const std::size_t sizeOfProtocolVersion = 4;
      const std::size_t sizeOfReceiveBufferSize = 4;
      const std::size_t sizeOfSendBufferSize = 4;
      const std::size_t sizeOfMaxMessageSize = 4;
      const std::size_t sizeOfMaxChunkCount = 4;

      return sizeOfProtocolVersion +
             sizeOfReceiveBufferSize +
             sizeOfSendBufferSize +
             sizeOfMaxMessageSize +
             sizeOfMaxChunkCount +
             RawSize(hello.EndpointUrl);
    }

    template<>
    std::size_t RawSize<Acknowledge>(const Acknowledge&)
    {
      const std::size_t sizeofProtocolVersion = 4;
      const std::size_t sizeofReceiveBufferSize = 4;
      const std::size_t sizeofSendBufferSize = 4;
      const std::size_t sizeofMaxMessageSize = 4;
      const std::size_t sizeofMaxChunkCount = 4;

      return sizeofProtocolVersion + sizeofReceiveBufferSize + sizeofSendBufferSize + sizeofMaxMessageSize + sizeofMaxChunkCount;
    }

    template<>
    std::size_t RawSize<Error>(const Error& err)
    {
      const std::size_t sizeofCode = 4;
      return sizeofCode + RawSize(err.Reason);
    }

    template<>
    std::size_t RawSize<AsymmetricAlgorithmHeader>(const AsymmetricAlgorithmHeader& ack)
    {
      const std::size_t sizeofUri = RawSize(ack.SecurityPolicyURI);
      const std::size_t sizeofCertificate = RawSize(ack.SenderCertificate);
      const std::size_t sizeofThumbprint = RawSize(ack.ReceiverCertificateThumbPrint);
      return sizeofUri + sizeofCertificate +  sizeofThumbprint;
    }

    template<>
    std::size_t RawSize<SequenceHeader>(const SequenceHeader&)
    {
      const std::size_t sizeofSequenceNumber = 4;
      const std::size_t sizeofRequestID = 4;

      return sizeofSequenceNumber + sizeofRequestID;
    }

    template<>
    std::size_t RawSize<SymmetricAlgorithmHeader>(const SymmetricAlgorithmHeader& header)
    {
      const std::size_t sizeofTokenID = 4;
      return sizeofTokenID;
    }

    template<>
    std::size_t RawSize<LocalizedText>(const LocalizedText& text)
    {
      std::size_t size = RawSize(text.Encoding);
      if (text.Encoding & HAS_LOCALE)
      {
        size += RawSize(text.Locale);
      }
      if (text.Encoding & HAS_TEXT)
      {
        size += RawSize(text.Text);
      }
      return size;
    };

    template<>
    std::size_t RawSize<QualifiedName>(const QualifiedName& name)
    {
      return RawSize(name.NamespaceIndex) + RawSize(name.Name);
    };
    template<>

    std::size_t RawSize<IntegerId>(const IntegerId&)
    {
      return 4;
    };

  }
}

