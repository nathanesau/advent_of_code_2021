def mark_board(board, e):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == e:
                board[i][j] = None

def is_solved(board):
    for i in range(len(board)): # row
        rc = 0
        for j in range(len(board[0])):
            if not board[i][j]: rc += 1
        if rc == len(board[0]):
            return True
    for j in range(len(board[0])): # col
        cc = 0
        for i in range(len(board)):
            if board[i][j] == None: cc += 1
        if cc == len(board):
            return True
    return False

def calculate_score(board):
    s = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]:
                s += board[i][j]
    return s

def score(order, boards, n):
    winners = set()
    for e in order:
        for index, board in enumerate(boards):
            if index in winners:
                continue
            mark_board(board, e)
            if is_solved(board):
                winners.add(index)
                if len(winners) == n:
                    return calculate_score(board) * e
    return None

def part1(order, boards):
    ans = score(order, boards, 1)
    print(ans)

def part2(order, boards):
    ans = score(order, boards, len(boards))
    print(ans)

with open("aoc2021_day04.txt") as f:
    data = f.read()
    lines = data.splitlines()
    order = [int(e) for e in lines[0].split(',')]
    boards = []
    board = []
    for line in lines[2:]:
        if not line:
            boards.append(board)
            board = []
            continue
        row = [int(e.strip()) for e in line.split(' ') if e.strip()]
        board.append(row)
    boards.append(board)

print("day04")
part1(order, boards)
part2(order, boards)
