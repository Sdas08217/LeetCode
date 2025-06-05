# 
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = [i for i in range(26)]  # Each character is initially its own parent

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  # Path compression
            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return
            # Union by lexicographical order (smaller one becomes the parent)
            if px < py:
                parent[py] = px
            else:
                parent[px] = py

        # Build the union-find structure using s1 and s2
        for a, b in zip(s1, s2):
            union(ord(a) - ord('a'), ord(b) - ord('a'))

        # Build the result string by finding smallest equivalent character
        result = []
        for ch in baseStr:
            smallest_char = chr(find(ord(ch) - ord('a')) + ord('a'))
            result.append(smallest_char)

        return ''.join(result)
