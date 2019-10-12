import unittest
from fun_with_collections import set_membership as sm


class MyTestCase(unittest.TestCase):
    def test_in_set_true(self):
        self.assertEqual(sm.in_set((1, 2, 3, 4), 3), True)

    def test_in_set_false(self):
        self.assertEqual(sm.in_set((2, 4, 6, 8), 10), False)


if __name__ == '__main__':
    unittest.main()
