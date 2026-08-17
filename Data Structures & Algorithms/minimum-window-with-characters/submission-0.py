class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #if lent> s: "" 
        if len(t) > len(s):
            return ""
        l, m = 0,0
        min_length = float("inf")
        t_map = Counter(t)
        window_map = {} # {x:1,a:1}, #add only if its a key from t_map

        for r in range(len(s)):
            if s[r] in t_map: #why not if not in window_map ?
                window_map[s[r]] = window_map.get(s[r], 0) + 1
            #w_map >= t_map
            while self.window_map_contains_t_map(window_map, t_map): 
                if s[l] in window_map:
                    window_map[s[l]] -= 1 
                if r-l+1 < min_length:
                    min_length = r-l+1
                    min_sub_str = s[l:r+1]  
                l+=1

        return min_sub_str    


    def window_map_contains_t_map(self, window_map, t_map) -> bool:
        """Return True if window_map covers all chars from t_map."""
        for ch in t_map:
            if window_map.get(ch, 0) < t_map[ch]:
                return False
        return True     


                

                






    #w - {}             no - 0








        