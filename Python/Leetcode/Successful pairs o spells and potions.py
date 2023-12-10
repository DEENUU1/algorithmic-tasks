# Solution 1 - time limit


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        n, m = len(spells), len(potions)

        # spells[i] = siła i elementu
        # potions[j] = sila j potionu

        # spell + potion >= success => succes

        # return [potion[i], poption[i]] = len(n)

        pairs = []

        for i in range(n):
            res = [x * spells[i] for x in potions]
            temp = []
            for r in res:
                if r >= success:
                    temp.append(r)

            pairs.append(len(temp))

        return pairs


# Solution 2

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        x = []

        for i in spells:
            l, r, ans = 0, len(potions) - 1, 0
            while l <= r:
                m = (l + r) // 2
                if potions[m]*i >= success:
                    ans += r - m + 1
                    r = m - 1
                else:
                    l = m + 1
            x.append(ans)
        return x