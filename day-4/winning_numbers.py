
def get_winning_numbers(input_path):
    input_file = input_file = list(open(input_path, 'r', encoding='utf-8'))
    lines = [line.strip() for line in input_file]

    total = 0

    for line in lines:
        line = line.split(':')[1].split('|')
        line = [numbers.strip() for numbers in line]

        numbers_i_have = line[0].split(' ')
        winning_numbers = line[1].split(' ')

        numbers_i_have = [int(number) for number in numbers_i_have if number != '']
        winning_numbers = [int(number) for number in winning_numbers if number != '']

        matches = 0
        sub_total = 0

        for number in numbers_i_have:
            if number in winning_numbers:
                matches += 1

        if matches > 0:
            sub_total = 1

            for _ in range(matches - 1):
                sub_total *= 2

        total += sub_total

    return total


result = get_winning_numbers('./inputs/input.txt')

print(result)
