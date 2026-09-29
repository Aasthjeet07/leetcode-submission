class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        size = len(nums)
        for i in range(size-1, -1, -1):
            nums.append(nums[i])
        return nums