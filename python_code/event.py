# -*- coding: utf-8 -*-
"""
Created on Fri May 16 04:14:31 2025

@author: wangj
"""

from random import random
from player import Player

class Event:
    def __init__(self, name: str, event_type: str, effects: dict, probability: float):
        self.name = name
        self.event_type = event_type
        self.effects = effects
        self.probability = probability

    def describe_event(self) -> str:
        return f"Event: {self.name}"

    def apply_effects(self, player: Player) -> str:
        """
        Applies the effects of the event to the player and returns a log describing what happened.
        """
        event_log = [f"Event triggered: {self.name}"]

        for resource, amount in self.effects.items():
            if resource == "water":
                if amount > 0:
                    player.add_water(amount)
                    event_log.append(f"+{amount} water")
                else:
                    player.remove_water(-amount)
                    event_log.append(f"{amount} water")

            elif resource == "wood":
                if amount > 0:
                    player.add_wood(amount)
                    event_log.append(f"+{amount} wood")
                else:
                    player.remove_wood(-amount)
                    event_log.append(f"{amount} wood")

            elif resource == "food":
                if amount > 0:
                    player.add_food(amount)
                    event_log.append(f"+{amount} food")
                else:
                    player.remove_food(-amount)
                    event_log.append(f"{amount} food")

            elif resource == "health":
                if amount > 0:
                    player.add_health(amount)
                    event_log.append(f"+{amount} health")
                else:
                    player.remove_health(-amount)
                    event_log.append(f"{amount} health")

            elif resource == "hunger":
                if amount > 0:
                    player.add_hunger(amount)
                    event_log.append(f"+{amount} hunger")
                else:
                    player.remove_hunger(-amount)
                    event_log.append(f"{amount} hunger")

            else:
                event_log.append(f"(Unknown resource: {resource})")

        return " | ".join(event_log)
