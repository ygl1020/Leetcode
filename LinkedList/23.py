# 给你一个list,里面的每一个element都是一个linkedin list,然后你需要merge所以的linkedin list最后进行返回
"""
    这题的思路是先写一个function用来merger两个linked list,然后我们在mergeKLists函数里面使用两个循环,第一个是while用来确定什么时候merge结束,然后再第二for循环里面
    我们不断把当前数组里面的元素进行merge通过调用mergeTwoList函数,这个过程中我们不断更新merged数组,for循环结束我们更新list为merged数组然后继续循环,一直到merge数组
    的长度为1
    """
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        while len(lists)>1:
            merged = []
            for i in range(0,len(lists),2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1<len(lists) else None
                merged.append(self.mergeTwoList(l1,l2))
            lists = merged
        return lists[0]


    def mergeTwoList(self,l,r):
        print(l,r)
        dummy = ListNode()
        tail = dummy
        while l and r:
            if l.val<r.val:
                tail.next = l
                l = l.next
            else:
                tail.next = r
                r = r.next
            tail = tail.next
        if l:
            tail.next = l
        if r:
            tail.next = r
        # print(dummy.next)
        return dummy.next