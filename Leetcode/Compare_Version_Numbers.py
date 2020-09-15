# Solution 1. Time : O(max(M, N)), Space : O(M+N)

# Solution 2. Time : O(max(M, N)), Space : O(1)


class Solution:
    def compareVersion_2(self, version1: str, version2: str) -> int:
        i, j = 0, 0
        while i < len(version1) or j < len(version2):
            n1, n2 = 0, 0
            while i < len(version1) and version1[i] != ".":
                n1 = n1 * 10 + int(version1[i])
                i += 1
            while j < len(version2) and version2[j] != ".":
                n2 = n2 * 10 + int(version2[j])
                j += 1
            if n1 > n2:
                return 1
            elif n1 < n2:
                return -1
            i, j = i + 1, j + 1
        return 0

    def compareVersion_1(self, version1: str, version2: str) -> int:
        v1, v2 = version1.split("."), version2.split(".")
        for i in range(max(len(v1), len(v2))):
            n1, n2 = (
                int(v1[i]) if i < len(v1) else 0,
                int(v2[i]) if i < len(v2) else 0,
            )
            if n1 > n2:
                return 1
            elif n1 < n2:
                return -1
        return 0
