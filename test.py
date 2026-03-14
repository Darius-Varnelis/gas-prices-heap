import unittest
from gas_prices import *

class TestMinHeap(unittest.TestCase):

    def setUp(self):
        """Creates a new clean heap and dictionary for every single test."""
        self.heap = MinHeap()
        stationDictionary.clear()

    def test_insert_and_get_min(self):
        self.heap.insert(['LT0001', 'Circle K Fabijoniškės', 'Viada', '', '','', 'Gasoline 95', '1.65'])
        self.heap.insert(['LT0002', 'Viada Fabijoniškės', 'Viada', '', '', '', 'Gasoline 95', '1.50'])
        self.assertEqual(self.heap.get_min_price(), ('LT0002', 'Viada Fabijoniškės','Gasoline 95', 1.50))

    def test_price_update(self):
        self.heap.insert(['LT0001', 'Circle K Fabijoniškės', 'Viada', '', '', '', 'Gasoline 95', '1.65'])
        self.heap.insert(['LT0001', 'Circle K Fabijoniškės', 'Viada', '', '', '', 'Gasoline 95', '1.40'])
        self.assertEqual(self.heap.get_min_price(), ('LT0001', 'Circle K Fabijoniškės', 'Gasoline 95', 1.4))

    def test_empty_heap_returns_none(self):
        self.assertIsNone(self.heap.get_min_price())

    def test_pop_removes_element(self):
        self.heap.insert(['LT0001', 'Circle K Fabijoniškės', 'Viada', '', '', '', 'Gasoline 95', '1.65'])
        self.heap.insert(['LT0002', 'Viada Fabijoniškės', 'Viada', '', '', '', 'Gasoline 95', '1.50'])
        self.heap.pop_min()
        self.assertEqual(self.heap.get_min_price(), ('LT0001','Circle K Fabijoniškės', 'Gasoline 95', 1.65))

    def test_empty_heap_pop_returns_none(self):
        self.assertIsNone(self.heap.pop_min())


if __name__ == "__main__":
    unittest.main()
