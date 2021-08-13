f = open('text_1.txt', 'w')
while True:
    text = input('введите данные: ')
    if text == ' ':
        break
    f.write(text + '\n')
f.close()
