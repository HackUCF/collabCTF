__author__ = 'austin'

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
