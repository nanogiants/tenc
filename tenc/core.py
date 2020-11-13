from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


def encrypt(raw, password):
    cipher = AES.new(pad(password.encode(), 16), AES.MODE_CBC)
    cypherTextBytes = cipher.encrypt(pad(raw.encode(), AES.block_size))

    return cipher.iv.hex() + ':' + cypherTextBytes.hex()


def decrypt(data, password):
    try:
        content = data.split(':')

        iv = bytes(bytearray.fromhex(content[0]))
        ciphertext = bytes(bytearray.fromhex(content[1]))

        cipher = AES.new(pad(password.encode(), 16), AES.MODE_CBC, iv)
        return unpad(cipher.decrypt(ciphertext), AES.block_size).decode('utf-8')
    except ValueError:
        print("There was an error")
        raise ValueError
