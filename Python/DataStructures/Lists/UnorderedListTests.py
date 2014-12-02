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

    def test_elements(self):
        # Elements should be identical when compared
        for i,x in enumerate(self.test_list):
            self.assertTrue(x == self.lst[i])

if __name__ == '__main__':
    unittest.main()
