class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist_map = {} #ex: (4,[2,2])
        
        for x,y in points:
            dist = x**2 + y**2
            dist_map[(dist, x, y)] = [x,y]

        k_close_freq_list = heapq.nsmallest(k,dist_map.keys()) 
        return [dist_map[i] for i in k_close_freq_list]



            
