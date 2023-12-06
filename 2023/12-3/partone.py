import re
from collections import defaultdict


class Number:
    position: (int, int)
    num: int
    line: str
    is_part: bool
    match: re.Match

    def __init__(self, x, y, num, line, match):
        self.position = (x, y)
        self.num = num
        self.line = line
        self.is_part = False
        self.match = match

    def get_len(self):
        return int(len(self.num))

    def get_position(self):
        return self.position

    def get_x(self):
        return self.position[0]

    def get_y(self):
        return self.position[1]

    def is_start(self):
        if self.position[0] == 0:
            return True
        else:
            return False

    def is_end(self):
        if self.match.end() == len(self.line):
            return True
        else:
            return False


def check_adjacent(num, lines):
    range = ()
    if num.get_x() == 0:
        range = (num.get_x(), num.get_x() + len(num.num) + 1)
    elif num.is_end():
        range = (num.get_x() - 1, num.get_x() + len(num.num))
    else:
        range = (num.get_x() - 1, num.get_x() + len(num.num) + 1)

    regex = re.compile(r"[^\d\.]")
    for line in lines:
        results = regex.finditer(line, pos=range[0], endpos=range[1])
        for result in results:
            if result is not None:
                num.is_part = True


def find_numbers(line, index):
    regex = re.compile(r"\d+")
    numbers = []
    for i in regex.finditer(line):
        if i is not None:
            numbers.append(Number(i.start(), index, i.group(), line, i))

    return numbers


with open("input.txt") as input:
    lines = defaultdict(str)
    index = 0
    all_numbers = []
    parts = []

    for line in input:
        lines[index] += line.rstrip()
        index += 1

    for index, line in lines.items():
        all_numbers += find_numbers(line, index)

    for num in all_numbers:
        adjacent_lines = []
        adjacent_lines.append(num.line)

        if num.get_y() == 0:
            adjacent_lines.append(lines[num.get_y() + 1])
        elif num.get_y() == len(lines) - 1:
            adjacent_lines.append(lines[num.get_y() - 1])
        else:
            adjacent_lines.append(lines[num.get_y() - 1])
            adjacent_lines.append(lines[num.get_y() + 1])

        check_adjacent(num, adjacent_lines)

        if num.is_part:
            parts.append(int(num.num))

    print(sum(parts), parts)
