# Lexicographical Numbers
class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = []
        
        def dfs(curr):
            if curr > n:
                return
            result.append(curr)
            for i in range(10):
                next_num = curr * 10 + i
                if next_num > n:
                    break
                dfs(next_num)
        
        for i in range(1, 10):
            if i > n:
                break
            dfs(i)
        
        return result

# Example usage
solution = Solution()
print(solution.lexicalOrder(13))  # Output: [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]
print(solution.lexicalOrder(2))   # Output: [1, 2]
