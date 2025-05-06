# 求叶子层的最左边的元素
def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        """
        这题需要使用bfs,找到有最后一层的values 然后返回第一个element
        """
        res = []
        queue = collections.deque([root])
        while queue:
            level = []
            level_len = len(queue)
            for _ in range(level_len):
                cur = queue.popleft()
                level.append(cur)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            res.append(level)
        return res[-1][0].val