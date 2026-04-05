class Solution:

    def getRequiredEatingTime(self, piles, eating_rate):
        hours = 0
        for p in piles:
            hours += math.ceil(p / eating_rate)  # ceil(p / k) without float
        return hours


    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        max_k = piles[len(piles)-1]

        start_index = 1
        end_index = max_k
        # search_index = (end_index - start_index) // 2 + start_index # this will always round down. for example 0.5 -> 0

        while start_index < end_index:
            search_index = (end_index - start_index) // 2 + start_index
            if self.getRequiredEatingTime(piles,search_index) <= h:
                end_index = search_index 
            else:
                start_index = search_index+1
       
        return start_index 
        







"""
piles = [4,8,5,6,3,2,9,4], h=6

step 1
    sort the array
    [2,3,4,4,5,6,8,9]

step 2
    find the smallest value/index at which we we CANNOT finish eating 
    --> k needs to be BIGGER than this value

step 3
    find the first value/index from the array where we CAN finish eating
    --> k can be smaller (or = this value)

step 4 
    the values above give us the range that we should be searching over
    --> look for the minimum value that enables us to still finish the bananas <= h 
            for this, we can binary search for the minimum

"""