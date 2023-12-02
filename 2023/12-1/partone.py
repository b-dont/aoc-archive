import regex as re


def get_numbers(line):
    return re.findall(r"\d", line)


def combine_digits(digits):
    return int(str(digits[0] + digits[-1]))


with open("input.txt") as input:
    digits = []
    for line in input:
        digits.append(combine_digits(get_numbers(line)))

    print(sum(digits))
