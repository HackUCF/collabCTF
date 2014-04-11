__author__ = 'broglea'

import hashlib

def hash(type=None, value=None):
    if type is None:
        return 'You must specify a type'
    if value is None:
        return 'You must specify a value'
    if type is 'MD5':
        return hashlib.md5(value).hexdigest()
    if type is 'SHA1':
        return hashlib.sha1(value).hexdigest()
    if type is 'SHA256':
        return hashlib.sha256(value).hexdigest()
    if type is 'SHA512':
        return hashlib.sha512(value).hexdigest()
    return 'Specified type not supported'