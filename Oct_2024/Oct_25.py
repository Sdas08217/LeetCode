# Remove Sub-Folders from the Filesystem
from typing import List

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()  # Sort folders lexicographically
        result = []
        
        # Add the first folder to the result list
        result.append(folder[0])
        
        for i in range(1, len(folder)):
            # Check if the current folder is a sub-folder of the last folder in the result
            if not folder[i].startswith(result[-1] + "/"):
                result.append(folder[i])  # Add to result if it's not a sub-folder
        
        return result
#Example Usage
  # Create an instance of the Solution class
solution = Solution()

# Example 1
folder1 = ["/a", "/a/b", "/c/d", "/c/d/e", "/c/f"]
output1 = solution.removeSubfolders(folder1)
print("Output for Example 1:", output1)  # Expected: ["/a", "/c/d", "/c/f"]

# Example 2
folder2 = ["/a", "/a/b/c", "/a/b/d"]
output2 = solution.removeSubfolders(folder2)
print("Output for Example 2:", output2)  # Expected: ["/a"]

# Example 3
folder3 = ["/a/b/c", "/a/b/ca", "/a/b/d"]
output3 = solution.removeSubfolders(folder3)
print("Output for Example 3:", output3)  # Expected: ["/a/b/c", "/a/b/ca", "/a/b/d"]
