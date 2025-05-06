def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
    """
    这题的思路很简单,我们直接判断cur.val 是否等于cur.next.val. 如果不等于那么就把cur移动到下一个元素进行判断,否者就删除下一个node: cur.next = cur.next.next
    另外这题其实可以不用dummy_head 因为这里是sorted 然后去除replicate,所以我们可以保证head不会被删除，但我们也可以用dummy_head. 然后这里cur是从dummy_head.next开始
    """
    if not head:
        return None
    dummy_head = ListNode(val =0,next=head)
    cur = dummy_head.next
    while cur.next:
        if cur.val == cur.next.val:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return dummy_head.next