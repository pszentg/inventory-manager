import unittest
from typing import Dict
from app.arm import Arm


class TestArmMoveWithStringInventory(unittest.TestCase):
    def setUp(self):
        self.arm_v1 = Arm(1)
        self.arm_v2 = Arm(2)

    def test_move_v1_single_box(self):
        inventory: Dict[int, str] = {1: "A", 2: ""}
        expected_inventory = {1: "", 2: "A"}
        self.assertEqual(self.arm_v1.move_v1(inventory, 1, 1, 2), expected_inventory)

    def test_move_v1_multiple_boxes(self):
        inventory: Dict[int, str] = {1: "ABC", 2: ""}
        expected_inventory = {1: "A", 2: "CB"}
        self.assertEqual(self.arm_v1.move_v1(inventory, 2, 1, 2), expected_inventory)

    def test_move_v1_from_empty_stack(self):
        inventory: Dict[int, str] = {1: "", 2: "A"}
        with self.assertRaises(IndexError):
            self.arm_v1.move_v1(inventory, 1, 1, 2)

    def test_move_v1_invalid_from_stack(self):
        inventory: Dict[int, str] = {1: "A", 2: ""}
        with self.assertRaises(KeyError):
            self.arm_v1.move_v1(inventory, 1, 10, 2)

    def test_move_v1_invalid_to_stack(self):
        inventory: Dict[int, str] = {1: "A", 2: ""}
        with self.assertRaises(KeyError):
            self.arm_v1.move_v1(inventory, 1, 1, 20)

    def test_move_v2_single_box(self):
        inventory: Dict[int, str] = {1: "A", 2: ""}
        expected_inventory = {1: "", 2: "A"}
        self.assertEqual(self.arm_v2.move_v2(inventory, 1, 1, 2), expected_inventory)

    def test_move_v2_multiple_boxes(self):
        inventory: Dict[int, str] = {1: "ABC", 2: ""}
        expected_inventory = {1: "A", 2: "BC"}
        self.assertEqual(self.arm_v2.move_v2(inventory, 2, 1, 2), expected_inventory)

    def test_move_v2_from_empty_stack(self):
        inventory: Dict[int, str] = {1: "", 2: "A"}
        with self.assertRaises(ValueError):
            self.arm_v2.move_v2(inventory, 1, 1, 2)

    def test_move_v2_invalid_from_stack(self):
        inventory: Dict[int, str] = {1: "A", 2: ""}
        with self.assertRaises(KeyError):
            self.arm_v2.move_v2(inventory, 1, 10, 2)

    def test_move_v2_invalid_to_stack(self):
        inventory: Dict[int, str] = {1: "A", 2: ""}
        with self.assertRaises(KeyError):
            self.arm_v2.move_v2(inventory, 1, 1, 20)


if __name__ == "__main__":
    unittest.main()
