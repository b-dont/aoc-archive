with open('input.txt') as f:
    game_input = f.readlines()

# A: Rock     | X: Loss
# B: Paper    | Y: Draw
# C: Scissors | Z: Win

rules = {
    'A': {'Draw': 'A', 'Win': 'C', 'Loss': 'B'},
    'B': {'Draw': 'B', 'Win': 'A', 'Loss': 'C'},
    'C': {'Draw': 'C', 'Win': 'B', 'Loss': 'A'},
}

decrypt = {
    'X': {'A': 'C', 'B': 'A', 'C': 'B'},
    'Y': {'A': 'A', 'B': 'B', 'C': 'C'},
    'Z': {'A': 'B', 'B': 'C', 'C': 'A'},
}

scores = {
    'choice': {'A': 1, 'B': 2, 'C': 3},
    'outcome': {'Win': 6, 'Draw': 3, 'Loss': 0}
}

def get_choice(game, rules, decrypt):
    return str(decrypt.get(game[2]).get(game[0]))

def get_outcome(game):
    return str(game[2])

def get_score(outcome, choice, scores):
    outcome_score = int(scores.get('outcome').get(str(outcome)))
    choice_score = int(scores.get('choice').get(str(choice)))

    return outcome_score+choice_score

final_scores = []

for i in game_input:
    choice = get_choice(i, rules, decrypt)
    outcome = get_outcome(i)
    final_scores.append(get_score(outcome, choice, scores))

print(sum(final_scores))
