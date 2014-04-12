__author__ = 'broglea'

import hashlib
import string
import itertools


def hash(type=None, value=None):
    if type is None:
        return 'You must specify a type'
    if value is None:
        return 'You must specify a value'
    if type == 'MD5':
        return hashlib.md5(str(value)).hexdigest()
    if type == 'SHA1':
        return hashlib.sha1(str(value)).hexdigest()
    if type == 'SHA256':
        return hashlib.sha256(str(value)).hexdigest()
    if type == 'SHA512':
        return hashlib.sha512(str(value)).hexdigest()
    return 'Specified type not supported'


#rotational cipher encoder/decoder
def rot(shift, value, encode):
    #If we want to encode this
    if encode == "True":
        alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
                    "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y",
                    "z"]
        dic = {}
        for i in range(0, len(alphabet)):
            dic[alphabet[i]] = alphabet[(i + int(shift, 10)) % len(alphabet)]

        #Convert each letter of plaintext to the corrsponding
        #encrypted letter in our dictionary creating the cryptext
        ciphertext = ""
        for l in value.lower():
            if l in dic:
                l = dic[l]
            ciphertext += l

        return ciphertext

    #If we want to decode a rotational cipher
    else:
        alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
                    "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y",
                    "z"]
        dic = {}
        for i in range(0, len(alphabet)):
            dic[alphabet[i]] = alphabet[(i + (26 - (int(shift, 10) % 26))) % len(alphabet)]

        #Convert each letter of plaintext to the corrsponding
        #encrypted letter in our dictionary creating the cryptext
        ciphertext = ""
        for l in value.lower():
            if l in dic:
                l = dic[l]
            ciphertext += l

        return ciphertext


#main base conversion function
def base_conversions(value=None, base=None, currBase=10):
    if base is None:
        return 'You must specify a base'
    if value is None:
        return 'You must specify a value'
    if base < 2:
        return 'Base must be greater than 1'

    base = int(str(base), 10)
    currBase = int(str(currBase), 10)

    if currBase == 10:
        value = int(str(value), 10)
        return int_to_base(value, base)
    else:
        value = int(str(value), currBase)
        return int_to_base(value, base)


#converts any integer to any base; only used internally, should never be called from the actual site
def int_to_base(value, base):
    digs = string.digits + string.lowercase

    if value < 0:
        sign = -1

    elif value == 0:
        return '0'
    else:
        sign = 1
    value *= sign
    digits = []
    while value:
        digits.append(digs[value % base])
        value /= base
    if sign < 0:
        digits.append('-')
    digits.reverse()
    return ''.join(digits)


def xor_tool(val=None, xor_key=None):
    if val is None:
        return 'You must specify a base'
    if xor_key is None:
        return 'You must specify a value'

    return ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(val, itertools.cycle(xor_key)))