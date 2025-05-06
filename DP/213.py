def findMax(self,nums):
        """
        这题我们需要注意考虑的两个情况,1)我们考虑第一个房间那么不考虑最后一个房间 2)我们不考虑第一个房间考虑第二个房间到最后一个房间. 一定要注意我们这里dp的含义是考虑元素i以及i之前的元素能获得的
        最大值,抢不抢房间i是由dp结果更新决定的. 一开始我想到了分情况讨论,但是我分情况是直接决定了要吗抢第一间房要吗抢最后一间房,这样是不对的.一定要记住dp数组的含义
        """
        dp = [0] * (len(nums))
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        for i in range(2,len(nums)):
            dp[i] = max(dp[i-1],dp[i-2]+nums[i])
        return dp[-1]
def rob(self, nums: List[int]) -> int:
    if len(nums) <=2:
        return max(nums)
    res1 = self.findMax(nums[1:])
    res2 = self.findMax(nums[:-1])
    return max(res1,res2)