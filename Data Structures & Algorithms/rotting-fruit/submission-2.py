class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        to_traverse = deque()
        visited = set()
        directions = [(-1,0),(1,0),(0,1),(0,-1)]
        num_fruits = 0
        rotten_fruits = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2 or grid[i][j] == 1:
                    num_fruits+=1
                if grid[i][j] == 2:
                    to_traverse.append((i,j,0))
        
        while len(to_traverse) > 0:
            (i,j,minute) = to_traverse.popleft()
            rotten_fruits.append((i,j,minute))
            for (x,y) in directions:
                new_i, new_j = i+x,j+y
                if 0 <= new_i < len(grid):
                    if 0 <= new_j < len(grid[0]):
                        if (new_i, new_j) not in visited and grid[new_i][new_j] == 1:
                            to_traverse.append((new_i,new_j,minute+1))
                            visited.add((new_i,new_j))
        
        if num_fruits == 0:
            return 0
        elif len(rotten_fruits) < num_fruits:
            return -1
        else:
            minimumMin = -math.inf
            for (_,_,minute) in rotten_fruits:
                minimumMin = max(minimumMin, minute)
            return minimumMin
                
                


