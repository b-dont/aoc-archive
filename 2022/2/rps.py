with open('input.txt') as f:
    game_input = f.readlines()

# A: Rock     | X: Loss
# B: Paper    | Y: Draw
# C: Scissors | Z: Win

rules = {
    'A': {'A': 'Draw', 'C': 'Win', 'B': 'Loss'},
    'B': {'B': 'Draw', 'A': 'Win', 'C': 'Loss'},
    'C': {'C': 'Draw', 'B': 'Win', 'A': 'Loss'},
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

def get_choice(game, decrypt):
    return decrypt[game[2]][game[0]]

def get_outcome(game, choice, rules):
    return rules[game[0]][choice]

def get_score(choice, outcome, scores):
    return scores['choice'][choice]+scores['outcome'][outcome]

final_scores = []

for i in game_input:
    choice = get_choice(i, decrypt)
    outcome = get_outcome(i, choice, rules)
    final_scores.append(get_score(choice, outcome, scores))

print(sum(final_scores))
