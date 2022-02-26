from nacl import pwhash, secret

KEY_SIZE = secret.SecretBox.KEY_SIZE
SALT_SIZE = pwhash.argon2i.SALTBYTES
SALT_DELIMITER = b":"
SALT_POS = 0
DATA_POS = 1
PASSWORD_SIZE = 32
