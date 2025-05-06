def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
    """
    dummy_head->1->2->3->4
    这题的思路是初始化一个dummy_head指向head, 然后我们可以定义一个current.从题目中我们可以得出我们需要交互2和1的位置所以具体可以分为四步
    1)current 指向2 2) 2指向1 3)1指向3 4)因为我们继续处理node3的顺序所以需要更新current的位置为1(reverse后的linked list为dummy_head->2->1->3->4->)
    从第四步可以看出while循环的条件是current.next and current.next.next 不为none
    这题还需要注意的细节是当我们执行完第一步 current.next不再指向1,所以如果2要指向1就失去了方向(direction断掉了),因此我们需要提前记录current.next的方向为temp1
    同理可得当我们处理完第二部,current.next.next.next不再指向3,所以如果1要指向3就失去了方向,因此我们需要提前记录current.next.next.next的方向为temp2
    这里不需要记录current.next.next是因为我们第一步更新时没有丢失这个信息
    有了temp1和temp2我们就可以开始按照顺序更新direction了,最后更新current的位置+2为下一个iteration做准备
    
    """
    dummy_head = ListNode(next=head)
    current = dummy_head
    while current.next and current.next.next:
        temp1 = current.next
        temp2 = current.next.next.next
        current.next= current.next.next
        current.next.next = temp1
        temp1.next = temp2
        current = current.next.next
    return dummy_head.next