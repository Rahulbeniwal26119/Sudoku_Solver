# Rules
# No number should repeat in line
# No number should repeat in column
# no number should repeat in corresponding square
# Valid numbers are 1-9

sudoku = [
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 3, 6, 0, 0, 0, 0, 0],
    [0, 7, 0, 0, 9, 0, 2, 0, 0],
    [0, 5, 0, 0, 0, 7, 0, 0, 0],
    [0, 0, 0, 0, 4, 5, 7, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 3, 0],
    [0, 0, 1, 0, 0, 0, 0, 6, 8],
    [0, 0, 8, 5, 0, 0, 0, 1, 0],
    [0, 9, 0, 0, 0, 0, 4, 0, 0]
]


def solve(board):
    find = find_zero(board)
    if not find:
        return True
    else:
        row, column = find

    for i in range(1, 10):
        if valid(board, i, (row, column)):
            board[row][column] = i

            if solve(board):  # backtracking if number is not valid then board[row][column] will set that value to 0
                return True
            board[row][column] = 0


def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print('-----------------------')
        for j in range(len(board)):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


def find_zero(board):  # finding the next empty slot
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                return i, j  # returning row and column


def valid(board, num, pos):  # checking if a number is valid
    for i in range(len(board)):
        if board[pos[0]][i] == num and pos[1] != i:  # checking for row
            return False
    for i in range(len(board)):  # checking for column
        if board[i][pos[1]] == num and pos[0] != i:
            return False
    box_x = pos[0] // 3
    box_y = pos[1] // 3

    for i in range(box_x * 3, box_x * 3 + 3):  # checking in the square
        for j in range(box_y * 3, box_y * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False
    return True


print_board(sudoku)
solve(sudoku)
print()
print_board(sudoku)
