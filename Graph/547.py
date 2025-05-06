def findCircleNum(self, isConnected: List[List[int]]) -> int:
    """
    这题的思路是用dfs, 我们首先把每一个相连接的节点找出来然后把这个相链接的节点标记为0,这样当我们找出这一个连通图的所有节点时,我们会退出dfs的recursive function,返回到外层for i in range(n)的下一个循环,然后我们判断:isConnected[i][i] ==1,因为在dfs中我们把相邻的节点的adjecent metrix里面的
    值都变为0了(当[isConnected[0][1] ==1那么节点 0和1相连,同理在[1][0]中也应该是1,所以应该把两种情况都变为0,节点本很相连的情况也考虑进去了).因此如果我们判断isConnected[i][i] ==1, ans +=1
    这里我们需要一个curr的参数在dfs里面,因为这样的话我们才知道当前我们判断的是哪一个city的matrix,然后bfs函数里面并没有之前的写binary tree的if 条件来判断什么时候结束recursive 然后递归的开始是因为这里的if 条件判断是否有新的city需要invoke recursive,当没有新的invoke情况然后for循环
    达到了上线就会自动对出循环,跳回到最外围的for loop进行下一个city的Matrix的判断
    
    递归的函数最好不要去思考每一个节点之间是怎么进行递归的,否则会把自己绕进去,我应该思考的是递归的情况是什么,递归的函数是什么,以及我们什么时候结束递归
    """
    def dfs(M, curr, n):
        for i in range(n):
            if M[curr][i] ==1:
                M[curr][i] = M[i][curr] =0
                dfs(M,i,n)
    n = len(isConnected)
    ans = 0
    for i in range(n):
        if isConnected[i][i] ==1:
            ans+=1
            dfs(isConnected,i,n)
    return ans