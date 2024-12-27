class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        max_score = 0
        best_i = values[0]  # Initialize best_i as values[0] + 0
        
        for j in range(1, len(values)):
            # Calculate score for pair (i, j)
            max_score = max(max_score, best_i + values[j] - j)
            
            # Update best_i to include values[j] + j
            best_i = max(best_i, values[j] + j)
        
        return max_score
