from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = Counter(s1)
        print(s1_count)
        s1_len = len(s1)
        for i in range(len(s2)):
            l, r = i, (i + s1_len)
            temp = Counter(s2[l:r])
            print(temp)
            if temp == s1_count:
                return True
        return False