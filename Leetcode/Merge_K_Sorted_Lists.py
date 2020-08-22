# Solution 1 : Heap 사용
# Time Complexity : O(NlogK), Space Complexity : O(K)

# Solution 2 : list 두개끼리 merge.
# Time Complexity : O(Nlogk), Space Complexity : O(1)


class Solution:
    def mergeKLists_2(self, lists: List[ListNode]) -> ListNode:
        def mergeTwoList(first: ListNode, second: ListNode) -> ListNode:
            dummy = cur = ListNode(0)
            while first and second:
                if first.val > second.val:
                    cur.next, second = second, second.next
                else:
                    cur.next, first = first, first.next
                cur = cur.next
            if first:
                cur.next = first
            elif second:
                cur.next = second
            return dummy.next

        temp = []
        while lists or temp:
            if len(lists) > 1:
                temp.append(mergeTwoList(lists.pop(), lists.pop()))
            else:
                if not temp:
                    return lists[0]
                lists.extend(temp)
                temp = []
        return None

    def mergeKLists_1(self, lists):
        K = len(lists)
        heads, heap = [head for head in lists], []
        for i in range(K):
            if heads[i]:
                heapq.heappush(heap, (heads[i].val, i))

        ans = ListNode(0)
        ans_head = ans
        while heap:
            idx = heapq.heappop(heap)[1]
            ans.next = heads[idx]
            ans = ans.next
            heads[idx] = heads[idx].next
            if heads[idx]:
                heapq.heappush(heap, (heads[idx].val, idx))

        return ans_head.next
