import argparse
import os
import sys
from pathlib import Path

from key import Key
from treasure import LockedTreasure, Treasure, UnlockedTreasure
from utils.data import InputTreasure, get_files, to_bytes
from utils.password import get_password

# create parser
parser = argparse.ArgumentParser(
    formatter_class=lambda prog: argparse.HelpFormatter(prog, max_help_position=50))

parser.add_argument('-k', '--keep', action='store_true',
                    help='keep the original file when encrypting or decrypting from a file')
parser.add_argument('-i', '--input', help='input file/directory path')
parser.add_argument('-o', '--output', help='output file/directory path')

# actions
actions_group = parser.add_argument_group('action options')
actions_options = actions_group.add_mutually_exclusive_group(required=True)
actions_options.add_argument(
    '-l', '--lock', action='store_true', help='encrypt content')
actions_options.add_argument(
    '-u', '--unlock', action='store_true', help='decrypt content')

# parse arguments
args = parser.parse_args()
dict_args = vars(args)


def parse_arguments():
    actions = {
        'lock': lock,
        'unlock': unlock
    }
    for k, v in actions.items():
        if dict_args[k]:
            return v


def lock():
    key = Key(get_password('treasure(s)'))
    data_gen = get_data(excludes='*.ENC')
    while True:
        try:
            input_treasure = next(data_gen)
        except:
            break
        unlocked = UnlockedTreasure.from_treasure(input_treasure.treasure)
        locked_treasure = unlocked.lock(key)
        output_path = get_output_path(input_treasure.source)
        output_data(locked_treasure.output(), output_path)
        delete_original(input_treasure.source)


def unlock():
    data_gen = get_data('*.ENC')
    key = None
    input_treasure = None
    while True:
        try:
            input_treasure = next(data_gen)
        except:
            break
        locked = LockedTreasure.from_treasure(input_treasure.treasure)
        if not key or key.salt != locked.salt:
            key = Key(get_password(
                f'{input_treasure.source} treasure'), locked.salt)
        unlocked_treasure = locked.unlock(key)
        output_path = get_output_path(input_treasure.source)
        output_data(unlocked_treasure.output(), output_path)
        delete_original(input_treasure.source)


def get_data(pattern='*', excludes=''):
    if args.input and os.path.exists(args.input):
        files = get_files(args.input, pattern, excludes)
        for file in files:
            yield InputTreasure(Treasure.from_file(file), file)
    else:
        stdin_data = to_bytes(sys.stdin.read().rstrip('\n'))
        yield InputTreasure(Treasure(stdin_data))


def output_data(data: bytes, filepath=None):
    if filepath:
        if args.lock:
            # add .ENC
            filepath = filepath + '.ENC'
        else:
            # remove .ENC
            filepath = filepath.split('.ENC')[0]
        file = Path(filepath)
        file.write_bytes(data)
    else:
        sys.stdout.buffer.write(data)


def delete_original(filepath: Path):
    if args.input and not args.keep:
        filepath.unlink()


def get_output_path(source):
    output_path = args.output
    if output_path and os.path.isdir(output_path):
        output_path = os.path.join(output_path, os.path.basename(source))
    return output_path


def check_args():
    # check if args.input or stdin is not empty
    if not args.input and sys.stdin.isatty():
        raise Exception('stdin is empty')

    # check if input was provided but could not be found
    if args.input and not os.path.exists(args.input):
        raise Exception(f'could not find {args.input}')


# Main
if __name__ == "__main__":
    # check arguments
    check_args()

    # read data from stdin or input
    action = parse_arguments()
    action()
