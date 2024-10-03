# string_module.py


def is_palindrome(s: str) -> bool:
    """
    Проверяет, является ли строка палиндромом.
    """
    s = ''.join(
        c.lower() for c in s if c.isalnum()
    )  # Удаление всех не буквенно-цифровых символов и приведение к нижнему регистру
    return s == s[::-1]


def count_vowels(s: str) -> int:
    """
    Подсчитывает количество гласных букв в строке.
    """
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)


def reverse_string(s: str) -> str:
    """
    Возвращает перевернутую строку.
    """
    return s[::-1]


def count_words(s: str) -> int:
    """
    Подсчитывает количество слов в строке.
    """
    return len(s.split())


def corrected_function(s: str) -> int:
    """
    Возвращает индекс последнего символа в строке.
    Если строка пуста, возвращает -1.
    """
    return len(s) - 1 if len(s) > 0 else s[0]
