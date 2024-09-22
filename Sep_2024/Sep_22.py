# K-th Smallest in Lexicographical Order
class Solution(object):
    def findKthNumber(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        def count_steps(curr, n):
            steps = 0
            first, last = curr, curr
            while first <= n:
                steps += min(n + 1, last + 1) - first
                first *= 10
                last = last * 10 + 9
            return steps

        curr = 1
        k -= 1  # We start from 1, so we decrease k by 1
        while k > 0:
            steps = count_steps(curr, n)
            if steps <= k:
                k -= steps
                curr += 1
            else:
                curr *= 10
                k -= 1
        return curr
#Example usage
# Create an instance of the Solution class
solution = Solution()

# Example 1:
n = 13
k = 2
result = solution.findKthNumber(n, k)
print(f"The {k}th lexicographically smallest number in the range [1, {n}] is: {result}")

# Example 2:
n = 1
k = 1
result = solution.findKthNumber(n, k)
print(f"The {k}th lexicographically smallest number in the range [1, {n}] is: {result}")
