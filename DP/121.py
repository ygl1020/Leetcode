#买卖股票,只能买卖一次且不能在同一天卖出求最大的利润是多少
def maxProfit(self, prices: List[int]) -> int:
        """
        dp[i][0],dp[i][1]分别代表在第i天拥有股票i和不拥有股票i的最大profit,初始化dp[0][0]=-prices[0]因为第一天买入股票所以利润未负数
        递推公式为dp[i][0] = max(dp[i-1][0], -prices[i])-->之前就已经拥有了和今天才拥有两种情况
         递推公式为dp[i][1] = max(dp[i-1][1], dp[i-1][0]+prices[i])-->之前就已经卖了和今天才卖出两种情况
        """
        # brute force solution
        # maxProfit = 0
        # for i in range(len(prices)):
        #     for j in range(i+1,len(prices)):
        #         maxProfit = max(maxProfit,prices[j]-prices[i])
        # return maxProfit
        # method 2 dynamic programming
        dp = [[-prices[0],0]]  * len(prices) # dp[i][0]-->在第i天拥有股票i的最大profit,  dp[i][1]-->在第i天未拥有股票i的最大profit
        print(dp)
        for i in range(1,len(prices)):
            dp[i][0] = max(dp[i-1][0], -prices[i]) # 我们只能买卖一次,因此在考虑当天买入的情况不需要加上之前没买入的dp状态
            dp[i][1] = max(dp[i-1][1], dp[i-1][0]+prices[i]) # 注意考虑未拥有股票时是要吗之前就已经买了所以i的maxprofit和之前一天的一样,或者今天卖了那么就是之前一天没卖的最大profit+prices[i]
        print(dp)
        return max(dp[-1])