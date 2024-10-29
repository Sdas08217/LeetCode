# Longest Square Streak in an Array
class Solution:
    def longestSquareStreak(self, nums):
        num_set = set(nums)  # Store elements for fast lookups
        max_streak = -1       # Initialize the max streak length
        for num in nums:
            streak_length = 0
            current = num
            # Continue the streak as long as squares exist in the set
            while current in num_set:
                streak_length += 1
                current *= current  # Move to the next square
            # If the streak is at least 2, update the max_streak
            if streak_length >= 2:
                max_streak = max(max_streak, streak_length)
        return max_streak
