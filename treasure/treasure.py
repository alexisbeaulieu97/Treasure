import base64
from pathlib import Path

from nacl import secret

from key import Key
from treasure.utils import data
from treasure.utils.constants import SALT_SIZE


class Treasure:
    def __init__(self, content):
        self.content = data.to_bytes(content)

    def output(self):
        return self.content

    @classmethod
    def from_file(cls, filepath: Path):
        return cls(filepath.read_bytes())

    @classmethod
    def from_treasure(cls, treasure):
        return cls(treasure.content)


class UnlockedTreasure(Treasure):
    def lock(self, key: Key):
        box = secret.SecretBox(key.value)
        return LockedTreasure(key.salt + box.encrypt(self.content))


class LockedTreasure(Treasure):
    def __init__(self, content):
        super().__init__(content)

    def output(self):
        return base64.b64encode(self.content)

    def unlock(self, key: Key):
        box = secret.SecretBox(key.value)
        return UnlockedTreasure(box.decrypt(self.content[SALT_SIZE:]))

    def forge_key(self, password: str) -> Key:
        return Key(password, self.content[:SALT_SIZE])
