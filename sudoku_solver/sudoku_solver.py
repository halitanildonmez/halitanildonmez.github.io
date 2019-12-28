board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]


def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")
        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return i, j
    return -1, -1


# Find some empty space
# Attempt to place the digits 1-9 in that space
# Check if that digit is valid in the current spot based on the current board
# a. If the digit is valid, recursively attempt to fill the board using steps 1-3.
# b. If it is not valid, reset the square you just filled and go back to the previous step.
# Once the board is full by the definition of this algorithm we have found a solution.
# pygame to draw board
def solve_brute(bo):
    e_r, e_c = find_empty(bo)
    if e_r == -1 and e_c == -1:
        return True
    empty_row = bo[e_r]
    empty_col = [sub[e_c] for sub in bo]
    for r_c in range(1, 10):
        if r_c not in empty_row and r_c not in empty_col:
            bo[e_r][e_c] = r_c
            if solve_brute(bo):
                return True
    bo[e_r][e_c] = 0
    return False

solve_brute(board)
print_board(board)

#
