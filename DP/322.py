# 完全背包,给你一个数组和amount,然后让你求满足子集和的和等于amount的最小集合长度
def coinChange(self, coins: List[int], amount: int) -> int:
        """
        这题其实很多细节需要注意,首先dp的初始化,我们是求背包里最小长度的子集合的和等于amount,那么我们初始化dp数组的时候就需要把dp的element初始化为最大值来避免对后面的值更新造成影响.而不应该用初始化为0,dp[0]=0因为当背包容量为0时不需要放入元素就可以装满
        另外就是状态转移方程应该是 dp[j]-->min(放入i和, 不放入i的)--> 那么就是min(dp[j],dp[j-i]+1)--> +1就代表把i放入j
        另外我们dp[j]的更新只在我们确认dp[j-i]不为float('inf')时,因为如果dp[j-i]等于float('inf')就代表没有解
        
        error1: dp数组的含义是背包容量为j的背包从coins数组中不断抽取能凑满的最小元素是多少, 然后我们初始化因为是找最小值所以是用float('inf'),dp[0]=0因为需要0个元素就满了
        error2: 这题其实是求的组合因此把先遍历物品再遍历背包,最最重要的是背包的遍历range是(i,amount+1)
        """
        dp = [float('inf')]*(amount+1)
        dp[0] = 0
        for i in coins:
            for j in range(i,amount+1):
                if dp[j-i] != float('inf'): # 如果dp[i - coin]不是初始值，则进行状态转移
                    dp[j] = min(dp[j],dp[j-i]+1)
        if dp[amount] ==float('inf'): # 判断dp[j]是否有解
            return -1
        return dp[amount]