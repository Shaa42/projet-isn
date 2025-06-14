# 🛬 Crash Point INSA

**Crash Point INSA** est un jeu de survie dans lequel vous incarnez un survivant d’un crash d’avion, perdu sur une île mystérieuse. Explorez l’île, gérez vos ressources (eau, bois, nourriture) et survivez assez longtemps pour trouver un moyen de vous échapper !

---

## 📖 Sommaire

1. [Présentation](#-présentation)
2. [Structure du Projet](#-structure-du-projet)
3. [Architecture du Code](#-architecture-du-code)
4. [Comment Jouer](#-comment-jouer)
5. [Répartition du Travail](#-répartition-du-travail)
6. [Difficultés et Réussites](#-difficultés-et-réussites)

---

## 🧭 Présentation

Le joueur débute l’aventure à **Crash Point** avec quelques ressources de base.  
À chaque tour, il dispose d’un **temps limité** pour interagir avec l’interface graphique et :

- **Choisir un lieu à explorer** sur la carte interactive.
- **Gérer ses ressources** (eau, bois, nourriture) en fonction des déplacements et actions.
- **Faire face à des événements aléatoires** qui peuvent affecter ses ressources ou sa progression.

Chaque lieu possède des **caractéristiques uniques** et des **ressources spécifiques**, mais aussi des **événements imprévus**. Le but du jeu est de **collecter assez de ressources** pour quitter l’île sain et sauf.

---

## 🧱 Structure du Projet

Le jeu s’inspire du jeu de cartes **Galérapagos**.  
Nous avons choisi de **l’adapter pour un seul joueur**, en conservant la logique de **jeu au tour par tour**.

Le développement s’est structuré en plusieurs étapes :

- Analyse des règles originales.
- Conception d’une version solo et numérique.
- Répartition des tâches par modules fonctionnels.
- Implémentation par classes orientées objet.

> 📅 Un **diagramme de Gantt** a été réalisé pour visualiser les étapes du projet.

---

## 🧠 Architecture du Code

Le projet est entièrement développé en **Python** en utilisant la **programmation orientée objet** pour une structure modulaire, évolutive et facilement maintenable.

### 🗂 Fichiers principaux

| Fichier     | Description |
|-------------|-------------|
| `main.py`   | Point d’entrée du jeu. Initialise Pygame, la boucle principale, et les interactions utilisateur. |
| `game.py`   | Contient la classe `Game` qui gère le déroulement global : jours, tours, victoires, défaites, navigation sur la carte, collecte de ressources, etc. |
| `player.py` | Décrit le joueur : ses ressources (`water`, `food`, `wood`), sa position (`Node`) et ses actions possibles. |
| `deck.py`   | Gère les cartes du jeu (bonus, objets, événements). Deux types : cartes à usage unique et objets permanents. |
| `event.py`  | Ajoute une couche d’aléatoire (ex. perte de ressources aléatoire). |
| `map.py`    | Représente la carte de l’île comme un graphe non orienté pondéré (lieux = nœuds, trajets = arêtes avec coût). |

### 🧩 Relations entre classes

Les relations entre les classes sont représentées dans le **diagramme UML** ci-dessous :  
📌 *(À insérer : diagramme UML)*

---

## 🎮 Comment Jouer

### ⚙️ Dépendances

- Python ≥ 3.10
- Pygame

### 🔧 Installation

```bash
git clone https://github.com/ton-projet/crash-point-insa.git
cd crash-point-insa
pip install -r requirements.txt
```

### 🚀 Lancement du jeu

```bash
python main.py
```

---

## 👥 Répartition du Travail

Chaque membre de l’équipe s’est vu attribuer un ou plusieurs modules (classes) à implémenter, permettant un développement parallèle efficace.

> 📝 *Liste des membres et de leurs modules respectifs à ajouter ici.*

---

## 🧗 Difficultés et Réussites

### 💥 Difficultés rencontrées

- Gestion des événements aléatoires équilibrés.
- Représentation graphique dynamique de la carte.
- Gestion des ressources avec pénalités de déplacement.

### ✅ Réussites

- Implémentation d’un graphe dynamique pour la carte.
- Interaction fluide avec l’interface Pygame.
- Modularité du code facilitant les tests et évolutions futures.

---

## 📸 Captures d’écran

📌 *(Ajouter des images du jeu ici)*

---

## 🏁 Objectif final

Explorez toute l’île, gérez intelligemment vos ressources, et récupérez assez d’éléments pour **construire un radeau et vous échapper** de l’île !

Bon jeu ! 🌴
