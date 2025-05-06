#reverse linked list
def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #method 1. two pointers
        """
        "首先需要搞清楚,这里是怎么数显链表反转的? 这题我们的大体思路是设置一个pre和cur指针,pre一开始指向none,cur指向head,然后我们把cur指向pre,然后同时向右移动pre和cur
        另外还要思考的是什么时候结束while循环, 1，2，3,如果我们有三个node,那么我们cur从1开始要移动到node3之后的none才算把全部节点取反,因为如果到了node3就停止的话我们就没有反转node3
        因为while循环的停止条件是while cur
        再while循环里面我们需要做1)先记录cur.next节点的信息否则我们把cur指向pre之后就不知道下一个node的信息了
        2)把cur指向pre 3)先把pre移动到cur,这个顺序很重要！！不然的话就完全错了  4)把cur移动到tmp"
        """
        # define two pointers
        pre = None #一开始pre是在head之前的节点所以是none
        current = head 
        while current: # 每一次遇见一个节点,我们都要把current和pre进行更新,一直到pre为之前的tail节点.这时current就指向了none的节点,所以while的条件是while current
            tmp = current.next #因为后面current会进行反转,反转完我们就不知道current.next的value了所以我们需要用一个临时的variable来记录current.next的值
            current.next = pre # 把directon进行反转
            pre = current #需要先更新pre的value否者如果先更新current的话pre的vlaue就指向了tmp
            current = tmp #移动到下一个节点
        return pre # 最后因为current会指向none,pre就是指向初始的tail节点 即反转后的头节点
    
    
        #method 2, recursive
        def res(current,pre):
            if current is None: # 当current为none时停止递归返回pre
                return pre
            tmp = current.next # 每一个iteration里面我们设置一个tmp来记录current.next
            current.next =pre #进行direction反转
            return res(tmp,current)
        return res(head,None)

