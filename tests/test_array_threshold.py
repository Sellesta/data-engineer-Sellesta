import unittest
from src.array_threshold import num_of_subarrays

class TestArrayThreshold(unittest.TestCase):
    def test_consecutive_numbers_with_threshold_4(self):
        """Test with consecutive repeated numbers and higher numbers at end"""
        arr = [2,2,2,2,5,5,5,8]
        k = 3
        threshold = 4
        self.assertEqual(num_of_subarrays(arr, k, threshold), 3)
        
    def test_descending_numbers_with_threshold_5(self):
        """Test with mostly descending sequence of numbers"""
        arr = [11,13,17,23,29,31,7,5,2,3]
        k = 3
        threshold = 5
        self.assertEqual(num_of_subarrays(arr, k, threshold), 6)
        
    def test_empty_array(self):
        """Test with empty array"""
        self.assertEqual(num_of_subarrays([], 3, 4), 0)
        
    def test_k_larger_than_array(self):
        """Test when k is larger than array length"""
        self.assertEqual(num_of_subarrays([1,2,3], 4, 2), 0)
        
    def test_exact_threshold(self):
        """Test when subarrays have exactly the threshold average"""
        arr = [4,4,4,4]
        k = 2
        threshold = 4
        self.assertEqual(num_of_subarrays(arr, k, threshold), 3)

    def test_negative_numbers(self):
        """Test with negative numbers in array"""
        arr = [-1,-2,-3,0,1,2]
        k = 3
        threshold = -1
        self.assertEqual(num_of_subarrays(arr, k, threshold), 2)

    def test_k_equals_one(self):
        """Test when k=1 (each element is a subarray)"""
        arr = [1,2,3,4,5]
        k = 1
        threshold = 3
        self.assertEqual(num_of_subarrays(arr, k, threshold), 3)

    def test_k_equals_array_length(self):
        """Test when k equals array length"""
        arr = [1,2,3]
        k = 3
        threshold = 2
        self.assertEqual(num_of_subarrays(arr, k, threshold), 1)

    def test_large_numbers(self):
        """Test with very large numbers"""
        arr = [1000000,1000000,1000000,1]
        k = 2
        threshold = 900000
        self.assertEqual(num_of_subarrays(arr, k, threshold), 2)

    def test_zero_threshold(self):
        """Test with zero threshold"""
        arr = [-2,-1,0,1,2]
        k = 2
        threshold = 0
        self.assertEqual(num_of_subarrays(arr, k, threshold), 2)

    def test_invalid_k(self):
        """Test with invalid k values"""
        arr = [1,2,3,4]
        self.assertEqual(num_of_subarrays(arr, 0, 1), 0)
        self.assertEqual(num_of_subarrays(arr, -1, 1), 0)

if __name__ == '__main__':
    unittest.main()