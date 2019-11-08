// Generated by gencpp from file om_aiv_util/Service2.msg
// DO NOT EDIT!


#ifndef OM_AIV_UTIL_MESSAGE_SERVICE2_H
#define OM_AIV_UTIL_MESSAGE_SERVICE2_H

#include <ros/service_traits.h>


#include <om_aiv_util/Service2Request.h>
#include <om_aiv_util/Service2Response.h>


namespace om_aiv_util
{

struct Service2
{

typedef Service2Request Request;
typedef Service2Response Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct Service2
} // namespace om_aiv_util


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::om_aiv_util::Service2 > {
  static const char* value()
  {
    return "4f7d11ca1dbd936717b1bb3469c922e4";
  }

  static const char* value(const ::om_aiv_util::Service2&) { return value(); }
};

template<>
struct DataType< ::om_aiv_util::Service2 > {
  static const char* value()
  {
    return "om_aiv_util/Service2";
  }

  static const char* value(const ::om_aiv_util::Service2&) { return value(); }
};


// service_traits::MD5Sum< ::om_aiv_util::Service2Request> should match 
// service_traits::MD5Sum< ::om_aiv_util::Service2 > 
template<>
struct MD5Sum< ::om_aiv_util::Service2Request>
{
  static const char* value()
  {
    return MD5Sum< ::om_aiv_util::Service2 >::value();
  }
  static const char* value(const ::om_aiv_util::Service2Request&)
  {
    return value();
  }
};

// service_traits::DataType< ::om_aiv_util::Service2Request> should match 
// service_traits::DataType< ::om_aiv_util::Service2 > 
template<>
struct DataType< ::om_aiv_util::Service2Request>
{
  static const char* value()
  {
    return DataType< ::om_aiv_util::Service2 >::value();
  }
  static const char* value(const ::om_aiv_util::Service2Request&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::om_aiv_util::Service2Response> should match 
// service_traits::MD5Sum< ::om_aiv_util::Service2 > 
template<>
struct MD5Sum< ::om_aiv_util::Service2Response>
{
  static const char* value()
  {
    return MD5Sum< ::om_aiv_util::Service2 >::value();
  }
  static const char* value(const ::om_aiv_util::Service2Response&)
  {
    return value();
  }
};

// service_traits::DataType< ::om_aiv_util::Service2Response> should match 
// service_traits::DataType< ::om_aiv_util::Service2 > 
template<>
struct DataType< ::om_aiv_util::Service2Response>
{
  static const char* value()
  {
    return DataType< ::om_aiv_util::Service2 >::value();
  }
  static const char* value(const ::om_aiv_util::Service2Response&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // OM_AIV_UTIL_MESSAGE_SERVICE2_H