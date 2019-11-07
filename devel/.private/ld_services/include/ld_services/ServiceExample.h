// Generated by gencpp from file ld_services/ServiceExample.msg
// DO NOT EDIT!


#ifndef LD_SERVICES_MESSAGE_SERVICEEXAMPLE_H
#define LD_SERVICES_MESSAGE_SERVICEEXAMPLE_H

#include <ros/service_traits.h>


#include <ld_services/ServiceExampleRequest.h>
#include <ld_services/ServiceExampleResponse.h>


namespace ld_services
{

struct ServiceExample
{

typedef ServiceExampleRequest Request;
typedef ServiceExampleResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct ServiceExample
} // namespace ld_services


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::ld_services::ServiceExample > {
  static const char* value()
  {
    return "b6541b31be965d2ea76445e10907a742";
  }

  static const char* value(const ::ld_services::ServiceExample&) { return value(); }
};

template<>
struct DataType< ::ld_services::ServiceExample > {
  static const char* value()
  {
    return "ld_services/ServiceExample";
  }

  static const char* value(const ::ld_services::ServiceExample&) { return value(); }
};


// service_traits::MD5Sum< ::ld_services::ServiceExampleRequest> should match 
// service_traits::MD5Sum< ::ld_services::ServiceExample > 
template<>
struct MD5Sum< ::ld_services::ServiceExampleRequest>
{
  static const char* value()
  {
    return MD5Sum< ::ld_services::ServiceExample >::value();
  }
  static const char* value(const ::ld_services::ServiceExampleRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::ld_services::ServiceExampleRequest> should match 
// service_traits::DataType< ::ld_services::ServiceExample > 
template<>
struct DataType< ::ld_services::ServiceExampleRequest>
{
  static const char* value()
  {
    return DataType< ::ld_services::ServiceExample >::value();
  }
  static const char* value(const ::ld_services::ServiceExampleRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::ld_services::ServiceExampleResponse> should match 
// service_traits::MD5Sum< ::ld_services::ServiceExample > 
template<>
struct MD5Sum< ::ld_services::ServiceExampleResponse>
{
  static const char* value()
  {
    return MD5Sum< ::ld_services::ServiceExample >::value();
  }
  static const char* value(const ::ld_services::ServiceExampleResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::ld_services::ServiceExampleResponse> should match 
// service_traits::DataType< ::ld_services::ServiceExample > 
template<>
struct DataType< ::ld_services::ServiceExampleResponse>
{
  static const char* value()
  {
    return DataType< ::ld_services::ServiceExample >::value();
  }
  static const char* value(const ::ld_services::ServiceExampleResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // LD_SERVICES_MESSAGE_SERVICEEXAMPLE_H