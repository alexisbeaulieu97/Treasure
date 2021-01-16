from nacl import pwhash, secret

KEY_SIZE = secret.SecretBox.KEY_SIZE
SALT_SIZE = pwhash.argon2i.SALTBYTES
PASSWORD_SIZE = 32
