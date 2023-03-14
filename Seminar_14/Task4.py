# pytest
import pytest
from string import ascii_letters


def text_filter(s: str) -> str:
    result = ''.join(c for c in s if c in set(ascii_letters + ' '))
    return result.lower()


def test_no_change():
    assert text_filter('hello world') == 'hello world'


def test_upper_lower():
    assert text_filter('Hello World') == 'hello world'


def test_punctuation():
    assert text_filter('hello123.,/\\ world456!') == 'hello world'


def test_not_ascii():
    assert text_filter('hello Питонистический world') == 'hello world'


def test_totals():
    assert text_filter('Hello123, Питонистический World!') == 'hello world'


if __name__ == '__main__':
    pytest.main(['-v'])