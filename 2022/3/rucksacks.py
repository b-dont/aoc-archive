class RuckSack:
    def __init__(self, pocket_one, pocket_two):
        self.pocket_one = pocket_one
        self.pocket_two = pocket_two

    def find_duplicate(self, pocket_one, pocket_two):
        for first_item in pocket_one:
            for second_item in pocket_two:
                if first_item == second_item:
                    return first_item
                    break

def create_lower():
    lowercase_items = {}
    for i in range(1, 27):
        letter = chr(ord('`')+i)
        lowercase_items.update({letter: i})

    return lowercase_items

def create_upper():
    uppercase_items = {}
    for i in range(1, 27):
        letter = chr(ord('@')+i)
        uppercase_items.update({letter: i+26})

    return uppercase_items

uppercase_items = create_upper()
lowercase_items = create_lower()
