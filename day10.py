from statistics import median

input = open("day10_input.txt", "r").read().strip().split('\n')


pairs = {"[": "]", "(": ")", "{": "}", "<": ">"}


def part1():
    scoring = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137,
    }

    invalids = []
    for idx, line in enumerate(input):
        starts = []
        for c in line:
            if c in pairs:
                starts.append(c)
            elif c != pairs[starts.pop()]:
                invalids.append(c)
                break
    print(sum([scoring[i] for i in invalids]))


def part2():
    scoring = {")": 1,
               "]": 2,
               "}": 3,
               ">": 4
               }
    scores = []
    for idx, line in enumerate(input):
        starts = []
        for c in line:
            if c in pairs:
                starts.append(c)
            elif c != pairs[starts.pop()]:
                break
        else:
            if starts:
                total_score = 0
                for c in starts[::-1]:
                    total_score = (total_score * 5) + scoring[pairs[c]]
                scores.append(total_score)
    print(median(scores))


part1()
part2()
