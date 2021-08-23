class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        s = set()
        for email in emails:
            a = email.split("@")
            s.add(str(a[0].split("+")[0].replace(".", "")) + "@"+ a[1])
        return len(s)
