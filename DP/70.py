# 70
def climbStairs(self, n: int) -> int:
    """
    1) dp[i] 代表什么: 这里的dp[i]代表的是当n==i时我们有多少种独特的解
    2) 如何初始化dp数组: 这里我们可以根据题目的例子得出 dp[0] ==0, dp[1] == 1, dp[2] ==2
    3) 从上面这个例子我么可以得出递推公式是dp[i] = dp[i-1] + dp[i-2]
    4) 循环开始的顺序和从哪里开始循环,从上面的递推公式我们可以得出应该从前往后,并且应从第三个数开始循环
    
    
    """
    # method1 使不使用背包直接用状态关系
    if n ==0:
            return 0
    if n==1:
        return 1
    if n==2:
        return 2
    dp = [0] * (n+1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3,n+1):
        dp[i] = dp[i-1]+dp[i-2]
    return dp[n]

    #method 2 完全背包：把n看作是容量为n的背包,然后步数1，2为物品,然后转化为完全背包问题
    dp = [0]* (n+1)
    dp[0] =1
    for j in range(0,n+1):
        for i in range(1,3):
            if j>=i:
                dp[j] = dp[j]+dp[j-i]
    print(dp)
    return dp[n]