class Solution:
    def isPalindrome(self, s: str) -> bool:
        s2 = ""
        s = s.lower()
        for ch in s:
            if ("A" <= ch <= "Z" or "a" <= ch <= "z" or "0" <= ch <= "9"):
                s2 += ch
        s = s2
        i = 0
        j = len(s) - 1
        pairs = len(s) // 2
        while pairs > 0:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
            pairs -= 1
        return True