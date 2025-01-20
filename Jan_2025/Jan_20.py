from typing import List

class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        
        # Step 1: Create a mapping of each number to its (row, column) position in mat
        position = {}
        for r in range(m):
            for c in range(n):
                position[mat[r][c]] = (r, c)
        
        # Step 2: Arrays to track painted rows and columns
        row_painted = [0] * m
        col_painted = [0] * n
        
        # Step 3: Iterate through arr and paint cells
        for i, num in enumerate(arr):
            r, c = position[num]
            
            # Paint the cell
            row_painted[r] += 1
            col_painted[c] += 1
            
            # Check if any row or column is fully painted
            if row_painted[r] == n or col_painted[c] == m:
                return i
        
        return -1  # This line shouldn't be reached if the input constraints are followed
