from passlib.hash import sha256_crypt
from passlib.hash import sha512_crypt
from passlib.hash import md5_crypt

from passlib.hash import md5_crypt as md5
from passlib.hash import sha256_crypt as sha256
from passlib.hash import sha512_crypt as sha512

'''
Format & Algorithm
[https://pythonhosted.org/passlib/lib/passlib.hash.sha256_crypt.html#f1]

An example sha256-crypt hash (of the string password) is:

    $5$rounds=80000$wnsT7Yr92oJoP28r$cKhJImk5mfuSKV9b3mumNzlbstFUplKtQXXMo4G6Ep5

An sha256-crypt hash string has the format $5$rounds=rounds$salt$checksum, where:

    $5$ is the prefix used to identify sha256-crypt hashes, following the Modular Crypt Format
    rounds is the decimal number of rounds to use (80000 in the example).
    salt is 0-16 characters drawn from [./0-9A-Za-z], providing a 96-bit salt (wnsT7Yr92oJoP28r in the example).
    checksum is 43 characters drawn from the same set, encoding a 256-bit checksum (cKhJImk5mfuSKV9b3mumNzlbstFUplKtQXXMo4G6Ep5 in the example).

There is also an alternate format $5$salt$checksum, which can be used when the rounds parameter is equal to 5000 (see the implicit_rounds parameter above).


some usage

from passlib.hash import md5_crypt as md5
from passlib.hash import sha256_crypt as sha256
from passlib.hash import sha512_crypt as sha512

passwd = 'zucca'
md5_passwd = str(md5.encrypt(str(passwd), rounds=5000, implicit_rounds=True))
sha256_passwd = sha256.encrypt(passwd, rounds=5000, implicit_rounds=True)
sha512_passwd = sha512.encrypt(passwd, rounds=5000, implicit_rounds=True)

'''
# generate new salt, encrypt password
print('fuuuuuuuuuuu' + '\n' + sha256_crypt.encrypt('password') + '\n' + 'mmmmaaaaaaaaaaannnnnnnnnnchuuuuuuuuuu')

hash = sha256_crypt.encrypt("password")
hash
# salted_hash = encrypt
'$5$rounds=80000$wnsT7Yr92oJoP28r$cKhJImk5mfuSKV9b3mumNzlbstFUplKtQXXMo4G6Ep5'
myhash = hash
'$5$rounds=80000$wnsT7Yr92oJoP28r$cKhJImk5mfuSKV9b3mumNzlbstFUplKtQXXMo4G6Ep5'
print('The current hash is' + myhash + '\n')

# same, but with explict number of rounds
sha256_crypt.encrypt("password", rounds=12345)
'$5$rounds=12345$q3hvJE5mn5jKRsW.$BbbYTFiaImz9rTy03GGi.Jf9YY5bmxN0LU3p3uI1iUB'

encrypted_hash = sha256_crypt.encrypt("password", rounds=12345)
'$5$rounds=12345$q3hvJE5mn5jKRsW.$BbbYTFiaImz9rTy03GGi.Jf9YY5bmxN0LU3p3uI1iUB'
print('The current hash is' + encrypted_hash)

# verify password
sha256_crypt.verify("password", hash)
True
sha256_crypt.verify("letmein", hash)
False

print('-'*120)

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
digest.update(b"abc")
digest.update(b"123")
digfin = digest.finalize()
'l\xa1=R\xcap\xc8\x83\xe0\xf0\xbb\x10\x1eBZ\x89\xe8bM\xe5\x1d\xb2\xd29%\x93\xafj\x84\x11\x80\x90'
print(str(digfin))

print('FERNET'+ '-'*120)

from cryptography.fernet import Fernet
# Put this somewhere safe!
key = Fernet.generate_key()
f = Fernet(key)
token = f.encrypt(b"A really secret message. Not for prying eyes.")
token
'...'
f.decrypt(token)
'A really secret message. Not for prying eyes.'
print(token)

print('-'*120)


key = Fernet.generate_key()
cipher_suite = Fernet(key)
cipher_text = cipher_suite.encrypt(b"a")
plain_text = cipher_suite.decrypt(cipher_text)

print("The cypher ::::: " + str(cipher_text))
print("....means: ::::: " + str(plain_text))
# ----------------------------------------------------------------------------------------------------
'''

#!/usr/bin/python
# -*- coding: utf-8 -*-
# import crypt
import passlib

def testPass(cryptPass):
    salt = cryptPass[0:2]
    dictFile = open('dictionary.txt', 'r')
    for word in dictFile.readlines():
        word = word.strip('\n')
        cryptWord = cryptPass.crcrypt.crypt(word, salt)
        if cryptWord == cryptPass:
            print('[+] Found Password: ' + word + '\n')
            return
    print('[-] Password Not Found.\n')
    return


def main():
    passFile = open('passwords.txt')
    for line in passFile.readlines():
        if ':' in line:
            user = line.split(':')[0]
            cryptPass = line.split(':')[1].strip(' ')
            print('[*] Cracking Password For: ' + user)
            testPass(cryptPass)


if __name__ == '__main__':
    main()
'''