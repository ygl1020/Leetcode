#给你一个集合然后求是否可以把这个子集分割为两个子集,这两个子集的和是相等的
def canPartition(self, nums: List[int]) -> bool:
        """
        这题求的是一个集合里面是否可以有两个子集,这两个子集的和都等于sum(nums)//2. 转化为背包问题的话就是给定一个target ==sum(nums)//2, 求背包容量为target时它的最大值是否等于target
        这题是一位数组背包,因为我们初始化dp数组等于0,另外我们是要找背包为target的情况因此dp的长度需要为target+1 
        第二个for循环我们是后序遍历,遍历的range是(target,i-1),i-1的原因是根据递推公式：dp[j] = max(dp[j],dp[j-i]+i) 我们得到j-i要>=0,因此j>=i, 所以我们到i-1为止
        
        这里可以看作是0,1背包问题.我们看背包容量为target时的dp[target]是否等于target
        dp[j]的定义为背包容量为j的背包最多可以装下的value为dp[j], 因为这里这里是一维数组所以我们需要我们遍历背包时需要用倒序来保证1) 前面的dp不被在被reference前不被改变2)每个物品只取一次
        """
        if sum(nums)%2 !=0:
            return False
        target = sum(nums) // 2
        dp = [0]*(target+1) # error 1:[0]*(len(nums)+1)
        for i in nums:
            for j in range(target,i-1,-1): # error 2: for j in range(len(num),-1,-1)
                dp[j] = max(dp[j],dp[j-i]+i)
        print(dp)
        return dp[-1] == target