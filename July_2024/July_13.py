# Robot Collisions
class Solution(object):
    def survivedRobotsHealths(self, positions, healths, directions):
        """
        :type positions: List[int]
        :type healths: List[int]
        :type directions: str
        :rtype: List[int]
        """
        # Combine all attributes of robots and sort by positions
        robots = sorted(zip(positions, healths, directions, range(len(positions))))
        
        stack = []
        survivors = []
        
        for pos, health, dir, index in robots:
            if dir == 'R':
                stack.append((pos, health, dir, index))
            else:
                while stack and health > 0:
                    r_pos, r_health, r_dir, r_index = stack[-1]
                    if r_health < health:
                        stack.pop()
                        health -= 1
                    elif r_health > health:
                        health = 0
                        stack[-1] = (r_pos, r_health - 1, r_dir, r_index)
                    else:
                        stack.pop()
                        health = 0
                
                if health > 0:
                    survivors.append((pos, health, dir, index))
        
        # Combine remaining stack (right-moving robots) with survivors
        survivors += stack
        
        # Sort survivors by their initial index
        survivors.sort(key=lambda x: x[3])
        
        # Return the healths of the survivors in the original order
        return [health for pos, health, dir, index in survivors]

  # Example usage:
solution = Solution()

positions1 = [5, 4, 3, 2, 1]
healths1 = [2, 17, 9, 15, 10]
directions1 = "RRRRR"
print(solution.survivedRobotsHealths(positions1, healths1, directions1))  # Output: [2, 17, 9, 15, 10]

positions2 = [3, 5, 2, 6]
healths2 = [10, 10, 15, 12]
directions2 = "RLRL"
print(solution.survivedRobotsHealths(positions2, healths2, directions2))  # Output: [14]

positions3 = [1, 2, 5, 6]
healths3 = [10, 10, 11, 11]
directions3 = "RLRL"
print(solution.survivedRobotsHealths(positions3, healths3, directions3))  # Output: []
