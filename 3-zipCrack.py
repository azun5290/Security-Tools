#!/usr/bin/python
# -*- coding: utf-8 -*-
import zipfile
import optparse
import sys
from threading import Thread


def extractFile(zFile, password):
    try:
        zFile.extractall(pwd=password)
        print('[+] Found password ' + password + '\n')
    except:
        pass


def main():
    parser = optparse.OptionParser(
        "Usage: {} -f <zipfile> -d <dictionaryfile>".format(sys.argv[0])
    )
    parser.add_option(
        '-f', dest='zname', type='string', help='specify zip file'
    )
    parser.add_option(
        '-d', dest='dname', type='string',help='specify dictionary file'
    )
    (options, args) = parser.parse_args()

    if options.zname and options.dname:
        zname = options.zname
        dname = options.dname
    else:
        print('Usage: {}'.format(parser.usage))
        exit(0)

    zFile = zipfile.ZipFile(zname)
    passFile = open(dname)
    with open(dname) as f:
        dcontent = f.readlines()

    for line in dcontent:
        password = line.strip('\n')
        t = Thread(target=extractFile, args=(zFile, password))
        t.start()


if __name__ == '__main__':
    main()
