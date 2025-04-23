class Node:
    """
    Node constituing the map
    """
    def __init__(self, water, wood, food, events, weather):
        """
        Initialise a node with the availaible resources, the actual weather and the events that can occur
        """
        ...

class Map:
    """
    A graph using the Node class
    """
    def __init__(self):
        dict_map = {} # Dictionnary linking the nodes
        
    def add_node(self, other_node : Node):
        ...