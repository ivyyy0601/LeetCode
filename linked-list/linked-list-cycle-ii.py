# Definition for singly-linked list.
# class ListNode: # 如果已经定义过，就不需要再定义一次？？？？？？？？？？？？
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast=head
        slow=head
        while fast!=None and fast.next!= None:
            fast=fast.next.next
            slow=slow.next
            if slow==fast:
                index1=fast#相遇点，z
                index2= head #起点 x
                while index1!= index2:
                    index1=index1.next
                    index2=index2.next
                return index1
        return None