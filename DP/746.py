#给你一个cost数组求到达len(cost)+1的位置时的最小花费
def minCostClimbingStairs(self, cost: List[int]) -> int:
    """
    这里dp数组的含义为到达index时所需要的最小cost.因为我们可以选择从index0或者1开始.因此当我们到达index0或者1时不需要计算cost,只有当往上跳的时候需要cost
    然后因为每次可以跳1步或者2步因此 dp[i]= min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])
    
    
    两点没有搞清楚
        1)搞清楚这里dp数组的含义是到达下标i的最小花费是多少,因为可以在0或者1的位置往上跳,到达0，1的时候是不需要花费的只有往上跳的时候是需要花费的.所以都是初始化为0
        2)然后dp[i]可以由dp[i-1]+cost[i-1]和dp[i-2]+cost[i-2]得到,那么我们就是两个之间选取最小花费的那一个
    """
    if len(cost) <=2: #当len(cost)<=2时我们直接选取最小的cost就是答案
        return min(cost)
    dp = [0] *(len(cost)+1) #题目的意思是求跳到len(cost)+1的台阶时的最小花费,因此这里需要(len(cost)+1)
    for i in range(2,len(cost)+1): # 我们从len(cost)>=3时即index==2时开始遍历
        dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])
    return dp[-1]
