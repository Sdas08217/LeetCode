# Minimum Number of Pushes to Type Word II
class Solution:
    def minimumPushes(self, word: str) -> int:
        from collections import Counter

        # Step 1: Count frequencies of each letter
        freq = Counter(word)

        # Step 2: Sort frequencies in descending order
        freq_list = sorted(freq.values(), reverse=True)

        # Step 3: Calculate minimum pushes
        num_keys = 8  # We have 8 keys (2 to 9)
        pushes = 0

        for i, count in enumerate(freq_list):
            # Determine the number of key presses for this letter
            key_presses = (i // num_keys) + 1
            pushes += count * key_presses

        return pushes

# Example usage
if _name_ == "_main_":
    sol = Solution()
    print(sol.minimumPushes("abcde"))          # Output: 5
    print(sol.minimumPushes("xyzxyzxyzxyz"))   # Output: 12
    print(sol.minimumPushes("aabbccddeeffgghhiiiiii"))  # Output: 24