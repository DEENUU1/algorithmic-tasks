class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        uniq = set()

        for email in emails:
            name, domain = email.split("@")
            name = name.split("+")[0]
            name = name.replace(".", "")
            email = name + "@" + domain
            uniq.add(email)
        return len(uniq)