class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_heap = []
        for (i, n) in enumerate(nums[0:k]):
          heapq.heappush(max_heap, (-n, -i))
        max_vals = []
        start, end = 0, k-1
        while end < len(nums):
            (max_val_negated, max_val_index_negated) = max_heap[0]
            
            while -max_val_index_negated < start:
              heapq.heappop(max_heap)
              (max_val_negated, max_val_index_negated) = max_heap[0]
            max_vals.append(-max_val_negated)
            end = end + 1     
            if end < len(nums):
              heapq.heappush(max_heap, (-nums[end], -end))  
            start = start + 1
       
        return max_vals