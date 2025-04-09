class Solution:
    def minOperations(self, nums, k):
        if any(num < k for num in nums):
            return -1  # Can't increase to k

        from collections import Counter

        count = Counter(nums)
        # Only values greater than k are relevant
        values = [val for val in count if val > k]
        if not values:
            return 0 if all(num == k for num in nums) else -1

        values.sort(reverse=True)  # Descending
        operations = 0
        current_total = 0  # How many values we're tracking above current h

        for i in range(len(values)):
            current_val = values[i]
            current_total += count[current_val]

            # Check if all values above next are equal
            next_val = values[i + 1] if i + 1 < len(values) else k

            # Valid operation step: all above next_val are current_val
            operations += 1

            if next_val == k:
                break

        return operations
