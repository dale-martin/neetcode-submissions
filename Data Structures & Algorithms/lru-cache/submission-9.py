class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.lru = {}
        self.cap = capacity
        
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        prev = node.prev
        next = node.next

        prev.next = next
        next.prev = prev
    
    def insert(self, node):
        prev = self.right.prev
        next = self.right

        prev.next = node
        node.prev = prev
        node.next = next
        next.prev = node

    def get(self, key: int) -> int:
        if key in self.lru:
            self.remove(self.lru[key])
            self.insert(self.lru[key])
            return self.lru[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.lru:
            self.remove(self.lru[key])

        node = Node(key, value)
        self.lru[key] = node
        self.insert(node)

        if len(self.lru) > self.cap:
            oldest = self.left.next
            self.remove(oldest)
            del self.lru[oldest.key]
