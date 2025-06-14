#给你一个nums数组,不能偷相邻的房间,问你能偷的最大价值是多少
def rob(self, nums: List[int]) -> int:
        
        #method1 2d dp
        """
        dp数组的含义是从0到i在i时抢能获得的最大利润时dp[i][0], 不抢能获得的最大利润时dp[i][1]. 递推公式为dp[i][0] = dp[i-1][1] +nums[i]-->今天抢那么昨天就不能抢,所以用昨天不强
        时的dp值加上今天能抢到的利润nums[i], dp[i][0] = max(dp[i-1][0],dp[i-1][1])-->今天不抢的最大利润就是昨天抢的最大利润或者昨天不强的最大利润取最大值. 
        通过递推公式我们可以得出当前dp[i]的状态取决于上一个dp[i-1]的状态,因此for循环的从1开始, 我们需要初始化dp[0][0], dp[0][1]
        """
        # dp = [[0,0] for _ in range(len(nums))]
        # dp[0][0] ,dp[0][1]= nums[0], 0
        # # dp[0][1] = dp[]
        # for i in range(1,len(nums)):
        #     dp[i][0] = dp[i-1][1]+nums[i]
        #     dp[i][1] = max(dp[i-1][0], dp[i-1][1])
        # return max(dp[-1])

        #method2 1d dp
        """
        一维dp的含义是从0到i在i是所能获得的最大利润为dp[i], 然后递推公式为dp[i]= max(dp[i-2]+nums[i],dp[i-1])-->从在i时抢和不抢的两个状态,然后再两个状态中选一个最大值.
        从dp数组我们可以推断出for循环是从2开始的,dp初始化为dp[0]=nums(0), dp[1] =max(dp[1],dp[0])
        """
        if len(nums) <=2:
            return max(nums)
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        for i in range(2,len(nums)):
            dp[i] = max(dp[i-2]+nums[i], dp[i-1])
        print(dp)
        return dp[-1]