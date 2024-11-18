import re


class Asterisk:
    position: (int, int)
    adj_lines: [str]
    is_gear: bool
    match = re.Match

    def __init__(self, x, y, line, match):
        self.position = (x, y)
        self.line = line
        self.is_gear = False
        self.match = match

    def get_pos(self):
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


def find_asterisks(line, index):
    regex = re.compile(r"\*")
    asterisks = []

    for i in regex.finditer(line):
        if i is not None:
            asterisks.append(Asterisk(i.start(), index, line, i))

    return asterisks
