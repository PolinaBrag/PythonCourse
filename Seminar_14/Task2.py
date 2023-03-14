# doctest

from string import ascii_letters


def text_filter(s: str) -> str:
    """
    >>> text_filter('hello world')
    'hello world'
    >>> text_filter('Hello World')
    'hello world'
    >>> text_filter('hello, world!')
    'hello world'
    >>> text_filter('hello Питонистический world')
    'hello world'
    >>> text_filter('Hello123, Питонистический World!')
    'hello world'
    """
    result = ''.join(c for c in s if c in set(ascii_letters + ' '))
    return result.lower()


if __name__ == '__main__':
    # print(text_filter('rewg23wegваыgf 1324sdg325 ывпвfgjы'))
    import doctest
    doctest.testmod(verbose=True)