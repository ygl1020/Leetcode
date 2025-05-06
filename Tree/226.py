# 反转tree的左右node的位置
def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        思路时用breadth迭代的写法,正常中序遍历时左中右,用queue的话先找左边然后找右边,这里的话就是先找右边然后找左边.改一下迭代的breadth搜索的左右节点处理顺序就好了
        另外需要注意,这题最后的return是修改过的root而不是一个list,这里我一开始的写法出现了错误因为是把它当成一个list来返回了
        """
        #error code
        # if not root:
        #     return []
        # levels = []
        # queue = collections.deque([root])
        # while queue:
        #     level_len = len(queue)
        #     for _ in range(level_len):
        #         node = queue.popleft()
        #         levels.append(node.val)
        #         if node.right:
        #             queue.append(node.right)
        #         if node.left:
        #             queue.append(node.left)
        # return levels
        
        if not root:
            return None
        queue = collections.deque([root])
        while queue:
            level_len = len(queue)
            for _ in range(level_len):
                node = queue.popleft()  # 注意cur的更新时在for里面,因为我们在for循环里面进行出队列和更新cur指针. 这样才能确保cur指针把每一层的所有元素都处理一遍,如果放在for循环的上面的话就只处理那一层的第一个元素
                node.left,node.right = node.right,node.left # 重要的是反转root左右node的位置,所以我们只要这这一步把他们的位置反转就好了
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root