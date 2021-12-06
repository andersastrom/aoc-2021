from collections import defaultdict

input = open("day06_input.txt", "r").read().strip().split(',')


def part1():
    input_list = list(map(int, input))
    cur = input_list.copy()
    new = input_list.copy()
    for i in range(80):
        cur = new.copy()
        for idx, days in enumerate(cur):
            if days == 0:
                new[idx] = 6
                new.append(8)
            elif days > 0:
                new[idx] = new[idx] - 1
    print(len(new))


def part2():
    input_list = list(map(int, input))
    days_map = defaultdict(int)
    for ints in input_list:
        for i in range(9):
            days_map[i] = input_list.count(i)

    for i in range(256):
        new_days = defaultdict(int)
        for days in days_map:
            count = days_map[days]
            if days > 0:
                new_days[days - 1] = count

        new_days[6] += days_map[0]
        new_days[8] = days_map[0]
        days_map = new_days.copy()

    print(sum(new_days.values()))


part1()
part2()
