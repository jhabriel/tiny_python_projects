#!/usr/bin/env python3
"""Gematria"""

import argparse
import os
import re


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Gematria',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text', metavar='str', help='Input text or file')

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read()

    return args


# --------------------------------------------------
def word2num(word):
    """Sum the ordinal values of all the characters"""

    word = re.sub('[^a-zA-Z0-9]', '', word)
    return str(sum(map(ord, word)))


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text = args.text

    for line in text.splitlines():
        print(' '.join(map(word2num, line.split())))


# --------------------------------------------------
if __name__ == '__main__':
    main()
