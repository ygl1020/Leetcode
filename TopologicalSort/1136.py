# 1136
def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
    #这题的思路是用bfs和topological sort一起来找出遍历过全部course所需要的最小步数, 之前的题目我们都是用简单的topological sort的代码就可以，这topological sort里面我门处理queue里面的course不是按照一个整体来处理的，而这个是bfs的关键-->一圈一圈处理不断向外围扩展
    #所以我们需要再加一个for循环在while循环里面,这个循环可以让我们把queue队列里面的所有course按照一个整体来处理，queue里面的全部course处理完了我们再开始进行下一步的
    #这题有好几个需要注意的点,1) n是从1到n的数而不是 0 到n-1， 所以我们获取indegree和构造adj_g时应该从1开始取值一直到n+1 2)我们需要建立初始化一个semester 和course_taken
    #3) semeter会加1 当每一次进入while循环时, 然后第一个for循环是把queue里面的全部元素处理完完才结束所以是level_len ， 之后我们再每一次处理queue里面的course时,courses_taken+=1
    #4） 最后如果有topological path, 这时处理的节点可能等于n--> n==courses_taken, 我们返回semester 否则没有topological path return -1
    
    indegrees = [0 for _ in range(n+1)]
    adj_g = [[] for _ in range(n+1)]
    queue = collections.deque()
    for pre, cur in relations:
        indegrees[cur] +=1
        adj_g[pre].append(cur)
    for i in range(1,n+1):
        if indegrees[i] ==0:
            queue.append(i)
    semester = 0   
    courses_taken =0 
    while queue:
        semester +=1
        level_len = len(queue)
        for level in range(level_len):
            pre = queue.popleft()
            courses_taken +=1
            for pre_adj in adj_g[pre]:
                indegrees[pre_adj] -=1
                if indegrees[pre_adj] ==0:
                    queue.append(pre_adj)
    return semester if n==courses_taken else -1