# find if there is a cycle linkedin list between two singly linked list, if there is reutrn the first linkedin node otherwise return none
def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    """
    注意这里的相同连接点是指node相同而不是仅仅时value相同
    这题我我们先求出两个链表的长度, 找出长度较长的那个链表,然后进行末尾对其.
    这样做的目的是确保两个链表如果有连接处我们一定不会漏掉,并且两个链表同长度时我们同时遍历两个链表判断其中是否有node相同,有的话直接返回那个node否者退出循环返回none
    这里我们一定是取长度更长的链表进行位置移动,否者我们不能保证是否会错过连接点,另外我们一定要进行末尾对齐,当需要进行链表互换时记得长度也要互换
    最后我们同时遍历链表A,B, 如果其中有一个node相同就触发return, 否者就移动到下一个node一直到遍历过整个链表
    如果遍历完整个链表还是没有找到相同值,那么我们可以肯定没有共同连接点,可以return none
    
    """
    # get the linked list A length and B length
    lenA, lenB = 0,0 
    cur = headA
    while cur:
        cur = cur.next
        lenA+=1
    cur = headB
    while cur:
        cur = cur.next
        lenB +=1
    # make sure linked list B has longer length, if not we will switch up the length and head with B to A
    if lenB>= lenA:
        curB,curA = headB, headA
    else:
        curB, curA = headA, headB
        lenB, lenA = lenA,lenB #remember to switch the length too
    # alignment both linked list to their end
    for i in range(lenB-lenA):
        curB = curB.next
    # traverse over the rest of linked list A and B to see if there is a match, if it is then return the node otherwise we exit the while loop and return none
    while curA:
        if curA == curB:
            return curA
        else:
            curA = curA.next
            curB = curB.next
    return None