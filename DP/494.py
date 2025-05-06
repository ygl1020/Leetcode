def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """
        method 1 用回溯会超时, 另外这里的话和一般的回溯不太一样.一般之前写回溯的话是求组合问题,然后我们需要用for循环和startindex来去重,这里的话不用for循环,但是每次的value要嘛是正数
        要吗是负数,我们还不能够跳过i选择i+1,所以不能用for循环而且需要两个回溯函数在每次递归的逻辑里面.另外值的注意的是这里我们是过了root节点才开始return,然后收集结果的逻辑再return里面

        method2, 这题我们可以思考为一个合集里面分为两个子集分别为left和right,left代表正数的value,right代表负数的value.那么我们可以得到left+right =sum(nums)--total, left-right=target
        right = total -left, 然后带入right=total-left 进left-(total-left) = target--> left=(target+total)/2--->当这个值为整数时我们可以找到符合条件的组合,否者找到不到组合
        然后这个题就换成了一个再一个合集中寻找所有能放满背包(target+total)/2的所有可能性
        1) dp[i][j]从物品0-i中不断抽取物品放入背包j,能把背包j放满的所有可能性
        2)dp[i][j] = dp[i-1][j]+ dp[i-1][j-i]
        3) 初始化dp数组,dp[0][0] ==1代表背包容量为0，物品0可以被放入或者不放入,因为背包容量为0,所有不放入物品1,value为1
        
        既然我们可以把一个数组分为正负两种可能,那么我们就可以把一个数组分为正负两个数组.那么已知条件由left+right=sum(nums), left-right=target, left = (sum(nums)+target)//2
        边界情况是当abs(target)>sum(nums) 或者(sum(nums)+target)不能被2整除就说明没有组合的可能. 其他情况的话我们就可以按正常的背包问题来解决了
        dp数组的含义是背包容量为j的背包能装满背包的组合由dp[j]种, 递推公式为dp[j]=dp[j]+dp[j-i] 然后初始化dp[0]=1, 不用装直接就满了  
        
        """
        #method 1 用回溯会超时, 另外这里的话和一般的回溯不太一样.一般之前写
        # total,res,startIndex = 0,0,0
        # def backTracking(nums,target,startIndex):
        #     nonlocal total,res
        #     if startIndex == len(nums):
        #         if total == target:
        #             res+=1
        #             return
        #         else:
        #             return
        #     for i in range(startIndex,startIndex+1):
        #         total+=nums[i]
        #         backTracking(nums,target,i+1)
        #         total-=nums[i]

        #         # Try subtracting nums[startIndex]
        #         total -= nums[startIndex]
        #         backTracking(nums, target, startIndex + 1)
        #         total += nums[startIndex]
        # backTracking(nums,target,startIndex)
        # return res

        # dp
        total = sum(nums)
        target_sum = (total+target) // 2 
        if abs(target) > total:
            return 0
        if (total+target) % 2  !=0:
            return 0
        dp = [0] * (target_sum+1)
        dp[0] = 1
        for i in nums:
            for j in range(target_sum,i-1,-1): # 这里注意range是(target_sum,i-1,-1) 而不是(target_sum,-1,-1)
                dp[j] = dp[j] + dp[j-i]
        return dp[target_sum]