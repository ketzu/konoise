import unittest
import random
from ko_noiser import Konoise


class TestKonoise(unittest.TestCase):
    def setUp(self) -> None:
        random.seed(15)
        self.noise = Konoise()
        return super().setUp()
    
    def test_proces(self):
        test = '나는 집을 깨끗이 청소했다.'
        self.assertEqual(self.noise.process(test), ' 나는 집을 깨끗이 청소했다.')

if __name__ == '__main__':
    unittest.main()