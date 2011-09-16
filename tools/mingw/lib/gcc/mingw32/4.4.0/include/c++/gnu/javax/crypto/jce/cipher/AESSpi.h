
// DO NOT EDIT THIS FILE - it is machine generated -*- c++ -*-

#ifndef __gnu_javax_crypto_jce_cipher_AESSpi__
#define __gnu_javax_crypto_jce_cipher_AESSpi__

#pragma interface

#include <gnu/javax/crypto/jce/cipher/CipherAdapter.h>
extern "Java"
{
  namespace gnu
  {
    namespace javax
    {
      namespace crypto
      {
        namespace jce
        {
          namespace cipher
          {
              class AESSpi;
          }
        }
      }
    }
  }
  namespace java
  {
    namespace security
    {
        class AlgorithmParameters;
        class Key;
        class SecureRandom;
      namespace spec
      {
          class AlgorithmParameterSpec;
      }
    }
  }
}

class gnu::javax::crypto::jce::cipher::AESSpi : public ::gnu::javax::crypto::jce::cipher::CipherAdapter
{

public:
  AESSpi();
public: // actually protected
  void engineInit(jint, ::java::security::Key *, ::java::security::spec::AlgorithmParameterSpec *, ::java::security::SecureRandom *);
  void engineInit(jint, ::java::security::Key *, ::java::security::AlgorithmParameters *, ::java::security::SecureRandom *);
public:
  static ::java::lang::Class class$;
};

#endif // __gnu_javax_crypto_jce_cipher_AESSpi__
