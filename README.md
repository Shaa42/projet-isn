# Crash Point INSA

Bienvenue dans **Crash Point INSA**, un jeu de survie dans lequel vous incarnez un survivant d’un crash d’avion, perdu sur une île mystérieuse.  
Explorez les différents lieux, gérez vos ressources (eau, bois, nourriture), et récupérez assez de ressources pour pouvoir quitter l’île !

Ce README décrit la structure et le fonctionnement du jeu. Bonne lecture !

## Principe du jeu

Le joueur débute le jeu à **Crash Point** avec quelques ressources.

À chaque tour, le joueur dispose d’un **temps limité** pour interagir avec l’interface graphique :

- Sélectionner un **endroit à visiter** sur la carte interactive.  
  Chaque lieu a ses caractéristiques propres en termes de ressources (eau, nourriture, bois), ainsi que des **événements aléatoires**.
- Voyager d’un point A à un point B **consomme des ressources**.
- Une fois arrivé à destination, le joueur **choisit quelle ressource récolter** parmi celles disponibles.

L'objectif du jeu est de parcourir l'entièreté de l'île avant la fin du chrono et obtenir suffisamment de ressource pour s'enfuir. 

## I. Explication du projet

Pour concevoir notre jeu, nous nous sommes basés sur le jeu de cartes **Galérapagos**, en en extrayant les éléments clés :  ressources, lieux, interactions, et dynamique de tour par tour.

Nous avons ensuite :

- **Adapté le jeu en solo**.
- Conservé la **logique tour par tour**.
- Divisé le projet en **modules fonctionnels** pour mieux répartir les tâches.


## II. Codage du projet

Nous avons choisi une approche en **programmation orientée objet (POO)** pour structurer le jeu de manière claire et évolutive.

### Pourquoi la POO ?

- Séparation des responsabilités par **classe**.
- Travail en groupe facilité.
- Code **modulaire** et **maintenable**.
- Représentation intuitive des entités du jeu (joueur, lieux, événements…).

### Structure du code

- `main.py`  
  Fichier principal. Il lance le jeu, initialise l’interface graphique (Pygame), gère la boucle de jeu et les interactions.

- `game.py`  
  Contient la classe **Game**, qui supervise le jeu : progression, gestion des tours, conditions de victoire/défaite, etc.

- `player.py`  
  Classe **Player** : gère les ressources du joueur (eau, nourriture, bois), sa position (objet Node), ses actions.

- `event.py`  
  Introduit des **événements aléatoires** pouvant faire perdre des ressources au joueur.

- `map.py`  
  Représente l’île comme un **graphe pondéré non orienté**.  
  Chaque lieu est un **nœud**, chaque trajet a un **coût** en ressources.
  
-`gui.py`
Code pour l'interface graphique. Permet d'introduire la logique dans une fenêtre et gère les entrées du joueur.

## III. Comment jouer au jeu ?

### Prérequis

- Python 3.x
- Bibliothèque [Pygame](https://www.pygame.org/)

### Installation

Copie le dépôt à l'aide de git.
```sh
git clone https://github.com/Shaa42/projet-isn.git
```
Accède au dossier.
```sh
cd Crash-Point-INSA
```
Installe les dépendances nécessaires au fonctionnement du jeu.
```sh
pip install -r requirement.txt
```

## Répartition des points du groupe
- Ryan Vigoureux - 0,5
- Antoine Fromentel - 0,2
- Baptiste Grateau - 0,1
- Jiayi Wang - 0,1
- Hanzi Jiang - 0,1


