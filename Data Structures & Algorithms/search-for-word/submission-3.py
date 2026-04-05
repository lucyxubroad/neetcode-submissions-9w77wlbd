class Solution:
    def word_search(self, x, y, l, seen, board, word):
        if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]):
            return False
        if (x,y) in seen or board[x][y] != word[l]:
            return False
        seen.add((x,y))
        if l==len(word)-1:
            return True
        found = (
            self.word_search(x+1,y,l+1,seen,board,word) or 
            self.word_search(x-1,y,l+1,seen,board,word) or 
            self.word_search(x,y+1,l+1,seen,board,word) or 
            self.word_search(x,y-1,l+1,seen,board,word)
        )
        seen.remove((x,y))
        return  found

    def exist(self, board: List[List[str]], word: str) -> bool:
        i, j = 0,0
        while (i < len(board)):
            j=0
            while (j < len(board[i])):
                if board[i][j] == word[0]:
                    seen = set()
                    found = self.word_search(i, j, 0, seen, board, word)
                    if found:
                        return True
                j+=1
            i+=1
        return False    