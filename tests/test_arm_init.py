import unittest
from app.arm import Arm


class TestArmInit(unittest.TestCase):
    def test_init_with_valid_type(self):
        arm = Arm("1")
        self.assertEqual(arm.arm_version, 1)

    def test_init_with_float_type(self):
        arm = Arm(1.0)
        self.assertEqual(arm.arm_version, 1)

    def test_init_with_invalid_type(self):
        with self.assertRaises(ValueError):
            Arm(3)

    def test_init_with_empty_type(self):
        with self.assertRaises(ValueError):
            Arm("")

    def test_init_with_none_type(self):
        with self.assertRaises(ValueError):
            Arm(None)


if __name__ == "__main__":
    unittest.main()
