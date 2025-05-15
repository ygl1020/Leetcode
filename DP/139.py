#让你在一个字符串中判断能否用wordDict里面的元素来构成这个字符串
def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        这题我们定义dp[i]数组含义为：s[i:]的字符串可以被wordDict里面的元素填满.然后我们的递推公式为dp[i] = dp[i+len(w)]. for循环的顺序一定要是背包在外面,然后物品在里面,因为递推公式决定了
        我们的dp[i]是由右边的答案来确定的,因此我们需要保证右边的结果时稳定不变的当我们求dp[i]时,如果换成物品在外面,背包在里面就会造成右边的结果可能发生改变来影响结果.另外就是如果外面放物品
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
        

