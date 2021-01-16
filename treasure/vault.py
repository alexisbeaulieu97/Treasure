import json

from treasure import LockedTreasure, UnlockedTreasure
from utils.constants import VAULT_PATH


class Vault:
    def __init__(self, key):
        vault_treasure = LockedTreasure.from_file(VAULT_PATH, key)
        self.content = json.loads(vault_treasure.unlock().content)
        print(self.content)

    def add_treasure(self):
        pass

    def remove_treasure(self):
        pass
