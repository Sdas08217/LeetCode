# Crawler Log Folder
class Solution(object):
    def minOperations(self, logs):
        """
        :type logs: List[str]
        :rtype: int
        """
        depth = 0
        for log in logs:
            if log == "../":
                if depth > 0:
                    depth -= 1
            elif log != "./":
                depth += 1
        return depth

  # Example usage:
solution = Solution()
logs1 = ["d1/", "d2/", "../", "d21/", "./"]
logs2 = ["d1/", "d2/", "./", "d3/", "../", "d31/"]
logs3 = ["d1/", "../", "../", "../"]

print(solution.minOperations(logs1))  # Output: 2
print(solution.minOperations(logs2))  # Output: 3
print(solution.minOperations(logs3))  # Output: 0
