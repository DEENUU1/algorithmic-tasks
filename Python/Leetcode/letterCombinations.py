class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        char_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        res = []

        def backtrack(i: int, string: str) -> None:
            if len(string) == len(digits):
                res.append(string)
                return
            for c in char_map[digits[i]]:
                backtrack(i + 1, string + c)

        if digits:
            backtrack(0, "")
        
        return res
