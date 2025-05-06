def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
    """
    这里其实和标准的dfs很像,但是我忘记了怎么写了,而且感觉思路有一些乱
    
    1) dfs里面需要什么参数: 我们需要graph,cur(这个代表每一次我们for循环对应的数组下标)
    2) 什么时候停止递归开始回溯: 当我们的下标cur等于len(graph)-1(代表我们找到了最后一个node时), 这里不需要额外判断一个leaf情况,因为在dfs里面我们要考虑到达leaf的情况,但是这里的for循环会自己出发return当当前的i时当下数组的index最大值时
    3) 每一个iteration里面我们需要做什么: 我们需要把当前visited的index value(在graph[cur]里面)放进path,然后我们使用bfs函数参数为(graph,i),因为我们深度搜索会更新bfs为当前visited的下标值
    
    """
    m= len(graph)
    res,path = [],[0]
    def dfs(graph,cur):
        if cur == m-1:
            res.append(path[:])
            return
        for i in graph[cur]:
            path.append(i)
            dfs(graph,i)
            path.pop()
        
    dfs(graph,0)
    return res



edges = [[0,1],[1,2],[2,0]]
adj = [[] for _ in range(3)]
for u, v in edges:
    adj[u].append(v)
    adj[v].append(u)
print(adj)