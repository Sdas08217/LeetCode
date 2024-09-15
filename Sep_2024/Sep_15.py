# Find the Longest Substring Containing Vowels in Even Counts

class Solution(object):
    def findTheLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Map each vowel to a specific bit position
        vowel_to_bit = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}
        
        # This will store the first occurrence of every bitmask state
        state_to_index = {0: -1}  # State 0 is when no vowels have been encountered
        state = 0  # Initially, all vowels appear an even number of times (none encountered yet)
        max_length = 0
        
        # Traverse the string
        for i, char in enumerate(s):
            if char in vowel_to_bit:
                # Flip the corresponding bit for the vowel
                state ^= (1 << vowel_to_bit[char])
            
            # Check if this state has been seen before
            if state in state_to_index:
                # Calculate the length of the substring
                max_length = max(max_length, i - state_to_index[state])
            else:
                # If state hasn't been seen before, store the index
                state_to_index[state] = i
        
        return max_length
# Example usage:
sol = Solution()
s = "eleetminicoworoep"
result = sol.findTheLongestSubstring(s)
print("The length of the longest substring is:", result)
