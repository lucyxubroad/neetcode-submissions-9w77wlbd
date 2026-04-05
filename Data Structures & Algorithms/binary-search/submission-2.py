class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        found = False
        start = 0 #4
        end = len(nums) #6

        while start != end:
            ind = int((end-start) / 2) + start
            if nums[ind] == target: 
                return ind
            elif target < nums[ind]:
                end = ind
            else:
                start = ind+1
        
        return -1
