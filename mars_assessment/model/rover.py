from __future__ import annotations

import random
from typing import TYPE_CHECKING

from model.agent import Agent

if TYPE_CHECKING:
    from model.location import Location
    from model.mars import Mars


class Rover(Agent):
    """
    Represents a rover agent in the simulation.

    Attributes:
        __space_craft_location: The location of the spacecraft the rover is assigned to.
    """

    def __init__(self, location: Location, space_craft_location: Location):
        """
        Initialize the Rover object with its location and assigned spacecraft location.

        Args:
            location (Location): The initial location of the rover.
            space_craft_location (Location): The location of the spacecraft the rover is assigned to.
        """
        super().__init__(location)
        self.__space_craft_location = space_craft_location

    def __repr__(self) -> str:
        """
        Return a string representation of the Rover object.

        Returns:
            str: A string representation of the Rover object.
        """
        return f"Rover({repr(self.get_location())})"

    def __str__(self) -> str:
        """
        Return a string describing the current location of the rover.

        Returns:
            str: A string describing the current location of the rover.
        """
        return f"Rover is located at: ({repr(self.get_location())})"

    def __move_to_random_location(self, mars: Mars):
        """
        Move the rover to a random adjacent location on Mars.

        Args:
            mars (Mars): The Mars environment.
        """
        free_locations = mars.get_free_adjacent_locations(self.get_location())
        random_free_location = random.choice(free_locations)
        previous_location = self.get_location()
        mars.set_agent(self, random_free_location)
        self.set_location(random_free_location)
        mars.set_agent(None, previous_location)

    def act(self, mars: Mars) -> None:
        """
        Execute the rover's action in the simulation.

        The rover moves to a random adjacent location on Mars.

        Args:
            mars (Mars): The Mars environment.
        """
        self.__move_to_random_location(mars)
