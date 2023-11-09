# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # the two pointers are slow - s and fast - f pointer

        '''

        s = head
        f = head

        #print(s.next.next.val)

        while f and f.next:
            s = s.next
            f = f.next.next
        
        return s


        '''

        if(head is None):
            return None
        else:

            s = head
            f = head

            #print(s.next.next.val)

            while(f and f.next):
                s = s.next
                f = f.next.next
            
            return s

        
  
        