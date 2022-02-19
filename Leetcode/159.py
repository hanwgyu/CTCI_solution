class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        """
        Sliding window. 최적화. 동일한 문자의 마지막 index를 저장.
        
        O(N) / O(1)
        """
        d = {}
        i = ans = 0
        for j, c in enumerate(s):
            if len(d.keys()) == 2 and c not in d:
                # 문자 하나를 없애야함.
                # 현재 포함된 여러 문자들 중, 마지막 index가 가장 작은 문자를 제거하여 길이를 제일 길게 만듬.
                c_del, i_del = sorted(d.items(), key=lambda e: e[1])[0]
                del d[c_del]
                i = i_del+1
            d[c] = j
            ans = max(ans, j-i+1)
        return ans