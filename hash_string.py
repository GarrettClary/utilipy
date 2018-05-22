#!/usr/bin/env python3

# Hash a word or string using SHA1, SHA256, or SHA512

import sys
import hashlib


def hash_1_digest(usr_input):
	hash_object = hashlib.sha1(usr_input.encode())
	hex_dig = hash_object.hexdigest()
	print('\n' + hex_dig + "\r\n")

def hash_256_digest(usr_input):
	hash_object = hashlib.sha256(usr_input.encode())
	hex_dig = hash_object.hexdigest()
	print('\n' + hex_dig + "\r\n")

def hash_512_digest(usr_input):
	hash_object = hashlib.sha512(usr_input.encode())
	hex_dig = hash_object.hexdigest()
	print('\n' + hex_dig + "\r\n")

def main():
    while True:
        hash_choice = input("Generate hash with SHA(1), SHA(256), SHA(512)? ")
        if hash_choice == '1':
            usr_input = input("\r\nEnter string to hash: ")
            hash_1_digest(usr_input)		    
        elif hash_choice == '256':
            usr_input = input("\r\nEnter string to hash: ")
            hash_256_digest(usr_input)        
        elif hash_choice == '512':
            usr_input = input("\r\nEnter string to hash: ")
            hash_512_digest(usr_input)	        
        else:
            print('\nInvalid choice\n')
            main()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\n\nQuitting program...')
        sys.exit()
