
input = open("day08_input.txt", "r").read().strip().split('\n')


def part1():
    lens = {2, 3, 4, 7}
    res = 0
    for idx, line in enumerate(input):
        inp = line.split(' | ')[1]
        for cur in inp.split(' '):
            if len(cur) in lens:
                res += 1
    print(res)


def part2():
    res = 0
    for idx, line in enumerate(input):
        sec_res = []
        segs = dict()
        inp, out = line.split(' | ')
        inp = inp.split(' ')
        for i in inp:
            if len(i) == 2:
                segs[1] = i
            elif len(i) == 3:
                segs[7] = i
            elif len(i) == 4:
                segs[4] = i
            elif len(i) == 7:
                segs[8] = i

        for i in inp:
            if len(i) == 6:
                if len(set(i) - set(segs[7])) == 4:
                    segs[6] = i
                elif len(set(i) - set(segs[4])) == 2:
                    segs[9] = i
                else:
                    segs[0] = i
            elif len(i) == 5:
                if len(set(i) - set(segs[7])) == 2:
                    segs[3] = i
                elif len(set(i) - set(segs[4])) == 3:
                    segs[2] = i
                elif len(set(i) - set(segs[4])) == 2:
                    segs[5] = i

        for o in out.split(' '):
            for i in segs:
                if set(o) == set(segs[i]):
                    sec_res.append(str(i))

        res += int("".join(sec_res))
    print(res)


part1()
part2()
