import regex as re


def sub_string(str):
    num_dict = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
        'zero': '0',
    }

    return num_dict[str]


def get_numbers(line):
    matches = list(re.finditer(r"[0-9?]|(one|two|three|four|five|six|seven|eight|nine)", line, overlapped=True))
    return [str(matches[0].group(0)), str(matches[-1].group(0))]


def to_int(pair):
    ints = []
    for num in pair:
        if len(num) > 1:
            ints.append(sub_string(num))
        else:
            ints.append(num)

    return int(str(ints[0] + ints[-1]))


with open("input.txt") as input:
    results = []
    for line in input:
        results.append(to_int(get_numbers(line)))

    print(sum(results))
