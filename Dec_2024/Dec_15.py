import heapq
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        # Helper function to calculate the difference in pass ratio when adding a student
        def gain(passed, total):
            return (passed + 1) / (total + 1) - passed / total
        # Create a max-heap based on the gain of adding a student to each class
        max_heap = [(-gain(passed, total), passed, total) for passed, total in classes]
        heapq.heapify(max_heap)
        # Assign extra students
        for _ in range(extraStudents):
            g, passed, total = heapq.heappop(max_heap)
            passed += 1
            total += 1
            heapq.heappush(max_heap, (-gain(passed, total), passed, total))
        # Calculate the final average pass ratio
        total_ratio = sum(passed / total for _, passed, total in max_heap)
        return total_ratio / len(classes)
# Example usage
solution = Solution()
classes = [[2, 4], [3, 9], [4, 5], [2, 10]]
extraStudents = 4
result = solution.maxAverageRatio(classes, extraStudents)
print(result)  # Expected output: 0.53485
