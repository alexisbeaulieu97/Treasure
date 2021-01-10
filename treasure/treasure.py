import argparse

from core import Key, LockedTreasure, UnlockedTreasure

parser = argparse.ArgumentParser()
args = parser.parse_args()

if __name__ == "__main__":
    key = Key("some password", securityLevel=Key.SecurityLevel.LOW)
    u = UnlockedTreasure("some message")
    print(u.content)

    l = u.lock(key)
    print(l.content)
