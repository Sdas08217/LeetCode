#Count Hills and Valleys in an Array
class Solution:
    def countHillValley(self, nums):
        # Step 1: Remove consecutive duplicates
        filtered = [nums[0]]
        for num in nums[1:]:
            if num != filtered[-1]:
                filtered.append(num)
        
        # Step 2: Count hills and valleys
        count = 0
        for i in range(1, len(filtered) - 1):
            if filtered[i] > filtered[i - 1] and filtered[i] > filtered[i + 1]:
                count += 1  # Hill
            elif filtered[i] < filtered[i - 1] and filtered[i] < filtered[i + 1]:
                count += 1  # Valley
        return count
