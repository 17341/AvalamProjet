# Projet Avalam IA

## Langage 
Python 3.8


# Stratégie de jeu IA
 
 Notre algorithme recupère l'etat du jeu à chaque fois, trouve toutes les positions des pions 
 et aussi  tous les coups possibles. A l'aide des informations de ses informations on peut faire
 appels à l'une des trois stratégies en fonction de la situation.
 - empiler les cases possibles des pions de 5 tout en se rassurant que les pion au sommet est le notre,
    ceci nous permet de gagner un point à chaque
 - Isoler les pions de l'adversaire tout en les recouvrant des notres 
 - et Enfin minimiser les pions de l'adversaire pour lui faire perdre des points tout en gagnant 