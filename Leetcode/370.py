class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        """
        update를 [0ㅡendIdx,inc] + [0~startIdx, -inc] 로 나눠서 생각.
        아래 방법과 동일한데, 굳이 sorting 할 필요 없이 ans에 저장해놓고 거꾸로 오면된다.

        O(n+k) / O(1)
        """
        ans = [0 for _ in range(length+1)]
        for start, end, inc in updates:
            ans[start] += -inc
            ans[end+1] += inc
        
        s = 0
        for i in reversed(range(length+1)):
            s, ans[i] = ans[i]+s, s
        return ans[:length]
    
    
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        """
        update를 [0ㅡendIdx,inc] + [0~startIdx, -inc] 로 나눠서 생각.
        그다음 거꾸로 sorting해서 update진행.
        
        O(n+klogk) / O(k)
        """
        l = []
        for start, end, inc in updates:
            l.append((start, -inc))
            l.append((end+1, inc))
        l = sorted(l, key=lambda e: -e[0])
        ans = [0 for _ in range(length)]
        s, last_i = 0, length
        for i, inc in l:
            for j in range(i, last_i):
                ans[j] = s
            s += inc
            last_i = i
        return ans