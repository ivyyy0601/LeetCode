# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy_head= ListNode()
        dummy_head.next=head
        #反了！！！ 定义dummy_head的时候要写标准
        fast=dummy_head 
        slow=dummy_head
        n+=1
        while n>0 and fast != None:  #移动fast，使fast和slow保持n+1，fast不为空！！不是fast.next
            n-=1
            fast=fast.next
        while fast!= None: #移动slow，使他到倒数n+1
            fast=fast.next
            slow=slow.next
        slow.next = slow.next.next
        return dummy_head.next
        