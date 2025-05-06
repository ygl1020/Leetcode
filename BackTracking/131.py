#在一个字符串中进行分割,找到所有分割的组合,组合呢的每一个字符串都是回文子串
def partition(self, s: str) -> List[List[str]]:
        """
        大体思路是用回溯,我们在每一次回溯的过程中把当前回合切割的字符串放入path,然后这里我们需要一个startIndex来记录上一次切割到哪个位置. return是在叶子节点,
        当我们startindex是大于len(s)时我们就到了叶子节点
        """
        if not s:
            return []
        path,res,startIndex = [],[],0
        def backtracking(s,startIndex):
            if startIndex >= len(s): # 当startIndex等于len(s)时代表我们不整个string都切完了,如果是n-1那表示我们还没有处理完最后一位string value就结束了
                valid = False
                for p in path:
                    left,right = 0, len(p)-1
                    while left<=right:
                        if p[left] !=p[right]:
                            valid=False # 只要有一个字符串不符合要求就退出
                            return
                        left+=1
                        right-=1
                        valid = True
                    if not valid: # 只要有一个字符串不符合要求就退出
                        return
                res.append(path[:])
            for i in range(startIndex,len(s)):
                tmp = s[startIndex:i+1] #每一层的时候我们都是截取当前层的slice然后加入到path里面,slice的value为s[startIndex,i+1]
                path.append(tmp)
                backtracking(s,i+1) #因为只能从后往前切来避免重复,所以需要i+1,代表我们从i的下一位开始
                path.pop()
        backtracking(s,startIndex)
        return res
    
p = '1'
p.startswith('0')