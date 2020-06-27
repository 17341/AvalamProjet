import pygame

# Initialisation : 
pygame.init()
# Constantes : 
BOARD = {"0":[6,7],"1":[4,5,6,7],"2":[2,3,4,5,6,7],"3":[0,1,2,3,4,5,6,7],"4":[0,1,2,3,4,5,6,7,8],"5":[1,2,3,4,5,6,7,8],"6":[1,2,3,4,5,6],"7":[1,2,3,4],"8":[2,3]}
COLORS = {"BLACK" : (0, 0, 0), "WHITE" : (255, 255, 255), "GREEN":(0, 255, 0),"RED" :(255, 0, 0),"YELLOW":(255,255,0)}
WIDTH = 50
HEIGHT = 50
SPACE = 10
RADIUS = 25
GRID = [[0 for x in range(9)] for y in range(9)]
WINDOW_SIZE = [HEIGHT*len(GRID)+(SPACE*(len(GRID)+1)),len(GRID)*WIDTH+(SPACE*(len(GRID)+1))]
FONT = pygame.font.SysFont('comicsans', 40)
# Setup : 
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Avalam")
clock = pygame.time.Clock()
FPS = 60
move = {}
for row in range(9):
    for column in range(9):
        move[row,column] = []
run = True

class Avalam_Game():
    def __init__(self):
        pass
                
    def draw_pawn():  
        screen.fill(COLORS["BLACK"])
        for row in BOARD.keys() :
            for column in BOARD[row]: 
                pos2 =  int(row)*(HEIGHT + SPACE)
                pos1 =  int(column)*(WIDTH + SPACE)
                if int(row) % 2 != 0 and int(column) % 2 == 0 or int(row) % 2 == 0 and int(column) % 2 != 0:
                    pygame.draw.circle(screen,COLORS["RED"],(pos1+(int(RADIUS+SPACE)),pos2+(int(RADIUS+SPACE))), int(RADIUS), int(RADIUS))
                else:
                    pygame.draw.circle(screen,COLORS["YELLOW"],(pos1+(int(RADIUS+SPACE)),pos2+(int(RADIUS+SPACE))), int(RADIUS), int(RADIUS))

        pygame.display.update()

while run :
    clock.tick(60)
    Avalam_Game.draw_pawn()
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            run = False  
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            column = pos[0] // (WIDTH + SPACE)
            row = pos[1] // (HEIGHT + SPACE)
            move[row,column].append(1)
    pygame.display.flip()


 