def uniquePath(self,m,n):
    '''
    1) dp[i][j]的含义 这里代表从dp[0][0] 到dp[i][j]有多少单独的path
    2) 如何初始化dp   我们知道第一行和第一列的所有空格到dp[i][j]的unique 路径都是1, 注意初始化row是是遍历 column, keep the row number constant dp[0][n]
    3) 递推公式是什么 从表格可以看出 dp[m][n] = dp[m-1][n] + dp[m][n-1]
    4) for循环的顺序是什么 我们应该先从左往右,在从上到下,因为从上到下 最后还是要从左往右的所以如果不先算从左往右的path就求不出答案
    
    这些是我知道前犯的错误1)初始化dp数组时dp =[[1]*(n) for _ in range(m)] 而不是dp =[[0 for _ in range(n)*m]] 2) 我们最后的return时dp[m-1][n-1]而不是dp[m][n],因为我们是从index0开始的
    3)这里的遍历顺序是先row再col,因为我们只有先算出row的结果才能计算col的结果
    
    
    数组的初始化错误1)这题和62相比多了一个obs判断,所以我们需要初始化dp第一行和第一例,如果在当前element出现obs那么这个元素和之后的全部元素都应该为0,否者就更改为1
        2)我们后面的循环每次都是先row再col. 3) obs判断需要用obstacleGrid数组而不是dp,因为我们初始化dp数组时只是更新了第一行和第一列所以可能会出现错误
        
    记住m和n是从1开始的,因为我们已经初始化了第0行和第0列的初始路径
    '''
    # define a 2d array
    dp = [[0]* m for _ in range(m)]
    
    # initiate the dp, so the frist row and first collum only has 1 path
    for j in range(n):
        dp[0][n] = 1
    for i in range(m):
        dp[i][0] = 1
    # loop direction should start from left to right then up to down  
    for i in range(1,m): #从第一列的第一行开始
        for j in range(1,n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[n-1][m-1]
    


