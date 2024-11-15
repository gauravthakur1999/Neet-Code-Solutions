class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        l = 0   
        window = {}
        count = Counter(t)
        have, need = 0, len(count)
        res, r_len = [-1, -1], float("infinity")
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0) 
            
            if c in count and window[c] == count[c]:
                have += 1

            while have == need:
                if (r - l +1) < r_len:
                    res = [l, r]
                    r_len = (r - l +1)

                window[s[l]] -= 1
                if s[l] in count and window[s[l]]< count[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l : r + 1] if r_len != float("infinity") else ""