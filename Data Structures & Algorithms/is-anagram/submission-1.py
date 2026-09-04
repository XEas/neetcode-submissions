class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_set = {}
        t_set = {}
        for c in s:
            if c in s_set:
                s_set[c] += 1
                continue
            s_set[c] = 1
        for c in t:
            if c in t_set:
                t_set[c] += 1
                continue
            t_set[c] = 1

        for el in s_set:
            if not (el in t_set and s_set[el] == t_set[el]):
                return False

        for el in t_set:
            if not (el in s_set and s_set[el] == t_set[el]):
                return False   

        return True