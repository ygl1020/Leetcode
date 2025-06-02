#在二维棋盘里每一个格子有一个字母,每次移动只能到相邻的格子,同一个格子只能用一次,求是否可以找到构成字符串的路径
def exist(self, board: List[List[str]], word: str) -> bool:
        row,col = len(board), len(board[0])
        i = 0
        seen = set()
        def backTracking(r,c,i):
            if i == len(word):
                return True
            if (r<0 or c<0 or r >=row or c>=col  or board[r][c]!=word[i] or i >=len(word) or (r,c) in seen):
                return False
            seen.add((r,c))
            res =  (backTracking(r+1,c,i+1) or
                    backTracking(r-1,c,i+1) or
                    backTracking(r,c+1,i+1) or
                    backTracking(r,c-1,i+1))
            # print(seen)
            seen.remove((r,c))
            return res
        for r in range(row):
            for c in range(col):
                i = 0
                if backTracking(r,c,i):
                    return True
        return False