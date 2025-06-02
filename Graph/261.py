# 判断valid tree
def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        这题的思考为什么是合格的树,我只想到了在递归节点的过程中不能有环,但是还有一个因素是递归完我们连接的节点个数需要等于n. 另外有一个edge case,因为我们这题是无方向的edge那么1,2相连的话那么判断
        完node1递归往下判断节点2时,我们会判断节点1已经在visited元组里面了,这样就会出现错误判断.这个情况我们需要跳过这个dfs的循环,而不是在dfs的最开始进行return的判断.因为如果按照
        if cur in visited and cur ==pre--》return true的话我们就没有遍历完完整的tree,这样的话最后的visited 长度不可能等于n.正确的做法是在下面的if条件进行判断
        """
        if n ==0:
            return True
        visited = set()
        connect = {node:[] for node  in range(n)}
        for i in edges:
            connect[i[0]].append(i[1])
            connect[i[1]].append(i[0])
        print(connect)
        def dfs(cur,pre):
            # error 1: if cur in visited and cur ==pre:
            #     return True
            if cur in visited :
                return False
            visited.add(cur)
            for subNode in connect[cur]:
                #error2 miss this logic
                if subNode == pre:
                    continue # 当我们从上到下判断完之后因为这题是无序的edges,所以cur的下一个节点也连接了cur,这样就造成了一个circle,因此这个edge case我们要跳过.
                if not dfs(subNode,cur):
                    return False
            return True 
        
        if dfs(0,-1) and len(visited)==n:
            print(len(visited))
            return True
        print(len(visited))
        return False