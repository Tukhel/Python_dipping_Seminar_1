# Задание №2
# ✔ Самостоятельно сохраните в переменной строку текста.
# ✔ Создайте из строки словарь, где ключ — буква, а значение — код буквы.
# ✔ Напишите преобразование в одну строку.

text = 'Самостоятельно сохраните в переменной строку текста'.replace(' ', '')
my_dict = {char: ord(char) for char in text}
print(my_dict)