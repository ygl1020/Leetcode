#求最大深度
def maxDepth(self, root: Optional[TreeNode]) -> int:
        # postorder
        # def postOrder(root):
        #     if not root:
        #         return 0
        #     left = postOrder(root.left)
        #     right = postOrder(root.right)
        #     depth = 1 + max(left,right)
        #     return depth
        # return postOrder(root)

        # bfs
        if not root:
            return 0
        queue,levels = collections.deque([root]),0
        while queue:
            level_len = len(queue)
            for i in range(level_len):
                cur = queue.popleft()
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            levels +=1
        return levels
