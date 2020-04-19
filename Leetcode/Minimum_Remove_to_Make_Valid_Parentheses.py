# Solution 1: stack 과 각 문자를 사용하는지 여부 usage를 사용해 마지막에 문자를 생성
# Time : O(N), Space : O(N)

# Solution 2: stack에 문자열 자체를 저장해감. 
# Time : O(N), Space : O(N)

class Solution:
    def minRemoveToMakeValid_2(self, s: str) -> str:
        st, cur = [], ''
        for c in s:
            if c == '(':
                st.append(cur)
                cur = ''
            elif c == ')':
                if st:
                    cur = st.pop() +'(' + cur + ')'
            else:
                cur += c
        while st:
            cur = st.pop() + cur
        return cur

    def minRemoveToMakeValid_1(self, s: str) -> str:
        usage, st = [False for _ in range(len(s))], []
        for i, c in enumerate(s):
            if c == '(':
                st.append((c, i))
            elif c == ')':
                if st:
                    usage[st.pop()[1]] = True
                    usage[i] = True
            else:
                usage[i] = True
        return ''.join([c for i,c in enumerate(s) if usage[i]])
