def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
    '''
    这题解题思路和62相识,区别在于当遇见obstacle时我们直接可以跳过当前row的后面的path已经当前column的下面的path,另外要单独判断一下当dp[0,0]和dp[m-1][n-1]为obstacle的情况
    1) dp[i][j]的含义 这里代表从dp[0][0] 到dp[i][j]有多少单独的path
    2) 如何初始化dp   我们知道第一行和第一列的所有空格到dp[i][j]的unique 路径都是1, 注意初始化row是是遍历 column, keep the row number constant dp[0][n]
        这里row为len(obstacleGrid), col为len(obstacleGrid[0]),另外注意初始化时如果遇见obstac直接可以结束循环
    3) 递推公式是什么 从表格可以看出 dp[m][n] = dp[m-1][n] + dp[m][n-1]
    4) for循环的顺序是什么 我们应该先从左往右,在从上到下,因为从上到下 最后还是要从左往右的所以如果不先算从左往右的path就求不出答案.循环里面要注意加一个if条件判断当前的path是不是obstacle,是的话就可以直接跳过这个iteration进行下一个iteration
    
    '''
    m,n = len(obstacleGrid), len(obstacleGrid[0])
    if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] ==1:
        return 0
    dp = [[0]*n for _ in range(m)]
    
    for j in range(m):
        if obstacleGrid[j][0] ==1:
            break
        else:
            dp[j][0] =1
    for i in range(n):
        if obstacleGrid[0][i] ==1:
            break
        else:
            dp[0][i] =1
            
    for i in range(1,m):
        for j in range(1,n):
            if obstacleGrid[i][j] == 1:
                continue
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[m-1][n-1]