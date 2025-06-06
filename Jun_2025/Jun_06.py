class Solution:
    def robotWithString(self, s: str) -> str:
        from collections import Counter

        count = Counter(s)  # Count of each character in s
        result = []         # This will be the final string written on paper
        stack = []          # This simulates the robot's t string
        min_char = 'a'      # Start with the smallest possible character

        for ch in s:
            stack.append(ch)
            count[ch] -= 1

            # Update min_char to the smallest character still left in s
            while min_char <= 'z' and count[min_char] == 0:
                min_char = chr(ord(min_char) + 1)

            # Pop from stack to result as long as it's <= smallest left char in s
            while stack and stack[-1] <= min_char:
                result.append(stack.pop())

        # Pop any remaining characters from stack
        while stack:
            result.append(stack.pop())

        return ''.join(result)
