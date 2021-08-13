with open('text_1.txt') as f:
    lines = f.readlines()
    lines_count = len(lines)
    print(f'количество строк в файле: {lines_count}')

    for index, value in enumerate(lines):
        words_count = len(value.split())
        print(f'количество слов в {index} строке: {words_count}')
