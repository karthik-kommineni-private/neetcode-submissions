class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []

        for num in nums:
            heapq.heappush(min_heap,num) #o(logk)*n
            if len(min_heap)>k:
                heapq.heappop(min_heap) #o(logk)
        return min_heap[0]    

        