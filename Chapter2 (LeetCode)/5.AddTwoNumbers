#Time Complexity : O(max(N,M)), Space Complexity : O(max(N,M))
class Solution(object):
    def addTwoNumbers(self, l1, l2):     
      res = ListNode(0)
      pivot_res = res
      pivot1 = l1
      pivot2 = l2
      
      carry = 0
      while pivot1 or pivot2:
          if pivot1:
              carry += pivot1.val
              pivot1 = pivot1.next
          if pivot2:
              carry += pivot2.val
              pivot2 = pivot2.next

          pivot_res.next = ListNode(carry%10)
          pivot_res = pivot_res.next
          carry //= 10
      
      if carry == 1:
          pivot_res.next = ListNode(1)
          
      return res.next
              