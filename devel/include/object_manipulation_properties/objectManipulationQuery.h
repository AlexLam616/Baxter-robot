// Generated by gencpp from file object_manipulation_properties/objectManipulationQuery.msg
// DO NOT EDIT!


#ifndef OBJECT_MANIPULATION_PROPERTIES_MESSAGE_OBJECTMANIPULATIONQUERY_H
#define OBJECT_MANIPULATION_PROPERTIES_MESSAGE_OBJECTMANIPULATIONQUERY_H

#include <ros/service_traits.h>


#include <object_manipulation_properties/objectManipulationQueryRequest.h>
#include <object_manipulation_properties/objectManipulationQueryResponse.h>


namespace object_manipulation_properties
{

struct objectManipulationQuery
{

typedef objectManipulationQueryRequest Request;
typedef objectManipulationQueryResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct objectManipulationQuery
} // namespace object_manipulation_properties


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::object_manipulation_properties::objectManipulationQuery > {
  static const char* value()
  {
    return "00b4b08f066e8274009b927a6e082179";
  }

  static const char* value(const ::object_manipulation_properties::objectManipulationQuery&) { return value(); }
};

template<>
struct DataType< ::object_manipulation_properties::objectManipulationQuery > {
  static const char* value()
  {
    return "object_manipulation_properties/objectManipulationQuery";
  }

  static const char* value(const ::object_manipulation_properties::objectManipulationQuery&) { return value(); }
};


// service_traits::MD5Sum< ::object_manipulation_properties::objectManipulationQueryRequest> should match
// service_traits::MD5Sum< ::object_manipulation_properties::objectManipulationQuery >
template<>
struct MD5Sum< ::object_manipulation_properties::objectManipulationQueryRequest>
{
  static const char* value()
  {
    return MD5Sum< ::object_manipulation_properties::objectManipulationQuery >::value();
  }
  static const char* value(const ::object_manipulation_properties::objectManipulationQueryRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::object_manipulation_properties::objectManipulationQueryRequest> should match
// service_traits::DataType< ::object_manipulation_properties::objectManipulationQuery >
template<>
struct DataType< ::object_manipulation_properties::objectManipulationQueryRequest>
{
  static const char* value()
  {
    return DataType< ::object_manipulation_properties::objectManipulationQuery >::value();
  }
  static const char* value(const ::object_manipulation_properties::objectManipulationQueryRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::object_manipulation_properties::objectManipulationQueryResponse> should match
// service_traits::MD5Sum< ::object_manipulation_properties::objectManipulationQuery >
template<>
struct MD5Sum< ::object_manipulation_properties::objectManipulationQueryResponse>
{
  static const char* value()
  {
    return MD5Sum< ::object_manipulation_properties::objectManipulationQuery >::value();
  }
  static const char* value(const ::object_manipulation_properties::objectManipulationQueryResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::object_manipulation_properties::objectManipulationQueryResponse> should match
// service_traits::DataType< ::object_manipulation_properties::objectManipulationQuery >
template<>
struct DataType< ::object_manipulation_properties::objectManipulationQueryResponse>
{
  static const char* value()
  {
    return DataType< ::object_manipulation_properties::objectManipulationQuery >::value();
  }
  static const char* value(const ::object_manipulation_properties::objectManipulationQueryResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // OBJECT_MANIPULATION_PROPERTIES_MESSAGE_OBJECTMANIPULATIONQUERY_H
