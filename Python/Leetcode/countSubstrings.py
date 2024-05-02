class Solution:
    def countSubstrings(self, s: str) -> int:

        count = 0
        n = len(s)

        for window_size in range(1, n + 1):
            for i in range(n - window_size + 1):
                substr = s[i:i+window_size]
                if self.is_palindrome(substr):
                    count += 1

        return count

    @staticmethod
    def is_palindrome(text):
        return text == text[::-1]
