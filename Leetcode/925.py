# 고민 1 :name에서 같은 문자가 연속할때만 처리를 잘해주면됨.
# Time : O(N+T), Space : O(1)

# 고민 2: 1번 풀이를 잘 정리.

class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = 0
        for j in range(len(typed)):
            if i < len(name) and name[i] == typed[j]:
                i += 1
            elif j == 0 or typed[j] != typed[j-1]:
                return False
        return i == len(name)

    def isLongPressedName_1(self, name: str, typed: str) -> bool:
        i, j = 0, 0
        while i < len(name) and j < len(typed):
            if name[i] != typed[j]:
                return False
            while i < len(name)-1 and name[i] == name[i+1]:
                if j >= len(typed) or name[i] != typed[j]:
                    return False
                i += 1
                j += 1
            while j < len(typed)-1 and typed[j] == typed[j+1]:
                j += 1
            i += 1
            j += 1

        return True if i == len(name) and j == len(typed) else False
