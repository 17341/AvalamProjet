# Projet Avalam IA
## Langage 
Python 3.8.2

## Auteurs  
- Name : FrigoFri
- Ferekh Khaled : 17341
- Thierry Joel Tchanteu Moumi : 17367
- Default Port : 8000

# Installation
- Télecharger ou clone le dossier AvalamProjet de github en tapant :
    git clone https://github.com/17341/AvalamProjet
- Télecharger ou clone le dossier AIGameRunner de github en tapant :
    git clone https://github.com/ECAM-Brussels/AIGameRunner
- Installer Cherrypy et Python 3 sur votre pc si ce n'est pas déja fait.

# How to test 
- Démarrer le serveur du superviseur pour avoir l'interface de jeu :
    - Ouvrir un premier terminal dans le dossier AIGameRunner
    - Taper : python server.py avalam
- S'enregistrer à la compétition (envoyer un message TCP au format json au port 3001): 
    - Ouvrir un deuxième terminal dans le dossier AvalamProjet 
    - Taper : python Subscribe.py 
- Démarrer le serveur AI :
    - Toujours dans le deuxième terminal 
    - Taper : python Avalam_AI.py Port 
   (Le port doit être le même que celui du fichier Subscribe.py, par défaut le port est 8000) 
- Enregister le Random à la compétition:
    - Ouvrir un troisième terminal dans le dossier AvalamProjet 
    - Modifier le port, matricules et name dans le fichier Subscribe.py
    - Taper : python Subscribe.py 
- Démarrer le serveur Random  :
   - Toujours dans le troisième terminal 
   - Taper : python Avalam_Random.py Port 
    (Le port doit être le même que celui du fichier Subscribe.py modifié) 
- Vous pouvez maintenant vous rendre au serveur web du superviseur et tester l'IA contre le Random.
# Informations Avalam 

## Règles du jeu  
- On peut jouer avec les pions de son adversaire.
- On peut déplacer les pions ou la piles de pions vers une case adjacente qui n'est pas vide.
- Une tour ne peut avoir qu'au maximum 5 pions.

## But du jeu
- Avoir un maximum de tours dont le pion supérieur est de sa couleur.

# Stratégie de jeu IA
Notre stratégie se résume en trois tactiques dans l'ordre de priorité suivant : 
- La tactique-isolate  : Trouver un pion ou une tour ennemie seul (encerclé par nos cases), et l'isoler en mettant un de nos pion au dessus.
- La tactique-five     : Trouver une case qui peut être potentiellement remplie (5 pions), la remplir en s'assurant que le dernier pion soit le nôtre.
- La tactique-minpoint : Reduire les pions de l'adversaire en les empilant les uns sur les autres, sauf si ça lui fait une tour de 5 pions.
- Random : Si aucune des tactiques n'est trouvée, on joue aléatoirement.



