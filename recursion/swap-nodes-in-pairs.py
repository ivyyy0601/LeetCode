# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head= ListNode()
        dummy_head.next=head
        cur=dummy_head
        while cur.next!=None and cur.next.next != None:
            temp= cur.next #1
            temp1=cur.next.next.next #3
            cur.next=cur.next.next  #指向2
            cur.next.next = temp
            temp.next=temp1
            cur=cur.next.next
        return dummy_head.next


        