"""
146. LRU Cache
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.



Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
lRUCache = new LRUCache(2)
lRUCache.put(1, 1) # cache is {1=1}
lRUCache.put(2, 2) # cache is {1=1, 2=2}
lRUCache.get(1)    # return 1
lRUCache.put(3, 3) # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2)    # returns -1 (not found)
lRUCache.put(4, 4) # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1)    # return -1 (not found)
lRUCache.get(3)    # return 3
lRUCache.get(4)    # return 4

"""

class Node:
    def __init__(self, key, data):
        self.key = key  # required to track the node in the lookup table
        self.data = data
        self.prev = None
        self.next = None

    def __eq__(self, other):
        if not isinstance(other, Node):
            return False
        return (self.key == other.key and
                self.data == other.data)

    def __repr__(self):
        return f"Node(key={self.key}, data={self.data})"

class DoubleLList:
    def __init__(self):
        self.head = None
        self.tail = None

    def move_to_front(self, node):
        """
        Moves the given node to the front of the list.
        - Removes the node from its current position.
        - Updates pointers to place it at the front.
        """
        # If the node is already at the front, no action needed
        if node == self.head:
            return

        # Remove node from its current position
        if node == self.tail:
            # If it's the tail, update the tail pointer
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            # Adjust the next and prev pointers of surrounding nodes
            node.prev.next = node.next
            node.next.prev = node.prev

        # Add the node to the front of the list
        node.next = self.head
        self.head.prev = node
        self.head = node

    def append_to_front(self, node):
        """
        Adds a new node to the front of the list.
        - Updates pointers to make the new node the head.
        """
        node.prev = None  # No previous node for the new head
        node.next = self.head  # Point to the current head

        if self.head:
            # If the list already has nodes, update the current head's prev pointer
            self.head.prev = node

        # Update the head to the new node
        self.head = node

        if not self.tail:
            # If the list was empty, set the tail to the new node
            self.tail = node

    def remove_from_tail(self):
        """
        Removes the last node (tail) from the list.
        - Updates pointers to detach the tail node.
        - Returns the removed node.
        """
        if not self.tail:
            # If the list is empty, return None
            return None

        node = self.tail  # Store the tail node to return later

        if self.tail.prev:
            # If there's a previous node, update its next pointer
            self.tail.prev.next = None
            self.tail = self.tail.prev  # Update the tail pointer
        else:
            # If the list has only one node, reset head and tail
            self.head = None
            self.tail = None

        return node


class LRUCache:

    def __init__(self, capacity: int):
        self.MAX_SIZE = capacity
        self.size = 0
        self.lookup = {}
        # Initialize an empty doubly linked list
        self.linked_list = DoubleLList()

    def get(self, key):
        """
        Get the value from the cache.
        Accessing a node updates its position to the front of the LRU list.
        """
        node = self.lookup.get(key)
        if node is None:
            return -1   # Key not found
        # Move the accessed node to the front of the LRU list
        self.linked_list.move_to_front(node)
        return node.data

    def put(self, key, value):
        """
        Set the value for the given key in the cache.

        When updating an entry, updates its position to the front of the LRU list.
        If the entry is new and the cache is at capacity, removes the oldest entry
        before the new entry is added.
        """
        node = self.lookup.get(key)
        if node is not None:
            # Key exists in cache, update the value
            node.data = value
            # Move the updated node to the front of the LRU list
            self.linked_list.move_to_front(node)
            return

        # Cache is FULL ?
        if self.size == self.MAX_SIZE:
            # Remove the oldest entry from the linked list and lookup, reduce size by 1
            self.lookup.pop(self.linked_list.tail.key, None)
            self.linked_list.remove_from_tail()
            self.size -= 1

        # Add the new key and value in the linked list and lookup, increase size by 1
        self.size += 1
        new_node = Node(key, value)
        self.linked_list.append_to_front(new_node)
        self.lookup[key] = new_node


if __name__ == '__main__':

    lRUCache = LRUCache(2)
    lRUCache.put(1, 1)  # cache is {1=1}
    assert lRUCache.lookup == {1: Node(1, 1)}

    lRUCache.put(2, 2)  # cache is {1=1, 2=2}
    assert lRUCache.lookup == {1: Node(1, 1), 2: Node(2, 2)}
    assert lRUCache.get(1) == 1  # return 1

    # Size Overload - Replace Old key.
    lRUCache.put(3, 3)  # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
    assert lRUCache.lookup == {1: Node(1, 1), 3: Node(3, 3)}
    assert lRUCache.get(2) == -1   # returns -1 (not found)
    assert lRUCache.get(3) == 3 # return 3

    # Value Overwrite - Replace Old key.
    lRUCache.put(3, 10)
    assert lRUCache.get(3) == 10 # return 10
    assert lRUCache.lookup == {1: Node(1, 1), 3: Node(3, 10)}
