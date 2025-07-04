#给你两个字符串,让你求在两个字符串中最长的公共字符串的长度,字符串的值可以是不连续的
def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        这题其实我的思路基本是对的,和718相比这题不要求子序列是连续的,因为还是把dp初始化为dp[i][j]代表从0到i-1和0到j-1的最长子序列.我们可以使用相同的dp公式
        但是区别在于当text1[j-1] ！= text2[i-1]时,dp[i][j]需要保存当天dp的最大值,因此要吗保持列不变网上一行搜索,要吗保持行不变搜索j-1的之前的最大值.这个思路我是思考到了的
        但是实现的话是错误的
        
        和718相比区别在于718求的是连续最长公共子序列,nums1[i-1] == nums2[j-1]的情况,这题的话是不连续的最长公共子序列,因此我们还需要考虑不相等的情况
        那么不相等的情况就是eg s1"abcd", s2"ace" 如果 s1[3]!s2[2], 那么最长公共子序列的最大值有两中可能性1)对比"abcd" 和"ac" 2)以及对比"abc" 和"ace" 
        然后两者之间取最大值
        """
        dp = [[0]*(len(text1)+1) for _ in range(len(text2)+1)]
        res =0
        for i in range(1,len(text2)+1):
            for j in range(1,len(text1)+1):
                # print(text1[j-1],text2[i-1])
                if text1[j-1] == text2[i-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1]) # 因为这题不要求子序列是连续的,当text1[j-1] ！= text2[i-1],我们需要找到dp[i-1][j]以及dp[i][j-1]取最大值
                if dp[i][j] >res:
                    res = dp[i][j]
        return res