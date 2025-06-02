#判断有几个相连接的集合个数
def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """
        这题是261的变种.思路其实是一样的.通过dfs函数来遍历每一个连接的点,在这个过程中不断把traver过的node放入visit,然后一个for循环遍历每一个node,遇见在
        visit里面的node我们就跳过当前node进行下一个元素的dfs,每一次dfs结束记录一下最后进行return
        
        """
        if n==0:
            return 0
        connect = {i:[] for i in range(n)}
        for i,j in edges:
            connect[i].append(j)
            connect[j].append(i)
        visit = set()
        count =0
        def dfs(cur,pre):
            if cur in visit:
                return
            visit.add(cur)
            for c in connect[cur]:
                if c == pre:
                    continue
                dfs(c,cur)
        for i in range(n):
            if i in visit:
                continue
            dfs(i,-1)
            count+=1
        return count