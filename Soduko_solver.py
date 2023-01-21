import numpy as np

grid = [[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,0,0]]

print(np.matrix(grid))



#Does number appear in row, col, or square?
def possible_solution(row, col, number, grid):

    #is it in row?
    for c in range(0,9):
        if grid[row][c] == number:
            return False
    #is it in col?
    for r in range(0,9):
        if grid[r][col] == number:
            return False
    #is it in square?
    square_row = 3 * (row // 3)
    square_col = 3 * (col // 3)
    for r in range(square_row, square_row + 3):
        for c in range(square_col, square_col + 3):
            if grid[r][c] == number:
                return False
