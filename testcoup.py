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
    for elem in position:     # peut faire le pion , on sauvegarde cela dans un dict avec comme clé la 
        l = elem[0]           # position des pions et comme valeur une liste des different positions possible que
        c = elem[1]           # peut faire ce dernier.
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


