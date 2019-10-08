# Catalan number
# 총 갯수 : 2nCn - 2nCn+1 = 1/(n+1) * 2nCn+1
# Time : O(4^N/N^(3/2)), Space : O(4^N/N^(3/2))


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def generateRight(s: List[str], n: int) -> List[List[str]]:
            ans, l, length = [], 0, len(s)       
            for c in s:
                if c == "(": l += 1
                else: l -= 1
             
            if l+length == 2 * n:
                for _ in range(l):
                    s.append(")")
                ans.append(s)
                return ans
            
            ans.append(copy.deepcopy(s))
            for i in range(l-1):
                s.append(")") 
                ans.append(copy.deepcopy(s))
            s.append(")") 
            ans.append(s)
            return ans
        
        stack, ans = [["("]], []
        while stack:
            s = stack.pop()
            for e in generateRight(s, n):
                if len(e) == 2*n:
                    ans.append("".join(e))
                else:
                    e.append("(")
                    stack.append(e)
        return ans
        
