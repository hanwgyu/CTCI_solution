# Solution : Backtracking 알고리즘.

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def findAllValidAddresses(s: str, start: int, count: int):
            if len(s)-start < count or count*3 < len(s)-start or count == 0:
                return
            tmp = []
            for i in range(1,4):
                if len(s)-start >= i and ((s[start] == '0' and i == 1) or s[start] != '0') and 0 <= int(s[start:start+i]) <= 255:
                    if count == 1 and start+i == len(s):
                        tmp.append([])
                    ret = findAllValidAddresses(s, start+i, count-1)
                    if ret:
                        for e in ret:
                            e.append(start+i)
                            tmp.append(e)
            return tmp
        
        ans = []
        ret = findAllValidAddresses(s, 0, 4)
        if ret:
            for e in ret:
                s1, s2, s3 = e[2], e[1], e[0]
                ans.append(s[0:s1] + "." + s[s1:s2] + "." + s[s2:s3] + "." + s[s3:] )
        return ans
                
