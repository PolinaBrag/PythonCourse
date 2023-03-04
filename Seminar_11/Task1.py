from time import time


class MyStr(str):
    """
    Создает строку из текста и ее автора.
    """
    def __new__(cls, value, author):
        """Возвращает экземпляр класса MyStr."""
        instance = super().__new__(cls, value)
        instance.author = author
        instance.time = time()
        return instance

    def __str__(self):
        """Возвращает строковое описание экземпляра класса MyStr."""
        return f'Строка {self!r} написана автором {self.author}'


if __name__ == '__main__':
    s = MyStr('Hello world!', 'prepod')
    print(s)
    print(s.author)
    s2 = MyStr('Hi', 'student')
    print(s2.author)
    print(s.upper())
    print(s.time, s2.time)