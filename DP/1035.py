#给你两个数组,求两个数组中相同value相连不交叉的最长子数组
def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        """
        这题和1143是一摸一样的题目,之不过时变了一下模式,本质还是求两个数组中的通过最长不连续子序列
        画一个图我们可以发现其实这里就是求两个数组中的最长不连续公共子序列的长度
        """
        res = 0
        dp = [[0]*(len(nums2)+1) for _ in range(len(nums1)+1)]
        for i in range(1,len(nums1)+1):
            for j in range(1,len(nums2)+1):
                # print(i,j)
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
                if res<dp[i][j]:
                    res= dp[i][j]
        return res