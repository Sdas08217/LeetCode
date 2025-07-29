from typing import List

class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [0] * n
        or_map = {}  # or_value: minimum end_index for that or_value
        max_or = 0

        for i in range(n - 1, -1, -1):
            new_map = {}
            max_or |= nums[i]
            new_map[nums[i]] = i

            for prev_or, end in or_map.items():
                new_or = prev_or | nums[i]
                if new_or in new_map:
                    new_map[new_or] = min(new_map[new_or], end)
                else:
                    new_map[new_or] = end

            or_map = new_map
            answer[i] = or_map[max_or] - i + 1

        return answer
