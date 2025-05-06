#不限制交易次数,每一次买入和卖出的组合会扣除一个手续费
def maxProfit(self, prices: List[int], fee: int) -> int:
        """
        这题在递推公式里面考虑持有或者不持有的时候扣除手续费都可以,如果是持有的时候扣除手续费那初始化就是dp[0][0]= -prices[0]-fee
        如果是在不持有的时候扣除手续费,那就是dp[0][1] = 0，dp[0][0]= -prices[0]
        dp[i][0]代表在第i天持有该股票的最大利润, dp[i][1]代表在第i天不持有该股票的最大利润， 
        """
        # dp = [[0,0]] * len(prices)
        # dp[0][0]= -prices[0]-fee
        # for i in range(1,len(prices)):
        #     dp[i][0] = max(dp[i-1][0], dp[i-1][1]-prices[i]-fee)
        #     dp[i][1] = max(dp[i-1][1], dp[i-1][0]+prices[i])
        # print(dp)
        # return max(dp[-1])

        dp = [[0,0]] * len(prices)
        dp[0][0]= -prices[0]
        for i in range(1,len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]-prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0]+prices[i]-fee)
        print(dp)
        return max(dp[-1])