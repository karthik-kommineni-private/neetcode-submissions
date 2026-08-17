class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        min_heap = []  # Min-heap to keep top k frequent elements
        res = []
        frq_map = Counter(nums)  # Frequency map in O(N)

        for key, freq in frq_map.items():
            heapq.heappush(min_heap, (freq, key))     # O(logK) operation
            if len(min_heap) > k:
                heapq.heappop(min_heap)               # Maintain size K → O(logK)

        while min_heap:
            res.append(heapq.heappop(min_heap)[1])    # Extract element → O(logK)

        return res[::-1]  # Optional: reverse if you want highest freq first

        