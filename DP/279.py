#使用完全平方的值来填满容量为n的背包最少需要多少个element
def numSquares(self, n: int) -> int:
        """
        这题的递推公式时：dp[j] = min(dp[j],dp[j-i*i]+1),需要使用dp[j-i*i]是因为我们需要保证我们每次使用的物品都是完全平方的值. 根据这个公式我们如果要满足j-i*i>=0, j >= i*i因此我们j的开始
        范围是i*i. 另外dp数组初始化的时候dp[0]=0因为背包容量为0时不放入任何物品就已经满了
        """
        dp = [float('inf')] * (n+1)
        dp[0]=0
        for i in range(1+n):
            for j in range(i*i,n+1):
                if dp[j-i*i] != float('inf'):
                    dp[j] = min(dp[j],dp[j-i*i]+1) 
        if dp[n] != float('inf'):
            return dp[n]
        return 0