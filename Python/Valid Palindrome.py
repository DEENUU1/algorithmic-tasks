class Solution:
    def isPalindrome(self, s: str) -> bool:
        char = []
        for letter in s.lower():
            if letter.isalnum():
                char.append(letter)
        
        return char == char[::-1]
        