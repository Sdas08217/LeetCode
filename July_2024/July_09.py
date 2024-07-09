# Average Waiting Time
class Solution(object):
    def averageWaitingTime(self, customers):
        total_waiting_time = 0
        current_time = 0
        
        for arrival, time in customers:
            if current_time < arrival:
                current_time = arrival
            waiting_time = current_time + time - arrival
            total_waiting_time += waiting_time
            current_time += time
        
        return float(total_waiting_time) / len(customers)

  # Example usage:
sol = Solution()
customers1 = [[1, 2], [2, 5], [4, 3]]
customers2 = [[5, 2], [5, 4], [10, 3], [20, 1]]
print(sol.averageWaitingTime(customers1))  # Output: 5.0
print(sol.averageWaitingTime(customers2))  # Output: 3.25
