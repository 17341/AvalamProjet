import pygame
import time 

BOARD={"0":[6,7],
        "1":[4,5,6,7],
        "2":[2,3,4,5,6,7],
        "3":[0,1,2,3,4,5,6,7],
        "4":[0,1,2,3,4,5,6,7,8],
        "5":[1,2,3,4,5,6,7,8],
        "6":[1,2,3,4,5,6],
        "7":[1,2,3,4],
        "8":[2,3]}
CASE_WIDTH = 50
CASE_HEIGHT = 50
CASE_SPACE = 10
PAWN_RADIUS = 25
COLORS={"BLACK" : (0, 0, 0),
        "WHITE" : (255, 255, 255),
        "GREEN":(0, 255, 0),
        "RED" :(255, 0, 0),
        "YELLOW":(255,255,0)}

class Avalam_Game:

    def __init__(self):
        # Constantes :
        self.BOARD=BOARD
        self.CASE_WIDTH = CASE_WIDTH
        self.CASE_HEIGHT = CASE_HEIGHT 
        self.CASE_SPACE = CASE_SPACE
        self.PAWN_RADIUS = PAWN_RADIUS
        self.GRID = [[0 for x in range(9)] for y in range(9)]
        self.WINDOW_SIZE = [self.CASE_HEIGHT*len(self.GRID)+(self.CASE_SPACE*(len(self.GRID)+1)),len(self.GRID)*self.CASE_WIDTH+(self.CASE_SPACE*(len(self.GRID)+1))]
        self.screen = pygame.display.set_mode(self.WINDOW_SIZE)
        self.moves = {}
        self.body = [[[] for x in range(9)]for y in range(9)]
        
    def draw_board(self):
        self.screen.fill(COLORS["BLACK"])
        pygame.display.set_caption("Avalam")
        for row in self.BOARD.keys() :
            for column in self.BOARD[row]: 
                row_pos =  int(row)*(self.CASE_HEIGHT + self.CASE_SPACE)
                col_pos =  int(column)*(self.CASE_WIDTH + self.CASE_SPACE)
                if int(row) % 2 != 0 and int(column) % 2 == 0 or int(row) % 2 == 0 and int(column) % 2 != 0:
                    pygame.draw.circle(self.screen,COLORS["RED"],(col_pos+(int(self.PAWN_RADIUS+self.CASE_SPACE)),row_pos+(int(self.PAWN_RADIUS+self.CASE_SPACE))), int(self.PAWN_RADIUS), int(self.PAWN_RADIUS))
                    self.body[int(row)][int(column)] =  [1]
                else:
                    pygame.draw.circle(self.screen,COLORS["YELLOW"],(col_pos+(int(self.PAWN_RADIUS+self.CASE_SPACE)),row_pos+(int(self.PAWN_RADIUS+self.CASE_SPACE))), int(self.PAWN_RADIUS), int(self.PAWN_RADIUS))
                    self.body[int(row)][int(column)] = [0]
        pygame.display.update()
        return(self.BOARD)

    def pawn_position(self):
        self.position = []
        self.coup_possible = {}     
        for l in range(9):              
            for c in range(9):          
                if len(self.body[l][c]) < 5 and len(self.body[l][c]) != 0:
                    self.position.append([l,c])
                    self.coup_possible[l,c] = []
        return(self.position)

    def possible_moves(self): 
        self.pawn_position()
        for f in self.position:      
            l = f[0]                 
            c = f[1]           
            if c < 8 and len(self.body[l][c+1]) < 5 and len(self.body[l][c+1]) != 0 : 
                if (len(self.body[l][c]) + len(self.body[l][c+1])) <= 5 : 
                    self.coup_possible[l,c].append([l,c+1])
            if c > 0 and len(self.body[l][c-1]) < 5 and len(self.body[l][c-1]) != 0 : 
                if (len(self.body[l][c]) + len(self.body[l][c-1])) <= 5 :     
                    self.coup_possible[l,c].append([l,c-1])
            if l < 8 and len(self.body[l+1][c]) < 5 and len(self.body[l+1][c]) != 0 : 
                if (len(self.body[l][c]) + len(self.body[l+1][c])) <= 5 :     
                    self.coup_possible[l,c].append([l+1,c])
            if l > 0 and len(self.body[l-1][c]) < 5 and len(self.body[l-1][c]) != 0 : 
                if (len(self.body[l][c]) + len(self.body[l-1][c])) <= 5 :     
                    self.coup_possible[l,c].append([l-1,c])
            if l > 0  and c > 0 and len(self.body[l-1][c-1]) < 5 and len(self.body[l-1][c-1]) != 0 : 
                if (len(self.body[l][c]) + len(self.body[l-1][c-1])) <= 5 :     
                    self.coup_possible[l,c].append([l-1,c-1])
            if l > 0 and c < 8 and len(self.body[l-1][c+1]) < 5 and len(self.body[l-1][c+1]) != 0 : 
                if (len(self.body[l][c]) + len(self.body[l-1][c+1])) <= 5 :     
                    self.coup_possible[l,c].append([l-1,c+1])
            if l < 8 and c > 0  and len(self.body[l+1][c-1]) < 5 and len(self.body[l+1][c-1]) != 0 : 
                if (len(self.body[l][c]) + len(self.body[l+1][c-1])) <= 5 :     
                    self.coup_possible[l,c].append([l+1,c-1])   
            if l < 8 and c < 8 and len(self.body[l+1][c+1]) < 5 and len(self.body[l+1][c+1]) != 0 : 
                if (len(self.body[l][c]) + len(self.body[l+1][c+1])) <= 5 :     
                    self.coup_possible[l,c].append([l+1,c+1])
        return(self.coup_possible)

    def show_moves(self,row,column):
        self.possible_moves()
        self.draw_board()
        for possible in self.coup_possible[(row,column)]:
            pos2 =  int(possible[0])*(self.CASE_HEIGHT + self.CASE_SPACE)
            pos1 =  int(possible[1])*(self.CASE_WIDTH + self.CASE_SPACE) 
            pygame.draw.circle(self.screen,COLORS["WHITE"],(pos1+(int(self.PAWN_RADIUS+self.CASE_SPACE)),pos2+(int(self.PAWN_RADIUS+self.CASE_SPACE ))), int(self.PAWN_RADIUS), int(self.PAWN_RADIUS))
          
def main():
    pygame.init()
    run = True
    game = Avalam_Game()
    clock = pygame.time.Clock()
    FPS = 60
    show = 0
    game.draw_board()
    while run :
        pos = pygame.mouse.get_pos()
        clock.tick(FPS)
        while show%2 != 0 :
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    final_pos = pygame.mouse.get_pos()
                    final_column = final_pos[0] // (CASE_WIDTH + CASE_SPACE)
                    final_row = final_pos[1] // (CASE_HEIGHT + CASE_SPACE)
                    print("To : ",(final_row, final_column))
                    show += 1 
                    
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:  
                run = False  
            elif event.type == pygame.MOUSEBUTTONDOWN:
                initial_pos = pygame.mouse.get_pos()
                initial_column = initial_pos[0] // (CASE_WIDTH + CASE_SPACE)
                initial_row = initial_pos[1] // (CASE_HEIGHT + CASE_SPACE)
                game.show_moves(initial_row,initial_column)
                print("From : ",(initial_row,initial_column))               
                show += 1
    
        pygame.display.flip() 

if __name__ == "__main__":
    main()
 
