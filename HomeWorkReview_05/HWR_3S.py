"""Невозможно загрузить на codewars
' You cannot submit your solution because the kata is retired.' ."""

def remove_vowels(strng):
    vowels = "aeiouAEIOU"

    result = "".join([char for char in strng if char not in vowels])

    return result