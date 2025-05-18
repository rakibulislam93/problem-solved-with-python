
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        i = head
        while i and i.next:
            if i.val == i.next.val:
                i.next = i.next.next
            else:
                i = i.next
            
        return head