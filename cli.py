#!/usr/bin/env python3

import sys
import os
import argparse

from encryption.methods import encrypt, decrypt

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Encrypt and decrypt files')

    parser.add_argument('-f', dest='path', help='path to file', required=True)
    parser.add_argument('-p', dest='password', help='password', required=True)
    parser.add_argument('-d', action='store_true', help='should decrypt otherwise encrypt')

    args = parser.parse_args()

    if not args.d:
        filename = args.path + '.enc'

        with open(args.path, 'r') as plainFile:
            with open(filename, 'w+') as f:
                f.write(encrypt(plainFile.read(), args.password))
                print('{} encrypted and saved as {}'.format(args.path, filename))
                f.close()

            plainFile.close()
    else:
        filename = os.path.join(os.path.dirname(args.path), 'dec_' + os.path.basename(args.path).replace('.enc', ''))

        with open(args.path, 'r') as encryptedFile:
            with open(filename, 'w+') as f:
                decrypted = decrypt(encryptedFile.read(), args.password)
                if decrypted:
                    f.write(decrypted)
                    print('{} decrypted and saved as {}'.format(args.path, filename))
                f.close()

            encryptedFile.close()
