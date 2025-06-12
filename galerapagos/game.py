from time import sleep
from threading import Thread
import sys


# Import classes from other modules
from galerapagos.player.player import Player
from galerapagos.maps.map import Map, Node


class Game:
    """
    The main class for the game. It will manage the game loop and the game state.
    """
    
    def __init__(self):
        self.player = Player(health=30, water=3, food=3)
        self.map = self.create_map()
        
    def create_map(self) -> Map:
        """
        Create the map for the game. It will be a graph of nodes.
        """
        # Create the map
        game_map = Map()
        
        # Create the nodes
        self.alpha_node = Node("Crashpoint alpha"       , 0, 2, 1)        
        self.cime_node  = Node("Cimetière brumeuse"     , 0, 3, 0)
        self.terr_node  = Node("Terrier des phacochères", 1, 1, 3)
        self.camp_node  = Node("Camps des survivants"   , 2, 2, 2)
        self.foret_node = Node("Forêt des tambours"     , 2, 3, 1)
        self.casc_node  = Node("Cascade brumeuse"       , 3, 1, 1)
        
        # Set the player's position to the alpha node
        self.player.set_position(self.alpha_node)
         
        # Add the nodes to the map
        game_map.add_node(self.alpha_node, self.cime_node , weight=(1, 0, 1))
        game_map.add_node(self.alpha_node, self.foret_node, weight=(2, 0, 1))
        game_map.add_node(self.cime_node , self.terr_node , weight=(1, 1, 1))
        game_map.add_node(self.terr_node , self.camp_node , weight=(1, 1, 1))
        game_map.add_node(self.camp_node , self.foret_node, weight=(1, 1, 1))
        game_map.add_node(self.camp_node , self.casc_node , weight=(1, 1, 1))
        game_map.add_node(self.foret_node, self.casc_node , weight=(1, 1, 1))

        return game_map
        """
        Log the player's resources and health.
        """
        print(f"Vos ressources sont : {self.player.dic_resources}")
        print(f"Votre santé est de {self.player.health}")
        print(f"Votre faim est de {self.player.hunger}")
    
    def input_move(self) -> None:
        """
        Ask the player to move to a new node.
        """
        move = ""
        move = input("Où voulez-vous aller ? (entrez le nom du point de la carte ; 'stay' pour rester) : ").strip()
        
        # Allow the player to stay in the same position
        if move == "stay":
            move_cost = 0
            # print("Vous restez sur place.")
            return
        
        # bool if the node neighbors
        can_move = self.map.get_node_from_name(move) in self.map.node_neighbors(self.player.position)

        # move the player
        if can_move:
            # Check if the player has enough resources to move
            move_cost = self.map.get_weight(self.player.position, self.map.get_node_from_name(move))
            wat_cost, wood_cost, food_cost = move_cost
            
            # Check if the player is sure to move
            # print(f"Le coût de déplacement vers {move} est de {wat_cost} d'eau, {wood_cost} de bois et {food_cost} de nourriture.")
            # while True:
            #     ask_player = input(f"Êtes-vous sûr de vouloir vous déplacer vers {move} ? (oui/non) : ").strip().lower()
            #     if ask_player == "non":
            #         print(f"Vous avez choisi de ne pas vous déplacer.")
            #         return
            #     elif ask_player == "oui":
            #         break
            #     else:
            #         print("Réponse invalide. Veuillez répondre par 'oui' ou 'non'.")


            if self.player.has_enough_resources(move_cost):
                # Remove the resources from the player
                self.player.rm_from_weight(move_cost)
                # print(f"Vous avez dépensé {wat_cost} d'eau, {wood_cost} de bois et {food_cost} de nourriture pour vous déplacer.")
            else:
                # print("Vous n'avez pas assez de ressources pour vous déplacer.")
                self.input_move()
                
            match move:
                case "Crashpoint alpha":
                    self.player.set_position(self.alpha_node)
                case "Cimetière brumeuse":
                    self.player.set_position(self.cime_node)
                case "Terrier des phacochères":
                    self.player.set_position(self.terr_node)
                case "Camps des survivants":
                    self.player.set_position(self.camp_node)
                case "Forêt des tambours":
                    self.player.set_position(self.foret_node)
                case "Cascade brumeuse":
                    self.player.set_position(self.casc_node)
            # print(f"Vous vous déplacez vers {move}")

                
        # Return to the main loop
        else:
            # print("Déplacement impossible !")
            # print("Veuillez entrer un point de la carte valide.")
            self.input_move()
            
    def input_action(self):
        """
        Ask the player to perform an action.
        """
        map_ressources = self.player.position.get_resources()
        is_map_empty = map_ressources["food"] == 0 and map_ressources["water"] == 0 and map_ressources["wood"] == 0
        if is_map_empty:
            # print("Il n'y a pas de ressources ici.")
            return
            
        action = input("Que voulez-vous faire ? (Choix : 'water', 'wood', 'food') : ").strip()
        match action:
            case "food":
                if map_ressources["food"] > 0:
                    self.player.add_food(map_ressources["food"])
                    self.player.position.remove_food()
                    print("Vous avez mangé de la nourriture.")
                else:
                        print("Il n'y a pas de nourriture ici.")
                        self.input_action()
            case "water":
                if map_ressources["water"] > 0:
                    self.player.add_water(map_ressources["water"])
                    self.player.position.remove_water()
                    print("Vous avez bu de l'eau.")
                else:
                    print("Il n'y a pas d'eau ici.")
                    self.input_action()
            case "wood":
                if map_ressources["wood"] > 0:
                    self.player.add_wood(map_ressources["wood"])
                    self.player.position.remove_wood()
                    print("Vous avez pris du bois.")
                else:
                    print("Il n'y a pas de bois ici.")
                    self.input_action()
            case _:
                print("Action impossible !")
                print("Veuillez entrer une action valide.")
                self.input_action()
             
    def game_over(self) -> bool:
        """
        Check if the game is over.
        """
        if self.player.get_health() <= 0:
            print("Vous êtes mort !")
            return True
        if self.player.get_food() <= 0:
            print("Vous êtes mort de faim !")
            return True
        if self.player.get_water() <= 0:
            print("Vous êtes mort de soif !")
            return True
        else:
            return False
    
    def main(self):
        # Set the timer thread for 30 seconds
        timer_thread = Thread(target=self.timer, args=(30,))
        timer_thread.start()
        
        # Introduction
        self.isRunning = True
        self.intro()
        print("")
        # Boucle de jeu
        while self.isRunning:
            # Deplacement du joueur
            
            # Afficher la carte
            print(self.map)
            
            # Afficher les déplacements possibles
            self.log_move()
            
            # Afficher le temps restant
            print(f"Il vous reste {self.time[0]} secondes !")
            
            # Afficher les ressources du joueur
            self.log_player()
            print("")
            
            # Demander au joueur de faire une action
            self.input_action()
            
            # Demander au joueur de se déplacer
            self.input_move()
            
            if self.game_over():
                isRunning = False
            
            
            # Action du joueur
        
        
        # print(self.player)
        # print(self.map)
        
if __name__ == "__main__":
    # Debug
    game = Game()
    game.main()