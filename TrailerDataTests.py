import unittest
from utils.TrailerData import TrailerData

class TestTrailerData(unittest.TestCase):
    def test_config_load(self):
        td = TrailerData()

        self.assertEqual(td.width, 100)
        self.assertEqual(td.height, 200)
        self.assertEqual(td.depth, 300)
        self.assertEqual(td.unit, 'meter')

if __name__ == '__main__':
    unittest.main()
