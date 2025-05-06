# 给你一个prices数组. index代表日期.value代表股票价格 让你求最大的profit
def maxProfit(self, prices: List[int]) -> int:
        """
        这题是贪心算法,贪心在于我们需要获取最大profit,那么我们通过获取每次local max profit然后把local max profit进行累加.取local max的方法在于计算cur的profit-->prices[i+1] - prices[i]. 如果cur>0，那么就是local max profit. 这样我们一直遍历到倒数第二个元素.因此最后一天计算买入我们的loca max也只能等于0.
        因此不需要考虑. 然后如果prices的数组长度小于等于1那么就直接return 0
        
        "用一个cur来代表prices[i+1] - prices[i]的差,如果差大于0就把结果进行统计"
        """
        if len(prices) <=1:
            return 0
        total = 0
        for i in range(len(prices)-1):
            cur = prices[i+1] - prices[i]
            if cur>0:
                total +=cur
        return total