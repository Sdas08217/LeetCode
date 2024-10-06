# Sentence Similarity III
class Solution(object):
    def areSentencesSimilar(self, sentence1, sentence2):
        """
        :type sentence1: str
        :type sentence2: str
        :rtype: bool
        """
        words1 = sentence1.split()
        words2 = sentence2.split()

        # Pointers for matching the start and end of both sentences
        left, right = 0, 0
        len1, len2 = len(words1), len(words2)

        # Match words from the start
        while left < len1 and left < len2 and words1[left] == words2[left]:
            left += 1

        # Match words from the end
        while right < len1 - left and right < len2 - left and words1[len1 - right - 1] == words2[len2 - right - 1]:
            right += 1

        # Check if the number of matched words is enough to cover one of the sentences
        return left + right == min(len1, len2)

  # Example Usage
sol = Solution()

# Example 1
sentence1 = "My name is Haley"
sentence2 = "My Haley"
print(sol.areSentencesSimilar(sentence1, sentence2))  # Output: True

# Example 2
sentence1 = "of"
sentence2 = "A lot of words"
print(sol.areSentencesSimilar(sentence1, sentence2))  # Output: False

# Example 3
sentence1 = "Eating right now"
sentence2 = "Eating"
print(sol.areSentencesSimilar(sentence1, sentence2))  # Output: True
