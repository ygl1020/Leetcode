#743 如何判断用sparse和dense写法是对比mlogm和n^2， m代表边的数量，如果mlogm >= n^2，dense 写法否者sparse
def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
    
    # for dense graph：稠密图 边的数量级和 n^2 相当的图 
    """
    主要分为两步: 
    1) 每次从未标记的节点中选择距离出发点最近的节点(Done[i]==Flase and dis[i]是最小的,标记(Done[i]=True),收录到最优路径合集中
    2) 计算刚加入的节点A和它的全部临近节点B的距离如若节点A的距离+节点A到B的边长 <节点B的距离,那么就更新节点B的距离  通俗点说因为临近点可能之再节点A之前就被其他点计算过(因为节点B是节点C的相邻点,并且节点C先于节点A被访问),
    那么此时节点B已经有了一个最优距离(从起始点经过C到B的最短距离),所以我们需要比较当前节点B的最短距离和从途径A到B的距离
    
    error1:记住是从k-1最为起点而不是0
    error2:注意是用done array不是dis 因为我门需要done里面的value--->ture or fasle
    error3:记住时比较dis[connected_node]-->从其他点出发到connected_node的距离 和从x点到connected_node的距离dis[connected_node]+weight
    """
    g = [[inf for _ in range(n)] for _ in range(n)] #  新建一个N*N的矩阵,g[i][j] 代表从点i到j的edges值是多少
    for stratnode,endNode,weight in times:
        g[stratnode-1][endNode-1] = weight
    dis = [inf] * n # 创建一个长度为n的矩阵,dis[i]代表从出发点到i的最短距离
    ans,dis[k-1]  = 0 ,0#设置最终的答案和dis[k]等于0, 因为从k出发到点k的最短距离为0-->到它自己的距离    # error 1
    done = [False] *n #设置done的数组, 这个数组代表我们是否找到了点done[i]的最短距离,如果已经找到了那么我们就不再需要重新访问这个点
    
    while True:
        x =-1
        for i, ok in enumerate(done): # error2 
            if not ok and (x <0 or dis[i] < dis[x]): #我们每次只找出没被找到最优距离的点中距离出发点行程最短的点,所以需要用for循环来遍历每一个点，if not可以保证每次只访问没被找到最优距离的点 ,x <0 确保每次的第一个点可以被更新 ，dis[i] < dis[x]确保我们找到的点是当前全部没找到最有距离点的最小的值
                x = i
        if x < 0: #当x<0时代表我们已经找到全部node 的最优值因为done[i] == True 所以第一个for循环里面的if条件不会被继续下去，我们只要返回ans就可以
            return ans
        if dis[x] ==inf: # 当for循环里的if条件通过,且这个dis为inf那么就代表它不和起始点相连接,那么我们就不可能从起始点通过每一个点,直接返回-1
            return -1
        ans = dis[x] #更新ans
        done[x] = True #标记当前的node为找到最短距离
        for connected_node, weight in enumerate(g[x]): # 遍历当前i的所有临近点,并给他们再dis的最短值进行更新,
            dis[connected_node]  = min(dis[connected_node],dis[x]+weight)   # error 3
    

    # for sparse graph 稀疏图 边的数量级远小于 n^2 相当的图
    """
    这个写法是用最小堆的方式,在堆中我们可以保证每一次heappop出的值是当前堆中的最小值,那么这就有可能同一个点多次入堆(举例：(0, 1, 1), (0, 2, 4), (1, 2, 2),这里节点2就会出堆两次(3,2)和(4,2)那么在第二种情况我们就需要把4和3作比较),我们需要判断这个值出堆的时候是否已经找到了他的minimum path,所以就需要把他的dx和dis[x]进行比较,如果dx>dis[x]我们可以知道
    这个值的最小path已经被处理过了所以我们可以跳过当前的操作执行continue,否者继续下一轮的for 循环.
    然后这种写法最后我们需要在return判断mx是否为inf,如果是的话那就代表从起始点出发并不能路过全部的点,我们返回-1
    
    """
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        g = [[] for _ in range(n)]  # 邻接表
        for x, y, d in times:
            g[x - 1].append((y - 1, d)) # 构建图的邻接表

        dis = [inf] * n  # 初始化距离数组，dis[i] 表示起点到节点 i 的最短距离
        dis[k - 1] = 0 # 起点到自身的距离为 0
        h = [(0, k - 1)] # 最小堆，存储 (距离, 节点)
        while h:
            dx, x = heappop(h)   # 弹出当前距离最小的节点
            if dx > dis[x]:  # 如果当前距离大于已知的最短距离，跳过
                continue
            for y, d in g[x]:  # 遍历节点 x 的邻居
                new_dis = dx + d  # 计算从起点到 y 的新距离
                if new_dis < dis[y]: # 如果新距离比已知的最短距离更小
                    dis[y] = new_dis  # 更新 x 的邻居的最短路
                    heappush(h, (new_dis, y)) # 将 (new_dis, y) 推入堆中
        mx = max(dis)
        return mx if mx < inf else -1

