class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []
        for num in nums:
            if len(min_heap) == k:
                curr_min = min_heap[0]
                if num > curr_min:
                    heapq.heappop(min_heap)
                    heapq.heappush(min_heap, num)
            else:
                heapq.heappush(min_heap, num)

        return min_heap[0]
        