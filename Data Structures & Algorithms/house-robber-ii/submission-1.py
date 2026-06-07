class Solution:

    def dp(self, nums, house, robbed_first, prev):
        if house == len(nums):
            return 0
        elif house == len(nums)-1:
            return nums[house] if not robbed_first else 0
        elif house == len(nums)-2:
            return max(nums[house], self.dp(nums, house+1, robbed_first, prev))
        elif house in prev:
            index = 0 if not robbed_first else 1
            if index in prev[house]:
                return prev[house][index]
            else:
                rob = nums[house] + self.dp(nums, house+2, robbed_first, prev)
                skip = self.dp(nums, house+1, robbed_first, prev)
                index = 0 if not robbed_first else 1
                prev[house][index] = max(rob, skip)
                return prev[house][index]
        elif house == 0:
            if robbed_first:
                return nums[house] + self.dp(nums, house+2, robbed_first, prev)
            else:
                return self.dp(nums, house+1, robbed_first, prev)
        else:
            rob = nums[house] + self.dp(nums, house+2, robbed_first, prev)
            skip = self.dp(nums, house+1, robbed_first, prev)
            index = 0 if not robbed_first else 1
            prev[house] = {}
            prev[house][index] = max(rob, skip)
            return prev[house][index]

    def rob(self, nums: List[int]) -> int:
        return max(self.dp(nums, 0, True, {}), self.dp(nums, 0, False, {}))

