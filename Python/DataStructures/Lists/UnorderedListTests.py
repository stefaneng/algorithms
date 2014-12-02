import unittest
import random
from UnorderedList import List

class TestUnorderedListFunctions(unittest.TestCase):
    "Tests the UnorderedList Data Structure"

    def setUp(self):
        self.lst = List()
        self.test_list = range(10)
        for i in self.test_list:
            self.lst.append(i)

    def test_size(self):
        self.assertTrue(len(self.lst) == len(self.test_list))

if __name__ == '__main__':
    unittest.main()