'N-Queens (Backtracking)'
n = 4
board = [["."]*n for _ in range(n)]

cols = set()
diag1 = set()
diag2 = set()

def backtrack(r):
    if r == n:
        for row in board:
            print(" ".join(row))
        print()
        return

    for c in range(n):
        if c in cols or (r-c) in diag1 or (r+c) in diag2:
            continue

        cols.add(c)
        diag1.add(r-c)
        diag2.add(r+c)
        board[r][c] = "Q"

        backtrack(r+1)

        cols.remove(c)
        diag1.remove(r-c)
        diag2.remove(r+c)
        board[r][c] = "."

backtrack(0)