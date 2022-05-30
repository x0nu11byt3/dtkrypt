#!/usr/bin/env python3

__authors__  = 'Bo Zhu [AES.py], Bruno Vermeulen [RSA.py], x0nu11byt3 [dtkrypt.py]'
__version__ = 'v1.0.0'
__github__  = 'https://github.com/x0nu11byt3/dtkrypt'
__email__   = 'x0nu11byt3@proton.me'
__license__ = 'GNU GPLv3'

import io
import os
import sys
import getpass

from optparse import OptionParser

from core.RSA import RSA
from core.AES import AES

class DtKrypt:
    
    END_LINE = ('0x'+('\End\Line'.encode('utf-8')).hex())
    
    def __init__(self,filename):
        self._filename = filename
        self._cyphertext_file = filename + '.cpt'
        
    def __repr__(self):
        return 'Daten-Krypto({})'.format(self._filename)
    
    @property
    def filename(self):
        return self._filename

    @filename.setter
    def filename(self, filename):
        self._filename = filename
        
    @property
    def cyphertext_file(self):
        return self._cyphertext_file

    @filename.setter
    def cyphertext_file(self, filename):
        self._cyphertext_file = filename + '.cpt'
    
    def get_filename(self): 
        return self._filename
    
    def get_cyphertext_file(self): 
        return self._cyphertext_file
    
    def get_message(self):
        with open(self._filename,'r') as file:
            plaintext = file.read().replace('\n', '')
        file.close()
        return plaintext
    
    def get_plaintext_lines(self):
        plaintext_lines = list()
        with open(self._filename,'r') as file:
            line = file.readlines()
            plaintext_lines.append(line)
        file.close()
        return plaintext_lines
    
    def package_plaintext(self):
        lines = list()
        with open(self._filename,'r') as file: 
            for line in file: 
                lines.append(line)
        file.close()
        
        list_file = list()
        list_line = list()
        hex_chain = list()
        
        for line in lines:
            index_chain = 1
            for char in line:
                if index_chain % 16 == 0 or char == '\n':
                    chain = ''.join(hex_chain)
                    list_line.append(chain)
                    hex_chain = list()
                else:
                    hex_chain.append(char)
                
                if char == '\n':
                    list_file.append(list_line)
                    list_line = list()
                index_chain += 1
        return list_file
    
    def get_cyphertext_message(self):
        with open(self._cyphertext_file,'r') as file:
            message_encryted = file.read()
        file.close()
        return message_encryted
    
    def get_cyphertext_lines(self):
        cyphertext_lines = []
        with open(self._cyphertext_file,'r') as file:
            line = file.readlines()
            if line == '':
                line = b''
            cyphertext_lines.append(line)
        file.close()
        return cyphertext_lines
    
    def assert_plaintext(self,plaintext,decrypted):
        if plaintext == decrypted:
            print('Thats Great,Decrypted successfull!')
            print(f'Original Message: {plaintext} \n Decrypted Message: {decrypted}')
        else:
            print('Ups!, Someting wrong :C')
    
    def file_encrypt(self,message_encryted):
        file = open(self._cyphertext_file,'w')
        file.write(str(message_encryted))
        file.close()
    
    def file_decrypt(self,message_decryted):
        file = open(self._filename,'w')
        file.write(str(message_decryted))
        file.close()
    
    def get_secret_key(self):
        secret_key = getpass.getpass()
        secret_key = secret_key.encode('utf-8')
        secret_key = int( secret_key.hex(), 16 )
        return secret_key
    
