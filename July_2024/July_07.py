# Water Bottles
class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        total_drunk = numBottles
        empty_bottles = numBottles

        while empty_bottles >= numExchange:
            new_bottles = empty_bottles // numExchange
            total_drunk += new_bottles
            empty_bottles = empty_bottles % numExchange + new_bottles

        return total_drunk

# Example usage:
solution = Solution()
print(solution.numWaterBottles(9, 3))  # Output: 13
print(solution.numWaterBottles(15, 4)) # Output: 19
