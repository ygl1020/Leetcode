def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
    """
    这题其实和template的稀疏图的写法是一样的,但因为template里面我们求的最小值,这题我们求的是最大值,并且最小堆的定义是每次heappop都是最小的值,所以我们把概率进行负数处理,这样我们就可以保证heappop出最小的概率
    当我们把最下的负概率正数话时,我们就找到了最大的概率,余下的操作和模板是一样的
    另外注意pro[start_node]要初始化为1,而不是0因为0乘任何数都是0
    
    
    """
    # Build adjacency list
    g = [[] for _ in range(n)]
    for i, (u, v) in enumerate(edges):
        prob = succProb[i]
        g[u].append((v, prob))
        g[v].append((u, prob))
    
    # Initialize probabilities
    pro = [0.0] * n
    pro[start_node] = 1.0  # Probability of reaching start_node is 1.0
    # Max-heap (priority queue) to store (-probability, node)
    h = [(-1.0, start_node)]
    while h:
        # Get the node with the highest probability
        neg_prob, x = heapq.heappop(h)
        curr_prob = -neg_prob  # Convert back to positive probability
        # If the current probability is less than the recorded probability, skip
        if curr_prob < pro[x]:
            continue
        # If we reach the end node, return its probability
        if x == end_node:
            return curr_prob
        # Explore neighbors
        for y, edge_prob in g[x]:
            new_prob = curr_prob * edge_prob
            # If a better probability is found, update and push to the heap
            if new_prob > pro[y]:
                pro[y] = new_prob
                heapq.heappush(h, (-new_prob, y))
    # If no path is found, return 0
    return 0.0
        