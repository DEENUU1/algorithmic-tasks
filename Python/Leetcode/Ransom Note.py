class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        char_counts = {}
        
        for char in magazine:
            if char in char_counts:
                char_counts[char] += 1
            else:
                char_counts[char] = 1
        
        for char in ransomNote:
            if char in char_counts and char_counts[char] > 0:
                char_counts[char] -= 1
            else:
                return False
        
        return True
