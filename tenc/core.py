import sys
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


def encrypt(data, password):
    """Enrcrypt data and return content in binary"""

    try:
        cipher = AES.new(password.encode(), AES.MODE_CBC)
        cypher_text_bytes = cipher.encrypt(pad(data.encode(), AES.block_size))

        return b'' + cipher.iv + b':' + cypher_text_bytes
    except ValueError:
        print("There was an error")
        raise ValueError


def decrypt(data, password):
    """Decrypt data and return decrypted string in utf-8"""

    try:
        iv = bytes(bytearray.fromhex(data[0:16].hex()))
        cipher_text = bytes(bytearray.fromhex(data[17:].hex()))

        cipher = AES.new(password.encode(), AES.MODE_CBC, iv)
        return unpad(cipher.decrypt(cipher_text), AES.block_size).decode('utf-8')
    except ValueError:
        print("There was an error")
        raise ValueError
