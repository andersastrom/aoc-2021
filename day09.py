from collections import Counter

input = open("day09_input.txt", "r").read().strip().split('\n')


def part1():
    len_x = len(input[0])
    len_y = len(input)

    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    adjs = []
    coords = set()
    for y_i, line in enumerate(input):
        for x_i, num in enumerate(line):
            coords.add((x_i, y_i))

    for coord in coords:
        x_i = coord[0]
        y_i = coord[1]
        num = input[y_i][x_i]
        check = []
        for d in dirs:
            x_adj = x_i + d[0]
            y_adj = y_i + d[1]
            if (x_adj >= 0) and (y_adj >= 0) and (x_adj < len_x) and (y_adj < len_y):
                if int(num) < int(input[y_adj][x_adj]):
                    check.append(1)
                else:
                    check.append(0)
        if all(check):
            adjs.append(int(num))

    print(sum(adjs) + len(adjs))


def part2():
    len_x = len(input[0])
    len_y = len(input)

    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    coords = set()
    for y_i, line in enumerate(input):
        for x_i, _ in enumerate(line):
            coords.add((x_i, y_i))

    basins = Counter()
    for x, y in coords:
        if int(input[y][x]) != 9:
            while True:
                for d in dirs:
                    x_adj = x + d[0]
                    y_adj = y + d[1]
                    if (x_adj >= 0) and (y_adj >= 0) and (x_adj < len_x) and (y_adj < len_y):
                        if input[y_adj][x_adj] < input[y][x]:
                            x += d[0]
                            y += d[1]
                            break
                else:
                    basins[x, y] += 1
                    break
    first, second, third = basins.most_common(3)
    print(first[1] * second[1] * third[1])


part1()
part2()
