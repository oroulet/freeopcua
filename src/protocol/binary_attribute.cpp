// @author Alexander Rykovanov 2012
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
#include <opc/ua/protocol/types.h>
#include <opc/ua/protocol/attribute.h>
#include <opc/ua/protocol/attribute_ids.h>
#include <opc/ua/protocol/expanded_object_ids.h>

#include <algorithm>
#include <memory>
#include <string>
#include <iostream>


namespace OpcUa
{
  // TODO move to appropriate file
  ReadValueId::ReadValueId()
    : Attribute(AttributeID::Value)
  {
  }

  ReadParameters::ReadParameters()
    : MaxAge(0)
    , TimestampsType(TimestampsToReturn::NEITHER)
  {

  }

} // namespace OpcUa

