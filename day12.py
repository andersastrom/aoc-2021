import string
from collections import defaultdict

input = open("day12_input.txt", "r").read().strip().split('\n')
lowers = list(string.ascii_lowercase)


class Total:
    def __init__(self):
        self.total_paths = 0

    def increment(self):
        self.total_paths += 1

    def __str__(self):
        return str(self.total_paths)


def part1():
    connection_map = defaultdict(list)
    for line in input:
        fro, to = line.split('-')
        connection_map[fro].append(to)
        connection_map[to].append(fro)

    total = Total()

    def traverse(current_node: str, path: list, visited: set, total: Total):
        connections = connection_map[current_node]
        for next_node in connections:
            is_small_cave = all(c in lowers for c in list(next_node))
            if (next_node in visited and is_small_cave) or next_node == "start":
                continue

            if next_node == "end":
                total.increment()
                continue

            new_path = path.copy()
            new_path.append(current_node)
            new_visited = visited.copy()
            new_visited.add(current_node)
            traverse(next_node, new_path, new_visited, total)

    traverse("start", [], set(), total)
    print(total)


def part2():
    connection_map = defaultdict(list)
    for line in input:
        fro, to = line.split('-')
        connection_map[fro].append(to)
        connection_map[to].append(fro)

    total = Total()

    def traverse(
            current_node: str,
            path: list,
            visited: set,
            total: Total,
            small_visited_twice: bool
    ):
        connections = connection_map[current_node]
        for next_node in connections:
            if not small_visited_twice:
                is_current_small_cave = all(c in lowers for c in list(current_node))
                small_visited_twice = is_current_small_cave and current_node in visited

            is_small_cave = all(c in lowers for c in list(next_node))
            if (next_node in visited and is_small_cave and small_visited_twice) or next_node == "start":
                continue

            if next_node == "end":
                total.increment()
                continue

            new_path = path.copy()
            new_path.append(current_node)
            new_visited = visited.copy()
            new_visited.add(current_node)
            traverse(next_node, new_path, new_visited, total, small_visited_twice)

    traverse("start", [], set(), total, False)
    print(total)


part1()
part2()
