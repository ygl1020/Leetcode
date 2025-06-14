#给你一个nums让你求出在nums里面按照顺序可以达成的最长递增子序列的长度
def lengthOfLIS(self, nums: List[int]) -> int:
        """
        dp数组的含义是以元素i为结尾,对比从nums[0]到nums[i-1]的最长递增子序列的长度,因为并不是说dp[-1]代表最长的子序列,我们需要在dp里面找到最大值
        eg:[1,3,6,7,9,4,10,5,6]--> dp=[1, 2, 3, 4, 5, 3, 6, 4, 5]
        然后dp数组的初始化也是必须要等于1,因为每一个元素的自身也是一个递增子序列,长度为1
        
        
        这题我一开始的思路是错误的,每一次考虑新的element其实需要把再这个element之前的所有数和它进行一个对比来得出新的最长递增数列,因此这里需要两个for循环,第二个for循环是用来遍历第一个for循环之前的值把它们和第一个for循环的i进行对比
        但是我之前的想法是如果nums[i] <= nums[i-1], dp[i]= dp[i-1]
        因此对于一些特殊情况就会发生错误: eg[4,10,3,3,8,9], 通过我的错误思路答案是4,但是正确答案应该是3-->3,8,9 
        正确的思路是再index i把它之前的元素遍历一遍和index i的元素最对比,然后我们更新dp[i]= max(dp[j+1, dp[i]]), 因为我们不断遍历对比index i和它之前的数值,这个过沉重我们不断更新dp[i]
        但是我们需要找到dp[i]的最大值
        """
        dp = [1] *len(nums)
        for i in range(1,len(nums)):
            for j in range(0,i):
                if nums[i]>nums[j]: # error if nums[i]>nums[i-1]:因为我们考虑的是非连续最长递增子序列的长度,所以dp[i]是由dp[0]-dp[i-1]决定的而不是单独由dp[i-1]决定的
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