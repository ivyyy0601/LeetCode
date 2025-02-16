#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverse(self,cur,pre):
        if cur ==None:
            return pre
        temp=cur.next
        cur.next=pre
        return self.reverse(temp,cur)

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.reverse(head,None)
        