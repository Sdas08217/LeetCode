class Solution:
    def findScore(self, nums: List[int]) -> int:
        # Create a list of (value, index) pairs and sort it
        indexed_nums = sorted((val, idx) for idx, val in enumerate(nums))
        
        # Set to track marked indices
        marked = set()
        score = 0
        
        # Iterate over the sorted list
        for val, idx in indexed_nums:
            if idx not in marked:  # If the index is not marked
                # Add the value to the score
                score += val
                
                # Mark the current index and its adjacent indices
                marked.add(idx)
                if idx - 1 >= 0:
                    marked.add(idx - 1)
                if idx + 1 < len(nums):
                    marked.add(idx + 1)
        
        return score
