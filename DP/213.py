def findMax(self,nums):
        """
        这题我们需要注意考虑的两个情况,1)我们考虑第一个房间那么不考虑最后一个房间 2)我们不考虑第一个房间考虑第二个房间到最后一个房间. 一定要注意我们这里dp的含义是考虑元素i以及i之前的元素能获得的
        最大值,抢不抢房间i是由dp结果更新决定的. 一开始我想到了分情况讨论,但是我分情况是直接决定了要吗抢第一间房要吗抢最后一间房,这样是不对的.一定要记住dp数组的含义
        
        这题我的松思路是先不考虑index0和index-1的数,然后先找出之间的数值的所能取的最大值,然后在考虑index0和1的情况.但是这样的话我们不知道index0或者index-1能不能取,因为
        中间区间计算最大值的时候我们不知道取了index1的值没有.正确的思路是把nums[0:len(nums)-1] 和nums[1:]两个区间分别求最大值,然后进行比较
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