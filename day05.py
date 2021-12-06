
input = open("day05_input.txt", "r").read().strip().split('\n')


def part1():
    covered = dict()
    for line in input:
        first, sec = line.split(' -> ')
        x1, y1 = map(int, first.split(','))
        x2, y2 = map(int, sec.split(','))
        if (x1 == x2):
            maxn = max(y2, y1)
            minn = min(y2, y1)
            for num in range(minn, (maxn + 1)):
                coordinate = (x1, num)
                if coordinate in covered:
                    covered[coordinate] = covered[(x1, num)] + 1
                else:
                    covered[coordinate] = 1
        elif (y1 == y2):
            maxn = max(x2, x1)
            minn = min(x2, x1)
            for num in range(minn, (maxn + 1)):
                coordinate = (num, y1)
                if coordinate in covered:
                    covered[coordinate] = covered[coordinate] + 1
                else:
                    covered[coordinate] = 1

    count = 0
    for cov in covered:
        if covered[cov] > 1:
            count += 1
    print(count)


def part2():
    covered = dict()
    for line in input:
        first, sec = line.split(' -> ')
        x1, y1 = map(int, first.split(','))
        x2, y2 = map(int, sec.split(','))
        if (x1 == x2):
            maxn = max(y2, y1)
            minn = min(y2, y1)
            for num in range(minn, (maxn + 1)):
                if (x1, num) in covered:
                    covered[(x1, num)] = covered[(x1, num)] + 1
                else:
                    covered[(x1, num)] = 1

        elif (y1 == y2):
            maxn = max(x2, x1)
            minn = min(x2, x1)
            for num in range(minn, (maxn + 1)):
                if (num, y1) in covered:
                    covered[(num, y1)] = covered[(num, y1)] + 1
                else:
                    covered[(num, y1)] = 1

        elif abs(x2 - x1) == abs(y2 - y1):
            max_x = max(x2, x1)
            min_x = min(x2, x1)
            max_y = max(y2, y1)
            min_y = min(y2, y1)
            i = 0

            for num in range(min_x, (max_x + 1)):
                if (y1 < y2):
                    y = min_y + i
                else:
                    y = max_y - i

                if (x1 < x2):
                    x = min_x + i
                else:
                    x = max_x - i
                coordinate = (x, y)

                if coordinate in covered:
                    covered[coordinate] = covered[coordinate] + 1
                else:
                    covered[coordinate] = 1
                i += 1

    count = 0
    for cov in covered:
        if covered[cov] > 1:
            count += 1
    print(count)


part1()
part2()
