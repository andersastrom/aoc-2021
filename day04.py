input = open("day04_input.txt", "r").read().strip().split('\n\n')
nrs = list(map(int, input[0].split(',')))
boards = input[1::]


def part1():
    board_res = dict()
    for board_nr, board in enumerate(boards):
        board_res[board_nr] = dict()
        for i in range(5):
            board_res[board_nr][i] = 0

    called_nrs = set()
    for nr in nrs:
        called_nrs.append(nr)
        for board_nr, board in enumerate(boards):
            for row_nr, row in enumerate(board.split('\n')):
                row = row.replace('  ', ' ').split(' ')
                row = [x for x in row if x]
                int_row = list(map(int, row))
                if nr in int_row:
                    board_res[board_nr][row_nr] += 1

        for board_nr, board in enumerate(board_res):
            for row in board_res[board]:
                for i in range(5):
                    if board_res[board][row] == 5:
                        calc_score(boards[board_nr], board_res[board_nr], nr, called_nrs)
                        return


def part2():
    won = set()
    board_res_row = dict()
    board_res_col = dict()
    for board_nr, board in enumerate(boards):
        board_res_row[board_nr] = dict()
        board_res_col[board_nr] = dict()
        for i in range(5):
            board_res_row[board_nr][i] = 0
            board_res_col[board_nr][i] = 0

    called_nrs = set()
    col_board = []
    for nr in nrs:
        called_nrs.append(nr)
        for board_nr, board in enumerate(boards):
            col_board = [b.strip().replace('  ', ' ').split(' ') for b in board.replace('\n ', '\n').split('\n')]
            col_board = list(zip(*col_board[::-1]))
            for row_nr, row in enumerate(board.split('\n')):
                row = row.replace('  ', ' ').split(' ')
                row = list(map(int, [x for x in row if x]))
                if nr in row:
                    board_res_row[board_nr][row_nr] += 1

            for col_nr, col in enumerate(col_board):
                col = list(map(int, col))
                if nr in col:
                    board_res_col[board_nr][col_nr] += 1

        for board_nr, board in enumerate(board_res_row):
            for row in board_res_row[board]:
                for i in range(5):
                    if board_res_row[board][row] == 5:
                        won.add(board_nr)
                        if len(won) == 100:
                            calc_score(boards[board_nr], board_res_row[board_nr], nr, called_nrs)
                            return

        for board_nr in board_res_col:
            for col in board_res_col[board_nr]:
                for i in range(5):
                    if board_res_col[board_nr][col] == 5:
                        won.add(board_nr)
                        if len(won) == 100:
                            calc_score(boards[board_nr], board_res_col[board_nr], nr, called_nrs)
                            return


def calc_score(board, board_res, final_num, called):
    score = 0
    for row in board.strip().split('\n'):
        for tile_nr, tile in enumerate(row.strip().replace('  ', ' ').split(' ')):
            if int(tile) not in called:
                score += int(tile)
    print(score * int(final_num))


part1()
part2()
