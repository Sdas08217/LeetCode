# Number of Atoms 
class Solution(object):
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        from collections import defaultdict

        self.i = 0

        def parse():
            n = len(formula)

            def parse_element():
                start = self.i
                self.i += 1  # Skip the first uppercase letter
                while self.i < n and formula[self.i].islower():
                    self.i += 1
                return formula[start:self.i]

            def parse_number():
                if self.i >= n or not formula[self.i].isdigit():
                    return 1  # Default count is 1 if there's no number
                start = self.i
                while self.i < n and formula[self.i].isdigit():
                    self.i += 1
                return int(formula[start:self.i])

            stack = [defaultdict(int)]
            while self.i < n:
                if formula[self.i] == '(':
                    self.i += 1
                    stack.append(defaultdict(int))
                elif formula[self.i] == ')':
                    self.i += 1
                    num = parse_number()
                    top = stack.pop()
                    for elem, count in top.items():
                        stack[-1][elem] += count * num
                else:
                    elem = parse_element()
                    num = parse_number()
                    stack[-1][elem] += num

            return stack[0]

        count = parse()
        result = []
        for elem in sorted(count.keys()):
            result.append(elem)
            if count[elem] > 1:
                result.append(str(count[elem]))

        return ''.join(result)

  # Example usage:
solution = Solution()
print(solution.countOfAtoms("H2O"))        # Output: "H2O"
print(solution.countOfAtoms("Mg(OH)2"))    # Output: "H2MgO2"
print(solution.countOfAtoms("K4(ON(SO3)2)2"))  # Output: "K4N2O14S4"
