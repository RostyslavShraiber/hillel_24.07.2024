import re


def first_word(text: str) -> str:
    """ Пошук першого слова """
    # Замінюємо всі символи (окрім апострофа) у рядку на пробіли
    text = re.sub(r"[^\w\s']", ' ', text)
    # Знаходимо перше слово рядка
    first_elem = text.split()[0]
    # Повертаємо перше слово рядка
    return first_elem


assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'
print('OK')
