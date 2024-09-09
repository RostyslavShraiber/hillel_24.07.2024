import string


def is_palindrome(text: str) -> bool:

    # Переводимо всі символи рядку у нижній регістр
    text = text.lower()

    # З'єднуємо всі символи рядка, ігноруємо знаки пунктуації та пробіли
    text = "".join([char for char in text if char not in string.punctuation and char != " "])

    #Перевертаємо рядок
    new_text = text[::-1]

    # Порівнюємо рядки та перевіряємо їх на паліндром
    if text == new_text:
        return True
    else:
        return False


assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")
