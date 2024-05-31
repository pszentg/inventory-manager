from typing import Dict

import logging

logger = logging.getLogger(__name__)


class Arm:
    """
    This class represents the robotic arm that moves boxes in the inventory
    """

    def __init__(self, arm_version: str) -> None:
        if (
            arm_version is None
            or arm_version == ""
            or (int(arm_version) != 1 and int(arm_version) != 2)
        ):
            raise ValueError("Invalid arm version")
        self.arm_version = int(arm_version)

    def move(
        self, inventory: Dict[int, str], move: int, pos_from: int, pos_to: int
    ) -> Dict:
        if self.arm_version == 1:
            self.move_v1(inventory, move, pos_from, pos_to)
        elif self.arm_version == 2:
            self.move_v2(inventory, move, pos_from, pos_to)

    def move_v1(
        self, inventory: Dict[int, str], move: int, pos_from: int, pos_to: int
    ) -> Dict:
        for _ in range(0, move):
            try:
                box = inventory[pos_from][-1]
                inventory[pos_from] = inventory[pos_from][:-1]
                inventory[pos_to] += box
            except IndexError:
                logger.error(
                    f"Stack {pos_from} is either empty or stack numbers are invalid!"
                )
                raise
        return inventory

    def move_v2(
        self, inventory: Dict[int, str], move: int, pos_from: int, pos_to: int
    ) -> Dict:
        # get the "move" amount of boxes from the inventory
        box = inventory[pos_from][-move:]

        if box == "":
            raise ValueError(f"There's no boxes left to move at position {pos_from}")

        # remove it from the pos_from stack and move it to the pos_to stack
        try:
            inventory[pos_from] = inventory[pos_from][:-move]
        except KeyError:
            raise KeyError(f"{pos_from} is not a valid stack to move boxes from!")

        try:
            inventory[pos_to] += box
        except KeyError:
            raise KeyError(f"{pos_to} is not a valid stack to move boxes to!")
        return inventory
