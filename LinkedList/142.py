# cycle linked list, only one linked list
def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        用快慢指针,slow和fast, slow每次移动一个单位,fast每次移动两个单位,如果有环那么fast一定先比slow如入环并且slow和fast一定会相遇
        相遇后把其中一个指针放回head然后两个指针同时移动一个单位一直到相遇为止
        
        1)初始化快慢指针从head出发,快指针每次移动两步慢指针移动一步
        2) 首先判断是否有环,如果有环的话那么快慢,当有环时,快指针一定先入环,并且每次以每次一步的速率靠近慢指针.这时他们肯定会相遇-->快指针等于慢指针
        3)如果有环,那么环的起点在哪里,我们把其中一个指针放会起点,另一个指针再相遇的位置,同时移动两个指针每次一个位置一直到两个指针重新相遇那就是环的起始点
        """
        slow,fast = head,head
        while fast and fast.next: #如果没有环的话fast会先遇到range limit所以我们要判断fast和fast.next
            slow = slow.next #slow移动一个单位
            fast = fast.next.next #fast一定两个单位
            if slow ==fast: #如果有环
                slow = head #把slow放回head
                while slow != fast: #继续循环一直到两个指针相遇为止
                    slow = slow.next
                    fast = fast.next
                return slow
        return None