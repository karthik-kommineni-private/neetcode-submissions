class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        min_heap = []
        res = []
        frq_map = Counter(nums) #using lib - alternate to manual freq-map, O(N)

        for key, freq in frq_map.items():
            heapq.heappush(min_heap,(freq,key)) #o(logN) - heare N is K -> O(Nlogk)
            if(len(min_heap) > k): heapq.heappop(min_heap) # we need heap of size k only

        while min_heap:
            res.append(heapq.heappop(min_heap)[1])   #O(logN) - here N is K ->O(logK)

        return res

        