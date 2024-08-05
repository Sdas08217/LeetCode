# Kth Distinct String in an Array
from collections import Counter

class Solution(object):
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """
        # Count the frequency of each string
        freq = Counter(arr)
        
        # Collect the distinct strings
        distinct_strings = [string for string in arr if freq[string] == 1]
        
        # Return the kth distinct string if it exists, otherwise return an empty string
        if k <= len(distinct_strings):
            return distinct_strings[k-1]
        else:
            return ""

#Example Usage   
arr1 = ["d","b","c","b","c","a"]
k1 = 2
arr2 = ["aaa","aa","a"]
k2 = 1
arr3 = ["a","b","a"]
k3 = 3

sol = Solution()
print(sol.kthDistinct(arr1, k1))  # Output: "a"
print(sol.kthDistinct(arr2, k2))  # Output: "aaa"
print(sol.kthDistinct(arr3, k3))  # Output: ""
