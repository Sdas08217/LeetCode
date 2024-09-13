# XOR Queries of a Subarray
class Solution(object):
    def xorQueries(self, arr, queries):
        """
        :type arr: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        # Step 1: Build the prefix XOR array
        n = len(arr)
        prefixXOR = [0] * n
        prefixXOR[0] = arr[0]
        
        for i in range(1, n):
            prefixXOR[i] = prefixXOR[i - 1] ^ arr[i]
        
        # Step 2: Answer each query using the prefix XOR array
        result = []
        for left, right in queries:
            if left == 0:
                result.append(prefixXOR[right])
            else:
                result.append(prefixXOR[right] ^ prefixXOR[left - 1])
        
        return result

#Example Usage
# Create an instance of the Solution class
sol = Solution()

# Define the array and queries
arr = [1, 3, 4, 8]
queries = [[0, 1], [1, 2], [0, 3], [3, 3]]

# Call the xorQueries method and print the result
result = sol.xorQueries(arr, queries)
print(result)  # Output: [2, 7, 14, 8]
