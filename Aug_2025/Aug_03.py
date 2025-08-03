from typing import List

class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        n = len(fruits)
        max_fruits = 0
        total = 0
        i = 0  # Left pointer for sliding window

        for j in range(n):
            # Add the current fruit amount at position j
            total += fruits[j][1]

            # Try shrinking the window from the left if steps exceed k
            while i <= j:
                left = fruits[i][0]
                right = fruits[j][0]

                # Calculate minimum steps required to cover this window
                min_steps = min(
                    abs(startPos - left) + (right - left),  # left then right
                    abs(startPos - right) + (right - left)  # right then left
                )

                if min_steps <= k:
                    break
                else:
                    total -= fruits[i][1]
                    i += 1

            max_fruits = max(max_fruits, total)

        return max_fruits
