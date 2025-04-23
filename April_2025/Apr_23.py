class Solution:
    def countLargestGroup(self, n: int) -> int:
        from collections import defaultdict

        def digit_sum(x):
            return sum(int(d) for d in str(x))

        group_count = defaultdict(int)

        for i in range(1, n + 1):
            s = digit_sum(i)
            group_count[s] += 1

        max_size = max(group_count.values())
        return sum(1 for count in group_count.values() if count == max_size)
