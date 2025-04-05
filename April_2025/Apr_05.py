class Solution:
    def subsetXORSum(self, nums):
        self.total = 0

        def backtrack(index, curr_xor):
            if index == len(nums):
                self.total += curr_xor
                return
            # Include current number
            backtrack(index + 1, curr_xor ^ nums[index])
            # Exclude current number
            backtrack(index + 1, curr_xor)

        backtrack(0, 0)
        return self.total
