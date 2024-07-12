# Maximum Score From Removing Substrings
class Solution(object):
    def maximumGain(self, s, x, y):
        """
        :type s: str
        :type x: int
        :type y: int
        :rtype: int
        """
        def remove_substring(s, sub1, sub2, points):
            stack = []
            total_points = 0
            for char in s:
                if stack and stack[-1] == sub1 and char == sub2:
                    stack.pop()
                    total_points += points
                else:
                    stack.append(char)
            return total_points, ''.join(stack)
        
        if x > y:
            # Remove "ab" first
            points1, remaining_string = remove_substring(s, 'a', 'b', x)
            points2, _ = remove_substring(remaining_string, 'b', 'a', y)
        else:
            # Remove "ba" first
            points1, remaining_string = remove_substring(s, 'b', 'a', y)
            points2, _ = remove_substring(remaining_string, 'a', 'b', x)
        
        return points1 + points2

# Example usage:
solution = Solution()

# Example 1
s1 = "cdbcbbaaabab"
x1 = 4
y1 = 5
print(solution.maximumGain(s1, x1, y1))  # Output: 19

# Example 2
s2 = "aabbaaxybbaabb"
x2 = 5
y2 = 4
print(solution.maximumGain(s2, x2, y2))  # Output: 20  
