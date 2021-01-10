from core import LockedTreasure, UnlockedTreasure, Key

key = Key("some password")
u = UnlockedTreasure("some message")
print(u.content)

l = u.lock(key)
print(l.content)
