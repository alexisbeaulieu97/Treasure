from nacl import secret
from key import Key
from os.path import realpath, dirname
import os
from pathlib import Path
import sys
from treasure import Treasure, UnlockedTreasure, LockedTreasure


key = Key()
a = UnlockedTreasure('test')
b = a.lock(key)
c = b.unlock(key)
print(b.content)
print(c.content)