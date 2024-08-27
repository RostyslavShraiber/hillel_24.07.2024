def second_index(text, some_str):

    #Знаходимо перше входження підрядка
    index_1 = text.find(some_str)
    #Перевіряємо, чи знайдено підрядок у основному рядку (вперше)
    if index_1 == -1:
        return None

    # Знаходимо друге входження підрядка
    index_2 = text.find(some_str, index_1 + len(some_str))
    #Перевіряємо, чи знайдено підрядок у основному рядку (вдруге)
    if index_2 == -1:
        return None

    return index_2


assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'
print('ОК')
