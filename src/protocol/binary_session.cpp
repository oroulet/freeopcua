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
#include <opc/ua/protocol/session.h>
#include <opc/ua/protocol/types.h>
#include <opc/ua/protocol/extension_identifiers.h>

#include <algorithm>
#include <memory>
#include <string>

namespace OpcUa
{

  UserIdentityToken::UserIdentityToken()
    : Header(USER_IDENTIFY_TOKEN_ANONYMOUS, HAS_BINARY_BODY)
  {
    Anonymous.Data = {9,0,0,0,'a', 'n', 'o', 'n', 'y', 'm', 'o', 'u', 's'};
  }

  CloseSessionRequest::CloseSessionRequest()
    : TypeID(CLOSE_SESSION_REQUEST)
    , DeleteSubscriptions(true)
  {
  }

} // namespace OpcUa

