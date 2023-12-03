from functools import reduce


def order_results(results):
    ordered_results = {
        "red": [],
        "blue": [],
        "green": []
    }

    print("Results: ", results)
    for result in results:
        for pair in result.split(", "):
            print("Pair: ", pair)
            ordered_results[pair.split(" ")[1].rstrip()].append(int(pair.split(" ")[0]))

    print("Ordered results:", ordered_results)
    return ordered_results


def find_largest(results):
    return int(max(results))


def get_power(results):
    return reduce(lambda x, y: x*y, results)


with open("input.txt") as input:
    all_power = []
    for line in input:
        print("Line:", line)
        current_results = []
        for color, results in order_results(line.split(": ")[1].split("; ")).items():
            current_results.append(find_largest(results))
            print("Color: ", color)
            print("Current results: ", current_results)

        print("Line power: ", get_power(current_results))
        all_power.append(get_power(current_results))
        print("Current all_power: ", all_power)

    print("All power: ", all_power)
    print(sum(all_power))
