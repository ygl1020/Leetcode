#再一个tree里面找到最小的两个nodes的公共祖先
def lowestCommonAncestor(self, root, p, q):
    """
    1)为什么是后序遍历? 
        我们需要再子节点中判断是否存在p,q节点,然后把信息回馈到root节点才行,所以这个顺序是左右中的后序遍历
    2) 为什么需要遍历整个树为不是只要遍历一条边就可以? 
        通常遍历一条边的情况是只要找一个tree里面是否有某种element存在,再找到了element我们就可以触发返回并且不继续后面的子节点的探索.通常我们可以直接return不需要再对信息做加工来得到答案(左右中的中过程可以省略) 
        对于需要遍历整个树的情况是我们需要左右两个节点的信息回馈来判断因此这样的话就要进行全局遍历,即使再某一个node找到答案,我们结束对这个node的subnode的探索 把result返回到father 节点,father节点的另一个branch还是会继续往下探索
    3)为什么这样写的话一定能找到最小公共祖先
        因为我们再后序遍历的边检涵盖了所有的可能性,所以不管这两个节点是出现在哪里我们都可以保证一定能找到最小公共节点
    4) 只遍历一条边和整个树有什么区别
        答案和3)是一样的
    5)这里的遍历是整个树但是不是遇见p或者q就提前返回了,因为还是遍历整个树呢
        答案和3)是一样的
    """
    if root==q or root==p or not root:
        return root
    left = self.lowestCommonAncestor(root.left, p, q)
    right = self.lowestCommonAncestor(root.right, p, q)

    if left and right:
        return root
    elif left and not right:
        return left
    elif not left and right:
        return right
    else:
        None