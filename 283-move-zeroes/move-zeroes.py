class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        j = -1
        n = len(nums)
        for i in range(0, n):
            if nums[i] == 0:
                j = i
                break
        if j == -1:
            return nums
        for i in range(j +1 , n):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1
        for i in range(j, n):
            nums[i] = 0
        
        return nums

  

        """
        Do not return anything, modify nums in-place instead.
        """
        