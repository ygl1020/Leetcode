def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
    """
    这题思路因为有可能会修改第一个node所以我们需要dummy_head.具体的思路是我们往前搜索cur.next 和cur.next.next,然后对比前面第二位的val是否等于第一位的val
    如果等于那么就说明有重复的值,然后进入第二个while循环(删除全部的重复值一直到遇见没有重复的值为止),所以我们是从cur.next开始删除而且要注意这里我们没有移动cur,
    我们所有的比较都是围绕cur.next来的.while的条件是while cur.next and cur.next.val==val 然后删除当前的cur.next = cur.next.next.这个while循环结束我们就回到第一个while循环.
    """

    dummy_head = ListNode(next=head)
    cur = dummy_head
    while cur.next and cur.next.next: #判断前面两个node所以要确保到cur.next.next
        val = cur.next.val #保存当前cur.next的值 为后面的比较做reference
        if cur.next.next.val == val: #如果判断有replicate
            while cur.next and cur.next.val==val: #进入循环如果cur.next存在并且cun.next.val==之前保存的val.我们就删除当前的cur.next并把cur.next指向cur.next.next
                cur.next = cur.next.next
        else:
            cur = cur.next
    return dummy_head.next