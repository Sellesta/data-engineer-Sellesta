import unittest
from src.longest_substring import length_of_longest_substring

class TestLongestSubstring(unittest.TestCase):
    def test_basic_substring_with_repeating_chars(self):
        """Test basic case with repeating characters"""
        self.assertEqual(length_of_longest_substring("abcabcbb"), 3)
        
    def test_all_same_chars(self):
        """Test string with all same characters"""
        self.assertEqual(length_of_longest_substring("bbbbb"), 1)
        
    def test_repeating_chars_with_different_substrings(self):
        """Test string with repeating characters forming different substrings"""
        self.assertEqual(length_of_longest_substring("pwwkew"), 3)
        
    def test_empty_string(self):
        """Test with empty string"""
        self.assertEqual(length_of_longest_substring(""), 0)
        
    def test_single_char(self):
        """Test with single character"""
        self.assertEqual(length_of_longest_substring("a"), 1)
        
    def test_all_unique_chars(self):
        """Test with string containing all unique characters"""
        self.assertEqual(length_of_longest_substring("abcdef"), 6)
        
    def test_repeating_chars_with_gap(self):
        """Test with repeating characters having gaps between them"""
        self.assertEqual(length_of_longest_substring("dvdf"), 3)
        
    def test_space_and_special_chars(self):
        """Test with spaces and special characters"""
        self.assertEqual(length_of_longest_substring("a b c!@#"), 6)
        
    def test_unicode_chars(self):
        """Test with unicode characters"""
        self.assertEqual(length_of_longest_substring("🌟🎈🌟"), 2)
        
    def test_numbers_and_letters(self):
        """Test with mix of numbers and letters"""
        self.assertEqual(length_of_longest_substring("a1b2c3a1"), 6)
        
    def test_case_sensitivity(self):
        """Test case sensitivity"""
        self.assertEqual(length_of_longest_substring("aAbBcC"), 6)
        
    def test_very_long_string(self):
        """Test with a very long string"""
        long_str = "abcdefghijklmnopqrstuvwxyz" * 1000 + "aaa"
        self.assertEqual(length_of_longest_substring(long_str), 26)
        
    def test_alternating_chars(self):
        """Test with alternating characters"""
        self.assertEqual(length_of_longest_substring("ababab"), 2)
        
    def test_substring_at_end(self):
        """Test when longest substring is at the end"""
        self.assertEqual(length_of_longest_substring("aabcd"), 4)
        
    def test_substring_at_start(self):
        """Test when longest substring is at the start"""
        self.assertEqual(length_of_longest_substring("abcaa"), 3)

if __name__ == '__main__':
    unittest.main()