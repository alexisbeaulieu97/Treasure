from dataclasses import dataclass
from pathlib import Path
from typing import Union

from treasure import Treasure


def to_bytes(s):
    try:
        s = s.encode()
    except (UnicodeEncodeError, AttributeError):
        pass
    return s


def get_files(basepath, pattern, excludes='') -> list[Path]:
    path_obj = Path(basepath)
    files = []
    if path_obj.is_dir():
        includes = path_obj.rglob(pattern)
        excludes = set(path_obj.rglob(excludes))
        files.extend([item for item in includes if item.is_file()
                      and item not in excludes])
    else:
        files.append(path_obj)

    return files


@dataclass
class InputTreasure:
    treasure: Treasure
    source: Union[str, Path] = 'stdin'
