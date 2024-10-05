#  Permutation in String
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        len1, len2 = len(s1), len(s2)
        
        if len1 > len2:
            return False
        
        s1_count = Counter(s1)
        s2_count = Counter(s2[:len1])
        
        if s1_count == s2_count:
            return True
        
        for i in range(len1, len2):
            s2_count[s2[i]] += 1
            s2_count[s2[i - len1]] -= 1
            
            if s2_count[s2[i - len1]] == 0:
                del s2_count[s2[i - len1]]
            
            if s1_count == s2_count:
                return True
        
        return False
# Example usage
s1 = "abc"
s2 = "eidbaooo"

solution = Solution()
result = solution.checkInclusion(s1, s2)
print(result)  # Output: True
