import pygame
import time 
# Constantes :
BOARD={ "0":[6,7],
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
        "GREEN":  (0, 255, 0),
        "RED" :   (255, 0, 0),
        "YELLOW": (255,255,0)}
board_color = {}

class Avalam_Game:

    def __init__(self):
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
        self.board_color = board_color 
        
    def draw_board(self):
        self.screen.fill(COLORS["BLACK"])
        pygame.display.set_caption("Avalam")
        for row in self.BOARD.keys() :
            for column in self.BOARD[row]: 
                row_pos =  int(row)*(self.CASE_HEIGHT + self.CASE_SPACE)
                col_pos =  int(column)*(self.CASE_WIDTH + self.CASE_SPACE)
                if int(row) % 2 != 0 and int(column) % 2 == 0 or int(row) % 2 == 0 and int(column) % 2 != 0:
                    self.body[int(row)][int(column)] =  [1]
                    self.board_color[(int(row),column)] = ["RED"]
                else:
                    self.body[int(row)][int(column)] = [0]
                    self.board_color[(int(row),column)] = ["YELLOW"]
        for pos in self.board_color.keys():
            row_pos =  int(pos[0])*(self.CASE_HEIGHT + self.CASE_SPACE)
            col_pos =  int(pos[1])*(self.CASE_WIDTH + self.CASE_SPACE)
            pygame.draw.circle(self.screen,COLORS[self.board_color[pos][-1]],(col_pos+(int(self.PAWN_RADIUS+self.CASE_SPACE)),row_pos+(int(self.PAWN_RADIUS+self.CASE_SPACE))), int(self.PAWN_RADIUS), int(self.PAWN_RADIUS))

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

    def show_move(self,position): 
        for possible in self.coup_possible[position]:
            pos2 =  int(possible[0])*(self.CASE_HEIGHT + self.CASE_SPACE)
            pos1 =  int(possible[1])*(self.CASE_WIDTH + self.CASE_SPACE) 
            pygame.draw.circle(self.screen,COLORS["WHITE"],(pos1+(int(self.PAWN_RADIUS+self.CASE_SPACE)),pos2+(int(self.PAWN_RADIUS+self.CASE_SPACE))),int(self.PAWN_RADIUS),int(self.PAWN_RADIUS))

    def make_move(self,initial_position,final_position):
        initial_color = ""
        #To remove possible move : 
        for elem in self.coup_possible.keys():
            if elem == initial_position:
                for pion in self.coup_possible.values():
                    if list(elem) in pion :
                        pion.remove(list(elem))     
                break
        #To remove from board :
    
        for value in self.BOARD[str(initial_position[0])]:
                if value == initial_position[1] :
                    self.BOARD[str(initial_position[0])].remove(value)
        
        for elem in self.board_color.keys():
            if elem == initial_position :
                initial_color = self.board_color[elem]
                self.board_color[elem] = ['BLACK']
                self.board_color[final_position].append(initial_color[0])
                print(self.board_color[final_position])
        self.draw_board()
        return(self.board_color)
        
def main():
    pygame.init()
    run = True
    game = Avalam_Game()
    clock = pygame.time.Clock()
    FPS = 60
    show = 0
    initial_row = 0
    initial_column = 0
    game.draw_board()
    game.possible_moves()
    while run :
        clock.tick(FPS)
        while show%2 != 0 :
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  
                    run = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    final_pos = pygame.mouse.get_pos()
                    final_column = final_pos[0] // (CASE_WIDTH + CASE_SPACE)
                    final_row = final_pos[1] // (CASE_HEIGHT + CASE_SPACE)
                    game.make_move((initial_row,initial_column),(final_row, final_column))
                    show += 1 
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:  
                run = False  
            elif event.type == pygame.MOUSEBUTTONDOWN:
                initial_pos = pygame.mouse.get_pos()
                initial_column = initial_pos[0] // (CASE_WIDTH + CASE_SPACE)
                initial_row = initial_pos[1] // (CASE_HEIGHT + CASE_SPACE)
                try :
                    game.show_move((initial_row,initial_column))   
                    show += 1
                except :
                    print("No pawn at this position!")
    
        pygame.display.flip() 

if __name__ == "__main__":
    main()
 
for elem in self.coup_possible.keys():
                    if elem == initial_position:
                        for pion in self.coup_possible.values():
                            if list(elem) in pion :
                                pion.remove(list(elem))