class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, f = 0, len(s) - 1

        while i < f:
            while i < f and not s[i].isalnum():
                i += 1
            while f > i and not s[f].isalnum():
                f -= 1
            if s[i].lower() != s[f].lower():
                return False
            i, f = i + 1, f - 1
        return True 