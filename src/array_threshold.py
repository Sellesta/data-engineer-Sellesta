from typing import List

def num_of_subarrays(arr: List[int], k: int, threshold: int) -> int:
    """
    Returns the number of sub-arrays of size k whose average is greater than or equal to threshold.
    
    Args:
        arr: List of integers
        k: Size of each subarray
        threshold: The threshold value to compare against
    
    Returns:
        Number of valid subarrays
    """
    # TODO: Implement function
    # Should handle empty arrays, invalid k values, and calculate averages of all k-sized subarrays
    
    if not arr or k <= 0 or k > len(arr):
        return 0
            
    count = 0
    for i in range(len(arr) - k + 1):
        subarray = arr[i:i + k]
        average = sum(subarray) / k
        if average >= threshold:
            count += 1
    return count        
