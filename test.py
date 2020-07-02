import pygame
import time 

# Global constants : 
BOARD ={"0":[6,7],
        "1":[4,5,6,7],
        "2":[2,3,4,5,6,7],
        "3":[0,1,2,3,4,5,6,7],
        "4":[0,1,2,3,4,5,6,7,8],
        "5":[1,2,3,4,5,6,7,8],
        "6":[1,2,3,4,5,6],
        "7":[1,2,3,4],
        "8":[2,3]}
COLORS = {"BLACK" : (0, 0, 0), "WHITE" : (255, 255, 255), "GREEN":(0, 255, 0),"RED" :(255, 0, 0),"YELLOW":(255,255,0)}
CASE_WIDTH = 50
CASE_HEIGHT = 50
CASE_SPACE = 10
PAWN_RADIUS = 25
GRID = [[0 for x in range(9)] for y in range(9)]
moves = {}
body = [[[] for x in range(9)]for y in range(9)]
for row in range(9):
    for column in range(9):
        moves[row,column] = []
WINDOW_SIZE = [CASE_HEIGHT*len(GRID)+(CASE_SPACE*(len(GRID)+1)),len(GRID)*CASE_WIDTH+(CASE_SPACE*(len(GRID)+1))]
screen = pygame.display.set_mode(WINDOW_SIZE)

class Avalam_Game:

    def __init__(self,BOARD):
        self.BOARD = BOARD
    def reset_game(self): 
        pass

    def draw_BOARD(self):   
        for row in self.BOARD.keys() :
            for column in self.BOARD[row]: 
                pos2 =  int(row)*(CASE_HEIGHT + CASE_SPACE)
                pos1 =  int(column)*(CASE_WIDTH + CASE_SPACE)
                if int(row) % 2 != 0 and int(column) % 2 == 0 or int(row) % 2 == 0 and int(column) % 2 != 0:
                    pygame.draw.circle(screen,COLORS["RED"],(pos1+(int(PAWN_RADIUS+CASE_SPACE)),pos2+(int(PAWN_RADIUS+CASE_SPACE))), int(PAWN_RADIUS), int(PAWN_RADIUS))
                    body[int(row)][int(column)] =  [1]
                else:
                    pygame.draw.circle(screen,COLORS["YELLOW"],(pos1+(int(PAWN_RADIUS+CASE_SPACE)),pos2+(int(PAWN_RADIUS+CASE_SPACE))), int(PAWN_RADIUS), int(PAWN_RADIUS))
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
            pos2 =  int(possible[0])*(CASE_HEIGHT + CASE_SPACE)
            pos1 =  int(possible[1])*(CASE_WIDTH + CASE_SPACE) 
            pygame.draw.circle(screen,COLORS["WHITE"],(pos1+(int(PAWN_RADIUS+CASE_SPACE)),pos2+(int(PAWN_RADIUS+CASE_SPACE ))), int(PAWN_RADIUS), int(PAWN_RADIUS))

        return(self.coup_possible)

    def move(self,initial,final):
        for value in self.BOARD[str(row)]:
            if value == column :
                self.BOARD[str(row)].remove(value)
        pygame.draw.circle(screen,COLORS["WHITE"],final,final, int(PAWN_RADIUS), int(PAWN_RADIUS))


def main():
    pygame.init()
    WINDOW_SIZE = [CASE_HEIGHT*len(GRID)+(CASE_SPACE*(len(GRID)+1)),len(GRID)*CASE_WIDTH+(CASE_SPACE*(len(GRID)+1))]
    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption("Avalam")
    clock = pygame.time.Clock()
    FPS = 60
    a = False 
    run = True 
    while run :
        screen.fill(COLORS["BLACK"])
        clock.tick(FPS)
        game = Avalam_Game(BOARD)
        game.draw_BOARD()
        game.pawn_position()
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:  
                run = False  
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                column = pos[0] // (CASE_WIDTH + CASE_SPACE)
                row = pos[1] // (CASE_HEIGHT + CASE_SPACE)
                moves[row,column].append(1)
                a = True
                
        if a:
            game.can_move((row,column))
            for value in BOARD[str(row)]:
                if value == column :
                    BOARD[str(row)].remove(value)
            
            
        pygame.display.flip() 
        
if __name__ == "__main__":
    main()
 