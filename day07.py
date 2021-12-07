
input = open("day07_input.txt", "r").read().strip().split(',')


def part1():
    inp_list = list(map(int, input))
    costs = []
    for first in inp_list:
        cost = 0
        for second in inp_list:
            cost += abs(int(second) - int(first))

        costs.append(cost)

    print(min(costs))


def part2():
    inp_list = list(map(int, input))
    costs = []
    for first in range(max(inp_list) + 1):
        cost = 0
        for second in inp_list:
            distance = (abs(int(second) - int(first)))
            cost += (distance * (distance + 1)) // 2

        costs.append(cost)
    print(min(costs))


part1()
part2()
