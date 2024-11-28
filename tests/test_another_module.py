import unittest
from src.my_module import add

class TestAnotherModule(unittest.TestCase):

    def test_add_large_numbers(self):
        self.assertEqual(add(1000, 2000), 3000)
        self.assertEqual(add(-1000, -2000), -3000)

    def test_add_edge_cases(self):
        self.assertEqual(add(0, 1000), 1000)
        self.assertEqual(add(0, -1000), -1000)

if __name__ == "__main__":
    unittest.main()
