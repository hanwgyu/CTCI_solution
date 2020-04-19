# Solution : use stack
# Time : O(N), Space : O(N)

class Solution:
    def removeDuplicates(self, S: str) -> str:
        st = []
        for s in S:
            if st and st[-1] == s:
                st.pop()
                continue
            st.append(s)
        return ''.join(st)
