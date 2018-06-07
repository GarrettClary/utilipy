#!/usr/bin/env python3

import string
import secrets
import os.path
import sys


def usage():
    file_name = os.path.basename(sys.argv[0])
    print("usage: " + file_name + " <password_length>")
    sys.exit()
    
def generate_password(password_length):
    password_length = int(sys.argv[1])
    usable = string.ascii_letters + string.digits + string.punctuation
    password = ''
    
    for i in range(password_length):
        password += secrets.choice(usable)
    
    print(password)


def main():
    if len(sys.argv) != 2:
        usage()
    else:
        try:
            int(sys.argv[1])
            if int(sys.argv[1]) < 10:
                print("Password length must be at least 10 characters")
                sys.exit()
            generate_password(sys.argv[1])
        except ValueError:
            print("Length of Password must be a whole number (8, 12, 15... )")
            sys.exit()

if __name__ == '__main__':
    main()
