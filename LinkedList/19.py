def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    """
    这题时非常经典的快慢指针解法,题目要求删去倒数第n个node,然后返回head.如果linked list是: 1,2,3,4,5 n=2,那么我们就需要删去4,这样的话我们的slow指针需要到3,
    如果我们fast指针先走2步,然后后面while循环到fast指针为空,在循环中slow和fast同时移动一格单位,那么最后slow指针会到4.
    所以fast指针需要先走4步,最后fast指针指向none然后slow指向3,这时我们直接删去node4然后返回dummy_head.next就可以了
    """
    dummy_head = ListNode(next=head)
    slow =fast = dummy_head # 需要把fast和slow指针也指向dummy_head这样就可以handle删除head节点的情况
    for i in range(n+1): #因为我们把指针初始化在dummy_head,所以需要n+1
        fast = fast.next
    while fast: #同时更新slow,fast直到fast为none
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next #删去target节点
    return dummy_head.next


    """
    method 2 这个是我自己想出来的解法,首先遍历一遍链表获取其长度,然后计算target node这样我们之后从哪里开始跳过下一个节点具体的解法是
    1)先遍历一遍链表条件是while cur.next, 2)然后我们我们计算需要第二次遍历需要到哪一个node使用for循环, 3)最后循环结束我们删除下一个节点
    """
    dummy_head = ListNode(next=head)
    cur = dummy_head
    length = 0
    while cur.next: #因为用了dummy_head所以求长度最好用cur.next，否则的话长度会+1,因为dummy_head 的长度也会被计算再里面
        length +=1
        cur = cur.next
    print(length)
    cur = dummy_head
    target = length - n
    print(target)
    for _ in range(target):
        cur = cur.next
    cur.next = cur.next.next
    return dummy_head.next