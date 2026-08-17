class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}
        for num in nums:
            freqMap[num] = freqMap.get(num,0)+1. # one pass count #O(n)
        
        arr = []
        for n,f in freqMap.items():
            arr.append([f,n])   #O(n)
        arr.sort()#O(nlogn)
        
        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res    


        #O nlogn
        #o(n)