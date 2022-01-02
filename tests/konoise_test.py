import unittest
import random
from konoise import Konoise


class TestKonoise(unittest.TestCase):
    def setUp(self) -> None:
        random.seed(15)
        self.noise = Konoise()
        return super().setUp()
    
    def test_proces(self):
        test = '나는 집을 깨끗이 청소했다.'
        self.assertEqual(self.noise.process(test), '나는 집을 깨끋이 청소핻다.')
