class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums)-1
        search = start+((end-start)//2)
        while start <= end:
            # print('start: ', start, 'end: ', end, 'search: ', search)
            if nums[search] == target:
                return search
            if nums[search] < nums[0]:
                # elements after this are sorted
                if  nums[search] < target <= nums[end]:
                    start = search + 1
                else:
                    end = search - 1
            elif nums[search] > nums[len(nums)-1]:
                # elements before this are sorted
                if nums[start] <= target < nums[search]:
                    end = search - 1
                else:
                    start = search + 1
            else:
                if target < nums[search]:
                    end = search - 1
                else:
                    start = search + 1
            search = start+((end-start)//2)
        print(start,end)
        return search if nums[search] == target else -1