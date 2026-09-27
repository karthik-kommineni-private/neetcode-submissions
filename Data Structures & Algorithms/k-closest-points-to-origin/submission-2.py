class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        res = []
        for x, y in points:
            dist = -(x**2 + y**2)   # negate so the FARTHEST point (biggest real distance) is easiest to evict
            heapq.heappush(maxHeap, (dist, x, y))
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)   # evicts the smallest (dist, ...) tuple = most negative dist = farthest point

        for dist, x, y in maxHeap:   # correctly named now — no confusion about what's in each slot
            res.append([x, y])

        return res