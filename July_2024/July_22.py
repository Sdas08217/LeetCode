# Sort the people
class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        # Pair names with heights
        paired = list(zip(names, heights))
        # Sort the pairs based on height in descending order
        paired.sort(key=lambda x: x[1], reverse=True)
        # Extract the sorted names
        sorted_names = [name for name, height in paired]
        return sorted_names

# Example usage:
solution = Solution()
names1 = ["Mary","John","Emma"]
heights1 = [180,165,170]
print(solution.sortPeople(names1, heights1))  # Output: ["Mary", "Emma", "John"]

names2 = ["Alice","Bob","Bob"]
heights2 = [155,185,150]
print(solution.sortPeople(names2, heights2))  # Output: ["Bob", "Alice", "Bob"]
