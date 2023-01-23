import numpy as np
import pygame

background_color = (251, 247, 245)
grid_element_colour = (50, 30, 150)
buffer = 5



grid_test = [[None, None, None, 9, None, 3, None, 5, 6], [4, None, None, 6, 8, None, 1, 2, None], [2, 6, None, None, None, 5, 3, None, None], [8, 9, None, None, 6, 4, 7, 3, 5], [None, None, None, 1, 7, None, 8, 4, 2], [None, None, None, 3, None, None, None, 6, None], [None, 2, 6, 8, None, 1, None, None, 7], [5, 1, 4, None, 9, 2, 6, None, 3], [9, 8, None, None, None, None, None, None, None]]

#print(np.matrix(grid))



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
    return True


def solve(grid, win, solved):
    myfont = pygame.font.SysFont('Comic Sans MS', 35)
    solved = 0
    for row in range(0,9):
        for col in range(0,9):
            if grid[row][col] is None:
                for number in range(1,10):
                    if possible_solution(row, col, number, grid) and solved ==0:
                        grid[row][col] = number
                        value = myfont.render(str(number), True, (0,0,0))
                        win.blit(value, ((col+1)*50 + 15,(row+1)*50 + 0))
                        pygame.display.update()
                        pygame.time.delay(25)

                        solve(grid,win, solved)
                        if(solved == 1):
                            return

                        grid[row][col] = None
                        pygame.draw.rect(win, background_color, ((col+1) * 50 + buffer, (row + 1)*50 + buffer, 50 - 2*buffer, 50 - 2*buffer))
                        pygame.display.update()
                return
    solved = 1
    
    
    
    


