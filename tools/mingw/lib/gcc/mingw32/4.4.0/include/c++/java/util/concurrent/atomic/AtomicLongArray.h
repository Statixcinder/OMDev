
// DO NOT EDIT THIS FILE - it is machine generated -*- c++ -*-

#ifndef __java_util_concurrent_atomic_AtomicLongArray__
#define __java_util_concurrent_atomic_AtomicLongArray__

#pragma interface

#include <java/lang/Object.h>
#include <gcj/array.h>

extern "Java"
{
  namespace sun
  {
    namespace misc
    {
        class Unsafe;
    }
  }
}

class java::util::concurrent::atomic::AtomicLongArray : public ::java::lang::Object
{

  jlong rawIndex(jint);
public:
  AtomicLongArray(jint);
  AtomicLongArray(JArray< jlong > *);
  virtual jint length();
  virtual jlong get(jint);
  virtual void set(jint, jlong);
  virtual void lazySet(jint, jlong);
  virtual jlong getAndSet(jint, jlong);
  virtual jboolean compareAndSet(jint, jlong, jlong);
  virtual jboolean weakCompareAndSet(jint, jlong, jlong);
  virtual jlong getAndIncrement(jint);
  virtual jlong getAndDecrement(jint);
  virtual jlong getAndAdd(jint, jlong);
  virtual jlong incrementAndGet(jint);
  virtual jlong decrementAndGet(jint);
  virtual jlong addAndGet(jint, jlong);
  virtual ::java::lang::String * toString();
private:
  static const jlong serialVersionUID = -2308431214976778248LL;
  static ::sun::misc::Unsafe * unsafe;
  static jint base;
  static jint scale;
  JArray< jlong > * __attribute__((aligned(__alignof__( ::java::lang::Object)))) array;
public:
  static ::java::lang::Class class$;
};

#endif // __java_util_concurrent_atomic_AtomicLongArray__