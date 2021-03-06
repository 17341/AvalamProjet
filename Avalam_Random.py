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
        self.IA()
        return {"move": {"from": self.f ,"to" : self.t},"message": "Ok" }

    def pion_position(self):
        self.body = cherrypy.request.json
        self.position = []
        self.coup_possible = {}
        self.liste = self.body["game"]       # On prend la situation de la partie
        for l in range(9):              # dans une nouvelle liste (position) qui a comme valeur de liste une 
            for c in range(9):          # liste avec les lignes et les colonnes des differentes posisions.
                if len(self.liste[l][c]) < 5 and len(self.liste[l][c]) != 0:
                    self.position.append([l,c])
                    self.coup_possible[l,c] = []
        return(self.position)

    def can_move(self):                 # On scann autour des positions des pions pour voir les coups possibles que
        for f in self.position:      # peut faire le pion , on sauvegarde cela dans un dict avec comme clé la 
            l = f[0]                 # position des pions et comme valeur une liste des different positions possible que
            c = f[1]                 # peut faire ce dernier.
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
    
    def joueur(self):
        if self.body["you"] == self.body["players"][0]:
            self.moi = 0
        else : 
            self.moi = 1

    def info_jeu(self):
        self.pion_position()
        self.can_move()
        self.joueur()

    def IA(self):
        self.info_jeu()    
        
        self.random = {}
        for f in self.coup_possible.keys():
            if len(self.coup_possible[f]) > 0:
                self.random[f] = self.coup_possible[f]
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