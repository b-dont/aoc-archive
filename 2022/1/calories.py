# Puzzle input 
with open('input.txt') as f:
    calories = f.readlines()

total_cals = [] 
current_cals = 0

for i in calories:
    try:
        if i != "\n":
            current_cals += int(i)
        elif i == "\n":
            total_cals.append(current_cals)
            current_cals = 0
    except IndexError:
        break

total_cals.sort(reverse=True)
top_three = 0

for i in range(0, 3):
    top_three += total_cals[i]

print(top_three)
