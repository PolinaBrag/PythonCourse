import json
import os
from pathlib import Path


def get_from_user(file: Path) -> None:
    unique_id = set()
    result = {str(i): {} for i in range(1, 7 + 1)}
    if file.is_file() and os.path.getsize(file) > 0:
        with open(file, 'r', encoding='utf-8') as js:
            result = json.load(js)
            unique_id.update(*((value.keys()) for key, value in result.items()))
    while True:
        value, user_id, name = input('>>> ').split()
        result[value].update({int(user_id): name})
        with open(file, 'w', encoding='utf-8') as f:
            print(result)
            json.dump(result, f, indent=2)


if __name__ == '__main__':
    get_from_user(Path('names.json'))