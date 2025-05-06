#买卖股票,可以买卖多次但不能在同一天卖出求最大的利润是多少
def maxProfit(self, prices: List[int]) -> int:
    """
    dp[i][0],dp[i][1]分别代表在第i天拥有股票i和不拥有股票i的最大profit,初始化dp[0][0]=-prices[0]因为第一天买入股票所以利润未负数
        递推公式为dp[i][0] = max(dp[i-1][0], dp[i][1]-prices[i])-->之前就已经拥有了和今天才拥有两种情况
         递推公式为dp[i][1] = max(dp[i-1][1], dp[i-1][0]+prices[i])-->之前就已经卖了和今天才卖出两种情况
    """
    # method 1 greedy
    # pre = prices[0]
    # res = 0
    # for i in range(1,len(prices)):
    #     cur = prices[i]
    #     if pre <cur:
    #         res += (cur-pre)
    #     pre = cur  
    # return res
    # method 2 dp
    
    dp = [[-prices[0],0]] *len(prices)
    for i in range(1,len(prices)):
        dp[i][0] = max(dp[i-1][0],dp[i-1][1]-prices[i]) # 我们可以买卖多次,因此在考虑当天买入的情况需要加上之前没买入的dp状态
        dp[i][1] = max(dp[i-1][1],dp[i-1][0]+prices[i])
    print(dp)
    return max(dp[-1])