def main(argv):
    usage = 'usage: ./dtkrypt.py -f yourfile -a [aes/rsa] [ -e (--encrypt) / -d (--decrypt) ] '

    parser = OptionParser(usage=usage)
    
    parser.add_option('-f', '--file', type='string',dest='filename', help='Select a file to encrypt/decrypt')
    parser.add_option('-a', '--algorithm',type='string',dest='algorithm',help='Select an encryption algorithm [aes/rsa]')
    parser.add_option('-e', '--encrypt', action='store_true', dest='encrypt',  help='Encrypt the file')
    parser.add_option('-d', '--decrypt', action='store_true', dest='decrypt',  help='Decrypt the file')
    parser.add_option('-v', '--version', action='store_true', dest='version',  help='Display version for more information')
    
    (options, args) = parser.parse_args()
    daten_krypto = DtKrypt('yourfile.txt')
    
    if options.encrypt:
        operation = 'encrypt'
    elif options.decrypt:    
        operation = 'decrypt'
        
    if options.filename:
        daten_krypto.filename = daten_krypto.cyphertext_file = options.filename
    else:
        filename = input('[+] :: Enter your filename:')
        daten_krypto.filename = daten_krypto.cyphertext_file = filename
        
    if options.algorithm:
        algorithm = (options.algorithm).lower()
        
        if algorithm != 'aes' and algorithm != 'rsa':
            sys.exit('The argument of the algorithm is invalid!')
        else:
            if algorithm == 'aes':
                secret_key = daten_krypto.get_secret_key()
                aes = AES(secret_key)
                if operation == 'encrypt':
                    package_plaintext = daten_krypto.package_plaintext()
                    file = open(daten_krypto.filename+'.cpt','w')
                    for plaintext_line in package_plaintext:
                        for hex_chain in plaintext_line:
                            if hex_chain != '':
                                hex_plaintext = (hex_chain.strip()).encode('utf-8') 
                                hex_plaintext = int(hex_plaintext.hex(),16)
                                cyphertext = aes.encrypt(hex_plaintext,256)
                                file.write(str(cyphertext)+'\n')
                            else:
                                file.write('\n')
                        file.write(str(DtKrypt.END_LINE)+'\n')
                    file.close()
                    print('[+] :: Successful encrypted file!')
                elif operation == 'decrypt':
                    cyphertext_lines = daten_krypto.get_cyphertext_lines()
                    file = open(daten_krypto.filename,'w')
                    plaintext_line = list()
                    for cyphertext in cyphertext_lines[0]:
                        cyphertext = cyphertext.strip()
                        if cyphertext != DtKrypt.END_LINE and cyphertext != '':
                            plaintext = aes.decrypt( int( cyphertext, 10 ) ,256)
                            plaintext = (bytes.fromhex(hex(plaintext)[2:] )).decode('utf-8')
                            plaintext_line.append(plaintext)
                        else:
                            line = (''.join(plaintext_line)).strip()
                            print(line)
                            plaintext_line = list()
                            file.write(line+'\n')
                    file.close()
                    print('[+] :: successfully decrypted file!')
            elif algorithm == 'rsa':
                rsa = RSA()
                keys = rsa.generate_keys(307, 311)
                print(keys)
                if operation == 'encrypt':
                    plaintext = daten_krypto.get_message()
                    encrypted = rsa.encrypt(plaintext)
                    daten_krypto.file_encrypt(encrypted)
                    print('[+] :: Successful encrypted file!')
                    os.remove(daten_krypto.get_filename())
                elif operation == 'decrypt':
                    encrypted = daten_krypto.get_cyphertext_message()
                    decrypted = rsa.decrypt(encrypted)
                    daten_krypto.file_decrypt(decrypted)
                    print('[+] :: successfully decrypted file!')
                    os.remove(daten_krypto.get_cyphertext_file())
    sys.exit()
            
if __name__ == '__main__':
    try:
        if sys.version_info >= (3, 5):
            main(sys.argv[1:])
        else:
            sys.exit('[+] :: Please update your python version 3.5 or higher.')
    except KeyboardInterrupt:
        sys.exit('[+] :: Ctrl + C .................... Bye :C')
    except Exception as exeption:
        sys.exit(f'[+] :: An exception has occurred: {str(exeption)}')
