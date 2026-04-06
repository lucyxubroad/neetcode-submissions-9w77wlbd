class Solution:
    def recurse(self, nums, path, remaining, permutations):
        if len(path) == len(nums):
            permutations.append(path)
            return
        for index, i in enumerate(remaining):
            if i:
                path_copy = path.copy()
                remaining_copy = remaining.copy()
                remaining_copy[index] = False
                self.recurse(nums, path_copy + [nums[index]], remaining_copy, permutations)

    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        remaining = [True for i in nums]
        self.recurse(nums, [], remaining, permutations)
        return permutations
