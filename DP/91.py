# 计算有多少种解码的方式
def numDecodings(self, s: str) -> int:
        """
        dp数组的含义是从s[0:i]中,再i时的解法方式有dp[i]种.然后dp公式为dp[i] = dp[i-1] + dp[i-2]分别对应的意思是把s[i]看作一个单独的数的组合以及把s[i-2:i]两个digitis看作一个整体的组合. 举例的话就是"123"
        3的解码方式是前面12的组合 加上前面1的组合. 然后for循环里面要注意最为一个digits时符合条件的解码情况是0<=int(s[i-1])<=9--> 这个digits要再0和9之间,然后两个digits最为整体的解码条件为
        0 <= int(s[i-2:i]) <=26. 然后初始化dp数组, 这里为了让dp[i]代表s[i],我们把dp数组的长度设为(len(s)+1), dp[0]代表空字符,dp[0]=1是因为即使是空字符串,它不能够被解码,这也算是一种解码方式
        df[1]=0. 一个digits只有一种解码方式

        特别需要注意的是只讨论一个digit的情况如果s[i-1] =='0' 就不符合情况, 然后讨论两个digits作为一个整体的情况时我们需要确保int(s[i-2:i])再 10 到26 这个区间内
        """
        if not s or s.startswith('0'):
            return 0
        dp = [0] * (len(s)+1)
        dp[0],dp[1] = 1,1
        for i in range(2,len(s)+1):
            if 0<int(s[i-1])<=9:
                dp[i] += dp[i-1]
            if 10 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2]
        # print(dp)
        return dp[-1]