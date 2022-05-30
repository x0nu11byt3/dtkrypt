#!/usr/bin/env python3

# Very important note!
# This implementation is a fork of the original implementation of: https://codereview.stackexchange.com/questions/226156/a-simple-implementation-of-the-principle-of-rsa-encryption
# If you would like to know more about his work and his person : Bruno Vermeulen (https://codereview.stackexchange.com/users/173492/bruno-vermeulen)
# Here I leave the link of github from Bruno Vermeulen : https://github.com/bvermeulen

'''  
    RSA encryption
        inspired on: https://www.youtube.com/watch?v=M7kEpw1tn50
        and http://jcla1.com/blog/rsa-public-private-key-encryption-explained

     some conditions:
        - prime numbers must be > 1 and not equal
        - prime factor must sufficiently large to accommodate the ascii numbers, let's say > 150
        - so for example (2, 191) will do as well as (11, 17)
'''

class RSA():
    """
    Asymmetric key cryptography algorithm based ( public key cryptography and private key cryptography )
    RSA is a public-key cryptographic algorithm based on the difficulty of factoring large integers (prime numbers).
    The algorithm is typically used for both encryption and authentication (digital signature).
    """
    def __init__(self):
        self._prime_factor = 0
        self._private_key = 0
        self._public_key = 0
    
    def get_prime_factor(self): 
        return self._prime_factor
    
    def get_private_key(self): 
        return self._private_key
    
    def get_public_key(self): 
        return self._public_key
    
    @staticmethod
    def gcd(a, b):
        """
        The greatest common divisor (gcd) of two or more integers,
        which are not all zero, is the largest positive integer that divides each of the integers.
        Based in  Euclid's algorithm, is an method for to get the greatest common divisor (GCD) of two integers.
        """
        while b:
            a, b = b, a % b
        return a
    
    @classmethod
    def generate_keys(self, prime_a, prime_b):
        """
        Key generation: Retur pair keys, The public key is ( n , e ) , i.e. the modulus and the cipher exponent. 
        The private key is ( n , d ) , i.e. the modulus and the decryption exponent, which must be kept secret.
        """
        # Choose two different prime numbers.
        self._prime_factor = prime_a * prime_b
        
        #  φ(n) = (p−1)(q−1)
        #  φ(Phi) is Euler's function to calculate: φ(n) = (p-1)*(q-1) ] based on the following two properties of Euler's function 
        #  [ φ(p) = p -1 if p is prime ] and [ If m and n are prime to each other, then φ ( m n ) = φ ( m ) φ ( n ) ].
        
        totient = (prime_a - 1) * (prime_b - 1)
        
        # determine d (by modular arithmetic) that satisfies the congruence e ⋅ d ≡ 1 ( mod φ ( n ) )
        # That is to say, that d is the inverse modular multiplier of e mod φ ( n ).
        public_keys = []
        for i in range(totient):
            if self.gcd(i, totient) == 1:
                public_keys.append(i)
        # select a positive integer smaller than φ ( n ) that is coprime with φ ( n ).
        self._public_key = public_keys[4]
        self._private_key = 0
        n = -1
        while n != 0:
            self._private_key += 1
            # Calculate n which is the product of p and q (selected prime numbers). n is used as the module for both public and private keys. 
            n = (self._public_key * self._private_key - 1) % totient
        return (self._prime_factor, self._public_key, self._private_key)

    @classmethod
    def encrypt(self, plaintext):
        """
        Encrypt message plaintext
        Example: person A sends public key ( n , e ) to person B and keeps the private key secret. Now person A wants to send a (encrypted) message M to person B.
        First, Person A converts M into an integer smaller than n by means of a reversible protocol agreed beforehand and which must ensure that m and n are co-primes.
        """
        plaintext_chars = [ord(char) for char in plaintext]
        # Now to encrypt sol it is sufficient to calculate by the operation c ≡ m e ( mod n ) 
        cyphertext = ''.join([chr( i ** self._public_key % self._prime_factor ) for i in plaintext_chars])
        return cyphertext

    @classmethod
    def decrypt(self, cyphertext):
        """
        Decrypt message cypher
        Example: Person B can recover m from c using its private key exponent d by the following calculation: m ≡ c d ( mod n )  
        """
        cyphertext_chars = [ord(char) for char in cyphertext]
        message = ''.join([chr( i ** self._private_key % self._prime_factor) for i in cyphertext_chars])
        return message
