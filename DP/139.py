#让你在一个字符串中判断能否用wordDict里面的元素来构成这个字符串
def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        这题我们定义dp[i]数组含义为：s[i:]的字符串可以被wordDict里面的元素填满.然后我们的递推公式为dp[i] = dp[i+len(w)]. for循环的顺序一定要是背包在外面,然后物品在里面,因为递推公式决定了
        我们的dp[i]是由右边的答案来确定的,因此我们需要保证右边的结果时稳定不变的当我们求dp[i]时,如果换成物品在外面,背包在里面就会造成右边的结果可能发生改变来影响结果.另外就是如果外面放物品
        """
        dp = [False] * (len(s)+1)
        dp[-1] = True
        for i in range(len(s)-1,-1,-1):
            for w in wordDict:
        # for w in wordDict: 
        #     for i in range(len(s)-1,-1,-1):
                if i + len(w) <= len(s) and s[i:i+len(w)] == w:
                    dp[i] = dp[i+len(w)]
                if dp[i]:
                    break
        print(dp)
        return dp[0]
        