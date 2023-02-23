import json
from pathlib import Path


def convert_json(file: Path) -> None:
    file_data = {}
    with open(file, 'r', encoding='utf-8') as f:
        for line in f:
            name, number = line.split()
            file_data[name.capitalize()] = float(number)
    with open(file.stem + '.json', 'w', encoding='utf-8') as f:
        json.dump(file_data, f, indent=2)


if __name__ == '__main__':
    convert_json(Path('../lesson_07/result.txt'))