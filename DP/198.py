#给你一个nums数组,不能偷相邻的房间,问你能偷的最大价值是多少
def rob(self, nums: List[int]) -> int:
        """
        dp数组的含义是考虑index i以及i之前的房间,能偷到的最大的value.然后递推公式分为考虑偷i的element-->dp[i-2] +nums[i] 以及不偷i的element-->dp[i-1], 然后我们两者取最大值
        
        dp数组的定义是再j天时所能偷取的最大利润时dp[j], error1,我在定义dp[1]的时候直接把dp[1]=nums[1]来但是其实如果nums[1]>nums[0],那么我们可以第一天不偷然后第二天偷
        """
        if len(nums) <=2:
            return max(nums)
        dp = [0] * (len(nums))
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        for i in range(2,len(nums)):
            print(i)
            # dp[i] = max(dp[i-1],dp[i-2]+nums[i])
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        return dp[-1]