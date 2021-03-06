import unittest

from combination import Combination


class TestCombination(unittest.TestCase):
    def setUp(self):
        self.comb = Combination(1000)

    def tearDown(self):
        pass

    def test_nCr(self):
        self.assertEqual(538992043, self.comb.nCr(100, 50))

    def test_nPr(self):
        self.assertEqual(505671657, self.comb.nPr(100, 50))

    def test_nHr(self):
        self.assertEqual(475860182, self.comb.nHr(100, 50))

    def test_rising_factorial(self):
        self.assertEqual(646654562, self.comb.rising_factorial(100, 50))

    def test_stirling_first(self):
        self.assertEqual(269325, self.comb.stirling_first(10, 5))

    def test_stirling_second(self):
        self.assertEqual(260006047, self.comb.stirling_second(100, 50))

    def test_balls_and_boxes_3(self):
        self.assertEqual(522986130, self.comb.balls_and_boxes_3(100, 50))

    def test_bernoulli(self):
        self.assertEqual(348484851, self.comb.bernoulli(10))

    def test_faulhaber(self):
        self.assertEqual(1108650, self.comb.faulhaber(10, 5))

    def test_lah(self):
        self.assertEqual(292877136, self.comb.lah(100, 50))

    def test_bell(self):
        self.assertEqual(772898722, self.comb.bell(100, 50))


if __name__ == '__main__':
    unittest.main()
