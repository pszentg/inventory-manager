import unittest
from app.inventory_manager import InventoryManager


class TestInventoryManagerInit(unittest.TestCase):

    def test_init_with_valid_arm_version(self):
        # Arrange
        arm_version = 1

        # Act
        inventory_manager = InventoryManager(arm_version)

        # Assert
        self.assertEqual(inventory_manager.inventory, {})
        self.assertEqual(inventory_manager.instructions, [])
        self.assertEqual(inventory_manager.arm_version, arm_version)


if __name__ == "__main__":
    unittest.main()
