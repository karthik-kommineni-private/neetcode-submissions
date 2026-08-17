class DllNode:
    def __init__(self,key = 0,val = 0, prev = None, next = None):
        self.key,self.val = key, val
        self.prev = self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        #head - LRU, tail -MRU
        self.head, self.tail = DllNode(), DllNode()
        self.cache = {} # key:DllNode. ?????
        self.cap = capacity  
        self.head.next = self.tail
        self.tail.prev = self.head 

    def get(self, key: int) -> int:
        if key in self.cache:
            #update linked list
            # remove node from curr pos -> insert MRU
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1    
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.remove(node)
            self.insert(node)
        else:
            if len(self.cache)>=self.cap:
                lru = self.head.next  # ✅ get LRU node
                self.remove(lru)
                del self.cache[lru.key]
            new_node = DllNode(key,value) 
            self.insert(new_node)
            self.cache[key] = new_node     


    #remove the node from curr pos    
    def remove(self,node: DllNode) -> None:
        prevN,nextN = node.prev,node.next
        prevN.next,nextN.prev = nextN,prevN

    #insert at the end    
    def insert(self, node: DllNode) -> None:
        temp = self.tail.prev
        temp.next = node
        node.prev = temp
        node.next = self.tail
        self.tail.prev = node
        






        
