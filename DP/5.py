#return 最长的回文字符串的value
def longestPalindrome(self, s: str) -> str:
        """
        首先定义dp数组的含义,这里我们采用2维dp数组,i,j分别代index i和index j,然后dp[i][j]代表从s[i:j]的字符串为回文字符串-->这里的i和j都是闭区间的. 然后我们再看一下递推公式--> abbbd, 我们可以看出如果s[i] ==s[j]
        那么我们只需要查看dp[i+1][j-1]来判断中间这个字符串是不是回文字符串,如果是的话我们dp[i][j]也是回文字符串. 额外需要注意的点在于我们需要考虑当i==j以及 j-1=1的情况,第一个情况的话代表j==i所以是一个单独的字符串,
        第二个情况代表i和j相邻并且s[i]==s[j],因此这两种情况都是回文字符串,其他情况的话就是需要查看dp[i+1][j-1]值. 因为我们dp数组的初始化需要把i==j的element初始化为True. 最后因为我们需要找最长的回文字符串
        那么我们可以先初始化一个res元组用来存储当前的最长字符串,然后每遇见一个新的回文字符串就进行更新.

        这里的遍历顺序也是有讲究的,如果画一个方位格我们可以看出dp[i][j]的值是从dp[i+1][j-1]的得出的,因为我们需要从下往上,从左往右遍历.又因为j的值是需要大于或等于i的值,所以我们第一个for循环用来遍历i range是从大到小
        第二个for循环用来遍历j range是(i,l) 从左往右
        """
        l = len(s)
        res = (1,s[0])
        dp = [[False]*l for _ in range(l)]
        for i in range(l):
            dp[i][i] = True
        for i in range(l-1,-1,-1):
            for j in range(i,l,1):
                if s[i] == s[j]:
                    if j -i <=1:
                        dp[i][j] = True
                        pal_len = (j-i+1, s[i:j+1])
                        res = max(res,pal_len)
                    else:
                        if dp[i+1][j-1] ==True:
                            dp[i][j] =True
                            pal_len = (j-i+1, s[i:j+1])
                            res = max(res,pal_len)
        # print(dp)
        # print(res)
        return res[1]
