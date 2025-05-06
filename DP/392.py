#给你两个字符串s,t,让你在t中寻找是否有s的不连续子序列，s不可以修改
def isSubsequence(self, s: str, t: str) -> bool:
        """
        还是相同的两个字符串中查找不连续最长子字符串的问题,但是区别是这次是在t中找s,t可以增删但是s是不可以的,因此当s[j-1]==t[i-1],递推公式是不变的
        但是当s[j-1]==t[i-1]我们不可以用dp[i][j] = max(dp[i-1][j],dp[i][j-1])-->这里考虑删除s或者t的情况，但是本题是s字符串不能被删除，所以只考虑dp[i-1][j]即
        往前一个单位(i-2)找和s的最长相等字符串
        """
        dp = [[0] * (len(s)+1) for _ in range(len(t)+1)]
        for i in range(1,len(t)+1):
            for j in range(1,len(s)+1):
                if s[j-1]==t[i-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    # dp[i][j] = max(dp[i-1][j],dp[i][j-1])
                    dp[i][j] = dp[i-1][j] # 这里的s字符串是不能删除的,所以我们只需要记录dp[i-1][j]的位置
        if dp[-1][-1] == len(s):
            return True
        return False