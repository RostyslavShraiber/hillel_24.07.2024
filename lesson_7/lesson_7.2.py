def correct_sentence(text: str) -> str:

    #Перевірка чи перша літера стрічки з маленької літери. У противному випадку зробити літеру великою
    if text[0].islower():
        text = text.capitalize()

    #Перевірка на наявність крапки в кінці рядка. У противному випадку додати крапку вкінці стрічки
    if not text.endswith("."):
        text += "."

    return text


assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
print('ОК')
