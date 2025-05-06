# 给定一个数组,求回文子串的个数
def countSubstrings(self, s: str) -> int:
        """
        dp[i][j]代表从index i到index j的字符串是回文子串
        这时递归公式为,当如果s[i] == s[j], 1)当j==i,那么就表示是单个字符串,那就是合格的回文子串,2)j-i==1，那么就是aa，这种情况也是合格的回文子串 3)j-i>1那么我们就需要判断dp[i+1][j-1]的回文子串是否合格,如果
        合格那么dp[i][j]就是回文子串否者不是
        那么我们初始化dp数组为false的二维数组用来代表i,j两个index,并且根据dp数组的定义我们可以得出dp数组只需要更新右对角的数组
        从递推公式我们可以知道遍历顺序需要从下往上从左往右,
        """
        n,res = len(s),0
        dp = [[False]*(n) for _ in range(n)]
        # for j in range(n-1, n//2+1,-1):
        #     for i in range(0,j+1,1):
        for i in range(n-1, -1,-1):
            for j in range(i,n): #保证遍历顺序需要从下往上从左往右,且j一定是>=i且只会遍历有对角的可能性
                print(i,j)
                if s[i] == s[j]:
                    if j-i<=1:
                        dp[i][j] = True
                        res+=1
                    elif dp[i+1][j-1]:
                        dp[i][j] = True
                        res+=1
        return res