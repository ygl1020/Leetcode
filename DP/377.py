# 完全背包问题 给定一个数组和targte,在数组张不断抽取element求有多少总排列的数量
def combinationSum4(self, nums: List[int], target: int) -> int:
        """
        这题需要注意,在完全背包中如果是先遍历物品在遍历背包,那么我们是求组合的数量,因为我们先遍历物品,这就注定了物品1只会出现在物品0的后面.因此本体如果是求排列的数量.我们需要先便利背包
        再遍历物品.另外要注意判断j一定要大于等于i
        """
        dp = [0] * (target+1)
        dp[0] =1
        for j in range(0,target+1): # 先遍历背包
            for i in nums: # 后遍历物品
                if j >=i:
                    dp[j] = dp[j]+dp[j-i]
        print(dp)
        return dp[target]