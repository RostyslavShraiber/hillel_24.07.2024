import codecs
import re


def delete_html_tags(html_file: str, result_file: str = 'cleaned.txt') -> None:
    """
    Функція видаляє всі HTML-теги з вхідного файлу та зберігає очищений текст у новий файл.

    Параметри:
    html_file (str): Шлях до вхідного HTML-файлу.
    result_file (str, опціонально): Шлях до файлу, в який буде записано очищений текст (за замовчуванням 'cleaned.txt').

    Опис:
    1. Вміст HTML-файлу зчитується з використанням кодування UTF-8.
    2. Використовується регулярний вираз для видалення всіх тегів, що починаються з '<' і закінчуються на '>'.
    3. Очищений текст записується у вихідний файл з кодуванням UTF-8.
    """
    # Читаємо вміст HTML-файлу
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()

    # Видаляємо всі HTML-теги
    cleaned_text = re.sub(r'<[^>]+>', '', html)


    # Записуємо очищений текст у новий файл
    with codecs.open(result_file, 'w', 'utf-8') as output_file:
        output_file.write(cleaned_text)
