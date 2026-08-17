from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        l = 0
        min_length = float("inf")
        min_sub_str = ""   # ✅ safe initialization
        t_map = Counter(t) # target map (frequency of t)
        window_map = {}    # current window frequency map

        for r in range(len(s)):
            # ✅ only add chars that are in t_map
            if s[r] in t_map:
                window_map[s[r]] = window_map.get(s[r], 0) + 1

            # ✅ shrink window while valid
            while self.window_map_contains_t_map(window_map, t_map):
                # update best result
                if r - l + 1 < min_length:
                    min_length = r - l + 1
                    min_sub_str = s[l:r+1]

                # shrink left
                if s[l] in window_map:
                    window_map[s[l]] -= 1
                l += 1

        return min_sub_str

    def window_map_contains_t_map(self, window_map, t_map) -> bool:
        """Return True if window_map covers all chars from t_map."""
        for ch in t_map:
            if window_map.get(ch, 0) < t_map[ch]:
                return False
        return True
