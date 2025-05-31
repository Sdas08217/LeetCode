from collections import deque
from typing import List

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)

        def get_coordinates(square: int) -> (int, int):
            # Maps a square number to its (row, col) on the board
            row = n - 1 - (square - 1) // n
            col = (square - 1) % n if (n - row) % 2 == 1 else n - 1 - (square - 1) % n
            return row, col

        visited = set()
        queue = deque()
        queue.append((1, 0))  # (current_square, number_of_moves)
        visited.add(1)

        while queue:
            square, moves = queue.popleft()
            if square == n * n:
                return moves
            for i in range(1, 7):  # Simulate dice rolls from 1 to 6
                next_square = square + i
                if next_square > n * n:
                    continue
                r, c = get_coordinates(next_square)
                if board[r][c] != -1:
                    next_square = board[r][c]
                if next_square not in visited:
                    visited.add(next_square)
                    queue.append((next_square, moves + 1))

        return -1
