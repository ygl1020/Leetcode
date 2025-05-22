#把原链表就行修改eg,1,2,3,4---> 1,4,2,3
def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        这题的关键在于找到中间的那个postion来分离list.我一开始是直接反转原来的list,然后想把原来的list和反转后的merge起来.但是这个做法已经把原本的
        list修改了,所以是错误的. 寻找中间的position我们用快慢指针.然后我们把第二个list进行反转,最后把第一个和第二个list 进行merge
        """
        # use slow,fast pointer to indentify the middle position
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        #starting of the second segment will be slow.next
        second = slow.next
        # break the link beween first segment list and second
        slow.next = None
        #reverse the second part list
        pre,cur = None,second
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur=tmp
        # merge two segment list together
        first, second = head, pre
        while first and second:
            tmp1 = first.next
            tmp2 = second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2