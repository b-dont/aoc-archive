with open('input.txt') as f:
    game_input = f.readlines()

# A, X: Rock
# B, Y: Paper
# C, Z: Scissors
def play(game):
    match game:
        case "A Y":
            return str("Win")
        case "A X":
            return str("Draw")
        case "A Z":
            return str("Loss")
        case "B Y":
            return str("Draw")
        case "B X":
            return str("Win")
        case "B Z":
            return str("Loss")
        case "C Y":
            return str("Loss")
        case "C X":
            return str("Win")
        case "C Z":
            return str("Draw")

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
    outcome = play(i[0:3])
    scores.append(outcome_score(outcome))
    scores.append(choice_score(i[2]))

print(sum(scores))
