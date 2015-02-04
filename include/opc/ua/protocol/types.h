/// @author Alexander Rykovanov 2012
/// @email rykovanov.as@gmail.com
/// @brief C++ types of binary protocol.
/// @license GNU LGPL
///
/// Distributed under the GNU LGPL License
/// (See accompanying file LICENSE or copy at
/// http://www.gnu.org/licenses/lgpl.html)
///

#ifndef __OPC_UA_MAPPING_TYPES_H__
#define __OPC_UA_MAPPING_TYPES_H__

#include <opc/ua/protocol/extension_identifiers.h>
#include <opc/ua/protocol/message_identifiers.h>
#include <opc/ua/protocol/object_ids.h>
#include <opc/ua/protocol/nodeid.h>
#include <opc/ua/protocol/datetime.h>
#include <opc/ua/protocol/status_codes.h>
#include <opc/ua/protocol/reference_ids.h>

#include <memory>
#include <stdint.h>
#include <string>
#include <vector>
#include <atomic>


namespace OpcUa
{

  typedef std::string LocaleID;

  struct ByteString
  {
    std::vector<uint8_t> Data;

    ByteString()
    {
    }

    explicit ByteString(const std::vector<uint8_t>& val)
      : Data(val)
    {
    }

    bool operator== (const ByteString& str) const
    {
      return Data == str.Data;
    }
  };

  class IntegerID
  {
  public:
    IntegerID();
    IntegerID(const IntegerID& id);
    explicit IntegerID(uint32_t num);
    IntegerID& operator= (const IntegerID& id);
    IntegerID& operator= (uint32_t value);
    operator uint32_t() const;

  private:
    uint32_t Value;
  };

  struct QualifiedName
  {
    uint16_t NamespaceIndex;
    std::string Name; // TODO rename to Text

    QualifiedName()
      : NamespaceIndex(0)
    {
    }

    QualifiedName(uint16_t nameSpace, const std::string& name)
      : NamespaceIndex(nameSpace)
      , Name(name)
    {
    }

    QualifiedName(const std::string& name, uint16_t nameSpace)
      : NamespaceIndex(nameSpace)
      , Name(name)
    {
    }

    explicit QualifiedName(const std::string& name)
      : NamespaceIndex(0)
      , Name(name)
    {
    }

    bool operator== (const QualifiedName& name) const
    {
      return NamespaceIndex == name.NamespaceIndex && Name == name.Name;
    }

    bool operator < (const QualifiedName& name) const
    {
      if (NamespaceIndex != name.NamespaceIndex)
      {
        return NamespaceIndex < name.NamespaceIndex;
      }
      return Name < name.Name;
    }
  };

  // LocalizedText encoding mask
  const uint8_t HAS_LOCALE = 1;
  const uint8_t HAS_TEXT = 2;

  struct LocalizedText
  {
    uint8_t Encoding;
    std::string Locale;
    std::string Text; // TODO rename to Data

    LocalizedText()
      : Encoding(0)
    {
    }

    explicit LocalizedText(const std::string& text)
      : Encoding(HAS_TEXT)
      , Text(text)
    {
    }

    explicit LocalizedText(const char* text)
      : Encoding(HAS_TEXT)
      , Text(text)
    {
    }

    LocalizedText(const std::string& text, const std::string& locale)
      : Encoding(HAS_TEXT | HAS_LOCALE)
      , Locale(locale)
      , Text(text)
    {
    }

    LocalizedText(const char* text, char* locale)
      : Encoding(HAS_TEXT | HAS_LOCALE)
      , Locale(locale)
      , Text(text)
    {
    }

    bool operator== (const LocalizedText& text) const
    {
      return Encoding == text.Encoding && Locale == text.Locale && Text == text.Text;
    }
  };

  struct AdditionalHeader
  {
    ExpandedNodeId TypeID;
    uint8_t Encoding;

    AdditionalHeader()
      : Encoding(0)
    {
    }
  };

  enum ExtensionObjectEncoding : uint8_t
  {
    NONE = 0,
    HAS_BINARY_BODY = 1,
    HAS_XML_BODY    = 2,
  };

  /*
  //TODO serialization tests
  struct ExtensionObjectHeader
  {
    ExpandedNodeId TypeID;
    ExtensionObjectEncoding Encoding;

    ExtensionObjectHeader();
    ExtensionObjectHeader(ExtensionObjectId objectID, ExtensionObjectEncoding encoding);
  };
  */

} // namespace OpcUa

#endif // __OPC_UA_MAPPING_TYPES_H__

