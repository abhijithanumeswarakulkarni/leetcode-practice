class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res = set()
        for email in emails:
            first, second = email.split("@")
            updatedFirst = ""
            for x in first:
                if x.isalpha():
                    updatedFirst += x
                if x == '+':
                    break
            updatedEmail = updatedFirst + "@" + second
            res.add(updatedEmail)
        
        return len(res)