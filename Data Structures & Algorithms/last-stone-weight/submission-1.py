class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        
        while len(stones) >= 2 :
            s1 = -heapq.heappop(stones)
            s2 = -heapq.heappop(stones)
            if abs(s1-s2) > 0:
                heapq.heappush(stones, -(abs(s1-s2)))
        
        if len(stones) == 1:
            return -stones[0]
        else:
            return 0
            