# Uncommon Words from Two Sentences
from collections import Counter

class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        # Split the sentences into words
        words1 = s1.split()
        words2 = s2.split()
        
        # Count the occurrences of each word in both sentences
        count1 = Counter(words1)
        count2 = Counter(words2)
        
        # List to store uncommon words
        uncommon_words = []
        
        # Check words in s1
        for word in count1:
            if count1[word] == 1 and count2[word] == 0:
                uncommon_words.append(word)
        
        # Check words in s2
        for word in count2:
            if count2[word] == 1 and count1[word] == 0:
                uncommon_words.append(word)
        
        return uncommon_words

  # Example usage
solution = Solution()
print(solution.uncommonFromSentences("this apple is sweet", "this apple is sour"))  # Output: ["sweet", "sour"]
print(solution.uncommonFromSentences("apple apple", "banana"))  # Output: ["banana"]
