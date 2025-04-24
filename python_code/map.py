class Node:
    """
    Node constituing the map
    """
    def __init__(self, name:str, water:int, wood:int, food:int, events = None, weather = None):
        """
        Initialise a node with the availaible resources, the actual weather and the events that can occur
        """
        self.name = name
        
        self.dic_resources : dict[str, int] = {
            "water" : water,
            "wood" : wood,
            "food" : food
        }
        
        self.events = events # to update with event class
        self.weather = weather # to update with weather class
    
    def __str__(self):
        """
        Print the name when used in print
        """
        # return f"water : {self.dic_resources["water"]}, wood : {self.dic_resources["wood"]}, food  : {self.dic_resources["food"]}"
        return f"{self.name}"
    
    def __repr__(self):
        """
        To print the name when represented in list
        """
        return f"{self.name}"

class Map:
    """
    An undiricted graph using the Node class
    """
    def __init__(self):
        self.dict_map : dict[Node,list[Node]] = {} # Dictionnary linking the nodes
        
    def __str__(self):
        _string = ""
        for key, value in game_map.dict_map.items():
            _string += f"{key} -> {value}\n"
        return _string
        
    def add_node(self, node1:Node, node2:Node):
        """
        Link node1 and node2
        """
        
        # link node1 to node2
        if self.dict_map.get(node1, 0):
            self.dict_map[node1].append(node2)
        else :
            self.dict_map[node1] = [node2]
        
        # link node2 to node1
        if self.dict_map.get(node2, 0):
            self.dict_map[node2].append(node1)
        else :
            self.dict_map[node2] = [node1]
            
            
if __name__ == "__main__":
    
    # Debug
    game_map = Map()
    origin_node = Node("map0", 0, 0, 0)
    first_node = Node("map1", 0, 1, 2)
    second_node = Node("map2", 0, 0, 3)
    third_node = Node("map3", 1, 1, 1)
    fourth_node = Node("map4", 5, 0, 0)
    
    game_map.add_node(origin_node, first_node)
    game_map.add_node(origin_node, third_node)
    
    game_map.add_node(first_node, second_node)
    game_map.add_node(first_node, fourth_node)
    
    print(game_map)