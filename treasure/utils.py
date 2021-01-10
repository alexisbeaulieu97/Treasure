import nacl.utils
from nacl import pwhash

SALT_SIZE = pwhash.argon2i.SALTBYTES
PASSWORD_SIZE = 32


def get_salt(size=SALT_SIZE):
    return nacl.utils.random(size)


def get_password(size=PASSWORD_SIZE):
    return nacl.utils.random(size)


def to_bytes(t):
    if not isinstance(t, bytes):
        t = t.encode()
    return t
