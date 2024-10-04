# Divide Players Into Teams of Equal Skill
class Solution(object):
    def dividePlayers(self, skill):
        """
        :type skill: List[int]
        :rtype: int
        """
        # Step 1: Sort the skill array
        skill.sort()
        
        n = len(skill)
        total_chemistry = 0
        
        # Step 2: Calculate the total skill of the first team
        target_sum = skill[0] + skill[-1]
        
        # Step 3: Check all pairs
        for i in range(n // 2):
            # Calculate the sum of the current pair
            if skill[i] + skill[n - 1 - i] != target_sum:
                return -1  # Return -1 if the sum doesn't match the target sum
            
            # Step 4: Add the chemistry of the current team
            total_chemistry += skill[i] * skill[n - 1 - i]
        
        return total_chemistry

  # Example usage
solution = Solution()

# Example 1
skill = [3, 2, 5, 1, 3, 4]
result = solution.dividePlayers(skill)
print(f"Example 1: {result}")  # Output: 22

# Example 2
skill = [3, 4]
result = solution.dividePlayers(skill)
print(f"Example 2: {result}")  # Output: 12

# Example 3
skill = [1, 1, 2, 3]
result = solution.dividePlayers(skill)
print(f"Example 3: {result}")  # Output: -1
