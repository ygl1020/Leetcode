#给你一个字符串,返回符合合格ip的全部组合
def restoreIpAddresses(self, s: str) -> List[str]:
        """
        这题的思路其实和131回文字符串切割时大致一样的.我们也需要一个startindex来记录当前切割点在哪里,然后再当前回合把切割的字符串放入path.当startindex的值大于等于len(s)就表示我们已经
        遍历完全部的元素,触发返回. 然后我们再return里面进行符合条件的path筛选.这里需要注意没有leading 0s的意思是开始可以为0
        但是不能是01，022这种形式.
        """
        if not s:
            return []
        res, path,startIndex = [],[],0
        def backTracking(s,startIndex):
            if startIndex>=len(s):
                if len(path)!=4:
                    return
                else:
                    valided = False
                    for p in path:
                        if len(p)>1 and p[0]=="0":# 注意不能有leading 0s的意思是不能出现01, 023这种形式
                            valided = False
                            break
                        if 0<=int(p)<=255:
                            valided = True
                        else:
                            valided = False
                            break
                    if valided:
                        res.append(".".join(path))
                        return
            for i in range(startIndex,len(s)):
                tmp = s[startIndex:i+1] 
                path.append(tmp)
                backTracking(s,i+1)# 注意是用backTracking(s,i+1), 而不是backTracking(s,startIndex+1) 因为我们向下递归是从当前签个点的下一个元素开始的
                path.pop()
        backTracking(s,startIndex)
        return res
