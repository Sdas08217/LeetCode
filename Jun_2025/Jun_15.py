class Solution:
    def maxDiff(self, num: int) -> int:
        s = str(num)
        
        # Step 1: Maximize the number by replacing one digit with '9'
        for digit in s:
            if digit != '9':
                max_num = int(s.replace(digit, '9'))
                break
        else:
            max_num = num  # All digits are already 9

        # Step 2: Minimize the number by replacing one digit with '1' or '0'
        first_digit = s[0]
        if first_digit != '1':
            min_num = int(s.replace(first_digit, '1'))  # Change first digit to '1'
        else:
            # Change first non-'0' and non-'1' digit to '0'
            for digit in s[1:]:
                if digit not in ('0', '1'):
                    min_num = int(s.replace(digit, '0'))
                    break
            else:
                min_num = num  # No suitable digit to replace, use original

        return max_num - min_num
