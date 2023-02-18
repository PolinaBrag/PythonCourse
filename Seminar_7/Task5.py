from Seminar_7.Task4 import make_files


def main_maker(extensions: dict):
    for extension, count in extensions.items():
        make_files(extension=extension, count=count)


if __name__ == '__main__':
    data = {
    'bin': 2,
    'zip': 3,
    }

    main_maker(data)