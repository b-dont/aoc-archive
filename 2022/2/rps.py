with open('input.txt') as f:
    game_input = f.readlines()

# A: Rock     | X: Loss
# B: Paper    | Y: Draw
# C: Scissors | Z: Win

decrypt = {
    'X': {'A': 'C', 'B': 'A', 'C': 'B'},
    'Y': {'A': 'A', 'B': 'B', 'C': 'C'},
    'Z': {'A': 'B', 'B': 'C', 'C': 'A'},
}

scores = {
    'choice': {'A': 1, 'B': 2, 'C': 3},
    'outcome': {'Z': 6, 'Y': 3, 'X': 0}
}

def get_choice(game, decrypt):
    return decrypt[game[2]][game[0]]

def get_score(choice, outcome, scores):
    return scores['choice'][choice]+scores['outcome'][outcome]

final_scores = []

for i in game_input:
    choice = get_choice(i, decrypt)
    final_scores.append(get_score(choice, i[2], scores))

print(sum(final_scores))
