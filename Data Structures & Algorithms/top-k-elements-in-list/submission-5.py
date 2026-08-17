class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        frqMap = Counter(nums)
        max_heap = [(-freq,key) for key, freq in frqMap.items()]
        heapq.heapify(max_heap)
        return [heapq.heappop(max_heap)[1] for _ in max_heap]


        