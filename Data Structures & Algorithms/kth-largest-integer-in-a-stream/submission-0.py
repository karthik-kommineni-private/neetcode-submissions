class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        heapq.heapify(nums)
        self.heap = nums
        self.k = k
        

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        res_list = heapq.nlargest(self.k,self.heap)
        return res_list[-1]
            


        
