#在s中找到能构成t的所有可能性,s中抽取的元素可以时不连续的
def numDistinct(self, s: str, t: str) -> int:
        """
        dp[i][j]代表从s的i-1结尾的元素中有dp[i][p]个元素等于t的0-i中的数组
        然后我们需要初始化第0行的所有列为0,以及第0列的所有行为1-->因为当0列是代表从s中有抽取空字符串
        然后递推公式分为,s[j-1]==t[i-1]和s[j-1]！=t[i-1], 等于时那就是dp[j-1][i-1](使用s[j-1]时的情况) + dp[j][i-1](不使用s[j-1])-->eg s="bagg", t="bag", 
        在s[3]等于t[2]时,我们需要计算使用了s[3]和没使用s[3]的情况
        """
        m, n = len(s), len(t)
        dp = [[0]*(n+1) for _ in range(m+1)] # t as col, s as row
        for i in range(0,m+1):
            dp[i][0] = 1
        print(dp)
        for i in range(1,n+1):
            for j in range(1,m+1):
                if s[j-1] == t[i-1]:
                    dp[j][i] = dp[j-1][i-1] + dp[j-1][i]
                else:
                    dp[j][i] =  dp[j-1][i]
        return dp[-1][-1]

m,n =3,3
dp = [[0]*(m+1) for _ in range(n+1)]
print(dp)