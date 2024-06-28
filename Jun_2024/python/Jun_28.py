# Miximum Total Importance of roads
class Solution(object):
    def maximumImportance(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        # Step 1: Calculate the degree of each city
        degree = [0] * n
        for a, b in roads:
            degree[a] += 1
            degree[b] += 1

        # Step 2: Sort cities by degree in descending order
        sorted_cities = sorted(range(n), key=lambda x: degree[x], reverse=True)
        
        # Step 3: Assign values to cities
        value = [0] * n
        current_value = n
        for city in sorted_cities:
            value[city] = current_value
            current_value -= 1
        
        # Step 4: Calculate total importance
        total_importance = 0
        for a, b in roads:
            total_importance += value[a] + value[b]
        
        return total_importance

# Example usage:
solution = Solution()

# Example 1
n1 = 5
roads1 = [[0, 1], [1, 2], [2, 3], [0, 2], [1, 3], [2, 4]]
print(solution.maximumImportance(n1, roads1))  # Output: 43

# Example 2
n2 = 5
roads2 = [[0, 3], [2, 4], [1, 3]]
print(solution.maximumImportance(n2, roads2))  # Output: 20
