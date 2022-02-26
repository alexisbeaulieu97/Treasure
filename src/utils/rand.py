import nacl.utils

from .constants import PASSWORD_SIZE, SALT_SIZE


def gen_salt(size=SALT_SIZE):
    return nacl.utils.random(size)


def gen_password(size=PASSWORD_SIZE):
    return nacl.utils.random(size)
