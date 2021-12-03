input = list(map(int, open("day01_input.txt", "r").read().split()))


def part1():
    count = 0
    for i, value in enumerate(input):
        if i == len(input) - 1:
            print("Part 1: {}".format(count))
            return

        if input[i + 1] > value:
            count += 1


def part2():
    sum = 0
    prev_sum = 0
    count = 0
    for i, value in enumerate(input):
        if i == len(input) - 2:
            print("Part 2: {}".format(count))
            return

        prev_sum = sum
        sum = value + input[i + 1] + input[i + 2]
        if prev_sum == 0:
            continue

        if sum > prev_sum:
            count += 1


part1()
part2()
