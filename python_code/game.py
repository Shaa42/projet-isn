from player import Player
from map    import Map, Node
# This is the main file for the game. It will be used to run the game and manage the game loop.

class Game:
    """
    The main class for the game. It will manage the game loop and the game state.
    """
    
    def __init__(self):
        self.player = Player()
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
        game_map.add_node(self.alpha_node, self.cime_node )
        game_map.add_node(self.alpha_node, self.foret_node)
        game_map.add_node(self.cime_node , self.terr_node )
        game_map.add_node(self.terr_node , self.camp_node )        
        game_map.add_node(self.camp_node , self.foret_node)
        game_map.add_node(self.camp_node , self.casc_node )
        game_map.add_node(self.foret_node, self.casc_node )
        
        return game_map
    
    def intro(self):
        """
        Print the introduction of the game.
        """
        print("Bienvenue dans Galèral'INSA !")
        print("Vous êtes un survivant d'un crash d'avion.")
        print("Vous devez explorer l'île et trouver des ressources pour survivre.")
        print("Vous pouvez vous déplacer entre les différents points de l'île.")
        print("Vous pouvez également interagir avec les objets et les autres survivants.")
        print("Bonne chance !")
    
    def log_move(self):
        """
        Log the player's move.
        """
        print(f"Vous êtes actuellement à {self.player.position}")
        print(f"Les ressources disponibles ici sont : {self.player.position.get_resources()}")
        possible_moves = self.map.node_neighbors(self.player.position)
        print(f"Vos déplacements possibles sont : {possible_moves}")
        
    def log_player(self):
        """
        Log the player's resources and health.
        """
        print(f"Vos ressources sont : {self.player.dic_resources}")
        print(f"Votre santé est de {self.player.health}")
        print(f"Votre faim est de {self.player.hunger}")
    
    def input_move(self):
        """
        Ask the player to move to a new node.
        """
        move = input("Où voulez-vous aller ? (entrez le nom du point de la carte) : ").strip()
        print(f"DEBUG : {move}")
        can_move = self.map.get_node_from_name(move) in self.map.node_neighbors(self.player.position)
        print(f"DEBUG : {move}")
        

        # Check if the move is valid
        if can_move:
            print(f"DEBUG : {move}")
            match move:
                case "Crashpoint alpha":
                    self.player.set_position(self.alpha_node)
                case "Cimetière brumeuse":
                    self.player.set_position(self.cime_node)
                    print("here !")
                    print(self.player.get_position())
                case "Terrier des phacochères":
                    self.player.set_position(self.terr_node)
                case "Camps des survivants":
                    self.player.set_position(self.camp_node)
                case "Forêt des tambours":
                    self.player.set_position(self.foret_node)
                case "Cascade brumeuse":
                    self.player.set_position(self.casc_node)
                    
            print(f"Vous vous déplacez vers {move}")
        else:
            print("Déplacement impossible !")
            print("Veuillez entrer un point de la carte valide.")
            self.input_move()
            
    def input_action(self):
        """
        Ask the player to perform an action.
        """
        map_ressources = self.player.position.get_resources()
        is_map_empty = map_ressources["food"] == 0 and map_ressources["water"] == 0 and map_ressources["wood"] == 0
        if is_map_empty:
            print("Il n'y a pas de ressources ici.")
            return
            
        action = input("Que voulez-vous faire ? (Choix : 'bouffe', 'eau', 'bois') : ").strip()
        match action:
            case "bouffe":
                if map_ressources["food"] > 0:
                    self.player.add_food(map_ressources["food"])
                    self.player.position.remove_food()
                    print("Vous avez mangé de la nourriture.")
                else:
                        print("Il n'y a pas de nourriture ici.")
                        self.input_action()
            case "eau":
                if map_ressources["water"] > 0:
                    self.player.add_water(map_ressources["water"])
                    self.player.position.remove_water()
                    print("Vous avez bu de l'eau.")
                else:
                    print("Il n'y a pas d'eau ici.")
                    self.input_action()
            case "bois":
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
        if self.player.health <= 0:
            print("Vous êtes mort !")
            return True
        # elif self.player.hunger <= 0:
        #     print("Vous avez faim !")
        #     return True
        # elif self.player.dic_resources["water"] <= 0:
        #     print("Vous êtes déshydraté !")
        #     return True
        else:
            return False
    
    def main(self):
        # Introduction
        isRunning = True
        self.intro()
        print("")
        # Boucle de jeu
        while isRunning:
            # Deplacement du joueur
            
            # Afficher la carte
            print(self.map)
            
            # Afficher les déplacements possibles
            self.log_move()
            
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
    game = Game()
    game.main()