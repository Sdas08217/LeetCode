# Pass the Pillow
class Solution(object):
    def passThePillow(self, n, time):
        """
        :type n: int
        :type time: int
        :rtype: int
        """
        # Calculate the effective time after removing complete forward and backward passes
        effective_time = time % (2 * (n - 1))
        
        # Determine the direction and position after the effective time
        if effective_time < n:
            # The pillow is moving forward
            return 1 + effective_time
        else:
            # The pillow is moving backward
            return n - (effective_time - (n - 1))

      # Example usage:
sol = Solution()
print(sol.passThePillow(4, 5))  # Output: 2
print(sol.passThePillow(3, 2))  # Output: 3
