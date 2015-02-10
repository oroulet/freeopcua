// @author Alexander Rykovanov 2012
/// @email rykovanov.as@gmail.com
/// @brief Opc Ua binary session services.
/// @license GNU LGPL
///
/// Distributed under the GNU LGPL License
/// (See accompanying file LICENSE or copy at
/// http://www.gnu.org/licenses/lgpl.html)
///

#include <opc/ua/protocol/binary/stream.h>
#include <opc/ua/protocol/protocol.h>

namespace OpcUa
{
  BrowseDescription::BrowseDescription()
    : BrowseDirection(BrowseDirection::Both)
    , IncludeSubtypes(false)
    , NodeClassMask(NodeClass::Unspecified)
    , ResultMask(BrowseResultMask::All)
  {
  }

  ReferenceDescription::ReferenceDescription()
    : IsForward(false)
    , NodeClass(NodeClass::Unspecified)
  {
  }


} // namespace OpcUa
