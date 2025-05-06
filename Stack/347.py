# 这题是求一个list中出现次数最多的k个数, 具体解题思路使用堆(Priority Queue or heap)堆是由二叉树构成的,大顶堆(Min-Priority Heap or Min Heap)就是root的值比两个子节点的值都大， 小顶堆(Max-Priority Heap or Max Heap)就是root的值比两个子节点的值都小，堆这种数据结构pop的时候是从堆顶开始pop的
"""
优先级队列和普通队列的 核心区别:
特性	            普通队列	                优先级队列
出队规则	    先进先出(FIFO)	    按优先级出队（优先级最高/最低优先）
元素顺序依赖	仅依赖插入顺序	        依赖元素的优先级值
典型应用场景	任务排队、消息缓冲	    任务调度、Dijkstra算法、哈夫曼编码
时间复杂度	    入队/出队均为 O(1)	    入队/出队通常为 O(log n)（基于堆实现）


问题	                    答案
新元素插入位置	                新元素加到列表末尾，通过“上浮”调整到正确位置。-->而插入和删除操作会通过内部的“上浮”(Sift Up)和“下沉”(Sift Down)操作动态调整堆结构，维持堆的性质不变
弹出哪个元素	                总是弹出 pri_que[0]（堆顶，最小元素）。
堆的排序依据	                按元组的第一个元素（freq）排序，如果相同则比较第二个元素（key）。
为什么不用集合（Set）	        集合无序，无法维护堆结构；必须用列表。
堆的物理存储是否有序	        列表存储看似无序，但逻辑上是完全二叉树，满足堆性质
"""


def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    """
    这题的解题思路分为3步 1) 遍历list计算每一个数值出现的次数并把这个结果存放在dict, key是num value是出现次数 2) 使用一个mini-heap来进行排序,这里选mini-heap而不是max-heap是因为堆的出堆规则是删除root节点,如果用
    max-heap, 那么就相当于我们把最大的那个值给删除了,最后保留下来的反而是最小的前k个数值 ,因此要用mini-heap每次删除最小的那个root. 另外这里mini_heap传入的是一个set(cur,key), 然后mini-heap里面会对第一个值cur进行排序
    当mini_heap的长度大于k时我们就删除root, 3) 把结果进行整理放入res数组中, 因为mini_heap的性质,出堆时的值root-->是最小的那个,所以我们要从后往前填充res数组,因此是for i in range(k-1,-1,-1) 
    代表从1到-1--> 按照index 为1,0的顺序进行填充
    """
    counts = {}
    # step 1, generate the key and its occurance counts
    for i in nums: 
        counts[i] = counts.get(i,0) +1
    # step 2 create a mini heap
    mini_heap = []
    for key, cur in counts.items():
        heapq.heappush(mini_heap, (cur,key))
        if len(mini_heap)>k:
        heapq.heappop(mini_heap)
    
    # step 3 organize the result and append into a array
    res = [0] *k
    for i in range(k-1,-1,-1):
        res[i] = heapq.heappop(mini_heap)[1]
    return res