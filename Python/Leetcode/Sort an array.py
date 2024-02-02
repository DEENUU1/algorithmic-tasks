class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.mergeSort(nums)
        return nums
    def mergeSort(self, nums: List[int]) -> None:
            if len(nums) > 1:
                mid = len(nums) // 2
                l, r = nums[:mid], nums[mid:]
                self.sortArray(l)
                self.sortArray(r)

                i = j = k = 0

                while i < len(l) and j < len(r):
                    if l[i] < r[j]:
                        nums[k] = l[i]
                        i += 1
                    else:
                        nums[k] = r[j]
                        j += 1
                    k += 1
                
                while i < len(l):
                    nums[k] = l[i]
                    i += 1
                    k += 1
                
                while j < len(r):
                    nums[k] = r[j]
                    j += 1
                    k += 1
                
