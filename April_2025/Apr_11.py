class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        for num in range(low, high + 1):
            s = str(num)
            if len(s) % 2 == 0:
                mid = len(s) // 2
                left = s[:mid]
                right = s[mid:]
                if sum(int(d) for d in left) == sum(int(d) for d in right):
                    count += 1
        return count
