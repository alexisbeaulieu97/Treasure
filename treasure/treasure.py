from nacl import secret, utils, pwhash


SALT_SIZE = pwhash.argon2i.SALTBYTES


def get_salt():
    return utils.random(SALT_SIZE)


def to_bytes(t):
    if not isinstance(t, bytes):
        t = t.encode()
    return t


class LockedTreasure:
    def __init__(self, content):
        self.content = to_bytes(content)

    def unlock(self, key):
        box = secret.SecretBox(key.value)
        return UnlockedTreasure(box.decrypt(self.content).decode())

    def save(self, filepath):
        open(filepath, 'wb').write(self.content)


class UnlockedTreasure:
    def __init__(self, content):
        self.content = to_bytes(content)

    def lock(self, key):
        box = secret.SecretBox(key.value)
        return LockedTreasure(box.encrypt(self.content))


class Key:
    KEY_SIZE = secret.SecretBox.KEY_SIZE

    class SecurityLevel:
        LOW = {'ops': pwhash.argon2i.OPSLIMIT_INTERACTIVE,
               'mem': pwhash.argon2i.MEMLIMIT_INTERACTIVE}
        MEDIUM = {'ops': pwhash.argon2i.OPSLIMIT_MODERATE,
                  'mem': pwhash.argon2i.MEMLIMIT_MODERATE}
        HIGH = {'ops': pwhash.argon2i.OPSLIMIT_SENSITIVE,
                'mem': pwhash.argon2i.MEMLIMIT_SENSITIVE}

    def __init__(self, password, salt=get_salt(), securityLevel=SecurityLevel.HIGH):
        self.salt = salt
        self.value = Key.derive(password)
        self.securityLevel = securityLevel

    @staticmethod
    def derive(password, salt=get_salt(), securityLevel=SecurityLevel.HIGH):
        return pwhash.argon2i.kdf(Key.KEY_SIZE, to_bytes(password), salt, securityLevel['ops'], securityLevel['mem'])
