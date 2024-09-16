# Minimum Time Difference
class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :param timePoints: List of strings representing time points
        :return: Minimum difference in minutes between any two time points
        """
        # Helper function to convert HH:MM to minutes
        def timeToMinutes(time):
            hours, minutes = map(int, time.split(":"))
            return hours * 60 + minutes
        
        # Convert all time points to minutes
        minutesList = [timeToMinutes(time) for time in timePoints]
        
        # Sort the list of minutes
        minutesList.sort()
        
        # Initialize the minimum difference to be large
        minDiff = float('inf')
        
        # Compare adjacent time points in the sorted list
        for i in range(1, len(minutesList)):
            minDiff = min(minDiff, minutesList[i] - minutesList[i - 1])
        
        # Handle the circular time wraparound (between last and first time points)
        minDiff = min(minDiff, 1440 - (minutesList[-1] - minutesList[0]))
        
        return minDiff

  # Example usage
timePoints = ["23:59", "00:00"]
solution = Solution()
result = solution.findMinDifference(timePoints)
print("Minimum difference in minutes:", result)
