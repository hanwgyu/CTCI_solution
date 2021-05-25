# Time Complexity : O(N). Space Complexity : O(1)
class Solution(object):
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return None
        dummy = ListNode()
        dummy.next = head
        prev, cur = dummy, head.next
        
        while cur:
            if prev.next.val == cur.val:
                while cur and prev.next.val == cur.val:
                    cur = cur.next
                prev.next = cur
            else:
                prev = prev.next
            if cur:
                cur = cur.next
        return dummy.next
    
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
                # Move 'remove' until becomes differ from 'pivot'
                while remove and pivot.next.val == remove.val:
                    remove = remove.next
                # remove nodes between 'pivot' and 'remove'
                pivot.next = remove
                if remove:
                    remove = remove.next
            else:
                remove = remove.next
                pivot = pivot.next

        return head
