# TIme : O(N), Space :O(N)


class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        c_to_s, s_to_c = {}, {}
        words = str.split(" ")
        if len(words) != len(pattern):
            return False
        for i, s in enumerate(words):
            c = pattern[i]
            if s not in s_to_c and c not in c_to_s:
                c_to_s[c], s_to_c[s] = s, c
            elif s not in s_to_c or c not in c_to_s:
                return False
            else:
                if s_to_c[s] != c:
                    return False
        return True
