import pygame
 
pygame.init()
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255,255,0)

WIDTH = 50
HEIGHT = 50

SPACE = 10

grid = [[0 for x in range(9)] for y in range(9)]
move = {}
for row in range(9) :
    for column in range(9) : 
        move[row,column] = []

WINDOW_SIZE = [HEIGHT*len(grid)+(SPACE*(len(grid)+1)),len(grid)*WIDTH+(SPACE*(len(grid)+1))]
screen = pygame.display.set_mode(WINDOW_SIZE)

pygame.display.set_caption("Avalam")

run = True

clock = pygame.time.Clock()

while run :
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            run = False  
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            column = pos[0] // (WIDTH + SPACE)
            row = pos[1] // (HEIGHT + SPACE)
            move[row,column].append(1)
            print(move)
            print("Click ", pos, "Grid coordinates: ", row, column)
 
    background_image = pygame.image.load("Sans titre.png").convert()
    screen.blit(background_image, [0,0])

    for row in range(9):
        for column in range(9):
            taille = [(SPACE + WIDTH) * column + SPACE,(SPACE + HEIGHT) * row + SPACE,WIDTH,HEIGHT]
            color = BLACK
            if row == 0 and column in [6,7]:
                pygame.draw.rect(screen,color,taille,1)
            if row == 1 and column not in [0,1,2,3,8]:
                pygame.draw.rect(screen,color,taille,1)
            if row == 2 and column not in [0,1,8]:
                pygame.draw.rect(screen,color,taille,1)
            if row == 3 and column != 8:
                pygame.draw.rect(screen,color,taille,1)
            if row == 4 :
                pygame.draw.rect(screen,color,taille,1)
            if row == 5 and column !=  0:
                pygame.draw.rect(screen,color,taille,1)
            if row == 6 and column not in [0,7,8]:
                pygame.draw.rect(screen,color,taille,1)
            if row == 7 and column not in [0,5,6,7,8]:
                pygame.draw.rect(screen,color,taille,1)
            if row == 8 and column in [2,3]:
                pygame.draw.rect(screen,color,taille,1)
           
    clock.tick(60)

    pygame.display.flip()

pygame.quit()