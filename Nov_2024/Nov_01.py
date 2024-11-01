# Delete Characters to Make Fancy String
class Solution:
    def makeFancyString(self, s: str) -> str:
        result = []
        
        for char in s:
            # Check if the last two characters in result are the same as the current char
            if len(result) >= 2 and result[-1] == char and result[-2] == char:
                continue  # Skip adding this char to avoid three consecutive chars
            result.append(char)
        
        # Join the result list to form the final fancy string
        return ''.join(result)

  # Example usage
s = "aaabaaaa"
solution = Solution()
fancy_string = solution.makeFancyString(s)
print(fancy_string)  # Output should be "aabaa"
