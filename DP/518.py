#完全背包问题,给定一个数组和target,然你求在nums中选取元素能有多少种可能性sum总和为target
def change(self, amount: int, coins: List[int]) -> int:
        """
        这里递推公式理解错了,我定义的dp[j]代表的是在背包容量为j时有多少种可能性,然后递推公式我写的是dp[j] = max(dp[j,dp[j-i]]), 但是正确的递推公式应该是dp[j] = dp[j]+dp[j-i]
        举例来说的话如果在题目494中数组是[1,1,1,1,1],递推公式为dp[i][j] = dp[i-1][j]+dp[i-1][j-i] 那么求dp[2][2]的情况时,我们应该找到dp[1][2]-->即把物品1，2放入背包中  和dp[1][1]-->放入物品0或者1进入背包, 所有可能性为1+2=3
        同样道理放在本题但是本题的递归公式不一样:dp[i][j] = dp[i-1][j]+dp[i][j-i]-->在dp[i][j-i]中的含义为我们打算让如物品i进入j中所有提前把i的重量在j中预留出来,然后因为物品可以使用多次所有我们不需要用[i-1]直接[i]就可以
        
        """
        dp = [0] * (1+amount)
        dp[0] =1
        for i in coins:
            for j in range(i,amount+1):
                dp[j] = dp[j]+dp[j-i]# error1
        return dp[amount]