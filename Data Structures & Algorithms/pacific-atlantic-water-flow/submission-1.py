class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific_reachable = [[0 for x in range(len(heights[0]))] for y in range(len(heights))]
        atlantic_reachable = [[0 for x in range(len(heights[0]))] for y in range(len(heights))]
        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        # traverse pacific
        # 1. add the edges to to_traverse list
        to_traverse = [] # note: there will be one duplicate here
        for j in range(len(heights[0])):
            to_traverse.append((0, j))
        for i in range(len(heights)):
            to_traverse.append((i, 0))
        
        # 2. visit to_traverse list in FIFO order
        # print('pacific to traverse')
        # print(to_traverse)

        while len(to_traverse) > 0:
            (x,y) = to_traverse.pop(0)
            if pacific_reachable[x][y] != 1:
                pacific_reachable[x][y] = 1
                current_height = heights[x][y]
                for (ns, ew) in directions:
                    if 0 <= x+ns < len(heights) and 0 <= y+ew < len(heights[0]):
                        if current_height <= heights[x+ns][y+ew]:
                            to_traverse.append((x+ns, y+ew))

        # traverse atlantic. note the algorithm will be the same as pacific

        to_traverse = []  # note: there will be one duplicate here
        for j in range(len(heights[0])):
            to_traverse.append((len(heights)-1, j))
        for i in range(len(heights)):
            to_traverse.append((i, len(heights[0])-1))


        # 2. visit to_traverse list in FIFO order
        # print('atlantic to traverse')
        # print(to_traverse)

        while len(to_traverse) > 0:
            (x,y) = to_traverse.pop(0)
            if atlantic_reachable[x][y] != 1:
                atlantic_reachable[x][y] = 1
                current_height = heights[x][y]
                for (ns, ew) in directions:
                    if 0 <= x+ns < len(heights) and 0 <= y+ew < len(heights[0]):
                        if current_height <= heights[x+ns][y+ew]:
                            to_traverse.append((x+ns, y+ew))

        reachable = []
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if pacific_reachable[i][j] == 1 and atlantic_reachable[i][j] == 1:
                    reachable.append([i,j])

        # print('reachable')
        # print(pacific_reachable)
        # print(atlantic_reachable)
        return reachable