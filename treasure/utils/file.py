import json

from treasure.utils.constants import SALT_SIZE


def read_json(filepath):
    return json.load(open(filepath, 'r'))


def write_json(filepath, d):
    json.dump(d, open(filepath, 'w'), indent=2)


def get_salt(filepath):
    return open(filepath, 'rb').read()[:SALT_SIZE]
