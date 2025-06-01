class Node:
    """
    Node constituing the map
    """
    def __init__(self, name:str, water:int, wood:int, food:int, events = None):
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