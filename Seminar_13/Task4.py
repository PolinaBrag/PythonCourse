import json
from pathlib import Path


class User:
    def __init__(self, lvl, idx, name):
        self.lvl = lvl
        self.idx = idx
        self.name = name


def read_json(file: Path) -> set[User]:
    users = set()

    with open(file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    for key, value in data.items():
        for idx, name in value.items():
            users.add(User(lvl=key, idx=idx, name=name))
    return users


if __name__ == '__main__':
    res = read_json(Path('names.json'))
    print(f'{res = }')