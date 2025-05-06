#102 层序遍历
def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # method1 iteration
        """
        method 1：这题用迭代的思路为我们单独处理每一层的node,每次处理完当前层的一个node,我们把它放进level 数组,然后我们把它的左右节点入队列,需要处理的个数是根据一开始队列的长度来决定的所以需要用for循环
        具体的思路是1)创建一个level数组用来储存每一层的node(这个数组在while循环中会每次都会进行清空), 定义一个当前层的长度remove_len 为当前队列长度 2)使用for循环来移除对列出这一层所有的元素,循环次数由remove_len定,循环里会从左移除第一个元素,然后把这个元素放入level. 之后我们把当前出队列的node的左右分节点入队列.3）每次for循环结束代表我们已经收集完当前level的全部元素,因此我们把level的数组放入res中.
        """
        if not root:
            return []
        queue = collections.deque([root])
        res = []
        while queue:
            level = []
            remove_len = len(queue)
            for _ in range(remove_len): # 这里是len(queue),因为我们是从队列里面弹出元素,并且弹出的个数是一开始就记录好了的,否者后面队列的长度会发生改变.这里弹出的个数为每一层的节点数
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level)
        return res

        """
        method 2：这题用递归的思路为 1)思考我们dfs函数里面需要什么参数 root和level的信息, root是节点的信息,level是当前的层数信息我们后面要这个信息把相应的node放入正确的位置在levels里面
        2）开始递归的条件:当遍历到了最后一层的节点之后,root为空时 3）每一层的逻辑:判断这一层的levels[level]是否已经被初始化过(是否存在一个array在levels[level]的位置), 把当前节点放进对应的level数组, 遍历当前level的左右节点
        """
        if not root:
            return []
        levels = []
        def dfs(root,level):
            if not root:
                return 
            #len(levels) == level代表当前level还没有在levels里面initiate,所以我们要放入一个空数组在levels[level]的位置
            if len(levels) == level:
                levels.append([])  #注意要用levels.append([]) 而不是levels[level] = [],因为一开始levels是空的,所以levels[0]是没有东西的,会超出index range
            levels[level].append(root.val)  #直接按照level的index把当前node放在对应的level里面
            dfs(root.left,level+1) #题目中说了是从左到右,所以先放左遍历左node
            dfs(root.right,level+1)
        dfs(root,0)
        return levels