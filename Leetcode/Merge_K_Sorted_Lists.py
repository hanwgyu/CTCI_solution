class Solution(object):
    # Time Complexity : O(NlogK), Space Complexity : O(K)
    def mergeKLists(self, lists):
        K = len(lists)
        heads, heap = [head for head in lists], []
        for i in range(K):
            if heads[i]:
                heapq.heappush(heap, (heads[i].val ,i))
        
        ans = ListNode(0)
        ans_head = ans
        while heap:
            idx = heapq.heappop(heap)[1]
            ans.next = heads[idx]
            ans = ans.next
            heads[idx] = heads[idx].next
            if heads[idx]:
                heapq.heappush(heap, (heads[idx].val ,idx))
        
        return ans_head.next
