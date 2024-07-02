# Intersection of Two Arrays II
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # Create dictionaries to count occurrences in both arrays
        counts1 = {}
        counts2 = {}

        for num in nums1:
            if num in counts1:
                counts1[num] += 1
            else:
                counts1[num] = 1

        for num in nums2:
            if num in counts2:
                counts2[num] += 1
            else:
                counts2[num] = 1

        # Find the intersection based on the counts
        intersection = []

        for num in counts1:
            if num in counts2:
                # Add the number min(counts1[num], counts2[num]) times to the intersection
                intersection.extend([num] * min(counts1[num], counts2[num]))

        return intersection

# Example usage:
solution = Solution()
print(solution.intersect([1, 2, 2, 1], [2, 2]))  # Output: [2, 2]
print(solution.intersect([4, 9, 5], [9, 4, 9, 8, 4]))  # Output: [4, 9]
