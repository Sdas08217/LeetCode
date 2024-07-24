# Sort the Jumbled Numbers
class Solution(object):
    def sortJumbled(self, mapping, nums):
        """
        :type mapping: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        def get_mapped_value(num):
            mapped_num = ''.join(str(mapping[int(digit)]) for digit in str(num))
            return int(mapped_num)
        
        return sorted(nums, key=lambda x: get_mapped_value(x))

# Example 1
mapping = [8,9,4,0,2,1,3,5,7,6]
nums = [991, 338, 38]
sol = Solution()
print(sol.sortJumbled(mapping, nums))  # Output: [338, 38, 991]

# Example 2
mapping = [0,1,2,3,4,5,6,7,8,9]
nums = [789, 456, 123]
print(sol.sortJumbled(mapping, nums))  # Output: [123, 456, 789]
