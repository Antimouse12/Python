def my_func(a, b, c):
    row = sorted((a, b, c), reverse=True)
    return row[0] + row[1]


result = my_func(5, 8, 20)
print(result)
