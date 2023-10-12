class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []

        max_values = []
        max_window = deque()

        for i, num in enumerate(nums):
            while max_window and max_window[0] < i - k + 1:
                max_window.popleft()

            while max_window and nums[max_window[-1]] < num:
                max_window.pop()

            max_window.append(i)

            if i >= k - 1:
                max_values.append(nums[max_window[0]])

        return max_values