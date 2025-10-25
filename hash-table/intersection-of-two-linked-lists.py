# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        indexA= headA
        indexB=  headB
        while indexA!=indexB:
            #正确算法是需要用 循环（while）反复移动 两个指针直到它们相遇。
            #  # 两个指针同时走，直到相遇或都为 None
            indexA= indexA.next if indexA else headB #(when indexA is none, then indexA=headB 就到下面那个了)
            indexB= indexB.next if indexB else headA
        return indexA

        