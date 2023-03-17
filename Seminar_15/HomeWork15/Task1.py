# Возьмите любые 1-3 задачи из прошлых домашних заданий. Добавьте к ним логирование ошибок и полезной информации.
# Также реализуйте возможность запуска из командной строки с передачей параметров.
import logging

logging.basicConfig(level=logging.ERROR, filename='PathError.log', encoding='utf-8')
logger = logging.getLogger(__name__)


def split_path_file(path_file: str):
    if "." or '\\' not in path_file:
        logger.error(f'Некорректный путь: {path_file}')
        return 'Некорректный путь файла'
    elif "." and '\\' in path_file:
        path, file_type = path_file.split(".")
        name = path.split('\\')[-1]
        path = path.replace(name, '')
        return f'Путь: {path}, название: {name}, расширение: {file_type}'

if __name__ == '__main__':
    print(split_path_file('C:\\user\\docs\\Letter'))