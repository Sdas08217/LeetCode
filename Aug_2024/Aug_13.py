# Combination Sum II
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def backtrack(start, target, path):
            if target == 0:
                res.append(path)
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > target:
                    break
                backtrack(i + 1, target - candidates[i], path + [candidates[i]])

        candidates.sort()
        res = []
        backtrack(0, target, [])
        return res

  # Example Usage
  solution = Solution()

# Example 1
candidates = [10,1,2,7,6,1,5]
target = 8
print(solution.combinationSum2(candidates, target))
# Output: [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]

# Example 2
candidates = [2,5,2,1,2]
target = 5
print(solution.combinationSum2(candidates, target))
# Output: [[1, 2, 2], [5]]
