class ListNode:
    def __init__(self,key=None, val=None):
        self.key = key
        self.val = val
        self.next = None



class MyHashMap:

    def __init__(self):
        self.arr = [ListNode() for _ in range(1000)]
        
    def put(self, key: int, val: int) -> None:
        index = self.hash(key)
        node = self.arr[index]
        while node.next:
            if node.next.key == key:
                node.next.val = val
                return
            node = node.next
        node.next = ListNode(key,val)
        

    def get(self, key: int) -> int:
        index = self.hash(key)
        node = self.arr[index]

        while node.next:
            if node.next.key == key:
                return node.next.val
            node = node.next
        return -1
        

    def remove(self, key: int) -> None:
            cur = self.arr[self.hash(key)]
            while cur.next:
                if cur.next.key == key:
                    cur.next = cur.next.next
                    return
                cur = cur.next

    def hash(self, key: int) -> int:
        index = key % 1000 #divide among available buckets
        return index    
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)