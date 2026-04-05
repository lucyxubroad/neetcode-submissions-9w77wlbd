class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        for [x,y] in points:
            distance = math.sqrt(x**2 + y**2)
            if len(max_heap) == k:
                (max_distance, (a,b)) = max_heap[0]
                if -max_distance >= distance:
                    heapq.heappop(max_heap)
                    heapq.heappush(max_heap, (-distance, (x,y)))
            else:
                heapq.heappush(max_heap, (-distance, (x,y)))

        closest = []
        for (distance, point) in max_heap:
            closest.append(point)
        return closest