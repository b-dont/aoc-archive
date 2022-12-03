with open('input.txt') as f:
    game_input = f.readlines()

# A, X: Rock
# B, Y: Paper
# C, Z: Scissors

left_choice = {
    'A': {'X': 'Draw', 'Y': 'Win', 'Z': 'Loss'},
    'B': {'X': 'Loss', 'Y': 'Draw', 'Z': 'Win'},
    'C': {'X': 'Win', 'Y': 'Loss', 'Z': 'Draw'}
}

right_choice = {
    'X': {'A': 'Draw', 'B': 'Loss', 'C': 'Win'},
    'Y': {'A': 'Win', 'B': 'Draw', 'C': 'Loss'},
    'Z': {'A': 'Loss', 'B': 'Win', 'C': 'Draw'}
}

def play(game, column):
    return column.get(game[2]).get(game[0])

def outcome_score(outcome):
    if outcome == "Win":
        return int(6)
    elif outcome == "Draw":
        return int(3)
    else:
        return int(0)

def choice_score(choice):
    if (choice == "A") or (choice == "X"):
        return int(1)
    elif (choice == "B") or (choice == "Y"):
        return int(2)
    elif (choice == "C") or (choice == "Z"):
        return int(3)
    else:
        return int(0)

scores = []

for i in game_input:
    outcome = play(i[:3], right_choice)
    scores.append(outcome_score(outcome)+choice_score(i[2]))

print(sum(scores))
