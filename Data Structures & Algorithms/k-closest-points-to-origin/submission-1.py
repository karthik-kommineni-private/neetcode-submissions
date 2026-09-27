class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        maxHeap = []
        res = []
        for x,y in points:
            dist = -(x**2+y**2)
            heapq.heappush(maxHeap, (dist,x,y))
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)

        for x,y,z in maxHeap:
            res.append([y,z])
            
        return res    
               



        
        