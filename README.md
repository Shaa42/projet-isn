Bienvenue dans Crash Point INSA, un jeu de survie dans lequel vous incarnez un survivant d’un crash d’avion, perdu sur une île mystérieuse. Explorez les différents lieux, gérez vos ressources (eau, bois, nourriture). Explorez toute l’île et récupérez assez de sources afin de quitter l’île !
Ce README décrit la structure et le fonctionnement du jeu, bonne lecture !

Le joueur débute le jeu à Crash Point avec quelques ressources. A chaque tour, le joueur dispose d’un temps limité pour interagir avec l’interface graphique pour : 
Sélectionner un endroit à visiter sur la carte intéractive. Chaque lieu de la carte a des caractéristiques propres en termes de ressources en eau, nourriture et bois mais également des potentiels évènements aléatoires qui peuvent arriver au joueur.
Voyager d’un point A à un point B peut coûter de l’eau, de la nourriture et du bois. 
Arrivé à la localisation souhaitée, il choisit quelle ressource récupérer parmi celles disponibles sur le lieu.

I) Explication du projet


Pour concevoir notre jeu, nous avons d’abord analysé les règles du jeu de cartes original Galérapagos afin de retenir les éléments fondamentaux : ressources, lieux, interactions entre joueurs et jeu. A partir de cette base, nous avons décidé de réduire le jeu à un seul joueur et de garder la logique de tour par tour. Avec les règles de notre jeu défini, nous avons ensuite divisé le jeu en plusieurs modules fonctionnelles et réparti les tâches entre nous. 

Les plusieurs étapes de notre projet sont expliqués dans ce diagramme de Gantt ci-dessous. 

Répartition du travail
Difficulté
réussites

II) codage du projet
Pour ce projet, nous avons choisi d’utiliser la programmation orientée objet (POO) afin de structurer notre jeu de manière claire, modulaire et évolutive. La POO nous a permis de séparer les différentes logiques du jeu en classes distinctes. Chaque classe correspond à une fonctionnalité spécifique. Cette séparation a facilité le travail en groupe, car chaque membre a pu se concentrer sur une classe précise sans interférer avec les autres, ce qui a rendu le développement plus efficace et organisé. Par ailleurs, l’approche orientée objet offre une meilleure maintenabilité : si nous souhaitons ajouter de nouvelles mécaniques de jeu ou modifier certaines règles, nous pouvons le faire en adaptant une seule classe sans risquer de perturber l’ensemble du code. Enfin, la POO s’adapte très bien aux jeux, car elle permet de modéliser les entités (joueur, lieux, cartes…) comme des objets vivants avec des propriétés et des comportements, ce qui rend le code plus intuitif et proche du fonctionnement réel du jeu.

LA COMPLEXITE algorithmique
main.py est le fichier principal qui lance le jeu, initialise l’interface graphique avec Pygame, gère la boucle de jeu et les interactions utilisateur. Il centralise l’appel aux autres classes. Voici une explication détaillée de chaque sous fichier contenant les classes principales de notre code. 


game.py
 Contient la classe Game qui supervise le déroulement global du jeu : avancement des jours, gestion des tours, conditions de victoire ou de défaite. Ce code centralise toute la logique du jeu: navigation sur la carte (graphe), consommation et collecte des ressources, interactions joueur-lieux et la gestion du temps.


player.py
Classe Player représentant le joueur, ses ressources ( water, food, wood), sa position (objet Node issu d’un graphe), et ses actions possibles (récolte, déplacement, usage de cartes). Elle gère l’état individuel du joueur.


deck.py
Gère les cartes du jeu (bonus, objets, effets spéciaux). Permet de jouer et gérer les cartes en main. Introduit de la stratégie et de l’aléatoire. Il y a deux types de cartes: les cartes à jouer et les cartes objets. Les cartes à jouer ne peuvent être utilisées qu’une seule fois, les cartes objets restent toute la partie. 


event.py
	Permet de rajouter une autre couche d’aléatoire. Fait possiblement perdre au joueur une ou des ressources à chaque tour ou presque.
map.py
Modélise l’île comme un graphe non orienté pondéré. Chaque lieu sur la carte est un nœud (Node), chaque trajet a un coût en eau/nourriture/bois. La classe gère les déplacements et les connexions entre les lieux. 
Ces classes sont utilisées entre elles et ces relations sont répertoriées dans le diagramme UML suivant : DIAGRAMME UML 
III) Comment jouer au jeu ?

mode d’emploi, dépendances, étapes de lancement

Comment lancer ?? bah on envoie le lien github puis … ? → Ryan
