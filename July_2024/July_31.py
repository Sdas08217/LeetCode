# Filling Bookcase Shelves
class Solution(object):
    def minHeightShelves(self, books, shelfWidth):
        """
        :type books: List[List[int]]
        :type shelfWidth: int
        :rtype: int
        """
        n = len(books)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        
        for i in range(1, n + 1):
            total_width = 0
            max_height = 0
            for j in range(i, 0, -1):
                total_width += books[j-1][0]
                if total_width > shelfWidth:
                    break
                max_height = max(max_height, books[j-1][1])
                dp[i] = min(dp[i], dp[j-1] + max_height)
        
        return dp[n]

# Example usage
solution = Solution()
books1 = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]]
shelfWidth1 = 4
print(solution.minHeightShelves(books1, shelfWidth1))  # Output: 6

books2 = [[1,3],[2,4],[3,2]]
shelfWidth2 = 6
print(solution.minHeightShelves(books2, shelfWidth2))  # Output: 4
