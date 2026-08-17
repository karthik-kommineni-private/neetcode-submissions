class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""

        #tracks index of each str
        for i in range(len(strs[0])):
            for j in range(len(strs)):
                if strs[j][i] != strs[0][i]: #ex: match first c in each str
                    return res        
        
            res = res + strs[0][i]

        return res    
        