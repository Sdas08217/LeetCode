# Spiral Matrix III
class Solution(object):
    def spiralMatrixIII(self, rows, cols, rStart, cStart):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        r, c = rStart, cStart
        visited = set([(r, c)])
        result = [[r, c]]
        step = 1
        dir_idx = 0
        
        while len(result) < rows * cols:
            for _ in range(2):  
                for _ in range(step):
                    r += directions[dir_idx][0]
                    c += directions[dir_idx][1]
                    
                    # Debug: Track the current position and check if it's within bounds
                    print("Moving to: ({}, {}), Current direction: {}".format(r, c, directions[dir_idx]))

                    if 0 <= r < rows and 0 <= c < cols and (r, c) not in visited:
                        result.append([r, c])
                        visited.add((r, c))
                        print("Added: ({}, {})".format(r, c))
                
                dir_idx = (dir_idx + 1) % 4
            step += 1
        
        return result

  # Example usage of the Solution class
solution = Solution()

# Define the parameters
rows = 1
cols = 4
rStart = 0
cStart = 0

# Call the method and get the result
result = solution.spiralMatrixIII(rows, cols, rStart, cStart)

# Print the result
print(result)
