import pytest
import tools


def test_is_palindrome_basis():
    assert tools.is_palindrome("madam")
    assert tools.is_palindrome("Madam")
    assert tools.is_palindrome("A man a plan a canal Panama")
    assert not tools.is_palindrome("hello")


def test_char_count_basic():
    s = "abca"
    expected = {
        "a": 2,
        "b": 1,
        "c": 1,
    }
    assert tools.char_count(s) == expected
    assert tools.char_count("") == {}


def test_word_count_basic():
    assert tools.word_count("one two three") == 3
    assert tools.word_count("   spaced   out   ") == 2
    assert tools.word_count("") == 0


def test_reverse_string_basic():
    assert tools.reverse_string("abc") == "cba"
    assert tools.reverse_string("") == ""


def test_vowel_count_basis():
    assert tools.vowel_count("hello") == 2
    assert tools.vowel_count("123") == 0
    assert tools.vowel_count("AEIOUАЕЁИОУЭЮЯ") == 14
    assert tools.vowel_count("Привет") == 2
