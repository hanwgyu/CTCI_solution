# Solution 0 : Brute-force. Time : O(n^2), Space : O(1)

# Solution 1 : DP. 각 위치를 끝으로 하는 palindrome의 모든 start idx를 저장. (is_all_same같이 저장.)
# 1) 매 step마다 현재 위치의 char과 최대 길이 이전의 char이 동일한지 체크.
# 2) 만약 저장된 palindrome의 모든 char이 똑같고, 현재 위치의 char도 똑같으면 이전 위치의 char체크 안하고 추가.
# Time : O(N), Space : O(N)


from collections import deque

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def updateAns(start, end):
            if len(self.ans) < end-start+1:
                self.ans = s[start:end+1]
                
        if len(s) == 0:
            return ""
        dp, self.ans = [(0, True)], s[0]
        for i in range(1, len(s)):
            temp = []
            for (start_idx, all_same) in dp:
                if start_idx-1 >= 0 and s[start_idx-1] == s[i]:
                    if all_same and s[i] != s[i-1]:
                        all_same = False
                    temp.append((start_idx-1, all_same))
                    updateAns(start_idx-1, i)
                elif all_same and s[i] == s[i-1]:
                    temp.append((start_idx, all_same))
                    updateAns(start_idx, i)
            temp.append((i, True))
            dp = temp
        return self.ans
