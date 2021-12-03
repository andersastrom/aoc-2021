input = open("day03_input.txt", "r").read().strip().split('\n')


def part1():
    gamma = []
    eps = []
    for bit in range(12):
        col = []
        for line in input:
            col.append(int(line[bit]))
        most_common = int(col.count(1) >= col.count(0))
        gamma.append(most_common)
        eps.append(most_common ^ 1)

    print(int("".join(str(x) for x in gamma), 2) * int("".join(str(x) for x in eps), 2))


def part2():
    oxygen = input.copy()
    co2 = input.copy()

    bit = 0
    while len(oxygen) > 1:
        col = []
        for line in oxygen:
            col.append(int(line[bit]))
        most_common = int(col.count(1) >= col.count(0))

        for line in oxygen[:]:
            if int(line[bit]) != most_common:
                oxygen.remove(line)
        bit += 1

    bit = 0
    while len(co2) > 1:
        col = []
        least_com = 1
        for line in co2:
            col.append(int(line[bit]))
        if col.count(0) <= col.count(1):
            least_com = 0

        for line in co2[:]:
            if int(line[bit]) != least_com:
                co2.remove(line)
        bit += 1

    res = int("".join(x for x in oxygen[0]), 2) * int("".join(x for x in co2[0]), 2)
    print(res)


part1()
part2()
