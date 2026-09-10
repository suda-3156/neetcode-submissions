class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        # least recent: left_dummy -> (nodes will be inserted here) -> right_dummy :most recent
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        # left_dummy -> A -> B -> C -> right_dummy
        # ~> left_dummy -> A -> C -> right_dummy
        # Given B then A = B.prev, C = B.next ~> A.next = C
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def insert(self, node):
        # left_dummy -> A -> B -> right_dummy
        # ~> left_dummy -> A -> B -> C -> right_dummy
        # Given C, then B.next = right_dummy.prev = C
        # and C.next = right_dummy, C.prev = B
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
