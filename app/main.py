import argparse
import os

from app.inventory_manager import InventoryManager

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

PROJECT_ROOT = os.path.join(os.path.dirname(os.path.dirname(__file__)))


def main(instructions_file: str, arm_version: int) -> None:
    inventory_manager = InventoryManager(arm_version)
    inventory_manager.read_instructions(instructions_file)
    inventory_manager.manage_inventory()
    logger.info(f"Final state:\n{inventory_manager.inventory}")
    inventory_manager.print_top_boxes()


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Run the main script")
    parser.add_argument(
        "-i", "--instructions", required=True, help="Path to the instructions file"
    )
    parser.add_argument(
        "-v", "--version", required=True, help="Arm version number to use"
    )

    args = parser.parse_args()
    instructions_file = args.instructions
    arm_version = int(args.version)
    if arm_version != 1 and arm_version != 2:
        raise ValueError("Invalid arm version")

    logger.info(f"Arm version is set to: {arm_version}")

    if os.path.exists(os.path.join(PROJECT_ROOT, f"resources/{args.instructions}")):
        instructions_file = os.path.join(PROJECT_ROOT, f"resources/{args.instructions}")
    try:
        main(instructions_file, arm_version)
    except Exception as e:
        logger.info("There was an error parsing the instructions.")
        logger.info(f"{e}")
