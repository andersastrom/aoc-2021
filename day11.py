from utils import FiniteGrid

input = open("day11_input.txt", "r").read().strip()


def part1():
    grid: FiniteGrid[int] = FiniteGrid.of_str(input, default='-1').map_values(int)

    total_flashes = 0
    for i in range(100):
        flashed = []
        for octo in grid.locations():
            if grid[octo] == 9:
                grid[octo] = 0
                flashed.append(octo)
                total_flashes += 1
            elif grid[octo] >= 0:
                grid[octo] += 1

        while flashed:
            octo = flashed.pop()
            for neighboor in octo.moore_neighbors():
                if grid[neighboor] == -1:
                    continue

                if grid[neighboor] == 9:
                    grid[neighboor] = 0
                    flashed.append(neighboor)
                    total_flashes += 1
                elif grid[neighboor] > 0:
                    grid[neighboor] += 1
    print(total_flashes)


def part2():
    grid: FiniteGrid[int] = FiniteGrid.of_str(input, default='-1').map_values(int)

    it = 1
    while True:
        flashed = []
        for octo in grid.locations():
            if grid[octo] == 9:
                grid[octo] = 0
                flashed.append(octo)
            elif grid[octo] >= 0:
                grid[octo] += 1

        while flashed:
            octo = flashed.pop()
            for neighboor in octo.moore_neighbors():
                if grid[neighboor] == -1:
                    continue

                if grid[neighboor] == 9:
                    grid[neighboor] = 0
                    flashed.append(neighboor)
                elif grid[neighboor] > 0:
                    grid[neighboor] += 1

        if sum([grid[octo] for octo in grid.locations()]) == 0:
            print(it)
            return
        it += 1


part1()
part2()
