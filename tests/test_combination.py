import unittest

from combination import Combination


class TestCombination(unittest.TestCase):
    def setUp(self):
        self.comb = Combination(100)

    def tearDown(self):
        pass

    def test_nCr(self):
        self.assertEqual(538992043, self.comb.nCr(100, 50))


if __name__ == '__main__':
    unittest.main()
