__author__ = 'broglea'

import hashlib


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
def rot(shift=None, value=None, encode=True):
    #If we want to encode this
    if encode:
        if shift is None:
            return 'You must specify a shift'
        if value is None:
            return 'You must specify a value'
        alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
                    "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y",
                    "z"]
        dic = {}
        for i in range(0, len(alphabet)):
            dic[alphabet[i]] = alphabet[(i + shift) % len(alphabet)]

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
        if shift is None:
            return 'You must specify a shift'
        if value is None:
            return 'You must specify a value'
        alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
                    "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y",
                    "z"]
        dic = {}
        for i in range(0, len(alphabet)):
            dic[alphabet[i]] = alphabet[(i + (26-shift)) % len(alphabet)]

        #Convert each letter of plaintext to the corrsponding
        #encrypted letter in our dictionary creating the cryptext
        ciphertext = ""
        for l in value.lower():
            if l in dic:
                l = dic[l]
            ciphertext += l

        return ciphertext