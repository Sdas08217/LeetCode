# Design Circular Deque
class MyCircularDeque(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.k = k  # Maximum size of deque
        self.deque = [0] * k  # Fixed-size list to store deque elements
        self.front = 0  # Front pointer
        self.rear = 0  # Rear pointer
        self.size = 0  # Current number of elements in the deque

    def insertFront(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        self.front = (self.front - 1 + self.k) % self.k  # Move front pointer backwards
        self.deque[self.front] = value
        self.size += 1
        return True

    def insertLast(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        self.deque[self.rear] = value
        self.rear = (self.rear + 1) % self.k  # Move rear pointer forward
        self.size += 1
        return True

    def deleteFront(self):
        """
        :rtype: bool
        """
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.k  # Move front pointer forward
        self.size -= 1
        return True

    def deleteLast(self):
        """
        :rtype: bool
        """
        if self.isEmpty():
            return False
        self.rear = (self.rear - 1 + self.k) % self.k  # Move rear pointer backwards
        self.size -= 1
        return True

    def getFront(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.deque[self.front]

    def getRear(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.deque[(self.rear - 1 + self.k) % self.k]

    def isEmpty(self):
        """
        :rtype: bool
        """
        return self.size == 0

    def isFull(self):
        """
        :rtype: bool
        """
        return self.size == self.k

# Initialize the deque with a capacity of 3
circularDeque = MyCircularDeque(3)

# Insert elements at the front and rear
print(circularDeque.insertLast(1))  # Returns True, as 1 is inserted at the rear
print(circularDeque.insertLast(2))  # Returns True, as 2 is inserted at the rear
print(circularDeque.insertFront(3)) # Returns True, as 3 is inserted at the front
print(circularDeque.insertFront(4)) # Returns False, deque is full

# Check front and rear values
print(circularDeque.getRear())  # Returns 2
print(circularDeque.isFull())   # Returns True, as the deque is full

# Delete elements from the front and rear
print(circularDeque.deleteLast())   # Returns True, last element deleted
print(circularDeque.insertFront(4)) # Returns True, 4 inserted at the front

# Check front value
print(circularDeque.getFront())  # Returns 4
