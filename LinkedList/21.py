#merge两个sorted linked list
def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        这题因为可能修改最开始的头节点所有需要设置一个dummy_head. 然后当list1和list2都不为空时，我们比较list1节点和list2节点的大小.之后更新更新的那个
        节点对应的next节点,以及移动tmp节点.最后我们需要注意一下list1或者list2有没有剩余的值,因为我们的while条件是只要list1和list2都不为空时才会继续
        """
        dummy = ListNode()
        tail = dummy
        while list1 and list2:
            if list1.val <=list2.val:
                # tmp = list1.next # 我们不需要删除tmp节点
                tail.next = list1
                list1 = list1.next
                
            else:
                # tmp = list2.next
                tail.next = list2
                list2 = list2.next
            tail = tail.next # 我们再每一次把当前最小的list append到tail之后需要把tail的位置进行更新,否者的话tail一直都停留在dummy的位置,后面的append是再同一个位置做覆盖
        if list1:
            tail.next= list1
        if list2:
            tail.next = list2
        # print(dummy)
        return dummy.next