def NAQD():
    position = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

    if not solve(position, 0):
        print("Not possible")
        return False

    for i in range(4):
        for j in range(4):
            print(position[i][j])
        print()
    return True


def secure(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, 4, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve(board, col):

    for i in range(4):
        if secure(board, i, col):
            board[i][col] = 1

            if not solve(board, col + 1):
                return True

            board[i][col] = 0

    return False

NAQD()
