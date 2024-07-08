# Find the Winner of the Circular Game
class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        winner = 0
        for i in range(1, n + 1):
            winner = (winner + k) % i
        return winner + 1

  # Example usage:
solution = Solution()
n1, k1 = 5, 2
n2, k2 = 6, 5

print(f"The winner for n = {n1}, k = {k1} is: {solution.findTheWinner(n1, k1)}")
print(f"The winner for n = {n2}, k = {k2} is: {solution.findTheWinner(n2, k2)}")
