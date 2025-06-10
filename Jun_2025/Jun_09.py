class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def count_prefix(n, prefix):
            curr = prefix
            next_ = prefix + 1
            count = 0
            while curr <= n:
                count += min(n + 1, next_) - curr
                curr *= 10
                next_ *= 10
            return count

        curr = 1
        k -= 1

        while k > 0:
            count = count_prefix(n, curr)
            if count <= k:
                k -= count
                curr += 1
            else:
                k -= 1
                curr *= 10

        return curr
