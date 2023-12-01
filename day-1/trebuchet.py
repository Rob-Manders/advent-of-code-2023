import re

REGEX_WORDS = 'one|two|three|four|five|six|seven|eight|nine'
WORD_NUMBER_MAP = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}

def parse_digit(digit):
    words = list(WORD_NUMBER_MAP.keys())

    if digit in words:
        return WORD_NUMBER_MAP[digit]

    return digit

def get_calibration(document_path):
    text = open(document_path, 'r', encoding='utf-8')
    lines = text.readlines()

    calibration = 0

    for line in lines:
        first_digit = re.findall(f'([1-9]|{REGEX_WORDS})', line)[0]
        last_digit = re.findall(f'([1-9]|{REGEX_WORDS[::-1]})', line[::-1])[0]

        first_digit = parse_digit(first_digit)
        last_digit = parse_digit(last_digit[::-1])

        number = first_digit + last_digit

        calibration += int(number)

    return calibration


test_calibration = get_calibration('test_calibration.txt')
second_test_calibration = get_calibration('second_test_calibration.txt')
actual_calibration = get_calibration('calibration.txt')

print(f"Test Calibration: {test_calibration}")
print(f"Second Test Calibration: {second_test_calibration}")
print(f"Actual Calibration: {actual_calibration}")
