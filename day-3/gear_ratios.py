import re

def gear_ratios(input_path):
    input_file = list(open(input_path, 'r', encoding='utf-8'))
    lines = [line.strip() for line in input_file]

    all_numbers = get_numbers(lines)

    sum_of_numbers = 0

    for number in all_numbers:
        if has_adjacent_symbol(number, lines):
            sum_of_numbers += int(number['number'])

    return sum_of_numbers

def has_adjacent_symbol(number_dict, lines):
    rows_start = number_dict['line_index']
    rows_end = rows_start + 2
    cols_start = number_dict['start_index']
    cols_end = number_dict['end_index'] + 1

    number_of_rows = len(lines) - 1
    number_of_columns = len(lines[0]) - 1

    adjacent_symbol = False

    rows_start -= 1 if rows_start > 0 else rows_start
    cols_start -= 1 if cols_start > 0 else cols_start

    for row in range(rows_start, rows_end):
        if row > number_of_rows:
            break

        for column in range(cols_start, cols_end):
            if column > number_of_columns:
                break

            char = lines[row][column]

            if is_number(char) is False and char != '.':
                adjacent_symbol = True

    return adjacent_symbol

def get_numbers(lines):
    numbers = []

    for line_index, line in enumerate(lines):
        number = False
        current_number = ''
        start_index = -1

        for char_index, char in enumerate(line):
            if is_number(char):
                number = True
                current_number = f"{current_number}{char}"

                if start_index == -1:
                    start_index = char_index

            elif number:
                numbers.append({
                    'number': current_number,
                    'start_index': start_index,
                    'end_index': char_index,
                    'line_index': line_index
                })

                number = False
                current_number = ''
                start_index = -1

    return numbers

def is_number(char):
    if re.match('(1|2|3|4|5|6|7|8|9|0)', char):
        return True

    return False

print(gear_ratios('./inputs/input.txt'))
