import numpy as np
import pygame
from sudoku import Sudoku

WIDTH = 550
background_color = (251, 247, 245)
grid_element_colour = (50, 30, 150)
buffer = 5
puzzle = Sudoku(3).difficulty(0.5)
grid = puzzle.board
grid_orginal = [[grid[x][y] for y in range(len(grid[0]))] for x in range(len(grid))]

def insert(win, position):
    r,c = position[1], position[0] #flipped when working in the backend
    myfont = pygame.font.SysFont('Comic Sans MS', 35)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                #1 tries to edit original grid
                if grid[r-1][c-1] is not None:
                    return
                #2 edit, 48 = 0 ascii
                if(event.key == 48):
                    grid[r-1][c-1] == event.key - 48
                    pygame.draw.rect(win, background_color, (position[0]* 50 + buffer, position[1]*50 + buffer, 50 - 2*buffer, 50 - 2*buffer))
                    pygame.display.update()
                #3 adding the digigts 
                if(0 < event.key - 48 < 10):
                    pygame.draw.rect(win, background_color, (position[0]* 50 + buffer, position[1]*50 + buffer, 50 - 2*buffer, 50 - 2*buffer))
                    value = myfont.render(str(event.key - 48), True, (0,0,0))
                    win.blit(value, (position[0]*50 + 15, position[1]*50))
                    grid[r-1][c-1] = event.key - 48
                    pygame.display.update()
                    return
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
    for r in range(0, len(grid[0])):
        for c in range(0, len(grid[0])):
            if grid[r][c] is not None:
                value = myfont.render(str(grid[r][c]), True, grid_element_colour)
                win.blit(value, ((c+1)*50 + 15,(r+1)*50 + 0))
    pygame.display.update()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                pos = pygame.mouse.get_pos()
                insert(win, (pos[0]//50, pos[1]//50))
            if event.type == pygame.QUIT:
                pygame.quit()
                return

main()