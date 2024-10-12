# Divide Intervals Into Minimum Number of Groups
class Solution(object):
    def minGroups(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        events = []

        # For each interval, add start and end events
        for left, right in intervals:
            events.append((left, 1))       # Start of interval
            events.append((right + 1, -1)) # End of interval (exclusive end)

        # Sort events first by time, then by type (-1 end before +1 start if equal time)
        events.sort()

        active_intervals = 0
        max_groups = 0

        # Sweep through events
        for time, event_type in events:
            active_intervals += event_type
            max_groups = max(max_groups, active_intervals)

        return max_groups

  # Example usage
intervals = [[5, 10], [6, 8], [1, 5], [2, 3], [1, 10]]

solution = Solution()
result = solution.minGroups(intervals)
print("Minimum number of groups:", result)
