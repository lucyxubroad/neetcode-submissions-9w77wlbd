from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        seen = [[False for col in grid[0]] for row in grid]
        num = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if seen[i][j] is False:
                    seen[i][j] = True
                    to_traverse = deque()
                    if grid[i][j] == '1':
                        to_traverse.append((i,j))
                        while len(to_traverse) > 0:
                            (visiting_i, visiting_j) = to_traverse.popleft()
                            seen[visiting_i][visiting_j] = True
                            top = (visiting_i-1,visiting_j) if visiting_i != 0 else None
                            down = (visiting_i+1,visiting_j) if visiting_i!= len(grid)-1 else None
                            left = (visiting_i,visiting_j-1) if visiting_j != 0 else None
                            right = (visiting_i,visiting_j+1) if visiting_j != len(grid[0])-1 else None
                            for next_visit in [top, down, left, right]:
                                if next_visit is not None:
                                    (x,y) = next_visit
                                    if not seen[x][y] and grid[x][y] == '1':
                                        to_traverse.append((x,y))
                        num+=1
        return num
        
