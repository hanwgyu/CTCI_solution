# Catalan number
# 총 갯수 : 2nCn - 2nCn+1 = 1/(n+1) * 2nCn+1
# Time : O(4^N/N^(3/2)), Space : O(4^N/N^(3/2))

# Solution 1: Iteration 돌고, string에 대한 array를 공유해가면서 계산해나아감.

# Solution 2: Tree의 Preorder Traversal처럼 동작. 왼쪽값부터 계산하면 항상 조건을 만족함.

class Solution:
    def generateParenthesis_2(self, n: int) -> List[str]:
        def preOrder(ans: List[str], s: str, l: int, r: int) -> None:
            if not l and not r:
                ans.append(s)
            if l: preOrder(ans, s + '(', l-1, r)
            if l < r: preOrder(ans, s + ')', l , r-1)
            return ans
        
        return preOrder([], "", n, n)
    
    
    def generateParenthesis_1(self, n: int) -> List[str]:
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
        
