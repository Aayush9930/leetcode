class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val 
        self.next = None
        self.prev = None  

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.h = {}
        self.l = Node(0, 0)
        self.r = Node(0, 0)
        
        self.l.next = self.r
        self.r.prev = self.l
    # i am adding the node on the right -> mru
    def add(self, node):
        p, nxt = self.r.prev, self.r
        p.next = node
        nxt.prev = node
        node.prev = p
        node.next = nxt

    def remove(self, node):
        p, nxt = node.prev, node.next
        p.next = nxt
        nxt.prev = p

    def get(self, key: int) -> int:
        if key not in self.h:
            return -1
        self.remove(self.h[key])
        self.add(self.h[key])
        return self.h[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.h:
            self.h[key].val = value
            self.remove(self.h[key])
            self.add(self.h[key])
        
        else:
            self.h[key] = Node(key, value)
            self.add(self.h[key])
            if len(self.h) > self.capacity:
                lru = self.l.next
                self.remove(lru)
                del self.h[lru.key]



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)