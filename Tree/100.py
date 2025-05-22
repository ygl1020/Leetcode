#判断两个tree是否是相同的tree
def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        bfs同时遍历两棵树, 当两个数的节点都为空那么就直接进行一个node的对比,这里不能直接return true因为后面的node还没有对比完 , 当两棵树中之一一个树的node是空或者两个树都不为空并且两个node的值不相等,可以直接return false
        否者我们对两个树继续进行正常bfs的步骤
        """
        # method 1: bfs
        queue1 = collections.deque([p])
        queue2 = collections.deque([q])
        while queue1 and queue2:
                cur1 = queue1.popleft()
                cur2 = queue2.popleft()
                if not cur1 and not cur2:
                    continue
                if not cur1 or not cur2 or cur1.val!=cur2.val:
                    return False
                queue1.append(cur1.left)
                queue2.append(cur2.left)
                queue1.append(cur1.right)
                queue2.append(cur2.right)
        return True

        """
        再递归里面,边界条件如果遇见两个node 都是true,那么我们return true.因为这里需要对当前节点的对比结果进行return
        否者如果两个数中只有其中一个node为空又或者两个node的值不相等我们都return false,每次进行函数召唤时,我们最先check当前的两个node是否是相等的,然后我们继续check他们的分节点， 最后我们开始递归并对左右两个数的子树结果进行汇总
        """
        # method 2:
        # if not p and not q:
        #     return True
        # if not p or not q or p.val!=q.val:
        #     return False
        # return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)