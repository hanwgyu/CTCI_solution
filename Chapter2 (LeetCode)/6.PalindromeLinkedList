#Time Complexity : O(N), Space Complexity : O(1)
# Solution : 전체 길이를 구하고 절반 이후로는 순서를 뒤집어 새롭게 연결. 그 이후, head와 tail에서 각각 정순, 역순으로 노드를 비교      
class Solution(object):
    def isPalindrome(self, head):
        # Calculate total length
        node = head
        length = 0
        while node:
            length += 1
            node = node.next
        
        # Find middle node
        node = head
        for _ in range((length-1)//2):
            node = node.next
        
        # Reverse the order
        target_node = node.next
        while target_node:
            next_node = target_node.next
            target_node.next = node
            
            node = target_node
            target_node = next_node
        
        # Compare two nodes starting from head and tail 
        for _ in range(length//2):
            if head.val != node.val:
                return False
            head = head.next
            node = node.next
            
        return True