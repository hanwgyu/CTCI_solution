class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        """
        O(N)/O(N)
        """
        st = []
        for c in s:
            if st and c == st[-1][0]:
                st[-1][1] += 1
            else:
                st.append([c,1])
            if st[-1][1] == k:
                st.pop()
        return "".join(c*n for c, n in st)