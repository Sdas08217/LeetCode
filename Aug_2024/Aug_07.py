# Integer to English Words
class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "Zero"
        
        less_than_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", 
                        "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        thousands = ["", "Thousand", "Million", "Billion"]
        
        def helper(n):
            if n == 0:
                return ""
            elif n < 20:
                return less_than_20[n] + " "
            elif n < 100:
                return tens[n // 10] + " " + helper(n % 10)
            elif n < 1000:
                return less_than_20[n // 100] + " Hundred " + helper(n % 100)
            else:
                for idx, word in enumerate(thousands):
                    if n < 1000 ** (idx + 1):
                        return helper(n // (1000 ** idx)) + word + " " + helper(n % (1000 ** idx))
        
        return helper(num).strip()

# Example usage
solution = Solution()
print(solution.numberToWords(123))          # Output: "One Hundred Twenty Three"
print(solution.numberToWords(12345))        # Output: "Twelve Thousand Three Hundred Forty Five"
print(solution.numberToWords(1234567))      # Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
``` &#8203;:citation[oaicite:0]{index=0}&#8203;
