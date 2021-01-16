from pathlib import Path
from nacl import secret

from utils import data
from utils.constants import SALT_SIZE


class Treasure:
    def __init__(self, content):
        self.content = data.to_bytes(content)

    def save(self, filepath: Path):
        filepath.write_bytes(self.content)

    @classmethod
    def from_file(cls, filepath: Path):
        return cls(filepath.read_bytes())

    @classmethod
    def from_treasure(cls, treasure):
        return cls(treasure.content)


class UnlockedTreasure(Treasure):
    def lock(self, key):
        box = secret.SecretBox(key.value)
        return LockedTreasure(key.salt + box.encrypt(self.content))


class LockedTreasure(Treasure):
    def __init__(self, content):
        self.salt = content[:SALT_SIZE]
        super().__init__(content)

    def unlock(self, key):
        box = secret.SecretBox(key.value)
        return UnlockedTreasure(box.decrypt(self.content[SALT_SIZE:]))
