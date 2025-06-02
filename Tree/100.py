#判断两个tree是否是相同的tree
def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        使用bfs时while循环的条件应该为当两个queue都不为空时,然后判断是否两个临时queue是否都为空,否者判断是否其中一个为空且另一个不为空,又或者两个queue的val不相等
        那么就直接return false.否者的话就把两个node的左右节点都放入对应的queue里面
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
        使用递归的话当在递归过程中如果某一对的node是相同的,我们不能直接return True,因为我们需要验证全部的node pair都是相等的.在这个过程中如果某一对nodes相同我们就继续
        递归判断他们的subnodes pairs,然后递归过程中只要出现有一对pair不相等-->if not p or not q or p.val!=q.val我们就可以return False. 最后当我们到了leaf节点就可以
        直接return true了
        """
        # method 2:
        # if not p and not q:
        #     return True
        # if not p or not q or p.val!=q.val:
        #     return False
        # return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)