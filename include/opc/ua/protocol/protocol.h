/// @author Olivier Roulet-Dubonnet 
/// @email olivier@sintef.no 
/// @brief Opc Ua Binary. 
/// @license GNU LGPL
///
/// Distributed under the GNU LGPL License
/// (See accompanying file LICENSE or copy at
/// http://www.gnu.org/licenses/lgpl.html)
///

#pragma once

#include <opc/ua/protocol/protocol_auto.h>
#include <opc/ua/protocol/variable_access_level.h>

#include <opc/ua/protocol/binary/stream.h> //FIXME move out
#include <opc/ua/protocol/input_from_buffer.h> //FIXME move out
#include <ostream>
#include <iostream>
#include <vector>
#include <queue>

//This file is mean to override autogenerated struct to add constructors or interval members we want
namespace OpcUa
{
  inline ReadValueId MakeReadValueId(NodeId node, AttributeID attr) 
  {
    ReadValueId rv;
    rv.TypeId = node;
    rv.AttributeId = attr;
    return rv;
  }

    template <typename T> 
    ExtensionObject& operator << (ExtensionObject& out, const T& obj)
    {
     //if (Encoding != Binary)
        //throw "Not implemented.";

     struct MyBuffer
     {
        void Send(const char* buffer, size_t size)
         {
           for (int i; i < size; ++i)
           {
             Buffer.push(buffer[i]);
           }
         }

         size_t Receive(char* buffer, size_t size)
         {
           for (int i; i < size; ++i)
           {
             if (Buffer.size() == 0 )
             {
               return i;
             }
              buffer[i] = Buffer.front();
              Buffer.pop();
           }
           return size;
         }

        std::queue<uint8_t> Buffer;
     };

     MyBuffer receiver;
     Binary::OStream<MyBuffer> ostream(receiver);
     Binary::IStream<MyBuffer> istream(receiver);
     //Binary::IOStream<MyBuffer> stream(istream, ostream);
    
     ostream << obj << Binary::flush;
     out << istream << Binary::flush;

     return out;

    }



}
