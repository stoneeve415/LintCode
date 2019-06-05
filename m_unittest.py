import unittest
from sort import *
from _46_major_element import *


class TestSort(unittest.TestCase):
    """Test sort.py"""

    def setUp(self):
        """init"""
        self.nums = [5, 2, 5, 1, 9, 7, 22, 4]
        self.res = [1, 2, 4, 5, 5, 7, 9, 22]

    def test_bubble(self):
        """Test bubble sort"""
        self.assertEqual(bubble(self.nums), self.res)
        #self.assertEqual(bubble(self.nums), self.res)

    def test_select(self):
        """Test select sort"""
        self.assertEqual(select(self.nums), self.res)

    def test_insert(self):
        """Test insert sort"""
        self.assertEqual(insert(self.nums), self.res)

    def test_quick(self):
        """Test quick sort"""
        self.assertEqual(quick(self.nums), self.res)

    def test_merge(self):
        """Test merge sort"""
        self.assertEqual(merge(self.nums), self.res)

    def test_shell(self):
        """Test shell sort"""
        self.assertEqual(shell(self.nums), self.res)

    def tearDown(self):
        """finally"""
        print('test sort over')


class TestMajorElement(unittest.TestCase):
    def setUp(self):
        """init"""
        self.nums = [1, 1, 1, 1, 2, 2, 2]
        self.res = 1

    def test_major(self):
        """test major"""
        self.assertEqual(major1(self.nums), self.res)

    def tearDown(self):
        """finally"""
        print('test major over')


if __name__ == '__main__':
    # suite = unittest.TestSuite()
    # runner = unittest.TextTestRunner()
    # suite.addTest(TestMajorElement('test_major'))
    # runner.run(suite)
    unittest.main()

