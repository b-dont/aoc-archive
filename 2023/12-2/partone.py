RED = 12
GREEN = 13
BLUE = 14


def get_id(game):
    return int(game.split(": ")[0].split(" ")[1])


def get_results(line):
    return line.split(": ")[1].split("; ")


def checkif_possible(pair):
    is_possible = True
    quant = int(pair[0])

    match pair[1].rstrip():
        case "red":
            if quant > RED:
                is_possible = False
        case "green":
            if quant > GREEN:
                is_possible = False
        case "blue":
            if quant > BLUE:
                is_possible = False
        case _:
            raise ValueError("Not a color")

    return is_possible


with open("input.txt") as input:
    all_games = []
    for line in input:
        results = get_results(line)
        game_is_possible = True
        print("Results are: ", results)
        for result in results:
            print("Result is: ", result)
            for pair in result.split(", "):
                print("Pairs are: ", pair)
                if not checkif_possible(pair.split(" ")):
                    game_is_possible = False
                    break

        if game_is_possible:
            all_games.append(get_id(line))

    print(sum(all_games))
