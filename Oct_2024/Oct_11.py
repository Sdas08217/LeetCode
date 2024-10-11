# The Number of the Smallest Unoccupied Chair
import heapq

class Solution:
    def smallestChair(self, times, targetFriend):
        n = len(times)
        # Add index to each friend's times for identifying the targetFriend
        times_with_index = [(times[i][0], times[i][1], i) for i in range(n)]
        
        # Sort friends by their arrival time
        times_with_index.sort()

        # Min-heap to keep track of available chairs
        available_chairs = []
        
        # Priority queue to track friends who will leave, sorted by leaving time
        leaving_friends = []
        
        # Initially, all chairs are available, we assume chairs start from 0
        for i in range(n):
            heapq.heappush(available_chairs, i)
        
        # Iterate over the friends sorted by arrival time
        for arrival, leaving, friend_index in times_with_index:
            # Release any chairs of friends who have left before the current arrival time
            while leaving_friends and leaving_friends[0][0] <= arrival:
                leave_time, chair = heapq.heappop(leaving_friends)
                heapq.heappush(available_chairs, chair)
            
            # The friend will sit on the smallest available chair
            chair = heapq.heappop(available_chairs)
            
            # If the current friend is the target friend, return the chair number
            if friend_index == targetFriend:
                return chair
            
            # Add the current friend and their chair to the leaving_friends queue
            heapq.heappush(leaving_friends, (leaving, chair))

        return -1

  # Example usage
times = [[1, 4], [2, 3], [4, 6]]
targetFriend = 1

sol = Solution()
result = sol.smallestChair(times, targetFriend)
print(f"The chair assigned to the target friend is: {result}")
