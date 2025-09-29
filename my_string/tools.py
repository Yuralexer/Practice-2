def is_palindrome(s: str) -> bool:
    """
    Проверяет, является ли строка палиндромом (без учёта регистра и пробелов).
    """
    clean = ''.join(ch.lower() for ch in s if ch.isalnum())
    return clean == clean[::-1]


def char_count(s: str) -> dict:
    """
    Возвращает словарь {символ: количество}.
    """
    counts = {}
    for ch in s:
        counts[ch] = counts.get(ch, 0) + 1
    return counts


def word_count(s: str) -> int:
    """
    Считает количество слов, разделённых пробелами.
    """
    return len(s.split())


def reverse_string(s: str) -> str:
    """
    Возвращает строку в обратном порядке.
    """
    return s[::-1]


def vowel_count(s: str) -> int:
    """
    Подсчёт количества гласных.
    """
    vowels = "aeiouyаеёиоуэюя"
    return sum(1 for ch in s if ch in vowels)
