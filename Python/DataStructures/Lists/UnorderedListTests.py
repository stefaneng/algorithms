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
        # Empty list should have length zero
        self.assertTrue(len(List()) == 0)

        # Compare builtin list length to UnorderedList Length
        self.assertTrue(len(self.lst) == len(self.test_list))

if __name__ == '__main__':
    unittest.main()
