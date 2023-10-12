class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        max_right = -1

        for i in range(n - 1, -1, -1):
            temp = arr[i]
            arr[i] = max_right
            max_right = max(max_right, temp)

        return arr