# Time Complexity : O(N). Space Complexity : O(1)
class Solution(object):
    def deleteDuplicates(self, head):
        if not head:
            return None
        if not head.next:
            return head
        
        pivot = head.next
        
        # Remove head
        if head.val == pivot.val:
            while pivot and head.val == pivot.val:
                pivot = pivot.next
            return self.deleteDuplicates(pivot)

        # Remove other nodes
        pivot = head
        remove = head.next.next
        while remove:
            if pivot.next.val == remove.val:
                #Move 'remove' until becomes differ from 'pivot'
                while remove and pivot.next.val == remove.val:
                    remove = remove.next
                #remove nodes between 'pivot' and 'remove'
                pivot.next = remove
                if remove:
                    remove = remove.next
            else:
                remove = remove.next
                pivot = pivot.next

        return head