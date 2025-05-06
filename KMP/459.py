class Solution:
    """
    这题需要判断再当前主字符串中是否存在一个字符串,通过重复这个子字符串可以构成主字符串
    可以在理解KMP算法的next数组的基础上，这样想：next数组存放的元素是某个阶段上重复的元素个数，由于能组成重复元素的长串next数组一定是整体向上递增的（即使中间数字会有波动起伏），
    取next最后一个元素就是最长相同前后缀（即重复的元素个数，记为max），len - max就是最小重复子串长度，如果len能被最小重复字串长度整除，说明长串均可由其构成。
    """
    def getNext(self,next,s):
        j = 0
        next[0] = 0
        for i in range(1,len(s)):
            while j>0 and s[i] != s[j]:
                j = next[j-1]
            if s[i] ==s[j]:
                j+=1
            next[i] = j
    def repeatedSubstringPattern(self, s: str) -> bool:
        j = 0
        next = [0]*len(s)
        self.getNext(next,s)
        if next[-1]!=0 and len(s) %(len(s)-next[-1])==0:
            return True
        return False