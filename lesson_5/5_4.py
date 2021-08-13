numbers_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open('text_4_rus.txt', 'w', encoding='utf-8') as f_rus:
    with open('text_4_eng.txt', 'r', encoding='utf-8') as f_eng:
        f_rus.write(str([line.replace(line.split()[0], numbers_dict.get(line.split()[0])) for line in f_eng]))

# результат получился ['Один - 1\n', 'Два - 2\n', 'Три - 3\n', 'Четыре - 4'],
# как преобразовать список в строки без печатания 1\n ?
