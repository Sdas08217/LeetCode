class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # Create a set for faster day lookup
        travel_days = set(days)
        # Initialize an array to store the minimum cost up to each day
        dp = [0] * (days[-1] + 1)
        for i in range(1, days[-1] + 1):
            if i not in travel_days:
                # If no travel is required on this day, cost is same as previous day
                dp[i] = dp[i - 1]
            else:
                # Calculate cost for each ticket type
                one_day_pass = dp[i - 1] + costs[0]
                seven_day_pass = dp[i - 7] + costs[1] if i >= 7 else costs[1]
                thirty_day_pass = dp[i - 30] + costs[2] if i >= 30 else costs[2]
                # Take the minimum of all options
                dp[i] = min(one_day_pass, seven_day_pass, thirty_day_pass)
        # Return the cost on the last travel day
        return dp[days[-1]]
