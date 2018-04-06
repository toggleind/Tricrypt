#!/usr/bin/env python
from base64 import b32decode
from hashlib import sha1
import time
import hmac

# all codes are returned as a totp instance
class totp(object):
    def __init__(self, code, validfor):
        self.code = code
        self.validfor = validfor

# HOTP(K,C) = Truncate(HMAC-SHA-1(K,C))
def int_to_bytestring(i, padding=8):
    result = bytearray()
    while i:
        result.append(i & 0xFF)
        i >>= 8
    return bytes(result[::-1].rjust(padding, b'\0'))

def now():
    return int(time.time())

def timecode(timeval):
    return int_to_bytestring(int(timeval)/30)

def otp(secretkey, codelen=6, timeval=now()):
    validFor = 30 - (timeval%30)
    hasher = hmac.new(b32decode(secretkey), timecode(timeval), sha1)
    hmac_hash = bytearray(hasher.digest())
    offset = hmac_hash[-1] & 0xf
    code = ((hmac_hash[offset] & 0x7f) << 24 |
            (hmac_hash[offset + 1] & 0xff) << 16 |
            (hmac_hash[offset + 2] & 0xff) << 8 |
            (hmac_hash[offset + 3] & 0xff))
    return totp(str(code % 10**codelen).zfill(codelen), validFor)
