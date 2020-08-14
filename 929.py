from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()
        for e in emails:
            local, domain = e.split('@')
            plus_idx = local.find('+')
            if plus_idx >= 0:
                local = local[:plus_idx]
            local = local.replace('.', '')
            unique_emails.add(local + '@' + domain)
        return len(unique_emails)

if __name__ == "__main__":
    s = Solution()
    emails = ["test.email+alex@leetcode.com","test.email.leet+alex@code.com"]
    print(s.numUniqueEmails(emails))