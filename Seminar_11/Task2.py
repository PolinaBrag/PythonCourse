class Archive:
    """
    При первом запуске создает экземпляр класса, при повторном - добавляет в архив прежние данные.
    """
    instance = None
    count_archive = []
    text_archive = []

    def __new__(cls, *args, **kwargs):
        """Возвращает экземпляр класса Archive."""
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        # cls.instance.count_archive = []
        # cls.instance.text_archive = []
        else:
            cls.instance.count_archive.append(cls.instance.count)
            cls.instance.text_archive.append(cls.instance.text)
        return cls.instance

    def __init__(self, count, text):
        """Инициализирует экземпляр класса Archive."""
        self.count = count
        self.text = text
    # self.count_archive.append(self.count)
    # self.text_archive.append(self.text)

    def __str__(self):
        """Возвращает строковое описание экземпляра класса Archive."""
        return f'Текст {self.text} содержит архив: {self.text_archive}'


if __name__ == '__main__':
    d1 = Archive(1, 'a')
    print(d1.text, d1.text_archive)
    print(d1)
    d2 = Archive(2, 'b')
    print(d2.text, d2.text_archive)
    print(d2)
    d3 = Archive(3, 'c')
    print(d3.text, d3.text_archive)
    print(d3)
