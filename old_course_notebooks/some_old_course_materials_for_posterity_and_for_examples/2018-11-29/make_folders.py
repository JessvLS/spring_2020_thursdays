from os import makedirs
from typing import List


def make_folders(names: List[str]) -> str:
    try:
        any(map(makedirs, names))
        return f'Created {len(names)} folders.'
    except FileExistsError as e:
        return f'File already exists: {e}.'
