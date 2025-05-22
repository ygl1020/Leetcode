#check if  there is a cycle inside a linked list
def hasCycle(self, head: Optional[ListNode]) -> bool:
        # method 1 using set
        # unique = set()
        # while head:
        #     if head in unique:
        #         return True
        #     unique.add(head)
        #     head = head.next
        # return False

        #method 2 using slow and fast pointer\
        fast,slow = head,head
        while fast and fast.next: # 我们只需要确保fast.next不为空这样的话即使fast.next.next是none也没关系.这个 条件是为了确保fast.next.next不会报错
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False