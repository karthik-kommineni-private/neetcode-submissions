class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""

        #tracks index of each str
        for i in range(len(strs[0])):
            for j in range(len(strs)):
                if i == len(strs[j]) or strs[j][i] != strs[0][i]: #ex: match first c in each str
                    return res        
        
            res = res + strs[0][i]

        return res    
'''
Longest Common Prefix — Summary

1. This solution uses vertical scanning across strings.
2. The first string is used as the reference.
3. Characters are compared column by column across all strings.
4. If any string ends, the prefix must stop.
5. If any character mismatches, the prefix must stop.
6. The result is built incrementally from left to right.
7. Early return ensures efficiency.
8. Time Complexity: O(n * m) — n strings and m characters per string.
9. Space Complexity: O(1) — excluding the output string.
'''