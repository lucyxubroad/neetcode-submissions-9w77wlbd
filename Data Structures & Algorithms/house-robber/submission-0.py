class Solution:

    def dp(self, nums, house, prev):
        if house == len(nums):
            return 0
        elif house == len(nums)-1:
            return nums[house]
        elif house in prev:
            return prev[house]
        else:
            rob_house = nums[house] + self.dp(nums, house+2, prev)
            dont_rob = self.dp(nums, house+1, prev)
            prev[house] = max(rob_house, dont_rob)
            return prev[house]

    def rob(self, nums: List[int]) -> int:
        return self.dp(nums,0,{})
