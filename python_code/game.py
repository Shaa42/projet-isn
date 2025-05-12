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
    
    def main(self):
        print(self.player)
        print(self.map)
        
if __name__ == "__main__":
    game = Game()
    game.main()