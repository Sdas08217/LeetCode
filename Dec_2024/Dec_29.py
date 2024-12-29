class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Calculate the sum of all windows of size k
        n = len(nums)
        window_sum = [0] * (n - k + 1)
        current_sum = sum(nums[:k])
        window_sum[0] = current_sum
        for i in range(1, len(window_sum)):
            current_sum += nums[i + k - 1] - nums[i - 1]
            window_sum[i] = current_sum
        
        # Step 2: Calculate left_max and right_max indices
        left_max = [0] * len(window_sum)
        max_idx = 0
        for i in range(len(window_sum)):
            if window_sum[i] > window_sum[max_idx]:
                max_idx = i
            left_max[i] = max_idx
        
        right_max = [0] * len(window_sum)
        max_idx = len(window_sum) - 1
        for i in range(len(window_sum) - 1, -1, -1):
            if window_sum[i] >= window_sum[max_idx]:  # >= ensures lexicographical order
                max_idx = i
            right_max[i] = max_idx
        
        # Step 3: Find the maximum sum by iterating over middle interval
        max_sum = 0
        result = [-1, -1, -1]
        for mid in range(k, len(window_sum) - k):
            left = left_max[mid - k]
            right = right_max[mid + k]
            total_sum = window_sum[left] + window_sum[mid] + window_sum[right]
            if total_sum > max_sum:
                max_sum = total_sum
                result = [left, mid, right]
        
        return result
