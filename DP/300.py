#给你一个nums让你求出在nums里面按照顺序可以达成的最长递增子序列的长度
def lengthOfLIS(self, nums: List[int]) -> int:
        """
        dp数组的含义是以元素i为结尾,对比从nums[0]到nums[i-1]的最长递增子序列的长度,因为并不是说dp[-1]代表最长的子序列,我们需要在dp里面找到最大值
        eg:[1,3,6,7,9,4,10,5,6]--> dp=[1, 2, 3, 4, 5, 3, 6, 4, 5]
        然后dp数组的初始化也是必须要等于1,因为每一个元素的自身也是一个递增子序列,长度为1
        """
        dp = [1] *len(nums)
        for i in range(1,len(nums)):
            for j in range(0,i):
                if nums[i]>nums[j]:
                    dp[i] = max(dp[j]+1,dp[i])
        # print(dp)
        return max(dp)

        #wrong method,我认为如果当前的i大于之前的i-1的值,我们就可以把最大递增子序列的长度加1,但是这个是一个错误的假设,因为很可能那个只是local的解
        # [4, 10, 4, 3, 8, 9]，我的题解是到8的时候最长子序列的长度是4,但是是错误的
        # dp = [0] *len(nums)
        # dp[0] =1
        # for i in range(1,len(nums)):
        #     if nums[i] > nums[i-1]:
        #         dp[i] = max(dp[i-1]+1,dp[i])
        #     else:
        #         dp[i] = dp[i-1]
        # print(dp)
        # return dp[-1]