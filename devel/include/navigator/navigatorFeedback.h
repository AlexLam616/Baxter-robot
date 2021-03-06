// Generated by gencpp from file navigator/navigatorFeedback.msg
// DO NOT EDIT!


#ifndef NAVIGATOR_MESSAGE_NAVIGATORFEEDBACK_H
#define NAVIGATOR_MESSAGE_NAVIGATORFEEDBACK_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace navigator
{
template <class ContainerAllocator>
struct navigatorFeedback_
{
  typedef navigatorFeedback_<ContainerAllocator> Type;

  navigatorFeedback_()
    : fdbk(0)  {
    }
  navigatorFeedback_(const ContainerAllocator& _alloc)
    : fdbk(0)  {
  (void)_alloc;
    }



   typedef int32_t _fdbk_type;
  _fdbk_type fdbk;





  typedef boost::shared_ptr< ::navigator::navigatorFeedback_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::navigator::navigatorFeedback_<ContainerAllocator> const> ConstPtr;

}; // struct navigatorFeedback_

typedef ::navigator::navigatorFeedback_<std::allocator<void> > navigatorFeedback;

typedef boost::shared_ptr< ::navigator::navigatorFeedback > navigatorFeedbackPtr;
typedef boost::shared_ptr< ::navigator::navigatorFeedback const> navigatorFeedbackConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::navigator::navigatorFeedback_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::navigator::navigatorFeedback_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::navigator::navigatorFeedback_<ContainerAllocator1> & lhs, const ::navigator::navigatorFeedback_<ContainerAllocator2> & rhs)
{
  return lhs.fdbk == rhs.fdbk;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::navigator::navigatorFeedback_<ContainerAllocator1> & lhs, const ::navigator::navigatorFeedback_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace navigator

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::navigator::navigatorFeedback_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::navigator::navigatorFeedback_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::navigator::navigatorFeedback_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::navigator::navigatorFeedback_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::navigator::navigatorFeedback_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::navigator::navigatorFeedback_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::navigator::navigatorFeedback_<ContainerAllocator> >
{
  static const char* value()
  {
    return "46cc8f8da6ebf35aedc6bad2e96b2e59";
  }

  static const char* value(const ::navigator::navigatorFeedback_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x46cc8f8da6ebf35aULL;
  static const uint64_t static_value2 = 0xedc6bad2e96b2e59ULL;
};

template<class ContainerAllocator>
struct DataType< ::navigator::navigatorFeedback_<ContainerAllocator> >
{
  static const char* value()
  {
    return "navigator/navigatorFeedback";
  }

  static const char* value(const ::navigator::navigatorFeedback_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::navigator::navigatorFeedback_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n"
"#feedback: optional; \n"
"int32 fdbk\n"
"\n"
;
  }

  static const char* value(const ::navigator::navigatorFeedback_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::navigator::navigatorFeedback_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.fdbk);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct navigatorFeedback_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::navigator::navigatorFeedback_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::navigator::navigatorFeedback_<ContainerAllocator>& v)
  {
    s << indent << "fdbk: ";
    Printer<int32_t>::stream(s, indent + "  ", v.fdbk);
  }
};

} // namespace message_operations
} // namespace ros

#endif // NAVIGATOR_MESSAGE_NAVIGATORFEEDBACK_H
