text_1 = input('введите текст - ')
text_1 = text_1.split()

for ind, element in enumerate(text_1):
    print(ind + 1, element[0:10])
