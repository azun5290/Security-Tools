#!/usr/bin/python
# -*- coding: utf-8 -*-
# import crypt
import passlib
import crypt
import sys

def testPass(cryptPass):
    salt = cryptPass[0:2]

    with open('dictionary.txt', 'r') as f:
        dictionary = f.readlines()

    for word in dictionary:
        cryptWord = crypt.crypt(word.strip('\n'), salt)
        if cryptWord == cryptPass:
            return word

    return


def main():

    passwd_filename = sys.argv[1] if len(sys.argv) == 2 else 'passwords.txt'

    with open(passwd_filename) as f:
        content = f.readlines()

    for line in content:
        if ':' in line:
            words = [word.strip() for word in line.split(':')]
            user        = words[0]
            cryptPass   = words[1]
            print('[*] Cracking Password For: ' + user)
            decryptPass = testPass(cryptPass)
           
            if not decryptPass:
                output = 'Password Not Found.'
            else:
                output = 'Found Password: {}'.format(decryptPass)

            print(output)

if __name__ == '__main__':
    main()
