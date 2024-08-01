# Number of Senior Citizens
class Solution(object):
    def countSeniors(self, details):
        """
        :type details: List[str]
        :rtype: int
        """
        count = 0

        for detail in details:
            # Extract age as the characters at indices 11 and 12
            age = int(detail[11:13])

            # Check if age is strictly more than 60
            if age > 60:
                count += 1

        return count

# Example usage
solution = Solution()
details1 = ["7868190130M7522", "5303914400F9211", "9273338290F4010"]
details2 = ["1313579440F2036", "2921522980M5644"]

print(solution.countSeniors(details1))  # Output: 2
print(solution.countSeniors(details2))  # Output: 0
