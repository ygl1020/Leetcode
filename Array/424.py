#给你一个字符串,以及一个k的整数,让你求在k次置换中,最长的相等子序列的长度
def characterReplacement(self, s: str, k: int) -> int:
        """
        解题思路是使用l,r来构成一个滑动窗口.再每一个窗口中我们需要确保窗口的长度-当前窗口出现最多的值<=k, 这样我们可以保证再置换k次元素后这个窗口的长就是最长的子序列.然后我们不断更新
        res. 当窗口的长度-当前窗口出现最多的值>k，我们开始移动左指针,一直到窗口的长度-当前窗口出现最多的值<=k,这个过程中我们需要更新count字典-->count[s[l]] -=1,移动左指针向右一个单位
        """
        count = {}
        l = 0
        res = 0
        for r in range(0,len(s)):
            count[s[r]] = 1 + count.get(s[r],0)
            while r-l+1 - max(count.values()) >k:
                count[s[l]] -=1
                l +=1
            res = max(res, r-l+1)
        return res