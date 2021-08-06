def my_func(x, y):
    return x**y


result = my_func(5, 10)
print(result)


def my_func(x, y):
    result = 1
    for i in range(y):
        result *= x

    print(result)


my_func(5, 10)
