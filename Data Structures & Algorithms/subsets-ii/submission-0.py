class Solution:
    def recurse(self, index, nums, path, subsets):
        if index >= len(nums):
            subsets.append(path)
            return
        
        next_index = index+1
        while next_index < len(nums) and nums[next_index] == nums[index]:
            next_index += 1
        self.recurse(next_index, nums, path, subsets)
        self.recurse(index+1, nums, path + [nums[index]], subsets)
        

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        nums.sort()
        self.recurse(0, nums, [], subsets)
        return subsets