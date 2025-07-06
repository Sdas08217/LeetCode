from collections import Counter

class FindSumPairs:

    def __init__(self, nums1, nums2):
        self.nums1 = nums1
        self.nums2 = nums2
        self.counter2 = Counter(nums2)

    def add(self, index, val):
        old_val = self.nums2[index]
        new_val = old_val + val
        self.counter2[old_val] -= 1
        if self.counter2[old_val] == 0:
            del self.counter2[old_val]
        self.nums2[index] = new_val
        self.counter2[new_val] += 1

    def count(self, tot):
        count = 0
        for num in self.nums1:
            complement = tot - num
            count += self.counter2.get(complement, 0)
        return count
