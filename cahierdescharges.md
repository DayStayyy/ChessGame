# Chess IA

## Cahier des charges

-ia(s): 6 points voir 9 si voila
-jeu d'echec en python en web (13 points) :

- 1VS1 (sur le meme écran, 1 points)
- 1VSIA (1pts)
- BDD(sauvegarder une partie, profil d'un joueur, login/register) (3 PTS)
- register/authentification (2 pts)
- Sauvegarder une game (2 points)
- Crud (4 points)

-Interactions utilisateurs (4 points) :

- Boutons lancer une partie
- Cliquer sur les pieces pour les déplacer
- Bouton sauvegarder une partie

Communication entre 2 logiciels (6 points)

- Human <-> Machine

## Fonctionnalités

Déroulement d’une partie (Difficulté 5)

- les deux joueurs apparaissent de part et d’autre de l’écran
- l’espace de jeu se limite à l’écran, pas de physique, la vue caméra est dite “topdown”
- un des boutons doit permettre au joueur de commencer une partie
- les données de la base doivent être utilisées pour gérer le profile du joueur
- un Joueur perd des points ou en gagne en fonction de l'issue de la partie.

Fin d’une partie (Difficulté 3) :

- la partie se termine quand un joueur est échec et mat, ou quand il y a un pat
- le logiciel bascule alors sur l’écran de fin de partie (gagnant joueur 1 ou joueur 2 ou Draw)
- pour le score, vous devez créer une formule prenant en compte la différence de points de vie, le temps passé sur la partie ainsi que la différence sur les données de BDD du joueur 1 et 2

Ecran d’option (1pts) :

- il devra permettre aux joueurs de modifier toutes leurs données (puissance de tir, vitesses ...) Difficulté : 3
- ces données devront être stockées dans une base de données, afin de pouvoir les réutilisées même après fermeture du logiciel Difficulté : 2

Total : 38 points

# Game

Class jeu
Class pieces
Class Joueur
