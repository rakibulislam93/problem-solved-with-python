
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def insert_at_tail(head,tail,value):
    newNode = ListNode(value)
    if head is None:
        head = newNode
        tail = newNode
        return head,tail
    tail.next = newNode
    tail = newNode
    return head,tail

def reverse_linklist(head):
    if head is None or head.next is None:
        return head
    newhead = reverse_linklist(head.next)
    head.next.next = head
    head.next = None
    return newhead

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        newhead = None
        newtail = None
        temp = head
        while temp is not None:
            newhead,newtail = insert_at_tail(newhead,newtail,temp.val)
            temp = temp.next

        newhead = reverse_linklist(newhead)
        
        temp = head
        while temp is not None:
            if temp.val != newhead.val:
                return False
            temp = temp.next
            newhead = newhead.next

        return True