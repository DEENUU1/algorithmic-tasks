class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        result = 0
        total = sum(arr[:k])

        for i in range(k, len(arr)):
            if total >= k * threshold:
                result += 1
            total += arr[i] - arr[i - k]

        if total >= k * threshold:
            result += 1

        return result