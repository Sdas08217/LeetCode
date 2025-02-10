class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        
        for ch in s:
            if ch.isdigit():
                if stack:  # Remove the closest non-digit character
                    stack.pop()
            else:
                stack.append(ch)
        
        return "".join(stack)
