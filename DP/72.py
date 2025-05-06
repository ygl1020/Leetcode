#编辑距离求每次删除，添加或者替换一个元素,两个数组都可以进行操作,需要几次w1才等于w2
def minDistance(self, word1: str, word2: str) -> int:
        """
        dp[i][j]的定义是以i-1为结尾的word2中可以匹配j-1为结尾的word1最少需要dp[i][j]次删除操作
        递推公式分为当word1[j-1] == word2[i-1]， 那么考虑使用word1[j]和word2[i]的情况和不考虑word1[j]和word2[i]一样-->dp[i][j] = dp[i-1][j-1]
        当word1[j-1] != word2[i-1]， 我们可以添加或者删除word1的最后一个元素,添加或者删除word2的最后一个元素和删除words1和word2的最后一个元素,又或者替换元素,替换元素的话就是用之前相等的情况在+1-->dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+1). 这里添加和删除的操作都是一样的,所以不需要单独分开写添加的操作
        dp的初始化为第一行和第一列-->这时的情况就是words1为空元素,这时word2有几个元素就删除几个元素,或者words2为空元素,这时word1有几个元素就删除几个元素
        """
        m,n = len(word1), len(word2)
        print(m,n)
        dp = [[0]*(m+1) for _ in range(n+1)]
        for i in range(0,m+1): # initiate row
            dp[0][i] = i
        for j in range(0,n+1): # initiate col
            dp[j][0] = j

        for i in range(1,n+1):
            for j in range(1,m+1):
            # for i in range(1,n+1):
                if word1[j-1] == word2[i-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+1)
        return dp[-1][-1]