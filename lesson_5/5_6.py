training_program = {}

with open('text_6.txt', 'r', encoding='utf-8') as f:
    for line in f:
        discipline, training_time = line.split(':')
        hours = [i for i in training_time if i == ' ' or ('0' <= i <= '9')]
        total_training_time = sum(map(int, "".join(hours).split()))
        training_program[discipline] = total_training_time
print(f'{training_program}')
