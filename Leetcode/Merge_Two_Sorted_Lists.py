#Time Complexity : O(M+N), Space Complexity : O(1)
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        if not l1 and l2:
            return l2
        elif l1 and not l2:
            return l1
        elif not l1 and not l2:
            return None
        
        if l1.val < l2.val:
            head = l1
            l1_node, l2_node, main_node = l1.next, l2, head
        else:
            head = l2
            l1_node, l2_node, main_node = l1, l2.next, head
        
        while l1_node and l2_node:
            if l1_node.val < l2_node.val:
                main_node.next = l1_node
                l1_node = l1_node.next
            else:
                main_node.next = l2_node
                l2_node = l2_node.next
            main_node = main_node.next
                
        if l1_node:
            main_node.next = l1_node
        elif l2_node:
            main_node.next = l2_node 
        return head
