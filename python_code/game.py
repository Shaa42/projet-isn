from player import Player
from map import Map, Node
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
        alpha_node = Node("Crashpoint alpha"       , 0, 2, 1)
        cime_node  = Node("Cimetière brumeuse"     , 0, 3, 0)
        terr_node = Node("Terrier des phacochères", 1, 1, 3)
        camp_node  = Node("Camps des survivants"   , 2, 2, 2)
        foret_node = Node("Forêt des tambours"     , 2, 3, 1)
        casc_node  = Node("Cascade brumeuse"       , 3, 1, 1)
        
        # Add the nodes to the map
        game_map.add_node(alpha_node, cime_node)
        game_map.add_node(alpha_node, foret_node)
        
        game_map.add_node(cime_node, terr_node)
        
        game_map.add_node(terr_node, camp_node)
        
        game_map.add_node(camp_node, foret_node)
        game_map.add_node(camp_node, casc_node)
        
        game_map.add_node(foret_node, casc_node)
        
        return game_map
    
    def main(self):
        print(self.player)
        print(self.map)
        
if __name__ == "__main__":
    game = Game()
    game.main()