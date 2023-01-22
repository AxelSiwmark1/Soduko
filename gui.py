import numpy as np
import pygame
import requests
from sudoku import Sudoku

WIDTH = 550
background_color = (251, 247, 245)
grid_element_colour = (50, 30, 150)
puzzle = Sudoku(3).difficulty(0.5)
grid = puzzle.board

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
            if event.type == pygame.QUIT:
                pygame.quit()
                return

main()