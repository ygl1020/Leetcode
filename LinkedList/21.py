#merge两个sorted linked list
def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        这题的解法其实是再两个list里面找到更小的那一个,然后把这个list放入到我们merged list里面-->tail.next=list2 or list1, 然后我们把被添加进merged list的list往前
        更新一个单位继续进行下一个对比,再每一次对比结束我们都需要更新tail到当前list的最后一个节点,否者它会不断的覆盖更新的值导致报错.最后当list1和list2当中有一个list
        为空时,我们退出循环然后把不为空的那个list放到merged list的最后面
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