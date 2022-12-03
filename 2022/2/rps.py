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

def get_score(choice, outcome, scores):
    return scores.get('choice').get(choice, 0)+scores.get('outcome').get(outcome, 0)

final_scores = []

for i in game_input:
    choice = get_choice(i, rules, decrypt)
    outcome = get_outcome(i)
    final_scores.append(get_score(choice, outcome, scores))

print(sum(final_scores))
