# 不可以跳过element,让你求最长递增子序列的长度
def findLengthOfLCIS(self, nums: List[int]) -> int:
        #method1 dp数组含义是从0到i结尾所能构成的连续递增数组长度,eg: nums = [1,3,5,4], dp[4] = 1而不是3. 这里因为不是计算连续的递增子序列,那么我们只需要对比nums[i]和nums[i-1]的值就可以了,当nums[i]>nums[i-1], 那么dp[i] = dp[i-1]+1, 因此只需要一个for循环就可以解决问题
        # dp = [1] *len(nums)
        # for i in range(1,len(nums)):
        #     if nums[i] > nums[i-1]:
        #         dp[i] = dp[i-1]+1
        #     else:
        #         dp[i] = dp[i]
        # print(dp)
        # return max(dp)

        #method 2 
        res,tmp= 1,1
        pre = nums[0]
        for i in range(1,len(nums)):
            cur = nums[i]
            if cur>pre:
                tmp+=1
                res = max(tmp,res)
            else:
                tmp=1
            pre=cur
        return res