# Solution 1 - error

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        res = int(''.join(str(x) for x in num)) + k
        t = []
        for i in str(res):
            t.append(int(i))
        return t


# Solution 2 

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        num.reverse()
        i = 0

        while k:
            digit = k % 10
            if i < len(num):
                num[i] += digit
            else:
                num.append(digit)

            carry = num[i] // 10
            num[i] = num[i] % 10

            k = k // 10
            k += carry
            i += 1

        num.reverse()
        return num
