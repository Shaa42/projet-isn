from galerapagos.maps.map import Node

class Player():
    """
    Class representing the player with its resources and its position.
    """
    # To add : Player's position as a node of the map's graph
    
    def __init__(self, health:int = 50, water:int = 0, wood:int = 0, food:int = 0, position:Node = None) -> None: # add position
        self.dic_resources : dict[str, int] = {
            "water" : water,
            "wood" : wood,
            "food" : food
        }
        
        self.health = health
        # self.hunger = hunger
        self.position = position
        
    def __str__(self) -> str:
        desc:str = f"The player's ressources : {self.dic_resources}\nPlayer's health : {self.health}\nPlayer's hunger : {self.hunger}\nPlayer's position : {self.position}"
        return desc
    
    
    # Methods to give items to the player
    def add_water(self, amount:int) -> None:
        self.dic_resources["water"] += amount
    
    def add_wood(self, amount:int) -> None:
        self.dic_resources["wood"] += amount
    
    def add_food(self, amount:int) -> None:
        self.dic_resources["food"] += amount
        
    def add_health(self, amount:int) -> None:
        self.health += amount
        
    # def add_hunger(self, amount:int) -> None:
    #     self.hunger += amount
    
    # Methods to remove items from the player
    def remove_water(self, amount:int) -> None:
        self.dic_resources["water"] -= amount
    
    def remove_wood(self, amount:int) -> None:
        self.dic_resources["wood"] -= amount
    
    def remove_food(self, amount:int) -> None:
        self.dic_resources["food"] -= amount
        
    def remove_health(self, amount:int) -> None:
        self.health -= amount
        
    # def remove_hunger(self, amount:int) -> None:
    #     self.hunger -= amount
        
    def rm_from_weight(self, weight:tuple[int, int, int]) -> None:
        """
        Remove resources from the player based on the weight tuple.
        """
        self.remove_water(weight[0])
        self.remove_wood(weight[1])
        self.remove_food(weight[2])
        
    # Set the position of the player
    def set_position(self, position:Node) -> None:
        self.position = position
        
    # Methods to retrieve data
    def get_water(self) -> int:
        return self.dic_resources["water"]

    def get_wood(self) -> int:
        return self.dic_resources["wood"]

    def get_food(self) -> int:
        return self.dic_resources["food"]

    def get_resources(self) -> tuple[int, int, int]:
        water = self.get_water()
        wood = self.get_wood()
        food = self.get_food()
        
        return(water, wood, food)
    
    def get_health(self) -> int:
        return self.health
    
    # def get_hunger(self) -> int:
    #     return self.hunger

    def get_position(self) -> Node:
        return self.position
    
    def has_enough_resources(self, weight:tuple[int, int, int]) -> bool:
        """
        Check if the player has enough resources to perform an action.
        """
        return (self.get_water() >= weight[0] and
                self.get_wood() >= weight[1] and
                self.get_food() >= weight[2])
    
    
    # Debug/Printing methods

if __name__ == "__main__":
    test_Player = Player()
    water, wood, food = test_Player.get_resources()
    print(f"Water: {water}, Wood: {wood}, Food: {food}")
    print(f"health : {test_Player.health}, hunger : {test_Player.hunger}")
    test_Player.add_water(5)
    test_Player.add_wood(3)
    test_Player.add_food(2)
    water, wood, food = test_Player.get_resources()
    print(f"Water: {water}, Wood: {wood}, Food: {food}")