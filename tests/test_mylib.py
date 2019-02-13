import unittest

from mylib.my_sum import my_sum, MySum

class TestMyLib(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = my_sum(data)
        self.assertEqual(result, 6)
        result2 = MySum.my_sum(data)
        self.assertEqual(result, result2)

if __name__ == '__main__':
        unittest.main()