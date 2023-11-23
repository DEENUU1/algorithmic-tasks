class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ["a", "e", "i", "o", "u"]

        vowels_in_s = []
        s_list = list(s)

        for char in s_list:
            if char.lower() in vowels:
                vowels_in_s.append(char)

        for i in range(len(s_list)):
            if s_list[i].lower() in vowels:
                s_list[i] = vowels_in_s.pop()

        return ''.join(s_list)