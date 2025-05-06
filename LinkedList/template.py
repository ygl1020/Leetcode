#203 删除某个节点
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        """
        在处理linked list的时候我们会考虑头节点的问题,如果要删除的节点在头节点那么如何可以在return的时候返回新的头节点呢?为了解决这个问题我们一般会采用一个dummy_head.
        这里我们用一个current=dummy_head因为我们希望dummy_head的固定的这样我们在返回时就可以保证返回新的head,current在这个是起到一个指针的作用
        然后这里我们的目的时删除某个节点,所以我们直接用current.next = current.next.next,如果current.next.val = current.next.next.val 是改变节点的value但是那个节点还在list里面 
        eg: 1->2->3->4,如果想删除3   1->2->4 但是如果用current.next.val = current.next.next.val就会变成1->2->4->4,所以那个节点还是在list里面
        
        """
        # create a dummy_head
        dummy_head = ListNode(next=head)
        current = dummy_head
        # loop through the linked list
        while current.next:
            if current.next.val ==val:
                current.next = current.next.next
                current.next.val = current.next.next.val
            else:
                current = current.next
        return dummy_head.next
    

# 707 增，查，删，加节点
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyLinkedList:
    def __init__(self):
        self.dummy_head = ListNode()
        self.length = 0

    def get(self, index: int) -> int:
        if index <0 or index >=self.length: # 这里如果等于length为link的长度,所以当index等于或者超出length 以及index 为负数,那么我们就可以直接返回-1 
            return -1
        current = self.dummy_head.next # 创建一个copy of head, 从头节点开始遍历
        for i in range(index): #index 1代表head.next
            current = current.next
        return current.val

    def addAtHead(self, val: int) -> None:
        self.dummy_head.next = ListNode(val=val,next= self.dummy_head.next) #直接用一个dummy_head.next 指向新的节点,然后新的节点会指向之前dummy_head.next
        self.length +=1 # 记住size要+=1
        

    def addAtTail(self, val: int) -> None:
        current = self.dummy_head
        while current.next: #循环到最后一个节点
            current = current.next
        current.next = ListNode(val) #把现在的tail指向到新的tail
        self.length +=1 #把length+=1

        
    def addAtIndex(self, index: int, val: int) -> None:
        if index <0 or index > self.length: #这里不用index >= self.length,因为当index==self.length,我们添加最后一位node
            return
        current = self.dummy_head
        for i in range(index):
            current = current.next
        current.next = ListNode(val=val, next=current.next)
        self.length +=1
        

    def deleteAtIndex(self, index: int) -> None:
        if index <0 or index >= self.length: # 这里我们排除index==length,否者就超出范围了
            return
        current = self.dummy_head
        for i in range(index):
            current = current.next
        current.next = current.next.next
        self.length -=1
        

