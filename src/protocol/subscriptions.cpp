/// @author Olivier Roulet-Dubonnet 
/// @email olivier@sintef.no 
/// @brief Opc Ua Binary. Subscription services structs.
/// @license GNU LGPL
///
/// Distributed under the GNU LGPL License
/// (See accompanying file LICENSE or copy at
/// http://www.gnu.org/licenses/lgpl.html)
///

#include "binary_serialization.h"

#include <opc/ua/protocol/binary/stream.h>
#include <opc/ua/protocol/protocol.h>

namespace OpcUa
{
  ////////////////////////////////////////////////////////
  // CreateSubscriptionParameters
  ////////////////////////////////////////////////////////

  CreateSubscriptionParameters::CreateSubscriptionParameters()
    : RequestedPublishingInterval(500)
    , RequestedLifetimeCount(3000)
    , RequestedMaxKeepAliveCount(10000)
    , MaxNotificationsPerPublish(0)
    , PublishingEnabled(true)
    , Priority(0)
  {
  }


  PublishResult::PublishResult()
    : MoreNotifications(false)
  {
  }

/*
  ////////////////////////////////////////////////////////
  // NotificationData
  ////////////////////////////////////////////////////////

    NotificationData::NotificationData(DataChangeNotification notification) : DataChange(notification)
    {
      //Header.TypeId  = ObjectId::DataChangeNotification; 
      Header.TypeId  = ExpandedObjectId::DataChangeNotification;
      Header.Encoding  = static_cast<ExtensionObjectEncoding>(Header.Encoding | ExtensionObjectEncoding::HAS_BINARY_BODY);
    }

    NotificationData::NotificationData(EventNotificationList notification) : Events(notification)
    {
      Header.TypeId  = ExpandedObjectId::EventNotificationList; 
      Header.Encoding  = static_cast<ExtensionObjectEncoding>(Header.Encoding | ExtensionObjectEncoding::HAS_BINARY_BODY);
    }

    NotificationData::NotificationData(StatusChangeNotification notification) : StatusChange(notification)
    {
      Header.TypeId  = ExpandedObjectId::StatusChangeNotification; 
      Header.Encoding  = static_cast<ExtensionObjectEncoding>(Header.Encoding | ExtensionObjectEncoding::HAS_BINARY_BODY);
    }

*/
  ////////////////////////////////////////////////////////
  // NotificationMessage
  ////////////////////////////////////////////////////////

  NotificationMessage::NotificationMessage()
    : SequenceNumber(0)
    , PublishTime(DateTime::Current())
  {
  }

  ////////////////////////////////////////////////////////
  // PublishingModeParameters
  ////////////////////////////////////////////////////////

  SetPublishingModeParameters::SetPublishingModeParameters()
    : PublishingEnabled(false)
  {
  }

} // namespace OpcUa
