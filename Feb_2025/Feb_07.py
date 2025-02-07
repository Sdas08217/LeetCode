from typing import List
from collections import defaultdict

class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ball_colors = {}  # Stores the latest color assigned to each ball
        color_count = defaultdict(int)  # Counts occurrences of each color
        distinct_colors = 0  # Tracks number of distinct colors
        result = []

        for ball, color in queries:
            # If the ball was previously colored, update the color count
            if ball in ball_colors:
                old_color = ball_colors[ball]
                color_count[old_color] -= 1
                if color_count[old_color] == 0:  # Remove color if no other ball has it
                    distinct_colors -= 1

            # Assign the new color to the ball
            ball_colors[ball] = color
            if color_count[color] == 0:
                distinct_colors += 1  # New color added
            color_count[color] += 1

            result.append(distinct_colors)

        return result
