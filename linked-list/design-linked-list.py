class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.dummy_head = ListNode()
        self.size = 0
    
    def get(self, index: int) -> int:
        if index<0 or index>=self.size:
            return -1
        cur=self.dummy_head.next #cur就和原来一样了
        while index>0:  #假设是0
            cur=cur.next
            index-=1
        return cur.val
        

    def addAtHead(self, val: int) -> None:
        new=ListNode(val)
        new.next=self.dummy_head.next
        self.dummy_head.next= new
        self.size+=1
        #头不需要cur。 不用cur直接改self

    def addAtTail(self, val: int) -> None:
        new=ListNode(val)
        cur=self.dummy_head.next #cur就和原来一样了
        while  cur.next != None:
            cur=cur.next
        cur.next= new
        self.size+=1
        

    def addAtIndex(self, index: int, val: int) -> None:
        new=ListNode(val)
        if index<0 and index>=self.size:
            return 
        cur=self.dummy_head #cur就和原来一样了 但是这个了不是head
        while index>0:  #假设是0
            cur=cur.next
            index-=1
        new.next=cur.next
        cur.next=new
        self.size+=1

    def deleteAtIndex(self, index: int) -> None:
        if index<0 and index>=self.size:
            return 
        cur=self.dummy_head
        while index>0:  #假设是0
            cur=cur.next
            index-=1
        cur.next = cur.next.next
        self.size-=1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)