
def popular_words(text: str, words: list[str]) -> dict[str, int]:
    # Перетворюємо текст на нижній регістр і розбиваємо на слова
    word_list = text.lower().split()

    # Створюємо пустий словник для підрахунку частоти слів
    word_count = {}

    # Cловник зі значенням 0 для кожного слова зі списку words
    for word in words:
        word_count[word] = 0

    # Підраховуємо появи кожного слова
    for word in word_list:
        if word in word_count:
            word_count[word] += 1

    return word_count


assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == {'i': 4, 'was': 3, 'three': 0, 'near': 0}
print('OK')
