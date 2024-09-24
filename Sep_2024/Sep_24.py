# Find the Length of the Longest Common Prefix
class Solution:
    def longestCommonPrefix(self, arr1, arr2):
        # Helper function to find the common prefix length between two strings
        def commonPrefixLength(str1, str2):
            min_length = min(len(str1), len(str2))
            for i in range(min_length):
                if str1[i] != str2[i]:
                    return i
            return min_length

        # Step 1: Convert numbers to strings and sort the arrays
        arr1_str = sorted([str(num) for num in arr1])
        arr2_str = sorted([str(num) for num in arr2])

        # Step 2: Initialize pointers and the maximum common prefix length
        max_prefix_length = 0
        i, j = 0, 0

        # Step 3: Use two-pointer technique to find the longest common prefix
        while i < len(arr1_str) and j < len(arr2_str):
            prefix_length = commonPrefixLength(arr1_str[i], arr2_str[j])
            max_prefix_length = max(max_prefix_length, prefix_length)

            # Step 4: Move the pointer that corresponds to the smaller number lexicographically
            if arr1_str[i] < arr2_str[j]:
                i += 1
            else:
                j += 1

        return max_prefix_length

  # Example usage
if __name__ == "__main__":
    solution = Solution()
    
    arr1 = [123, 1245, 1234]
    arr2 = [1233, 1248, 1235]
    
    result = solution.longestCommonPrefix(arr1, arr2)
    print(f"The length of the longest common prefix is: {result}")
