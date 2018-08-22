import hashlib
import struct

STR = "This is a string!"


def make_encrypt_table():
    m = hashlib.md5()
    s = m.digest()
    a, b = struct.unpack('<QQ', s)
    encrypt_table = [c for c in ''.join(map(chr, range(256)))]
    print(encrypt_table)
    for i in range(1, 1024):
        encrypt_table.sort(key=lambda x: int(a % (ord(x) + i)))
    print(encrypt_table)
    return ''.join(encrypt_table)


def make_decrypt_table(encrypt_table):
    return str.maketrans(encrypt_table, ''.join(map(chr, range(256))))


def encrypt(plaintext, encrypt_table):
    return plaintext.translate(encrypt_table)


def decrypt(ciphertext, decrypt_table):
    return ciphertext.translate(decrypt_table)


encrypt_table = make_encrypt_table()
decrypt_table = make_decrypt_table(encrypt_table)
cipher = encrypt(STR, encrypt_table)
plain = decrypt(cipher, decrypt_table)
print(cipher, plain)
