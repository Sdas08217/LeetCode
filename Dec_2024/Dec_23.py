from collections import deque
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        def min_swaps_to_sort(arr):
            n = len(arr)
            indexed_arr = sorted([(value, index) for index, value in enumerate(arr)])
            visited = [False] * n
            swaps = 0
            for i in range(n):
                if visited[i] or indexed_arr[i][1] == i:
                    continue
                cycle_size = 0
                j = i
                while not visited[j]:
                    visited[j] = True
                    j = indexed_arr[j][1]
                    cycle_size += 1
                if cycle_size > 1:
                    swaps += cycle_size - 1
            return swaps
        if not root:
            return 0
        # Perform level order traversal
        queue = deque([root])
        total_swaps = 0
        while queue:
            level_size = len(queue)
            level_values = []
            for _ in range(level_size):
                node = queue.popleft()
                level_values.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            # Calculate minimum swaps for the current level
            total_swaps += min_swaps_to_sort(level_values)
        return total_swaps
