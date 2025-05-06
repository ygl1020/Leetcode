#207
def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    """
    思路是使用拓扑排序,如果prerequisites里面没有环,那么就一定dequeue的次数定于numCourses.所以如果numCourses==0,那么就满足拓扑排序
    1) 首先创立一个indegrees:代表每一个节点有多少条入度 , graph:是二维数组,代表了index i连接了那些节点。 所以我们遍历prerequisites来获取这两个array的信息
    2) 找出入度为0的所有node并把他们放入queue里面
    3) 遍历每一个queue的值,每次dequeue时numCourses -1,
    4) 循环当前dequeue值的所有连接点, 每一个连接点的入度-1, 并且判断连接点的入度是否为0,如果是0那么就enqueue
    """
    # 创立indegrees, graph
    indegrees = [0 for _ in range(numCourses)]
    graph = [[] for _ in range(numCourses)]
    queue = collections.deque([])
    for course, pre in prerequisites:
        indegrees[course] +=1
        graph[pre].append(course)
    #找出indegrees == 0的点然后入队列
    for i in range(len(indegrees)):
        if indegrees[i] ==0:
            queue.append(i) #这里enqueue 的是index（course num）
    #开始拓扑排序
    while queue:
        pre = queue.popleft()
        numCourses -=1
        for adj_node in graph[pre]:
            indegrees[adj_node] -=1
            if indegrees[adj_node] ==0:
                queue.append(adj_node)
    return numCourses ==0


#210

def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    """
    和207一样的代码,区别在于我们新建了一个result数组,当最后有拓扑路径存在时--->当numCourses==0,我们返回result
    这里需要注意的是这题只要求了返回任意一条路径,但是其实我们有多条路径
    
    """
    indegrees = [0 for _ in range(numCourses)]
    graph = [[] for _ in range(numCourses)]
    queue = collections.deque([])
    result = []
    for course,pre in prerequisites:
        indegrees[course] +=1
        graph[pre].append(course)
    
    for i in range(len(indegrees)):
        if indegrees[i] ==0:
            queue.append(i)
    while queue:
        pre = queue.popleft()
        numCourses -=1
        result.append(pre)
        for adj_course in graph[pre]:
            indegrees[adj_course] -=1
            if indegrees[adj_course] ==0:
                queue.append(adj_course)
    return result if numCourses==0 else []