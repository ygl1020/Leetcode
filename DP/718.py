#两个数组中让你求连续的最长公共子序列的长度
def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        """
        这题是判断两个数组中最长连续公共子序列的长度,然后子序列的元素顺序需要相同.如果我们画一个二维的图我们可以看出dp[i][j] = dp[i-1][j-1]+1, 那么我们这里如果是需要从index 0 开始循环的话就会出现不知道怎么得到dp[-1][-1]的问题,因此我们需要把dp初始定义为
        再index i-1的num1数组中和index j-1的nums2的数组中的最长公共子序列的长度为dp[i][j], 然后我们两个for循环的遍历都是从1开始.然后判断nums1[i-1]和nums2[j-1]的数值是否相同来更新dp数组-->如果不用i-1的话会出现index out of range的问题
        
       本体是判断连续的最长相等子序列,如果判断完nums1[i] == nums2[j]，我们需要继续判断nums1[i-1] == nums2[j-1]是否相等,因此如果nums1[i] == nums2[j]
       我们dp[i][j]=dp[i-1][j-1]=+1. 更具这个dp公式我们知道dp[i][j]是通过前一个状态判断来的,所以我们初始化的时候需要延申数组一个单位-->dp数组从0开始,dp[i][j]代表
       num1[i-1]到nums2[j-1]的最长公共子数组的长度.为什么是nums[i-1]和nums[j-1]是因为nums1和nums2的长度都是5,但是dp长度是6,我们两个for循环都是从1开始遍历到len(num1)+1
       那么就会出现一个问题,nums1和nums2的最大下标是4,当我们遍历nums[5]的时候就会报错,因此我们需要i-1来定义dp数组
       
       画一个二维的dp数组,然后演示一遍可以发现dp[i][j] = dp[i-1][j-1]+1，从dp数组的定义我们可以看出我们需要从index1开始遍历,但是这样的话我们就遗漏了
        index0的情况.但是如果我们从index0开始遍历,那么i-1-->0-1会等于负数.因此我们需要增加dp数组1各单位的长度,然后dp数组的含义为以nums1 i-1和nums2
        j-1为结尾的最长公共子数组的长度. 这样我们再for循环中从1开始遍历的就是nums1[0],nums2[0]的元素.  

        我的错误在于我没有考虑到这个情况然后我的dp是直接等于len(nums1),   
        """
        dp = [[0] * (len(nums2)+1) for _ in range(len(nums1)+1)]
        res = 0
        for i in range(1,len(nums1)+1):
            for j in range(1,len(nums2)+1):
                if nums1[i-1] == nums2[j-1]: # ,nums1和nums2的最大下标是4,我们会遍历到nums[5],因此需要用nums[i-1]来避免范围出错
                    dp[i][j] = dp[i-1][j-1]+1

                if dp[i][j]>res:
                    res =  dp[i][j]
        return res    