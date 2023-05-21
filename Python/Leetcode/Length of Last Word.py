class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last = s.split()
        return len(last[-1])