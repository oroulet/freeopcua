/// @author Alexander Rykovanov 2012
/// @email rykovanov.as@gmail.com
/// @brief Opc Ua Binary. Secure channel service.
/// @license GNU LGPL
///
/// Distributed under the GNU LGPL License
/// (See accompanying file LICENSE or copy at
/// http://www.gnu.org/licenses/lgpl.html)
///

#ifndef OPC_UA_PROTOCOL_SUBSCRIPTIONS_H
#define OPC_UA_PROTOCOL_SUBSCRIPTIONS_H

#include <opc/ua/protocol/types.h>
#include <opc/ua/protocol/data_value.h>

namespace OpcUa
{

  struct NotificationData
  {
    ExtensionObjectHeader Header;
    DataChangeNotification DataChange;
    EventNotificationList Events;
    StatusChangeNotification StatusChange;

    NotificationData(){}
    NotificationData(DataChangeNotification notification);
    NotificationData(EventNotificationList notification);
    NotificationData(StatusChangeNotification notification);
  };


} // namespace OpcUa

#endif /// OPC_UA_PROTOCOL_SUBSCRIPTIONS_H
