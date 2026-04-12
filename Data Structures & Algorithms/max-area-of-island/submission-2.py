class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        seen = [[False for col in grid[0]] for row in grid]
        maxArea = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if seen[i][j] is False:
                    seen[i][j] = True
                    to_traverse = collections.deque()
                    if grid[i][j] == 1:
                        to_traverse.append((i,j))
                        area = 0
                        while len(to_traverse) > 0:
                    
                            (visiting_i, visiting_j) = to_traverse.popleft()
                            area+=1
                            seen[visiting_i][visiting_j] = True
                            top = (visiting_i-1,visiting_j) if visiting_i != 0 else None
                            down = (visiting_i+1,visiting_j) if visiting_i!= len(grid)-1 else None
                            left = (visiting_i,visiting_j-1) if visiting_j != 0 else None
                            right = (visiting_i,visiting_j+1) if visiting_j != len(grid[0])-1 else None
                            for next_visit in [top, down, left, right]:
                                if next_visit is not None:
                                    (x,y) = next_visit
                                    if not seen[x][y] and grid[x][y] == 1 and (x,y) not in to_traverse:
                                        to_traverse.append((x,y))
                          
                        maxArea = max(area, maxArea)
            
        
        return maxArea