# String Compression III
class Solution:
    def compressedString(self, word: str) -> str:
        comp = ""
        i = 0
        n = len(word)
        
        while i < n:
            count = 1
            # Count consecutive characters up to a maximum of 9
            while i + count < n and word[i] == word[i + count] and count < 9:
                count += 1
            # Append the count and character to comp
            comp += str(count) + word[i]
            i += count  # Move the index forward by count
        
        return comp

  #Example Usage
  # Instantiate the Solution class
solution = Solution()

# Test the compressedString method with an example input
word = "aaabbbcccccaaa"
compressed = solution.compressedString(word)
print(compressed)  # Output should be "3a3b5c3a"
