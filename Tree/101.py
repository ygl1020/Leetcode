def isSymmetric(self, root: TreeNode) -> bool:
        """
        这题的思路是把整棵树拆分为左右两颗树,左边用左右中的顺序遍历,右边用右左中的顺序,然后我们分别对比第一棵树的root.left和第二棵树的root.right-->两个外侧的node进行对比 
        以及第一棵树的root.right和第二棵树的root.left-->两个内侧的node进行对比. 用两个variable来分别储存这两个对比结果. 注意我们在一开始的return的条件中考虑到了4种情况,其中第二种情况是处理到达了最下面的
        子节点的情况. 除了这四种情况,如果left.val ==right.val我们就需要继续递归下去,因为我们要确保左右两个树的每一个root的sub nodes都是可以反转的.因此这里也需要最后一个return,否则当left.val ==right.val
        我们没有任何的返回,但是这里我们应该返回true
        递归三部曲1) 需要同时递归左右子树,因此需要左右子树两个参数 2）停止条件 a.当左node为none,右node不为none b.当左node不为none,右node为none c.当左node.val !=right.val d.当左node为none and 右none为none
        3）每一次循环里面的logic: 我们对比左子树的左节点和右子树的右节点-->外侧, 对比左子树的右节点和右子树的左节点-->内侧. 返回这两个result的对比结果-->只有都是true才返回true
        """
        if not root:
            return False
        def compareTree(left,right):
            if not left and right:
                return False
            elif left and not right:
                return False
            elif not left and not right:
                return True
            elif left.val!= right.val: # 这里不能用left!=right 因为即使左子树和右子树symmetric,他们还是不相同.他们相等的只是node的value
                return False
            outside = compareTree(left.left,right.right) #这里的话我们需要存储递归函数的output,否则的话最后返回的是一个空值,那么我们的逻辑就不成立了
            inside = compareTree(left.right,right.left)
            return outside and inside #我们一定要有一个return在这里,而且这个return是一个boole类型代表当前左右两个tree的sub node的对比情况.另外如果这里没有return,那么当left.val == right.val就没有返回值了,这样这个函数最后的return是none并且这个结果会被传递到上层最终引发错误
        
        return compareTree(root.left,root.right)