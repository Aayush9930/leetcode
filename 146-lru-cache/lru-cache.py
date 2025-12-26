class Node:
    def __init__(self, key = None, val = None):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.h = {}
        self.left = Node()
        self.right = Node()
        self.left.next = self.right
        self.right.prev = self.left
        self.capacity = capacity
    
    def get(self, key: int) -> int:
        if key not in self.h:
            return -1
        self.remove(self.h[key])
        self.add(self.h[key])
        return self.h[key].val

    def add(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = node
        nxt.prev = node
        node.next = nxt
        node.prev = prev

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev
    
    def put(self, key: int, value: int) -> None:
        if key in self.h:
            self.h[key].val = value
            self.remove(self.h[key])
            self.add(self.h[key])
        else:
            self.h[key] = Node(key, value)
            self.add(self.h[key])
            if len(self.h) > self.capacity:
                lru = self.left.next
                del self.h[lru.key]
                self.remove(lru)



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)