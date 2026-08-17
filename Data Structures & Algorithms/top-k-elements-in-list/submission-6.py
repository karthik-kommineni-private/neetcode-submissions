class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frqMap = Counter(nums)  # O(N)
        max_heap = [(-freq, key) for key, freq in frqMap.items()]  # O(N)
        heapq.heapify(max_heap)  # O(N)

        return [heapq.heappop(max_heap)[1] for _ in range(k)]  # O(k log N)

        