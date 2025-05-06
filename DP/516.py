# 给一个字符串求最长回文子子序列的长度
def longestPalindromeSubseq(self, s: str) -> int:
        """
        这题和647不太一样,647是求回文子串所以是连续的,这里的话是回文子序列可以是不连续的.dp[i][j]的含义是以i为开始,j为末尾的s字符串中,最长的回文子序列长度是多少
        递推公式是如果s[j] == s[i],dp[i][j] = dp[i+1][j-1]+2--> "abca", aa是回文子序列但是bc不是,所以dp[i+1][j-1]+2=2， 当s[j] ！= s[i],dp[i][j],我们可以考虑增加左边的情况(dp[i][j-1])或者增加
        右边的情况（dp[i+1][j]），这样两者取最大就好了
        dp数组初始化的我们需要把dp全部初始化为0，然后考虑i==j的情况并把他们初始化为1,这样后面遍历的时候我们就不需要考虑j=i情况了,我们j是从i+1开始的
        """
        if len(s)<=1:
            return len(s)
        n,res = len(s),0
        dp = [[0]*n for _ in range(n)]
        for i in range(n):
            dp[i][i] =1
        for i in range(n,-1,-1):
            for j in range(i+1,n):
                if s[j] == s[i]:
                    dp[i][j] = dp[i+1][j-1]+2
                else:
                    dp[i][j] = max(dp[i+1][j],dp[i][j-1])
                if dp[i][j]>res:
                    res = dp[i][j]
        return res