class Solution:
    # bfs to find the path to a treasure
    def findPathToTreasure(self, i, j,grid):
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        visited = set()
        to_traverse = deque()
        to_traverse.append((i,j,0))
        minPath = 2147483647
        while len(to_traverse) > 0:
            (a,b,c) = to_traverse.popleft()
            if grid[a][b] == 0:
                minPath = min(minPath, c)
            elif grid[a][b] != 2147483647:
                minPath = min(minPath, c+grid[a][b])
            else:
                for (x,y) in directions:
                    new_x, new_y = a+x, b+y
                    if new_x >= 0 and new_x<len(grid) and new_y >= 0 and new_y<len(grid[0]) and (new_x, new_y) not in visited and grid[new_x][new_y] != -1:
                        visited.add((new_x,new_y))
                        to_traverse.append((new_x,new_y,c+1))
        return minPath


    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2147483647:
                    grid[i][j] = self.findPathToTreasure(i,j,grid)
        
                    
                    
                        
                        



