# Problem : let 으로 시작하는 원소를 dig 보다 앞에오게하고, let들은 뒷부분 문자열로 정렬하고, 문자가 똑같으면 id로 정렬.
# Time : O(NlogN), Space : O(N)


class Solution:
    def sort(self, e):
        i, log = e.split(" ", 1)
        if log[0].isalpha():
            return (0, log, i)
        else:
            return (1, None, None)

    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        return sorted(logs, key=self.sort)
