class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lower = 0
        upper = 1
        longest = 1
        if len(s) == 0:
            return 0
        ch = set(s[0])
        while (upper < len(s)):
            if s[upper] in ch:
                while s[lower] != s[upper]:
                    ch.remove(s[lower])
                    lower += 1
                lower += 1
            longest = max(longest, upper - lower + 1)
            ch.add(s[upper])
            upper += 1

        return longest