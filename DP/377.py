# 完全背包问题 给定一个数组和targte,在数组张不断抽取element求有多少总排列的数量
def combinationSum4(self, nums: List[int], target: int) -> int:
        """
        这题需要注意,在完全背包中如果是先遍历物品在遍历背包,那么我们是求组合的数量,因为我们先遍历物品,这就注定了物品1只会出现在物品0的后面.因此本体如果是求排列的数量.我们需要先便利背包
        再遍历物品.另外要注意判断j一定要大于等于i
        
        这题和518求组和不太一样,我们这里求的是排列,因此我们需要先遍历背包再遍历物品,如果先便利物品再遍历背包的话我们后面就不会再考虑遍历完只后的物品,所以会导致物品的遗忘
        然后这题的递推公式对于是一维和二维的dp初始化都是不一样的,当我们不考虑二维时,dp[j] = dp[j]+dp[j-i]， 如果是二维的话就是dp[i][j] = (dp[i-1][j] +dp[-1][j-nums[i]]）
        """
        dp = [0] * (target+1)
        dp[0] =1
        for j in range(0,target+1): # 先遍历背包
            for i in nums: # 后遍历物品
                if j >=i:
                    dp[j] = dp[j]+dp[j-i]
        print(dp)
        return dp[target]
    
        #method 2 2d array
        # # dp[][j]和为j的组合的总数
        # dp = [[0] * (target+1) for _ in nums]
        
        # for i in range(len(nums)):
        #     dp[i][0] = 1
            
        # # 这里不能初始化dp[0][j]。dp[0][j]的值依赖于dp[-1][j-nums[0]]
            
        # for j in range(1, target+1):
        #     for i in range(len(nums)):
                
        #         if j - nums[i] >= 0:
        #             dp[i][j] = (
        #                 # 不放nums[i]
        #                 # i = 0 时，dp[-1][j]恰好为0，所以没有特殊处理
        #                 dp[i-1][j] +
        #                 # 放nums[i]。对于和为j的组合，只有试过全部物品，才能知道有几种组合方式。所以取最后一个物品dp[-1][j-nums[i]]
        #                 dp[-1][j-nums[i]]
        #             )
        #         else:
        #             dp[i][j] = dp[i-1][j]
        # print(dp)
        # return dp[-1][-1]