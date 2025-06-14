#让你在一个字符串中判断能否用wordDict里面的元素来构成这个字符串
def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        首先我们对dp数组的定义是长度为i的字符串可以被拆分为wordDict中的字符串.然后我们需要判断这个题是需要考虑排列还是组合的解法.
        因为leetcode字符串如果被拆分不能被拆作起始为code,所以我们判断顺序是需要被考虑的.因为我们先遍历背包然后物品.
        这个时候我们判断一个再长度为i的字符串中,从s[0:i]是否可以被拆分,我们需要判断dp[i]是否为True,然后s[i:j]是否再wordDict当中.
        如果两个条件都满足那么dp[j]就是true,最后我们return
        """
        #method 1, 类似双指针
        # dp = [False] * (len(s)+1)
        # dp[0] = True
        # for i in range(1,len(s)+1):
        #     for j in range(0,i):
        #         if dp[j] and s[j:i] in wordDict:
        #             dp[i] = True
        # return dp[-1]

        #method 2, 完全背包
        dp = [False] * (len(s)+1)
        dp[0] = True
        for i in range(1,len(s)+1):
            for j in wordDict:
                if i-len(j) >=0 and dp[i-len(j)] and s[i-len(j):i] ==j:
                    dp[i] = True
        return dp[-1]
        

