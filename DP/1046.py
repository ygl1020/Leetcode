#给你一个集合,让你把这个集合分成两个子集然后求两个子集的最小差是多少
def lastStoneWeightII(self, stones: List[int]) -> int:
        """
        这题需要转变思路,可以这样思考,我们需要求把stones里面分成两个子集，需求求两个子集的最小差是多少.那么只有当两个子集的和越靠近 sum(stones)//2是差才会最小.这样我们就把问题转化为背包问题
        然后求dp[target]的值-->当背包最大重量为target时最多可以装多少value， 然后用sum(stones)-dp[target]获取另一个子集的和.最后把两个子集进行求差
        """
        if not stones:
            return 0
        total_sum = sum(stones)
        target = total_sum//2
        dp = [0] * (target+1)
        for i in stones:
            for j in range(target,i-1,-1): # error 1 范围不是(target, i+1,-1)
                dp[j] = max(dp[j],dp[j-i]+i)
        restw = total_sum - dp[target]
        print(dp,target)
        return restw - dp[target] # error 2 不是restw - target