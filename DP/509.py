#求Fibonacci的dp[n]的值
def fib(self, n: int) -> int:
        """
        这里初始化dp数组为[0,1,1,2,3,5,8...], 所以dp[0]=0,dp[1]=1, dp[2]=1,dp[3]=2, 注意如果我们要求dp[3]，那么就要遍历到n+1的位置
        """
        if n == 0:
            return 0
        dp=[0]*(n+1)
        dp[0]=0
        dp[1]=1
        for i in range(2,n+1):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[n]