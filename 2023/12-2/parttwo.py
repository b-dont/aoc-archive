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
            ordered_results[pair.split(" ")[1].rstrip()].append(int(pair.split(" ")[0]))

    return ordered_results


def find_largest(results):
    return int(max(results))


def get_power(results):
    return reduce(lambda x, y: x*y, results)


with open("input.txt") as input:
    all_power = []
    for line in input:
        current_results = []
        for color, results in order_results(line.split(": ")[1].split("; ")).items():
            current_results.append(find_largest(results))

        all_power.append(get_power(current_results))

    print(sum(all_power))
