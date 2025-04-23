class Player():
    """
    Class representing the player with its resources and its position.
    """
    # To add : Player's position as a node of the map's graph
    
    def __init__(self, water:int = 0, wood:int = 0, food:int = 0) -> None:
        self.dic_resources : dict[str, int] = {
            "water" : water,
            "wood" : wood,
            "food" : food
        }
    
    
    # Methods to give items to the player
    def add_water(self, amount) -> None:
        self.dic_resources["water"] += amount
    
    def add_wood(self, amount) -> None:
        self.dic_resources["wood"] += amount
    
    def add_food(self, amount) -> None:
        self.dic_resources["food"] += amount
        
        
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
    
    
    # Debug/Printing methods

if __name__ == "__main__":
    test_Player = Player()
    water, wood, food = test_Player.get_resources()
    print(f"Water: {water}, Wood: {wood}, Food: {food}")
    test_Player.add_water(5)
    test_Player.add_wood(3)
    test_Player.add_food(2)
    water, wood, food = test_Player.get_resources()
    print(f"Water: {water}, Wood: {wood}, Food: {food}")