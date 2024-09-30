# Design a Stack With Increment Operation
class CustomStack(object):
    def __init__(self, maxSize):
        """
        :type maxSize: int
        """
        self.stack = []
        self.maxSize = maxSize

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if len(self.stack) < self.maxSize:
            self.stack.append(x)

    def pop(self):
        """
        :rtype: int
        """
        if not self.stack:
            return -1
        return self.stack.pop()

    def increment(self, k, val):
        """
        :type k: int
        :type val: int
        :rtype: None
        """
        limit = min(k, len(self.stack))
        for i in range(limit):
            self.stack[i] += val

#Example Usage
# Initialize a stack with max size 3
customStack = CustomStack(3)

# Push elements to the stack
customStack.push(1)  # Stack becomes [1]
customStack.push(2)  # Stack becomes [1, 2]
customStack.push(3)  # Stack becomes [1, 2, 3]
customStack.push(4)  # Stack remains [1, 2, 3] because the stack size is maxed out

# Pop elements from the stack
print(customStack.pop())  # Returns 3, stack becomes [1, 2]
print(customStack.pop())  # Returns 2, stack becomes [1]
print(customStack.pop())  # Returns 1, stack becomes []
print(customStack.pop())  # Returns -1 because the stack is empty

# Increment bottom k elements of the stack
customStack.push(1)  # Stack becomes [1]
customStack.push(2)  # Stack becomes [1, 2]
customStack.increment(2, 100)  # Stack becomes [101, 102] because we added 100 to the first 2 elements

print(customStack.pop())  # Returns 102, stack becomes [101]
print(customStack.pop())  # Returns 101, stack becomes []

