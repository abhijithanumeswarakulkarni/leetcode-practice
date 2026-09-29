class Solution:
    def uniqueEmailGroups(self, emails: list[str]) -> int:
        unq_emails = set()

        for email in emails:
            local, domain = email.split('@')
            normalised_local = ""
            for char in local:
                if char == '.':
                    continue
                elif char == '+':
                    break
                normalised_local += char.lower()
            normalised_domain = domain.lower()
            normalised_email = normalised_local + '@' + normalised_domain
            unq_emails.add(normalised_email)

        return len(unq_emails)            