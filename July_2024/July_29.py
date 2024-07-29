# Count Number of Teams
class Solution(object):
    def numTeams(self, rating):
        """
        :type rating: List[int]
        :rtype: int
        """
        n = len(rating)
        count = 0

        for j in range(n):
            less_left = greater_left = 0
            less_right = greater_right = 0

            for i in range(j):
                if rating[i] < rating[j]:
                    less_left += 1
                elif rating[i] > rating[j]:
                    greater_left += 1
            
            for k in range(j + 1, n):
                if rating[k] < rating[j]:
                    less_right += 1
                elif rating[k] > rating[j]:
                    greater_right += 1

            count += less_left * greater_right + greater_left * less_right

        return count

# Example usage:
solution = Solution()

# Example 1
rating = [2, 5, 3, 4, 1]
print(solution.numTeams(rating))  # Output: 3

# Example 2
rating = [2, 1, 3]
print(solution.numTeams(rating))  # Output: 0

# Example 3
rating = [1, 2, 3, 4]
print(solution.numTeams(rating))  # Output: 4
