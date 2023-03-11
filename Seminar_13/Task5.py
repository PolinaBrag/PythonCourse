import json
from pathlib import Path
from Seminar_13.Task3 import AccessError, LevelError


class User:
    def __init__(self, lvl, idx, name):
        self.lvl = lvl
        self.idx = idx
        self.name = name

    def __eq__(self, other):
        return self.idx == other.idx and self.name == other.name

    def __hash__(self):
        return hash((self.idx, self.name))

    def __repr__(self):
        return f'User(lvl={self.lvl}, idx={self.idx}, name={self.name})'


class Project:
    _users = set()

    def __init__(self):
        self.me = None

    def read_json(self, file: Path):
        with open(file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        for lvl, value in data.items():
            for idx, password in value.items():
                self._users.add(User(int(lvl), int(idx), password))

        return self._users

    def sign_in(self, name, idx):
        spam_user = User(name=name, idx=idx, lvl=0)

        if spam_user not in self._users:
            raise AccessError('Отказано в доступе')
        for user in self._users:
            if user == spam_user:
                self.me = user
                return user

    def user_add(self, name, idx, lvl):
        spam_user = User(name=name, idx=idx, lvl=lvl)
        if spam_user.lvl < self.me.lvl:
            raise LevelError("Level value error...")
        self._users.add(spam_user)
        return spam_user


if __name__ == '__main__':
    project = Project()
    res = project.read_json(Path('names.json'))
    print(f'{res = }')
    print(project.sign_in("nick", 12345))
    print(project.user_add('wsad', 741, 3))
