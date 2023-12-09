# Solution 1 - Output Limit


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        res = 0
        counter = 0
        vowels = ["a", "e", "i", "o", "u"]

        for i in range(len(s) - k + 1):
            x = s[i:i + k]
            for char in x:
                if char in vowels:
                    print(f"ADD: {char}")
                    counter += 1

            if counter > res:
                res = counter
                counter = 0
            else:
                counter = 0

        return res



# Solution 2

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ["a", "e", "i", "o", "u"]
        count, ans = 0, 0

        for i in range(k):
            if s[i] in vowels:
                count += 1
        ans = max(ans, count)

        for i in range(k, len(s)):
            if s[i-k] in vowels:
                count -= 1
            if s[i] in vowels:
                count += 1
                ans = max(ans, count)
        return ans