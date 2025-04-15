from typing import List

class FenwickTree:
    def __init__(self, size):
        self.size = size + 2
        self.tree = [0] * self.size

    def update(self, i, delta):
        i += 1  # BIT is 1-indexed
        while i < self.size:
            self.tree[i] += delta
            i += i & -i

    def query(self, i):
        i += 1
        res = 0
        while i > 0:
            res += self.tree[i]
            i -= i & -i
        return res

class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        
        # Map each value to its index in nums2
        pos_in_nums2 = [0] * n
        for i in range(n):
            pos_in_nums2[nums2[i]] = i
        
        # Transform nums1 into their indices in nums2
        arr = [pos_in_nums2[val] for val in nums1]

        # Count left_smaller[i] using Fenwick Tree
        left_tree = FenwickTree(n)
        left_smaller = [0] * n
        for i in range(n):
            left_smaller[i] = left_tree.query(arr[i] - 1)
            left_tree.update(arr[i], 1)

        # Count right_larger[i] using Fenwick Tree
        right_tree = FenwickTree(n)
        right_larger = [0] * n
        for i in range(n - 1, -1, -1):
            right_larger[i] = right_tree.query(n - 1) - right_tree.query(arr[i])
            right_tree.update(arr[i], 1)

        # Final count of good triplets
        total = 0
        for i in range(n):
            total += left_smaller[i] * right_larger[i]
        
        return total
