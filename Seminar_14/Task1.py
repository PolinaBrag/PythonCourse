# проверка строки

from string import ascii_letters


def text_filter(s: str) -> str:
    result = ''.join(c for c in s if c in set(ascii_letters + ' '))
    return result.lower()


if __name__ == '__main__':
    print(text_filter('rewg23wegваыgf 1324sdg325 ывпвfgjы'))