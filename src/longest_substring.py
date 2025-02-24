def length_of_longest_substring(s: str) -> int:
    """
    Find the length of the longest substring without repeating characters.
    
    Args:
        s: Input string
    
    Returns:
        Length of the longest substring without repeating characters
    """
    # TODO: Implement function
    # Should handle empty strings, single characters, and strings with repeating characters
    if not s:
        return 0
    start = 0
    end = 0
    max_length = 0
    char_set = set()

    while end < len(s):
        if s[end] not in char_set:
            char_set.add(s[end])
            end += 1
            max_length = max(max_length, len(char_set))
        else:
            char_set.remove(s[start])
            start += 1
    return max_length         
             
    