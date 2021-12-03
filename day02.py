input = open("day02_input.txt", "r").read().strip().split('\n')
dep_map = {"up": -1, "down": 1}


def part1():
    hor = 0
    dep = 0
    for line in input:
        inst, val = line.split()
        val = int(val)
        if inst == "forward":
            hor += val
        else:
            dep += dep_map[inst] * val
    print(hor * dep)


def part2():
    aim = 0
    hor = 0
    dep = 0
    for line in input:
        inst, val = line.split(' ')
        val = int(val)

        if inst == "forward":
            hor += val
            dep += aim * val
        else:
            aim += dep_map[inst] * val

    print(dep * hor)


part1()
part2()
