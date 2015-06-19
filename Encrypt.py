#!/usr/bin/python3
# -*- coding: utf-8 -*-
__author__ = 'Saylenty'


def main():
    message = input("Enter your message to encode: ")
    shift = input("Enter shift for encoding: ")
    try: shift = int(shift)
    except ValueError:
        print("shift must be an integer value > 0 and < {}".format(26))
        return
    if 0 > shift or shift >= 26:
        print("shift must be an integer value > 0 and < {}".format(26))
        return
    for c in message:
        if c.islower():
            if ord(c) <= ord('z') - shift:
                print(chr(ord(c) + shift), end='')
            else:
                print(chr(ord('a') + shift - (ord('z') - ord(c)) - 1), end='')
        elif c.isupper():
            if ord(c) <= ord('Z') - shift:
                print(chr(ord(c) + shift), end='')
            else:
                print(chr(ord('A') + shift - (ord('Z') - ord(c)) - 1), end='')
        else:
            print(c, end='')

if __name__ == "__main__": main()