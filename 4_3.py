for number in range(20, 241):
    if number % 20 == 0 or number % 21 == 0:
        print(number)

my_list = [number for number in range(20, 241) if number % 20 == 0 or number % 21 == 0]
print(my_list)

# интересно, можно ли написать код в одну строку сразу вместе с функцией print
