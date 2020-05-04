import cherrypy
import sys
import json
from random import choice

class Server:
   
    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
     
    def move(self):
        # Deal with CORS
        cherrypy.response.headers['Access-Control-Allow-Origin'] = '*'
        cherrypy.response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
        cherrypy.response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization, X-Requested-With'
        if cherrypy.request.method == "OPTIONS":
            return ''     
        self.body = cherrypy.request.json
        self.IA()
        print(self.f, self.t)
        
        return {"move": {"from": self.f ,"to" : self.t},"message": self.msg }
    
    ##############################################################################################
    ##### On prend la situation de la partie dans une nouvelle liste(position) qui      ##########
    ##### a comme valeur de liste une liste avec les lignes et colonnes des différentes ##########
    ##### positions.                                                                    ##########
    ##############################################################################################
    def pion_position(self):
        self.position = []
        self.coup_possible = {}
        self.liste = self.body["game"]       
        for l in range(9):              
            for c in range(9):          
                if len(self.liste[l][c]) < 5 and len(self.liste[l][c]) != 0:
                    self.position.append([l,c])
                    self.coup_possible[l,c] = []
        return(self.position)

    #####################################################################################################
    #####On scanne autour des positions des pions pour voir les coups possibles que peut faire ##########
    #####le pion, on sauvegarde cela dans un dictionnaire avec comme clé la position des pions ##########
    #####et comme valeur une liste des différentes positions possibles que peut faire ce derniers########                                                                 
    #####################################################################################################
    def can_move(self):                
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
        return(self.coup_possible)
    
    #####################################################################################################
    #####                   Identification en récupérant les données du jeu                     #########
    #####################################################################################################
    def joueur(self):
        if self.body["you"] == self.body["players"][0]:
            self.moi = 0
        else : 
            self.moi = 1
    
    #######################################################################################################################
    ##### Information sur le jeu, récupération des données sur les positions, les coups possibles des pions et le joueur###             
    #######################################################################################################################      
    def info_jeu(self):
        self.pion_position()
        self.can_move()
        self.joueur()

    ############################################################################
    #### Completer les cases à 5 pions avec les notres et gagner un point  #####
    ############################################################################   
    def tac_five(self):
        self.five = {}   
        for f in self.coup_possible.keys():   #On recupère toutes les clès des coups possibles
            self.five[f] = []
            for pos in self.coup_possible[f]:  # On parcours la liste de liste des valeurs de chaque clé 
                if len(self.body["game"][f[0]][f[1]]) + len(self.body["game"][pos[0]][pos[1]]) == 5 : # On vérifie si la taille du pion + son coup possible =5
                    if self.body["game"][f[0]][f[1]][-1] == self.moi and self.body["game"][pos[0]][pos[1]][-1] != self.moi  : #on vérifie si le dernier pion 
                        self.five[f].append(pos)                                                                              #de la case initiale c'est le notre et celui de la case du coup possible  
        return(self.five)  #On retourne contenant 5 pions dont le pion au sommet est le notre                                 # est celui de l'adversaire

    ########################################################################################################
    ###La fonction tac_isolate permet d'isoler les pions de l'adversaire en rajoutant nos pions au dessus###
    ########################################################################################################
    def tac_isolate(self):
        self.isolate = {}
        for f in self.coup_possible.keys():
            self.isolate[f] = []
            if self.body["game"][f[0]][f[1]][-1] != self.moi: #On vérifie si le dernier pion n'est pas le notre
                for pos in self.coup_possible[f]:             #On parcourt tous les coups possibles à cette position
                     if self.body["game"][pos[0]][pos[1]][-1] == self.moi: #On vérifie si le dernier pion du coup posible est le notre 
                        self.isolate[f].append(pos)           #On rajoute notre pion au dessus de l'adversaire
        return(self.isolate)
    #################################################################################################################
    ######La fonction tac_minpoint permet de mininiser les pions de l'adversaire tout en maximisant les notres#######
    #################################################################################################################
    def tac_minpoint(self):
        self.minpoint = {}
        for f in self.coup_possible.keys():
            self.minpoint[f] = []
            if self.body["game"][f[0]][f[1]][-1] != self.moi:  
                for pos in self.coup_possible[f]:
                     if self.body["game"][pos[0]][pos[1]][-1] != self.moi: #On vérifie que le dernier pion du coup possible n'est pas le notre
                        if len(self.body["game"][f[0]][f[1]]) + len(self.body["game"][pos[0]][pos[1]]) != 5 : #On vérifie que la taille des deux est différente de 5
                            self.minpoint[f].append(pos) #On empile les pions de l'adversaire entre eux pour diminuer ses points 
        return(self.minpoint)
#####################################################################################################################
#####On récupere les données des fonctions précedentes dans notre IA,on parcoure le dictionnaire en récupérant ######
##### les clé(dans f) puis on vérifie l'une des conditions tout en éffectuant un break à la fin de la condition,#####
##### dans le cas contraire on fait jouer le random                                                             #####
#####################################################################################################################
    def IA(self):
        self.info_jeu()
        self.tac_isolate()
        self.tac_five()
        self.tac_minpoint()
        for f in self.coup_possible.keys():
            #AVEC MES PIONS : 
            if len(self.isolate[f]) == len(self.coup_possible[f]) and len(self.coup_possible[f]) > 0:
                self.f = choice(self.coup_possible[f]) #On choisit un coup au hasard dans la liste, position après le coup
                self.t = list(f)  #position avant le coup
                print(self.f, self.t)
                self.msg = "pions isolés :):)"
                break
            if len(self.five[f]) > 0:
                self.f = list(f)
                self.t = choice(self.five[f])
                print(self.f, self.t)
                self.msg = "HiHIHIHI + 1 point pour nous :):) "
                break
            #AVEC LES PIONS DE L'ADVERSAIRE :    
            if len(self.minpoint[f]) > 0:
                self.f = choice(self.coup_possible[f])
                self.t = list(f)
                print(self.f, self.t)
                self.msg = "AHHHAHH -1 point pour toi"
                break
            #RANDOM :    
            else:
                self.random = {}
                for f in self.coup_possible.keys():
                    if len(self.coup_possible[f]) > 0:
                        self.random[f] = self.coup_possible[f]
                msg = ['hmm','ok','ahah', "amusant", "tu fais moins le malin"]
                self.msg = choice(msg)
                self.f = list(choice(list(self.random.keys())))
                self.t = choice(self.random[tuple(self.f)] )

    @cherrypy.expose
    def ping(self):
        return "pong"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        port=int(sys.argv[1])
    else:
        port=8080

    cherrypy.config.update({'server.socket_host': '0.0.0.0', 'server.socket_port': port})
    cherrypy.quickstart(Server())

