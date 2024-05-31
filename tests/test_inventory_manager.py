import os
import unittest
from unittest import mock
from unittest.mock import mock_open, patch
from app.inventory_manager import InventoryManager
from app.input_parser import InputParser

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
VALID_INSTRUCTIONS_PATH = os.path.join(PROJECT_ROOT, "test_set.txt")


class TestInventoryManager(unittest.TestCase):

    def test_read_instructions_success(self):
        read_data = "|A|\n1\nbottom\nmove 1 from 1 to 1"
        mock_open = mock.mock_open(read_data=read_data)

        with mock.patch("builtins.open", mock_open):
            inventory_manager = InventoryManager(arm_version=1)
            inventory_manager.read_instructions(VALID_INSTRUCTIONS_PATH)

        self.assertEqual(
            inventory_manager.inventory, InputParser.parse_state("|A| \n1")
        )
        self.assertEqual(
            inventory_manager.instructions,
            InputParser.parse_instructions("move 1 from 1 to 1"),
        )

    @patch("builtins.open", new_callable=mock_open, read_data="|A|\n1")
    def test_read_instructions_no_bottom_keyword(self, mock_file):
        inventory_manager = InventoryManager(arm_version=1)
        with self.assertRaises(IndexError):
            inventory_manager.read_instructions(VALID_INSTRUCTIONS_PATH)

    @patch("builtins.open", new_callable=mock_open, read_data="")
    def test_read_instructions_empty_file(self, mock_file):
        inventory_manager = InventoryManager(arm_version=1)
        with self.assertRaises(ValueError):
            inventory_manager.read_instructions(VALID_INSTRUCTIONS_PATH)

    @patch(
        "builtins.open",
        new_callable=mock_open,
        read_data="initial_state bottom",
    )
    def test_read_instructions_no_instructions(self, mock_file):
        with self.assertRaises(ValueError):
            inventory_manager = InventoryManager(arm_version=1)
            inventory_manager.read_instructions(VALID_INSTRUCTIONS_PATH)


if __name__ == "__main__":
    unittest.main()
