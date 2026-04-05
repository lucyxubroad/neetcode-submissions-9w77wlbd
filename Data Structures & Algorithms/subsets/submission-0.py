class Solution:

    def recurse(self, past, index, nums, subsets):
        if index == len(nums)-1:
            subsets.append(past + [nums[index]])
            subsets.append(past + [])
            return 
        self.recurse(past + [nums[index]], index+1, nums, subsets)
        self.recurse(past + [], index+1, nums, subsets)
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        all_subsets = []
        self.recurse([], 0, nums, all_subsets)
        return all_subsets
        
        