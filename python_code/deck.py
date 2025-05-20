class Card:
    """
    Class representing the cards and their effects on the game
    """
    def __init__(self, water=0, food=0, wood=0):
        self.water = water
        self.food = food
        self.wood = wood


# Cards with instant effect, single use only
class ThrowawayCard(Card):
    def __init__(self, water=0, food=0, wood=0):
        super().__init__(water, food, wood)
        self.used = False


class WaterFallCard(ThrowawayCard):
    def __init__(self):
        super().__init__(water=2)


class CoconutCard(ThrowawayCard):
    def __init__(self):
        super().__init__(water=1, food=1)


class RiceCaseCard(ThrowawayCard):
    def __init__(self):
        super().__init__(food=2)


class ThirstyFishCard(ThrowawayCard):
    def __init__(self):
        super().__init__(food=1)


class BranchCard(ThrowawayCard):
    def __init__(self):
        super().__init__(wood=1)


# Normal cards, with continuous effects or use

class ObjectCard(Card):
    def __init__(self, water=0, food=0, wood=0):
        super().__init__(water, food, wood)


class Machete(ObjectCard):
    def __init__(self):
        super().__init__(wood=1)


class FishingPool(ObjectCard):
    def __init__(self):
        super().__init__(food=1)


class WaterBottle(ObjectCard):
    def __init__(self):
        super().__init__(water=1)