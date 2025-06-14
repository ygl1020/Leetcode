#给你一个数组求该数组中的子数组,该子数组可以有最大累加和
def maxSubArray(self, nums: List[int]) -> int:
        """
        用一个total来记录和,一个res来记录最大值.每次total<0就更新total为0
        如果使用dp的思路的话应该就分为两种情况,一种是继续累加那dp[i]=dp[i-1]+nums[i],或者从i从新开始累加那就是dp[i] = nums[i]. 我们两者取最大就好了
        dp[i]的定义是从0到i结尾,最大的累加是多少
        """
        # greedy 写发
        # total,res =0, float('-inf')
        # for i in nums:
        #     total+=i
        #     # if total >=0: #这里如果用了if条件的话如果出现nums里面都是负数就会跳过执行而导致res不会进行更新
        #     #     res = max(res,total)
        #     res = max(res,total)
        #     if total<0:
        #         total = 0
        # return res

        # dp 错误的写法,我这个写法如果出现多个负数元素在nums里面就会报错,因为我们一定要选取最少一个element当len(nums)=1时,但是如果max(dp[i-1]+nums[i],0)就代表可以不选取元素
        # dp = [0]*len(nums)
        # if nums[0]>0:
        #     dp[0] = nums[0]
        # res = dp[0]
        # for i in range(1,len(nums)):
        #     if nums[i]>=0:
        #         dp[i] = dp[i-1]+nums[i]
        #     else:
        #         dp[i] = max(dp[i-1]+nums[i],0)
        #     if res <dp[i]:
        #         res=dp[i]
        #     print(res)
        # print(dp)
        # return res
        #正确的dp写法
        dp = [0]*len(nums)
        dp[0] = nums[0]
        res = dp[0]
        for i in range(1,len(nums)):
            dp[i] = max(dp[i-1]+nums[i],nums[i])
            if res <dp[i]:
                res=dp[i]
        return res