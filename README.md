# Projet Avalam IA
## Langage 
Python 3.8

## Règles du jeu
- on ne peut pas déplacer une tour sur une case vide
- Une tour ne peut avoir qu'au maximum 5 pions.

## But du jeu
- Obtenir au maximum la couleur de nos pions au sommet de chaque tour tout en respectant les règles.

# Stratégie de jeu IA
On recupère l'etat du jeu à chaque coup et on recupère les positions des tours et les coups possibles associés à ces tours. Par la suite nous appliquons notre stratégie qui se résume en trois étapes : 
- la tactique five : parcourir à chaque fois les coups possibles des tours,compléter les tours possibles à 5 avec notre pion au sommet.
- La tactique isolate : Quand on trouve un pion de l'adversaire qui est au milieu de nos pions, on met notre pion au dessus de celui de l'adversaire pour l'isoler.
- tactique minimiser point : on reduit les pions de l'adversaire en les empilant les uns sur les autres.

### auteurs : 17341 & 17367