# Maximum Difference by Remapping a Digit
class Solution:
    def minMaxDifference(self, num: int) -> int:
        num_str = str(num)
        max_val = int(num)
        min_val = int(num)

        # Try replacing each digit with 9 to find the maximum possible value
        for d in set(num_str):
            max_candidate = int(num_str.replace(d, '9'))
            max_val = max(max_val, max_candidate)

        # Try replacing each digit with 0 to find the minimum possible value
        for d in set(num_str):
            min_candidate = int(num_str.replace(d, '0'))
            min_val = min(min_val, min_candidate)

        # Return the difference between the maximum and minimum values
        return max_val - min_val
