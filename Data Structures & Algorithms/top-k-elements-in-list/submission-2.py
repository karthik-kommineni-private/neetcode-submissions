class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}
        for num in nums:
            freqMap[num] = freqMap.get(num,0)+1. # one pass count #O(n)
        
        minHeap = []
        for n,f in freqMap.items():
            heapq.heappush(minHeap,(f,n))
        while len(minHeap) > k:
            heapq.heappop(minHeap)
        
        res = []
        while len(res) < k:
            res.append(heapq.heappop(minHeap)[1])
        return res    


        #O logn
        #o(n)