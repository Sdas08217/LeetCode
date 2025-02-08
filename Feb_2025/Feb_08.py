import heapq

class NumberContainers:

    def __init__(self):
        self.index_to_number = {}  # Maps index to its current number
        self.number_to_indices = {}  # Maps number to a min-heap of indices
        self.valid_indices = {}  # Maps number to a set of valid indices

    def change(self, index: int, number: int) -> None:
        # If index already contains a number, remove it from the previous number's set
        if index in self.index_to_number:
            old_number = self.index_to_number[index]
            if old_number in self.valid_indices:
                self.valid_indices[old_number].discard(index)
        
        # Assign the new number to the index
        self.index_to_number[index] = number
        
        # Add the index to the new number's heap and set
        if number not in self.number_to_indices:
            self.number_to_indices[number] = []
            self.valid_indices[number] = set()
        
        heapq.heappush(self.number_to_indices[number], index)
        self.valid_indices[number].add(index)

    def find(self, number: int) -> int:
        if number not in self.number_to_indices:
            return -1  # No index contains this number
        
        # Ensure we return only valid indices
        while self.number_to_indices[number] and self.number_to_indices[number][0] not in self.valid_indices[number]:
            heapq.heappop(self.number_to_indices[number])
        
        return self.number_to_indices[number][0] if self.number_to_indices[number] else -1
