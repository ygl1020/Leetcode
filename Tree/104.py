#求最大深度
def maxDepth(self, root: Optional[TreeNode]) -> int:
        # use bfs method and return the len(levels)
        if not root:
            return 0
        levels = []
        queue=collections.deque([root])
        while queue:
            level = []
            level_nodes = len(queue)
            for i in range(level_nodes):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            levels.append(level)
        return len(levels)
