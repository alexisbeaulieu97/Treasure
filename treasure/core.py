from nacl import pwhash, secret

from utils import get_salt, to_bytes, get_password


class Key:
    KEY_SIZE = secret.SecretBox.KEY_SIZE

    class SecurityLevel:
        LOW = {'ops': pwhash.argon2i.OPSLIMIT_INTERACTIVE,
               'mem': pwhash.argon2i.MEMLIMIT_INTERACTIVE}
        MEDIUM = {'ops': pwhash.argon2i.OPSLIMIT_MODERATE,
                  'mem': pwhash.argon2i.MEMLIMIT_MODERATE}
        HIGH = {'ops': pwhash.argon2i.OPSLIMIT_SENSITIVE,
                'mem': pwhash.argon2i.MEMLIMIT_SENSITIVE}

    def __init__(self, password=get_password(), salt=get_salt(), securityLevel=SecurityLevel.HIGH):
        self.securityLevel = securityLevel
        self.salt = salt
        self.value = Key.derive(password, securityLevel=self.securityLevel)

    @staticmethod
    def derive(password, salt=get_salt(), securityLevel=SecurityLevel.HIGH):
        return pwhash.argon2i.kdf(Key.KEY_SIZE, to_bytes(password), salt, securityLevel['ops'], securityLevel['mem'])


class UnlockedTreasure:
    def __init__(self, content):
        self.content = to_bytes(content)

    def lock(self, key):
        box = secret.SecretBox(key.value)
        return LockedTreasure(box.encrypt(self.content))


class LockedTreasure:
    def __init__(self, content):
        self.content = to_bytes(content)

    def unlock(self, key):
        box = secret.SecretBox(key.value)
        return UnlockedTreasure(box.decrypt(self.content).decode())
