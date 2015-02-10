/// @author Alexander Rykovanov 2012
/// @email rykovanov.as@gmail.com
/// @brief Opc Ua binary session services.
/// @license GNU LGPL
///
/// Distributed under the GNU LGPL License
/// (See accompanying file LICENSE or copy at 
/// http://www.gnu.org/licenses/lgpl.html)
///

#include "binary_serialization.h"

#include <opc/ua/protocol/binary/stream.h>
#include <opc/ua/protocol/protocol.h>
#include <opc/ua/protocol/object_ids.h>

#include <algorithm>
#include <memory>
#include <string>

namespace OpcUa
{

  UserIdentityToken::UserIdentityToken()
    : Encoding(HAS_BINARY_BODY),
      TypeId(ObjectId::AnonymousIdentityToken_Encoding_DefaultBinary)
  {
    PolicyId = {9,0,0,0,'a', 'n', 'o', 'n', 'y', 'm', 'o', 'u', 's'};
  }

  CloseSessionRequest::CloseSessionRequest()
    : TypeId(CLOSE_SESSION_REQUEST)
    , DeleteSubscriptions(true)
  {
  }

} // namespace OpcUa

