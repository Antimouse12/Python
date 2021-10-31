keys = ('name', 'last_name', 'year_of_birth', 'city', 'email', 'phone_number')
details = {}
for key in keys:
    info = input(f'введите информацию о пользователе - {key} : ')
    details[key] = info

print(details)


def user_info(**details):
    return ' '.join(details.values())
# не могу понять как распаковать словарь в строку




