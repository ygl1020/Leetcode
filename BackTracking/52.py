def totalNQueens(self, n: int) -> List[List[str]]:
        """
        解题思路还是回溯,关键在于这里的数组是二维的数组,那么二维数组要怎么处理？什么时候return?再每一层递归我们都要干什么?如果验证当前放置的'Q'符合要求？
        1)建立一个二维数组,以n为长和宽,最里面的数组为字符串. 2)当我们遍历到row==len(n)时-->代表我们已经再最后的row放置完'Q'并且验证完了结果,我们然后进入下一层递归return 结果
        3)我们再当前row的每一个col放置Q然后每放置完一次Q进行递归以及回溯4)我们判断当前row的所有col是否有Q，45度角和135度角是否有Q，如果任何一个条件中找到了Q那就说明当前摆放不符合规定
        这里我们不需要确认225和315度的验证,因为根据递归的特性.我们不会再当前row的下面放置'Q'
        """
        res = []
        board = ['.'*n for _ in range(n)] # 这里的'.'不需要放进数组里['.']，它本身就可以看作一个一维数组,并且放入数组对后面的处理反而造成麻烦
        def backtracking(n,row,board,res):
            if row==n: # 需要再row==n时return因为要执行完n-1层的'Q'的放置,然后继续递归到下一层再return, error 应该是当row==n,而不是len(path)==n
                res.append(board[:])
                return 
            for col in range(n):
                if self.isValid(row,col,board): #error # 应该先判断棋盘是否合格再进行下一步,可以想象为这个回合修改了棋盘然后下个回合要先判断棋盘是否合格再继续下一步
                    board[row] = board[row][:col] + 'Q' + board[row][col+1:] #error  这里是用row和col来进行具体的切割的,如果只用row的话并不能达到再当前row中每一次对一个col进行Q的放置 这里需要赋值board[row]这样才算放置了queen在棋盘上, 而不是用tmp接住它
                    backtracking(n,row+1,board,res)
                    board[row] = board[row][:col] + '.' + board[row][col+1:]
        backtracking(n,0,board,res)
        return len(res)
        def isValid(self,row,col,board):
            #这里我们不需要确认225和315度的验证,因为根据递归的特性.我们不会再当前row的下面放置'Q'
            for r in range(row):
                if board[r][col] == "Q":
                    return False
            
            i,j = row-1,col-1 #error: 这里需要一个新的变量记录原本row和col的值,不然这个while循环之后值就发生改变了,那么第二个for循环就错了
            while i >=0 and j>=0: #error 是大于等于而不是大于
                if board[i][j] =='Q':
                    return False
                i-=1
                j-=1
            
            i,j = row-1, col+1
            while i >=0 and j<len(board): #error 是row >=0 and col<len(board) 而不是 row >0 and col<n
                if board[i][j] =='Q':
                    return False
                i-=1
                j+=1
            return True