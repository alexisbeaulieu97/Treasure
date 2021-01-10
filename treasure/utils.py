import nacl.utils
from nacl import pwhash

SALT_SIZE = pwhash.argon2i.SALTBYTES


def get_salt():
    return nacl.utils.random(SALT_SIZE)


def to_bytes(t):
    if not isinstance(t, bytes):
        t = t.encode()
    return t
