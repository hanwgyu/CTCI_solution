class Solution:
    def simplifyPath(self, path: str) -> str:
        ans = []
        for s in path.split("/"):
            if s == "" or s ==".":
                continue
            elif s == "..":
                if ans:
                    ans.pop()
            else:
                ans.append(s)
        return "/"+"/".join(ans)