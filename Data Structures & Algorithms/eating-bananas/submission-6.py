class Solution:

    def findIndex(self, piles, eating_rate):
        index = 0
        while index < len(piles) and piles[index] <= eating_rate: 
            index+=1
        return index

    def getRequiredEatingTime(self, piles, eating_rate):
        eating_rate_max_index = self.findIndex(piles, eating_rate)
        hours_to_complete = eating_rate_max_index
        for i in range(eating_rate_max_index, len(piles)):
            hours_to_complete+=math.ceil(piles[i]/eating_rate)
        return hours_to_complete


    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        max_k = piles[len(piles)-1]

        start_index = 1
        end_index = max_k
        search_index = (end_index - start_index) // 2 + start_index # this will always round down. for example 0.5 -> 0
        

        while start_index < end_index and end_index-start_index>1:
            hours_to_complete = self.getRequiredEatingTime(piles,search_index)
            if hours_to_complete <= h:
                end_index = search_index 
            else:
                start_index = search_index
            search_index = ((end_index - start_index) // 2) + start_index # this will always round down. for example 0.5 -> 0
        # print(start_index,self.getRequiredEatingTime(piles,start_index))
        # print(end_index,self.getRequiredEatingTime(piles,end_index))
        return start_index if self.getRequiredEatingTime(piles, start_index) <= h else end_index
        







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