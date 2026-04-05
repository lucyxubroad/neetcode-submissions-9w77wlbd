class Solution:

    def dfs(self, past, index, nums, target, combos):
        curr_sum = sum(past)
        
        if curr_sum == target:
            combos.append(past)
            return
        elif curr_sum > target:
            return
        elif index >= len(nums):
            return
        
        self.dfs(past + [nums[index]], index, nums, target, combos)
        self.dfs(past, index+1, nums, target, combos)

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combinations = []
        self.dfs([], 0, nums, target, combinations)       
        return combinations
        