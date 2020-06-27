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
body = [[[] for x in range(9)]for y in range(9)]
for row in range(9):
    for column in range(9):
        move[row,column] = []

run = True

class Avalam_Game:
    
    def __init__(self):
        pass

    def draw_board(self):   
        screen.fill(COLORS["BLACK"])
        for row in BOARD.keys() :
            for column in BOARD[row]: 
                pos2 =  int(row)*(HEIGHT + SPACE)
                pos1 =  int(column)*(WIDTH + SPACE)
                if int(row) % 2 != 0 and int(column) % 2 == 0 or int(row) % 2 == 0 and int(column) % 2 != 0:
                    pygame.draw.circle(screen,COLORS["RED"],(pos1+(int(RADIUS+SPACE)),pos2+(int(RADIUS+SPACE))), int(RADIUS), int(RADIUS))
                    body[int(row)][int(column)] =  [1]
                else:
                    pygame.draw.circle(screen,COLORS["YELLOW"],(pos1+(int(RADIUS+SPACE)),pos2+(int(RADIUS+SPACE))), int(RADIUS), int(RADIUS))
                    body[int(row)][int(column)] = [0]
        pygame.display.update()

    def pawn_position(self):
        self.position = []
        self.coup_possible = {}
        self.liste = body      
        for l in range(9):              
            for c in range(9):          
                if len(self.liste[l][c]) < 5 and len(self.liste[l][c]) != 0:
                    self.position.append([l,c])
                    self.coup_possible[l,c] = []
        return(self.position)

    def can_move(self,pawn): 
        for f in self.position:      
            l = f[0]                 
            c = f[1]           
            if c < 8 and len(self.liste[l][c+1]) < 5 and len(self.liste[l][c+1]) != 0 : 
                if (len(self.liste[l][c]) + len(self.liste[l][c+1])) <= 5 : 
                    self.coup_possible[l,c].append([l,c+1])
            if c > 0 and len(self.liste[l][c-1]) < 5 and len(self.liste[l][c-1]) != 0 : 
                if (len(self.liste[l][c]) + len(self.liste[l][c-1])) <= 5 :     
                    self.coup_possible[l,c].append([l,c-1])
            if l < 8 and len(self.liste[l+1][c]) < 5 and len(self.liste[l+1][c]) != 0 : 
                if (len(self.liste[l][c]) + len(self.liste[l+1][c])) <= 5 :     
                    self.coup_possible[l,c].append([l+1,c])
            if l > 0 and len(self.liste[l-1][c]) < 5 and len(self.liste[l-1][c]) != 0 : 
                if (len(self.liste[l][c]) + len(self.liste[l-1][c])) <= 5 :     
                    self.coup_possible[l,c].append([l-1,c])
            if l > 0  and c > 0 and len(self.liste[l-1][c-1]) < 5 and len(self.liste[l-1][c-1]) != 0 : 
                if (len(self.liste[l][c]) + len(self.liste[l-1][c-1])) <= 5 :     
                    self.coup_possible[l,c].append([l-1,c-1])
            if l > 0 and c < 8 and len(self.liste[l-1][c+1]) < 5 and len(self.liste[l-1][c+1]) != 0 : 
                if (len(self.liste[l][c]) + len(self.liste[l-1][c+1])) <= 5 :     
                    self.coup_possible[l,c].append([l-1,c+1])
            if l < 8 and c > 0  and len(self.liste[l+1][c-1]) < 5 and len(self.liste[l+1][c-1]) != 0 : 
                if (len(self.liste[l][c]) + len(self.liste[l+1][c-1])) <= 5 :     
                    self.coup_possible[l,c].append([l+1,c-1])   
            if l < 8 and c < 8 and len(self.liste[l+1][c+1]) < 5 and len(self.liste[l+1][c+1]) != 0 : 
                if (len(self.liste[l][c]) + len(self.liste[l+1][c+1])) <= 5 :     
                    self.coup_possible[l,c].append([l+1,c+1])
        for possible in self.coup_possible[pawn]:
            pos2 =  int(possible[0])*(HEIGHT + SPACE)
            pos1 =  int(possible[1])*(WIDTH + SPACE) 
            pygame.draw.circle(screen,COLORS["WHITE"],(pos1+(int(RADIUS+SPACE)),pos2+(int(RADIUS+SPACE))), int(RADIUS), int(RADIUS))

        return(self.coup_possible)
a = False   
while run :
    clock.tick(FPS)
    game = Avalam_Game()
    game.draw_board()
    game.pawn_position()
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            run = False  
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            column = pos[0] // (WIDTH + SPACE)
            row = pos[1] // (HEIGHT + SPACE)
            move[row,column].append(1)
            a = True
    if a:
        game.can_move((row,column))

    pygame.display.flip() 
    


 