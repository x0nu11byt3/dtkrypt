[![GitHub release](https://img.shields.io/badge/release-v1.0.0-green)](https://github.com/x0nu11byt3/dtkrypt)

# Daten Krypto
Daten Krypto: Encrypt and Decrypt is small application of  implementation of the functioning of a  system cryptography ( symmetric and  asymmetric key cryptography ) . Application written in Python3.8 to  encrypt data on a small scale. At the moment this app can only encrypt plain text files for example *.txt or .md.

# Requirements
The project can be used with **python3.8** for to build. However, it requires **python3.5** as minimum. And  **getpass** package. 
If you don't want to install python3.8 on your main operating system, you can install python3.8 on a virtual environment you can use **virtualenv** or **pipenv**

# Algorithms
  - __AES__
    AES Is Symmetric key cryptography algorithm ( secret key cryptograph ) AES ( Advanced Encryption Standard )
    The Advanced Encryption Standard (AES), also known by its original name Rijndael.
    Aditional Note:
    At the moment the key expansion implementation only supports 128 bits of key length, 
    in the future this implementation will be changed to one that supports 128,192 and 256 Bits
    
    Additional note: Be careful when using this implementation it only has a small bug that returns a file with an extra line break,
    and removes a couple of special characters.
    
  - __RSA__ (**Rivest–Shamir–Adleman**)
    Asymmetric key cryptography algorithm based ( public key cryptography and private key cryptography )
    RSA is a public-key cryptographic algorithm based on the difficulty of factoring large integers (prime numbers).
    The algorithm is typically used for both encryption and authentication (digital signature).
    
    The basic principle on which the RSA algorithm is based is the search to find three very large positive integers e,
    d and n, so that with a modular exponent for all integers m { 0 ≤ m < n }: 
    
    Additional note: Be careful when using this implementation it only has a small issue,
    it only accepts files with less than 16 characters, this bug is temporary. :(
    
# Usage dtkrypt
    Usage: ./dtkrypt.py -f yourfile -a [aes/rsa] [ -e (--encrypt) / -d (--decrypt) ]

    Options:
    -h, --help            show this help message and exit
    -f FILENAME, --file=FILENAME
                            Select a file to encrypt/decrypt
    -a ALGORITHM, --algorithm=ALGORITHM
                            Select an encryption algorithm [aes/rsa]
    -e, --encrypt         Encrypt the file
    -d, --decrypt         Decrypt the file
    -v, --version         Display version for more information
    
# Example
    ./dtkrypt.py -f sample_aes.txt -a aes -e
    ./dtkrypt.py -f sample_aes.txt -a aes -d
    python dtkrypt.py --file=sample_rsa.txt --algorithm=rsa --encrypt
    python dtkrypt.py --file=sample_rsa.txt --algorithm=rsa --decrypt

# Installation
```sh
# normally this package is already installed in most unix-based 
# distributions e.g. GNU/Linux, Freebsd, etc.
# Install python3 in operating systems based on Debian.
$ sudo apt update
$ sudo apt upgrade
$ sudo apt install python3
# Install python3 in operating systems based on ArchLinux
$ sudo pacman -Sy python
# Finally check the installed version
$ python --version
# You can install keyboard package with pip or pip3
$ pip install getpass
# clone the repository
$ git clone https://github.com/x0nu11byt3/dtkrypt.git
# access the project directory
$ cd dtkrypt
# ready ! you can try dtkrypt.py
$ python dtkrypt.py --help
# or also you can use
$ ./dtkrypt.py -h
```
   
# special thanks
Special thanks to the implementation of the AES algorithm by [Bo Zhu](https://github.com/bozhu) and the implementation of the RSA algorithm by [Bruno Vermeulen](https://github.com/bvermeulen), thanks to these projects provided a lot of support and inspiration. Please visit their repositories you may be interested to you.

# Disclaimer
This project is not recommended for use in production environments, it is for demonstration and educational use only.
instead you can use projects like **OpenPGP**, **GPG**, **ccencrypt**, etc.

If you are looking for an api for the development/use of cryptographic systems I recommend you to take a look at the projects like:
   
   -   [Fernet (symmetric encryption)](https://cryptography.io/en/latest/fernet/)
        -   Fernet is an authenticated implementation of symmetric cryptography, also known as **secret key**.
            Fernet also has support for implementing key rotation through MultiFernet.
            
   -   [Pycryptodome](https://pycryptodome.readthedocs.io/en/latest/)
    
        -   PyCryptodome is a standalone package of low-level cryptographic systems.
            It supports Python 2.6 and 2.7, Python 3.4 and newer, and PyPy.
        -   Authenticated encryption modes (GCM, CCM, EAX, SIV, OCB)
        -   Accelerated AES on Intel platforms via AES-NI
        -   Elliptic curves cryptography (NIST P-256, P-384 and P-521 curves only)
        -   Better and more compact API (nonce and iv attributes for ciphers,
            automatic generation of random nonces and IVs, simplified CTR cipher mode, and more)
        -   SHA-3 (including SHAKE XOFs), truncated SHA-512 and BLAKE2 hash algorithms
        -   Salsa20 and ChaCha20/XChaCha20 stream ciphers
        -   Poly1305 MAC
        -   ChaCha20-Poly1305 and XChaCha20-Poly1305 authenticated ciphers
        -   Deterministic (EC)DSA
        -   Password-protected PKCS#8 key containers
        -   Shamir’s Secret Sharing scheme
        -   Random numbers get sourced directly from the OS (and not from a CSPRNG in userspace)
        -   Cleaner RSA and DSA key generation (largely based on FIPS 186-4)
