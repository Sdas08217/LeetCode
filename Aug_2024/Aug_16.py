# Maximum Distance in Arrays
class Solution(object):
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        # Initialize with the first array's min and max
        min_val = arrays[0][0]
        max_val = arrays[0][-1]
        max_distance = 0

        # Iterate over the remaining arrays
        for i in range(1, len(arrays)):
            current_min = arrays[i][0]
            current_max = arrays[i][-1]

            # Calculate distance with the current array's max and previous min
            max_distance = max(max_distance, abs(current_max - min_val))
            # Calculate distance with the current array's min and previous max
            max_distance = max(max_distance, abs(current_min - max_val))

            # Update the global min and max values
            min_val = min(min_val, current_min)
            max_val = max(max_val, current_max)

        return max_distance

  # Example Usage
  sol = Solution()
print(sol.maxDistance([[1, 2, 3], [4, 5], [1, 2, 3]]))  # Output: 4
print(sol.maxDistance([[1], [1]]))  # Output: 0
