def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
    """
    这题需要创建一个adjecent table,因为graph里面的包含的只是edges的信息,所以我们需要一个adj table,里面index代表某一个点, adj[i]代表这个点连接了哪一个点
    1) dfs里面需要什么参数: adj(用来遍历每一个point找到它的所有连接点),cur(我们当前找的是哪一个index的array在adj里面)
    2) 什么时候触发return:当cur==destination 或我们把关于source的所有连接点都遍历过一遍但是还是没有找到destination时
    3) 在每一次的recursive里面我们需要做什么: 我们首先要判断这个点之前是否visit过,如果时的话就直接跳过这个点进行下一轮的for循环判断. 如果没有的话我们在visited里面标记一下,然后把这个参数放入dfs里面
    
    """
    adj = [[] for _ in range(n)]
    for u,v in edges:
        adj[u].append(v)
        adj[v].append(u)
    visited = [0] * n
    res = False
    def dfs(adj,cur):
        nonlocal res
        if cur == destination:
            res = True
            return 
        for i in adj[cur]:
            if visited[i] ==0:
                visited[i] = 1
                dfs(adj,i)
    dfs(adj,source)
    return res