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
            "wood"  : wood,
            "food"  : food
        }
        
        self.events  = events # to update with event class
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
    
    def get_resources(self) -> dict[str, int]:
        """
        Get the resources of the node
        """
        return self.dic_resources
    
    def remove_water(self):
        """
        Remove water from the node
        """
        self.dic_resources["water"] = 0
    
    def remove_wood(self):
        """
        Remove wood from the node
        """
        self.dic_resources["wood"] = 0
    
    def remove_food(self):
        """
        Remove food from the node
        """
        self.dic_resources["food"] = 0


class Map:
    """
    An undiricted graph using the Node class
    """
    def __init__(self):
        self.dict_map : dict[Node,list[Node]] = {} # Dictionnary linking the nodes
        
    def __str__(self):
        _string = ""
        for key, value in self.dict_map.items():
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
        
    def node_exists(self, node:Node) -> bool:
        """
        Check if the node exists in the map
        """
        return node in self.dict_map.keys()
    
    def node_neighbors(self, node:Node) -> list[Node]:
        """
        Return the neighbors of the node
        """
        if self.node_exists(node):
            return self.dict_map[node]
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
            
if __name__ == "__main__":
    
    # Debug
    game_map = Map()
    origin_node = Node("map0", 0, 0, 0)
    first_node  = Node("map1", 0, 1, 2)
    second_node = Node("map2", 0, 0, 3)
    third_node  = Node("map3", 1, 1, 1)
    fourth_node = Node("map4", 5, 0, 0)
    
    game_map.add_node(origin_node, first_node)
    game_map.add_node(origin_node, third_node)
    
    game_map.add_node(first_node, second_node)
    game_map.add_node(first_node, fourth_node)
    
    print(game_map)
    # print(game_map.dict_map[origin_node])
    print(game_map.node_neighbors(first_node))