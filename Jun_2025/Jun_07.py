class Solution:
    def clearStars(self, s: str) -> str:
        from collections import defaultdict

        st = defaultdict(list)  # st[char] = list of indices
        for i, ch in enumerate(s):
            if ch == '*':
                for c in range(26):
                    if st[chr(c + ord('a'))]:
                        st[chr(c + ord('a'))].pop()
                        break
            else:
                st[ch].append(i)

        tmp = [' '] * len(s)
        for c in range(26):
            ch = chr(c + ord('a'))
            for idx in st[ch]:
                tmp[idx] = ch

        return ''.join(c for c in tmp if c != ' ')
