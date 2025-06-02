# 复制一个graph
def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        这题需要用递归来写,dfs或者bfs都是可行的.写dfs的时候还是要根据三部曲了些不需要具体的思考递归的过程不然会绕进去.首先我们需要一个oldToNew
        字典来吧map 当前node为copy.因此我们递归的返回条件就是当node在字典中为key存在时.这时我们直接return这个map对应node的copy就行了
        当node不存在字典里时,我们创建node对应的copy，把node放去字典然后对应的value为copy.这时我们开始for循环来当前node的neighbors放入
        copy.neighbors，因为我们只有确认neighbor里面的node已经有对应的copy时才能append到当前copy，所以我们在for循环到copy.neighbors.append
        使用dfs
        """
        oldToNew = {}
        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]
            copy = Node(val=node.val)
            oldToNew[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
                print('from edge',copy.val, nei.val)
            return copy
        return dfs(node) if node else None