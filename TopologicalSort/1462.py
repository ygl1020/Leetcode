# 1462

def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
    """
    这题的解法其实和模板是一样的,但是我们多了了一个条件如何判断indirect path? 比如说 a-->b-->c-->d 这里c和d是直接相连所以我门可以直接判断c可以到d但是a和b都是连接c的所以同理a和b也可以到达d
    因为我们可以额外建立一个path的2d array,这里的path[i][j]代表了有一条从i到j的路径,在我们处理入度时,我们在里面再加一个for循环,这个循环会判断会遍历全部numCourses节点,如果其中的中间任何一个节点满足path[other_path][cur] or path[other_path][pre],那么我们就把path里面的值标价为true进行联通
    
    """
    indegrees = [0 for _ in range(numCourses)]
    adj_g = [[] for _ in range(numCourses)]
    path = [[False] * numCourses for _ in range(numCourses)]
    queue = collections.deque()
    
    for pre,course in prerequisites:
        indegrees[course] +=1
        adj_g[pre].append(course)

    for i in range(len(indegrees)):
        if indegrees[i] ==0:
            queue.append(i)
    
    while queue:
        pre = queue.popleft()
        for cur in adj_g[pre]:
            path[pre][cur] = True
            for other_path in range(numCourses):
                path[other_path][cur] = path[other_path][cur] or path[other_path][pre]
            indegrees[cur] -=1
            if indegrees[cur] ==0:
                queue.append(cur)

    return [path[i][j] for i,j in queries]