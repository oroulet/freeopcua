#include <opc/ua/protocol/binary/stream.h> //FIXME move out
#include <opc/ua/protocol/input_from_buffer.h> //FIXME move out
#include <ostream>
#include <iostream>
#include <vector>

namespace OpcUa
{

  struct ExtensionObject
  {
    uint8_t Encoding;
    OpcUa::ExpandedNodeId TypeId;
    std::vector<uint8_t> Body;


    ExtensionObject()
      //: Encoding(Binary)
    {
    }


    template <typename T>
    std::ostream&  operator >> (T& obj)
    {
     //if (obj.Encoding != Binary)
        //throw "Not implemented.";
     InputFromBuffer input(obj.Body);
     OpcUa::Binary::IStream<T> stream(input);
     stream >> *this;
     //return *this;
    }
    

    template <typename T> 
    ExtensionObject& operator << ( const T& obj)
    {
     //if (Encoding != Binary)
        //throw "Not implemented.";

     struct OutToBuffer
     {
        void Send(const char* buffer, size_t size)
         {
             Buffer.assign(buffer, buffer + size);
         }
        std::vector<uint8_t> Buffer;
     };

     OutToBuffer receiver;
     OpcUa::Binary::OStream<T> stream(receiver);

     stream << obj << std::flush;
     *this << stream;
     //Body = std::move(receiver.Buffer)
     //BodyLength = Body.size; // Do we need this field at all?
    }

    template <typename T> 
    ExtensionObject& operator = (const T& obj)
    {
     *this << obj;
    }

  };


}

