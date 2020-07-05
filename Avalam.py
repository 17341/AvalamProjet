import pygame
import time 
# Constantes :
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
        "YELLOW":(255,255,0),
        "BLUE":(0,0,255)}
board_color = {}

class Avalam_Game:

    def __init__(self):
        self.board_color = board_color
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
        self.joueur = 0
        for row in self.BOARD.keys() :
            for column in self.BOARD[row]: 
                if int(row) % 2 != 0 and int(column) % 2 == 0 or int(row) % 2 == 0 and int(column) % 2 != 0:
                    self.body[int(row)][int(column)] =  [1]
                    self.board_color[(int(row),column)] = ["RED"]
                else:
                    self.body[int(row)][int(column)] = [0]
                    self.board_color[(int(row),column)] = ["YELLOW"]
                
    def draw_board(self):
        self.possible_moves()
        self.screen.fill(COLORS["BLACK"])
        pygame.display.set_caption("Avalam")
        for pos in self.board_color.keys():
            row_pos =  int(pos[0])*(self.CASE_HEIGHT + self.CASE_SPACE)
            col_pos =  int(pos[1])*(self.CASE_WIDTH + self.CASE_SPACE)
            pygame.draw.circle(self.screen,COLORS[self.board_color[pos][-1]],(col_pos+(int(self.PAWN_RADIUS+self.CASE_SPACE)),row_pos+(int(self.PAWN_RADIUS+self.CASE_SPACE))), int(self.PAWN_RADIUS), int(self.PAWN_RADIUS))
            num = len(self.body[pos[0]][pos[1]])
            self.draw_txt(num,col_pos+self.PAWN_RADIUS,row_pos+self.PAWN_RADIUS-5,COLORS["BLUE"])
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
        try :
            for possible in self.coup_possible[position]:
                pos2 =  int(possible[0])*(self.CASE_HEIGHT + self.CASE_SPACE)
                pos1 =  int(possible[1])*(self.CASE_WIDTH + self.CASE_SPACE) 
                pygame.draw.circle(self.screen,COLORS["WHITE"],(pos1+(int(self.PAWN_RADIUS+self.CASE_SPACE)),pos2+(int(self.PAWN_RADIUS+self.CASE_SPACE))),int(self.PAWN_RADIUS),int(self.PAWN_RADIUS))
        except:
            print("Cette tour est remplie ! ")

    def make_move(self,initial_position,final_position):
        try : 
            if list(final_position) in self.coup_possible[initial_position] : 
                self.body[final_position[0]][final_position[1]] += self.body[initial_position[0]][initial_position[1]]
                self.body[initial_position[0]][initial_position[1]].clear()
                #Remove pawn from board : 
                for value in self.BOARD[str(initial_position[0])]:
                    if value == initial_position[1] :
                        self.BOARD[str(initial_position[0])].remove(value)
                #Remove color from pawn :
                for value in self.board_color.keys():
                    if  initial_position == value :
                        initial_color = self.board_color[value]
                        self.board_color[final_position] = initial_color
                        del self.board_color[value]
                        break
            else:
                print("Not possible")   
        except: 
            print("Not possible")   
        
        pygame.display.update()
   
    def draw_txt(self,txt,x,y,color,size = 50):
        Letter_font = pygame.font.SysFont('comicsans',size)
        text = Letter_font.render(str(txt),1,color)
        self.screen.blit(text,(x,y))

def main():
    pygame.init()
    run = True
    game = Avalam_Game()
    clock = pygame.time.Clock()
    FPS = 60
    show = 0
    i = 0
    game.draw_board()
    while run :
        clock.tick(FPS)
        while show%2 != 0 :
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  
                    run = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    final_position = pygame.mouse.get_pos()
                    final_column = final_position[0] // (CASE_WIDTH + CASE_SPACE)
                    final_row = final_position[1] // (CASE_HEIGHT + CASE_SPACE)
                    game.make_move((initial_row,initial_column),(final_row, final_column))
                    game.draw_board()
                    print(game.possible_moves())
                    show += 1 
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:  
                run = False  
            elif event.type == pygame.MOUSEBUTTONDOWN:
                initial_position = pygame.mouse.get_pos()
                initial_column = initial_position[0] // (CASE_WIDTH + CASE_SPACE)
                initial_row =initial_position[1] // (CASE_HEIGHT + CASE_SPACE)
                if str(initial_row) in BOARD.keys() and initial_column in BOARD[str(initial_row)]:
                    game.show_move((initial_row,initial_column))
                    i+=1   
                    show += 1
                else :
                    print("No pawn here!")
    
        pygame.display.flip() 

if __name__ == "__main__":
    main()
 
