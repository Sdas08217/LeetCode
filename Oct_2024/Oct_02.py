# Rank Transform of an Array
class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        # Step 1: Sort the unique elements
        sorted_unique = sorted(set(arr))
        
        # Step 2: Map each element to its rank
        rank_map = {val: rank + 1 for rank, val in enumerate(sorted_unique)}
        
        # Step 3: Replace each element in the original array with its rank
        return [rank_map[num] for num in arr]

# Example usage:
arr = [40, 10, 20, 30]
solution = Solution()
print(solution.arrayRankTransform(arr))  # Output: [4, 1, 2, 3]
