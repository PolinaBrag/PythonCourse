import unittest


def split_path_file(path_file: str):
    if "." and '\\' in path_file:
        path, file_type = path_file.split(".")
        name = path.split('\\')[-1]
        path = path.replace(name, '')
        return f'Путь: {path}, название: {name}, расширение: {file_type}'
    else:
        return 'Некорректный путь файла'


class TestSplitPath(unittest.TestCase):
    def test_incorrect_path(self):
        self.assertEqual(split_path_file('Letter'), 'Некорректный путь файла')

    def test_split_path(self):
        self.assertEqual(split_path_file(r'C:\\user\\docs\\Letter.txt'),
                         'Путь: C:\\\\user\\\\docs\\\\, название: Letter, расширение: txt')


if __name__ == '__main__':
    #  print(split_path_file('C:\user\docs\Letter.txt'))
    unittest.main(verbosity=2)