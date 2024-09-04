# Walking Robot Simulation
class Solution(object):
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        # Define directions as vectors: North, East, South, West
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dir_index = 0  # Start facing North
        x, y = 0, 0  # Start position
        max_dist_squared = 0

        # Convert the list of obstacles to a set for O(1) lookup
        obstacle_set = set(map(tuple, obstacles))

        for command in commands:
            if command == -2:  # Turn left
                dir_index = (dir_index - 1) % 4
            elif command == -1:  # Turn right
                dir_index = (dir_index + 1) % 4
            else:
                # Move forward k steps
                for _ in range(command):
                    next_x = x + directions[dir_index][0]
                    next_y = y + directions[dir_index][1]
                    
                    # Check if the next position is an obstacle
                    if (next_x, next_y) not in obstacle_set:
                        x, y = next_x, next_y
                        max_dist_squared = max(max_dist_squared, x**2 + y**2)
                    else:
                        break  # Stop moving in this direction if there's an obstacle

        return max_dist_squared

# Example test cases
solution = Solution()

print(solution.robotSim([4,-1,3], []))  # Output: 25
print(solution.robotSim([4,-1,4,-2,4], [[2,4]]))  # Output: 65
print(solution.robotSim([6,-1,-1,6], []))  # Output: 36
