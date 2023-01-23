import numpy as np
import pygame
from sudoku import Sudoku


WIDTH = 550
background_color = (251, 247, 245)
grid_element_colour = (50, 30, 150)
buffer = 5
puzzle = Sudoku(3).difficulty(0.5)
grid_board = puzzle.board
grid_orginal = [[grid_board[x][y] for y in range(len(grid_board[0]))] for x in range(len(grid_board))]



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

solved = 0
def solve(grid, win):
    myfont = pygame.font.SysFont('Comic Sans MS', 35)
    for row in range(0,9):
        for col in range(0,9):
            if grid[row][col] is None:
                for number in range(1,10):
                    if possible_solution(row, col, number, grid):
                        grid[row][col] = number
                        value = myfont.render(str(number), True, (0,0,0))
                        win.blit(value, ((col+1)*50 + 15,(row+1)*50 + 0))
                        pygame.display.update()
                        pygame.time.delay(25)

                        solve(grid,win)
                        global solved
                        if(solved == 1):
                            return

                        grid[row][col] = None
                        pygame.draw.rect(win, background_color, ((col+1) * 50 + buffer, (row + 1)*50 + buffer, 50 - 2*buffer, 50 - 2*buffer))
                        pygame.display.update()
                return
    solved = 1
    pass

def draw(win, grid):
    myfont = pygame.font.SysFont('Comic Sans MS', 35)
    for r in range(0, 9):
        for c in range(0, 9):
            if grid[r][c] is not None:
                value = myfont.render(str(grid[r][c]), True, grid_element_colour)
                win.blit(value, ((c+1)*50 + 15,(r+1)*50 + 0))
    pygame.display.update()
    return



def insert(win, position):
    r,c = position[1], position[0] #flipped when working in the backend
    myfont = pygame.font.SysFont('Comic Sans MS', 35)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                #1 tries to edit original grid
                if grid_orginal[r-1][c-1] is not None:
                    return
                #2 edit, 48 = 0 ascii
                if(event.key == 48):
                    grid_board[r-1][c-1] == event.key - 48
                    pygame.draw.rect(win, background_color, (position[0]* 50 + buffer, position[1]*50 + buffer, 50 - 2*buffer, 50 - 2*buffer))
                    pygame.display.update()
                #3 adding the digigts 
                if(0 < event.key - 48 < 10):
                    pygame.draw.rect(win, background_color, (position[0]* 50 + buffer, position[1]*50 + buffer, 50 - 2*buffer, 50 - 2*buffer))
                    value = myfont.render(str(event.key - 48), True, (0,0,0))
                    win.blit(value, (position[0]*50 + 15, position[1]*50))
                    grid_board[r-1][c-1] = event.key - 48
                    pygame.display.update()
                    return
                if(event.key == 115):# if s is pressed: solve
                    solve(grid_orginal, win)

                return

    

def main():
    pygame.init()
    win = pygame.display.set_mode((WIDTH, WIDTH))
    pygame.display.set_caption("Sudoko")
    #set background colour
    win.fill(background_color)
    myfont = pygame.font.SysFont('Comic Sans MS', 35)
    #Create grid
    for i in range(0,10):
        if(i%3 == 0):
            thickness = 4
        else:
            thickness = 2            
        pygame.draw.line(win, (0,0,0), (50 + 50*i, 50), (50 + 50*i, 500), thickness) #Vertical lines
        pygame.draw.line(win, (0,0,0), (50, 50 + 50*i), (500, 50 + 50*i), thickness) #Horizontal lines
    pygame.display.update()

    #Create number for starting grid
    draw(win,grid_board)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                pos = pygame.mouse.get_pos()
                insert(win, (pos[0]//50, pos[1]//50))
            if event.type == pygame.QUIT:
                pygame.quit()
                return

main()