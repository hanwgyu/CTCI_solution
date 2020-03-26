# Solution 1 : Time : O(l1+l2), Space : O(1)

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def index(s: str) -> int:
            return ord(s) - ord('a')
        
        if len(s1) > len(s2):
            return False
        a1, a2 = [0]*26, [0]*26
        for i in range(len(s1)):
            a1[index(s1[i])] += 1
            a2[index(s2[i])] += 1
        if a1 == a2:
            return True    
        for i in range(len(s1), len(s2)):
            a2[index(s2[i-len(s1)])] -= 1
            a2[index(s2[i])] += 1
            if a1 == a2:
                return True
        return False
        
