class Solution:
    def findMin(self, nums: List[int]) -> int:
        start, end = 0, len(nums)-1
        minimum = math.inf

        while start <= end:
            search = start+((end-start)//2)
            # print(minimum)
            if nums[search] < nums[0]:
                # pivot must be before this index
                minimum = min(minimum, nums[search])
                end = search - 1
            elif nums[search] > nums[len(nums)-1]:
                # pivot must be after this index
                minimum = min(minimum, nums[search])
                start = search + 1
            else:
                return nums[0]

        return minimum


