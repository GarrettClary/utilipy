#!/usr/bin/env python3
#
# A simple password generator using Python's "secrets".
#


import string
import secrets
import os.path
import sys


def usage():
    file_name = os.path.basename(sys.argv[0])
    print('usage: ' + file_name + ' <password_length>')
    sys.exit()
    
def gen_passwd(pwd_length):
    pwd_length = int(sys.argv[1])
    usable = string.ascii_letters + string.digits + string.punctuation
    pwd = ''
    
    for i in range(pwd_length):
        pwd += secrets.choice(usable)
    
    print(pwd)


def main():
    if len(sys.argv) != 2:
        usage()
    else:
        try:
            int(sys.argv[1])
            if int(sys.argv[1]) < 8:
                print('You can do better than that...')
                sys.exit()
            gen_passwd(sys.argv[1])
        except ValueError:
            print('Length of Password must be a whole number (8, 12, 15, etc)')
            sys.exit()

if __name__ == '__main__':
    main()
