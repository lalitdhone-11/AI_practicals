def is_safe(board, row, col, n):
    # Check column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check left diagonal
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check right diagonal
    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solve(board, row, n):
    # If solution found
    if row == n:
        for i in range(n):
            for j in range(n):
                if board[i][j] == 1:
                    print(j + 1, end=" ")
        print()
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1      # place queen
            solve(board, row + 1, n)
            board[row][col] = 0      # backtrack


# Driver code
n = 4
board = [[0]*n for _ in range(n)]

solve(board, 0, n)