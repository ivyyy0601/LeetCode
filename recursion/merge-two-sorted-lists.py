# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #链表都是需要dummy和current的
        dummy=ListNode()
        current=dummy
        while list1 and list2: #while list就要遍历list了
            if list1.val <=list2.val:
                current.next= list1
                list1=list1.next
            else:
                current.next= list2
                list2=list2.next
            current= current.next #移到最后
        if list1:
            current.next= list1
        else:
            current.next= list2
        return dummy.next # 因为第一个事空的
        
        