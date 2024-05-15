from __future__ import annotations

from typing import List, TYPE_CHECKING

from model.agent import Agent
from model.rover import Rover

if TYPE_CHECKING:
    from model.location import Location
    from model.mars import Mars


class Spacecraft(Agent):

    def __init__(self, location: Location):
        super().__init__(location)

    def act(self, mars: Mars) -> None:
        found_rovers = self.__scan_for_rovers_in_adjacent_cells(mars)
        print(f"Spacecraft detected the following rovers:\n{found_rovers}")

    def __scan_for_rovers_in_adjacent_cells(self, mars) -> List[Rover]:
        """
        Scans adjacent cells for rovers and returns a list of found rovers.
        """
        adjacent_locations = mars.get_adjacent_locations(self.get_location())
        found_rovers = []
        for adjacent_location in adjacent_locations:
            agent = mars.get_agent(adjacent_location)
            if isinstance(agent, Rover):
                found_rovers.append(agent)
        return found_rovers
