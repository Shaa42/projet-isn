from node import Node

class Map:
    """
    An undiricted weighted graph using the Node class
    """
    def __init__(self):
        self.dict_map : dict[Node,dict[Node, int]] = {} # Dictionnary linking the nodes
        
    def __str__(self):
        _string = ""
        for key, value in self.dict_map.items():
            _string += f"{key} -> {value}\n"
        return _string
        
    def add_node(self, node1:Node, node2:Node, weight = 0) -> None:
        """
        Link node1 and node2 with each other in the map with a weight.
        """
        
        # link node1 to node2
        if self.dict_map.get(node1, 0):
            self.dict_map[node1][node2] = weight
        else :
            self.dict_map[node1] = {node2 : weight}
        
        # link node2 to node1
        if self.dict_map.get(node2, 0):
            self.dict_map[node2][node1] = weight
        else :
            self.dict_map[node2] = {node1 : weight}
        
    def node_exists(self, node:Node) -> bool:
        """
        Check if the node exists in the map
        """
        return node in self.dict_map
    
    def node_neighbors(self, node:Node) -> list[Node]:
        """
        Return the neighbors of the node
        """
        if self.node_exists(node):
            return list(self.dict_map[node].keys())
        else:
            return []
    
    def get_node_from_name(self, name:str) -> Node:
        """
        Get the node from its name
        """
        for node in self.dict_map.keys():
            if node.name == name:
                return node
        return None
    
    def get_weight(self, player_pos:Node, other_node:Node) -> int:
        """
        Get the weight between the player's node and one of the neighbour's node
        """
        # print(self.node_neighbors(player_pos))
        if other_node not in self.node_neighbors(player_pos):
            return None

        return self.dict_map[player_pos][other_node]
        
        
            
        
        
            
if __name__ == "__main__":
    
    # Debug
    game_map = Map()
    origin_node = Node("map0", 0, 0, 0)
    first_node  = Node("map1", 0, 1, 2)
    second_node = Node("map2", 0, 0, 3)
    third_node  = Node("map3", 1, 1, 1)
    fourth_node = Node("map4", 5, 0, 0)
    
    game_map.add_node(origin_node, first_node, weight=42)
    game_map.add_node(origin_node, third_node)
    
    game_map.add_node(first_node, second_node)
    game_map.add_node(first_node, fourth_node)
    
    print(game_map)
    print(game_map.node_neighbors(first_node))
    weight = game_map.get_weight(origin_node, first_node)
    print(weight)