
class Solution(object):
    def isPalindrome(self, head: ListNode) -> bool:
        """
            Time Complexity : O(N), Space Complexity : O(N)
            Solution : list만들어서 two pointer로 비교
        """
        cur = head
        a = []
        while cur:
            a.append(cur.val)
            cur = cur.next
        for i in range(len(a)):
            if a[i] != a[len(a)-1-i]:
                return False
        return True
    
    def isPalindrome(self, head):
        """
            Time Complexity : O(N), Space Complexity : O(1)
            Solution : 전체 길이를 구하고 절반 이후로는 순서를 뒤집어 새롭게 연결. 그 이후, head와 tail에서 각각 정순, 역순으로 노드를 비교
        """
        # Calculate total length
        node = head
        length = 0
        while node:
            length += 1
            node = node.next

        # Find middle node
        node = head
        for _ in range((length - 1) // 2):
            node = node.next

        # Reverse the order
        target_node = node.next
        while target_node:
            next_node = target_node.next
            target_node.next = node

            node = target_node
            target_node = next_node

        # Compare two nodes starting from head and tail
        for _ in range(length // 2):
            if head.val != node.val:
                return False
            head = head.next
            node = node.next

        return True
