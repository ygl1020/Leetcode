#两个数组中让你求连续的最长公共子序列的长度
def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        """
       本体是判断连续的最长相等子序列,如果判断完nums1[i] == nums2[j]，我们需要继续判断nums1[i-1] == nums2[j-1]是否相等,因此如果nums1[i] == nums2[j]
       我们dp[i][j]=dp[i-1][j-1]=+1. 更具这个dp公式我们知道dp[i][j]是通过前一个状态判断来的,所以我们初始化的时候需要延申数组一个单位-->dp数组从0开始,dp[i][j]代表
       num1[i-1]到nums2[j-1]的最长公共子数组的长度.为什么是nums[i-1]和nums[j-1]是因为nums1和nums2的长度都是5,但是dp长度是6,我们两个for循环都是从1开始遍历到len(num1)+1
       那么就会出现一个问题,nums1和nums2的最大下标是4,当我们遍历nums[5]的时候就会报错,因此我们需要i-1来定义dp数组
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