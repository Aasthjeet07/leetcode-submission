class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        num_set = set(nums) #{12.3.4.100.200}
        ans = 0
        for num in num_set:
            if num - 1 not in num_set:
                curr = num
                curr_l = 1
                while curr + 1 in num_set:
                    curr += 1
                    curr_l += 1
                ans = max(ans , curr_l)
        return ans


        



        