import logging
import re

from app.input_parser import InputParser
from app.arm import Arm

logger = logging.getLogger(__name__)


# this class could interact with a database instead of having the inventory in-memory
class InventoryManager:
    """
    Manager class for the inventory. Stores the inventory state, the initial instructions and an arm.
    """

    def __init__(self, arm_version: int):
        self.inventory = {}
        self.instructions = []
        self.arm_version = arm_version

    def read_instructions(self, instructions_file: str) -> None:

        with open(instructions_file, "r") as file:
            instructions = file.read()

            # Split the instructions file with a regex at the "bottom" keyword.
            inputs = re.split(r"bottom", instructions, maxsplit=1)
            try:
                self.inventory = InputParser.parse_state(inputs[0].rstrip())
                logger.info(f"Initial state:\n{self.inventory}")

                self.instructions = InputParser.parse_instructions(inputs[1].lstrip())
                logger.debug(f"Instructions:\n{self.instructions}")
            except IndexError or ValueError:
                logger.error(f"Instructions file format is incorrect!")
                raise

    def manage_inventory(self, instructions: tuple = None) -> None:
        # this way either the pre-parsed instructions can be used
        # or you can pass custom instructions to it through an interface
        if not instructions:
            self.manage_inventory(self.instructions)

        else:
            for instruction in instructions:
                logger.debug(f"Instruction: {instruction}")
                self.move_boxes(instruction)

    def move_boxes(self, instruction: tuple) -> None:
        arm = Arm(arm_version=self.arm_version)
        arm.move(self.inventory, instruction[0], instruction[1], instruction[2])

    def print_top_boxes(self):
        top_boxes = ""
        for v in self.inventory.values():
            top_boxes += v[-1]

        if len(top_boxes) > 0:
            logger.info(f"Top boxes are: {top_boxes}")

        else:
            logger.info("Inventory is empty!")
