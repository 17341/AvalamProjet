import json 
from random import choice

with open('body.json') as f: # On lis le fichier json 
    info = json.load(f)

liste = info["game"] # On prend la situation de la partie
position = []
move = {}

def position_pion(liste): # On parcours la liste pour trouver les positions des pions et on va les mettre
    for l in range(9):    # dans une nouvelle liste (position) qui a comme valeur de liste une liste avec
        for c in range(9):# les lignes et les colonnes des differentes posisions.
            if len(liste[l][c]) < 5 and len(liste[l][c]) != 0:
                position.append([l,c])
                move[l,c] = []
               
    return(position)

def can_move(liste,position): # On scann autour des positions des pions pour voir les coups possibles que
    for f in position:     # peut faire le pion , on sauvegarde cela dans un dict avec comme clé la 
        l = f[0]           # position des pions et comme valeur une liste des different positions possible que
        c = f[1]           # peut faire ce dernier.
        if c < 8 and len(liste[l][c+1]) < 5 and len(liste[l][c+1]) != 0 : 
            if (len(liste[l][c]) + len(liste[l][c+1])) <= 5 : 
                move[l,c].append([l,c+1])
        if c > 0 and len(liste[l][c-1]) < 5 and len(liste[l][c-1]) != 0 : 
            if (len(liste[l][c]) + len(liste[l][c-1])) <= 5 :     
                move[l,c].append([l,c-1])
        if l < 8 and len(liste[l+1][c]) < 5 and len(liste[l+1][c]) != 0 : 
            if (len(liste[l][c]) + len(liste[l+1][c])) <= 5 :     
                move[l,c].append([l+1,c])
        if l > 0 and len(liste[l-1][c]) < 5 and len(liste[l-1][c]) != 0 : 
            if (len(liste[l][c]) + len(liste[l-1][c])) <= 5 :     
                move[l,c].append([l-1,c])
        if l > 0  and c > 0 and len(liste[l-1][c-1]) < 5 and len(liste[l-1][c-1]) != 0 : 
            if (len(liste[l][c]) + len(liste[l-1][c-1])) <= 5 :     
                move[l,c].append([l-1,c-1])
        if l > 0 and c < 8 and len(liste[l-1][c+1]) < 5 and len(liste[l-1][c+1]) != 0 : 
            if (len(liste[l][c]) + len(liste[l-1][c+1])) <= 5 :     
                move[l,c].append([l-1,c+1])
        if l < 8 and c > 0  and len(liste[l+1][c-1]) < 5 and len(liste[l+1][c-1]) != 0 : 
            if (len(liste[l][c]) + len(liste[l+1][c-1])) <= 5 :     
                move[l,c].append([l+1,c-1])   
        if l < 8 and c < 8 and len(liste[l+1][c+1]) < 5 and len(liste[l+1][c+1]) != 0 : 
            if (len(liste[l][c]) + len(liste[l+1][c+1])) <= 5 :     
                move[l,c].append([l+1,c+1])             
    return(move)

position_pion(liste)
can_move(liste,position)
print(move)
print(choice(list(move.keys())))
print(list(choice(list(move.keys()))))


"""
move_5 = {}
def move5():
    for pos in move.keys():
        if len(info["game"][pos[0]][pos[1]]) + len(info["game"][move[(pos)][0][0]][move[(pos)][0][1]]) == 5 :
            t = pos
            f = move[(pos)][0]
            move_5[tuple(f)] = t
move5()
   


def move_5(self):
        self.move5 = {}
        self.info_jeu()
        for pos in self.coup_possible.keys():
            if len(self.body["game"][pos[0]][pos[1]]) + len(self.body["game"][self.coup_possible[(pos)][0][0]][self.coup_possible[(pos)][0][1]]) == 5 :
                t = list(pos)
                f = self.coup_possible[(pos)][0]
                self.move5[tuple(f)] = t
            else: 
                pass 
        
for pos in self.coup_possible.keys() :    
            if len(self.body["game"][pos[0]][pos[1]]) == 4 :
                self.f = list(pos)
                if len(self.coup_possible[tuple(pos)]) != 0 :
                    self.t = choice(self.coup_possible[pos])
                print(self.f, self.t) 
            else : 
                if len(self.position) != 0 :
                    self.f = choice(self.position)
                if len(self.coup_possible[tuple(self.f)]) != 0 :
                        self.t = choice(self.coup_possible[tuple(self.f)])     
            
isolate = {}
def isolation():
    
    for f in move.keys():
        isolate[f] = []
        if info["game"][f[0]][f[1]][-1] != 0:
            
            for pos in move[f]:
                if info["game"][pos[0]][pos[1]][-1] == 0:
                    isolate[f].append(pos) 
    return(isolate)
isolation()

for f in move.keys():
    if len(isolate[f]) == len(move[f]):
        f = choice(move[f])
        t = list(f)
        print(f, t)
    else :
        pass

minpoint = {}
def tac_minpoint():
    for f in move.keys():
        minpoint[f] = []
        if info["game"][f[0]][f[1]][-1] != 0:
            for pos in move[f]:
                if info["game"][pos[0]][pos[1]][-1] != 0:
                    minpoint[f].append(pos)
    return(minpoint)

tac_minpoint()
print(minpoint)
"""