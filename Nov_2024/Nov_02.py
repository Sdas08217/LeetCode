# Circular Sentence
class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split()
        
        # Check each word's last character with the next word's first character
        for i in range(len(words)):
            if words[i][-1] != words[(i + 1) % len(words)][0]:
                return False
        
        return True

#Eaxmple usage
  # Create an instance of the Solution class
solution = Solution()

# Example sentences
sentence1 = "leetcode exercises sound delightful"
sentence2 = "happy year round"
sentence3 = "good dog goat game"

# Check if each sentence is circular
print(solution.isCircularSentence(sentence1))  # Output: True
print(solution.isCircularSentence(sentence2))  # Output: False
print(solution.isCircularSentence(sentence3))  # Output: True
