#最多买卖一次股票,让你求最大利润是多少
def maxProfit(self, prices: List[int]) -> int:
        # dp = [[0,0]] * (len(prices))
        # dp[0][0] = -prices[0]
        # for i in range(1,len(prices)):
        #     dp[i][0] = max(dp[i-1][0], -prices[i])
        #     dp[i][1] = max(dp[i-1][1], dp[i-1][0]+prices[i])
        # return max(dp[-1])
        
        """
        滑动窗口的解法是初始化左右两个指针，每个回合中都移动右指针,然后我们比较左指针对应的元素和右指针对应的元素.如果右指针对应的值大于左指针,就计算最大的profit,否者我们就把左子针移动到右指针-->因为我们找到了最低点
        """
        l, r = 0,1
        res = 0
        while r <len(prices):
            if prices[l] < prices[r]:
                profit = prices[r]-prices[l]
                res = max(res,profit)
                print(prices[r],prices[l])
            else:
                l=r
            r+=1
        return res