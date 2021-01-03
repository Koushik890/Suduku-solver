board = [
    [3,0,0,8,0,1,0,0,2],
    [2,0,1,0,3,0,6,0,4],
    [0,0,0,2,0,4,0,0,0],
    [8,0,9,0,0,0,1,0,6],
    [0,6,0,0,0,0,0,5,0],
    [7,0,2,0,0,0,4,0,9],
    [0,0,0,5,0,9,0,0,0],
    [9,0,4,0,8,0,7,0,5],
    [6,0,0,1,0,7,0,0,3]
]

def print_board(brd):
    for i in range(len(brd)):
        if i % 3 == 0 and i != 0:
            print(" --------------------------- ")

        for j in range(len(brd[i])):
            if j % 3 == 0:
                print(" | ", end="")
                
            if j == 8:
                print(str(brd[i][j]) + " | ")

            else:
                print(str(brd[i][j]) + " ", end="")


# print_board(board)

def find_empty(brd):
    
    for i in range(len(brd)):
        for j in range(len(brd[i])):
            if brd[i][j] == 0:
                return (i, j)


def is_valid(brd, value, pos):
    
    #checking all the row with the current row or current y value
    for i in range(len(brd[0])):
        if brd[pos[0]][i] == value and pos[1] != i:
            return False

    #checking all the column with the current column or current x value
    for i in range(len(brd)):
        if brd[i][pos[1]] == value and pos[0] != i:
            return False

    # checking all the square boxes
    box_y = (pos[0] // 3) * 3
    box_x = (pos[1] // 3) * 3

    for i in range(box_y, box_y + 3):
        for j in range(box_x, box_x + 3):
            if brd[i][j] == value and (i, j) != pos:
                return False

    return True


def solve_sudoku(brd):
    
    find = find_empty(brd)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if is_valid(brd, i, (row, col)):
            brd[row][col] = i

            if solve_sudoku(brd):
                return True

            brd[row][col] = 0

    return False


print_board(board)
solve_sudoku(board)
print( "\n")
print("*****************************SOLVED SUDOKU*************************************")
print("\n")
print_board(board)