# All O`one Data Structure
class Node:
    def __init__(self, count):
        self.count = count
        self.keys = set()
        self.prev = None
        self.next = None

class AllOne(object):

    def __init__(self):
        self.key_count = {}
        self.count_node = {}
        self.head = Node(float('-inf'))  # Dummy head
        self.tail = Node(float('inf'))   # Dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_node(self, new_node, prev_node):
        new_node.prev = prev_node
        new_node.next = prev_node.next
        prev_node.next.prev = new_node
        prev_node.next = new_node

    def _remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def inc(self, key):
        """
        :type key: str
        :rtype: None
        """
        if key in self.key_count:
            current_count = self.key_count[key]
            self.key_count[key] += 1
            new_count = self.key_count[key]
            
            # Remove the key from the current count node
            current_node = self.count_node[current_count]
            current_node.keys.remove(key)

            # If current node is empty after removal, remove it
            if not current_node.keys:
                self._remove_node(current_node)
                del self.count_node[current_count]

            # Add key to the new count node
            if new_count not in self.count_node:
                new_node = Node(new_count)
                self.count_node[new_count] = new_node
                # Insert new_node into the linked list
                # Find the right place to insert
                prev_node = self.head
                while prev_node.next.count < new_count:
                    prev_node = prev_node.next
                self._add_node(new_node, prev_node)
                
            self.count_node[new_count].keys.add(key)
        else:
            self.key_count[key] = 1
            if 1 not in self.count_node:
                new_node = Node(1)
                self.count_node[1] = new_node
                self._add_node(new_node, self.head)
            self.count_node[1].keys.add(key)

    def dec(self, key):
        """
        :type key: str
        :rtype: None
        """
        current_count = self.key_count[key]
        current_node = self.count_node[current_count]
        current_node.keys.remove(key)
        
        if current_count == 1:
            del self.key_count[key]
            if not current_node.keys:
                self._remove_node(current_node)
                del self.count_node[current_count]
        else:
            self.key_count[key] -= 1
            new_count = self.key_count[key]
            if new_count not in self.count_node:
                new_node = Node(new_count)
                self.count_node[new_count] = new_node
                # Insert new_node into the linked list
                prev_node = self.head
                while prev_node.next.count < new_count:
                    prev_node = prev_node.next
                self._add_node(new_node, prev_node)

            self.count_node[new_count].keys.add(key)
            if not current_node.keys:
                self._remove_node(current_node)
                del self.count_node[current_count]

    def getMaxKey(self):
        """
        :rtype: str
        """
        return "" if self.tail.prev == self.head else next(iter(self.tail.prev.keys))

    def getMinKey(self):
        """
        :rtype: str
        """
        return "" if self.head.next == self.tail else next(iter(self.head.next.keys))

#Example Usage
# Initialize the AllOne data structure
allOne = AllOne()

# Increment "hello" twice
allOne.inc("hello")
allOne.inc("hello")

# Get the key with the maximum count
print(allOne.getMaxKey())  # Output: "hello"

# Get the key with the minimum count
print(allOne.getMinKey())  # Output: "hello"

# Increment "leet" once
allOne.inc("leet")

# Get the key with the maximum count
print(allOne.getMaxKey())  # Output: "hello"

# Get the key with the minimum count
print(allOne.getMinKey())  # Output: "leet"

# Decrement "hello" once
allOne.dec("hello")

# Get the key with the maximum count
print(allOne.getMaxKey())  # Output: "hello"

# Get the key with the minimum count
print(allOne.getMinKey())  # Output: "leet"

# Decrement "hello" once more
allOne.dec("hello")

# Get the key with the maximum count
print(allOne.getMaxKey())  # Output: "leet"

# Get the key with the minimum count
print(allOne.getMinKey())  # Output: "leet"
