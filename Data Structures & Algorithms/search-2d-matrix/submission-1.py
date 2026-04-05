class Solution:

    # 1x2, (0, 0..1)
    # 
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) < 1:
            return False
        num_rows = len(matrix)
        num_cols = len(matrix[0])
        min_row, max_row = 0, num_rows-1 # 0, 0
        min_col, max_col = 0, num_cols-1 # 0, 1
        search_row, search_col = int(max_row/2), int(max_col/2) # 0, 0

        while (
            search_row >= min_row and search_row<=max_row 
            and search_col >= min_col and search_col<=max_col
        ):
            if target < matrix[search_row][0]:
                max_row = search_row-1
            elif target > matrix[search_row][num_cols-1]:
                min_row = search_row+1
            else:
                if matrix[search_row][search_col] == target:
                    return True 
                elif target < matrix[search_row][search_col]:
                    max_col = search_col-1
                elif target > matrix[search_row][search_col]:
                    min_col = search_col+1 # min_col = 1
            search_row = int((max_row-min_row) / 2) + min_row
            search_col = int((max_col-min_col) / 2) + min_col
        
        return False
                

            
