# Sum of Prefix Scores of Strings
class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0

class Solution(object):
    def sumPrefixScores(self, words):
        """
        :type words: List[str]
        :rtype: List[int]
        """
        # Initialize the root of the Trie
        root = TrieNode()
        
        # Step 1: Build the Trie and count prefixes
        for word in words:
            current = root
            for char in word:
                if char not in current.children:
                    current.children[char] = TrieNode()
                current = current.children[char]
                current.count += 1
        
        # Step 2: Calculate the sum of prefix scores for each word
        result = []
        for word in words:
            current = root
            score = 0
            for char in word:
                current = current.children[char]
                score += current.count
            result.append(score)
        
        return result

# Example usage
words = ["apple", "app", "apricot", "bat", "ball"]
solution = Solution()
result = solution.sumPrefixScores(words)
print(result)
