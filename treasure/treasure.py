from pathlib import Path
import base64

from nacl import secret

from utils import data
from utils.constants import SALT_SIZE


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
    def lock(self, key):
        box = secret.SecretBox(key.value)
        return LockedTreasure(base64.b64encode(key.salt + box.encrypt(self.content)))


class LockedTreasure(Treasure):
    def __init__(self, content):
        decoded = base64.b64decode(content)
        self.content = data.to_bytes(decoded)
        self.salt = decoded[:SALT_SIZE]
        super().__init__(self.content)

    def output(self):
        return base64.b64encode(self.content)

    def unlock(self, key):
        box = secret.SecretBox(key.value)
        return UnlockedTreasure(box.decrypt(self.content[SALT_SIZE:]))
