# Solution 1 : Hash + Heap. (Time : O(NlogN), Space : O(N))
# Solution 2 : Hash 두개 사용. (Time : O(N), Space : O(N))

from collections import Counter, defaultdict


class Solution:
    def topKFrequent_2(self, nums: List[int], k: int) -> List[int]:
        val_to_cnt, cnt_to_val = defaultdict(int), defaultdict(list)
        for num in nums:
            val_to_cnt[num] += 1

        for val, cnt in val_to_cnt.items():
            cnt_to_val[cnt].append(val)

        ans = []
        for cnt in reversed(range(len(nums) + 1)):
            if cnt in cnt_to_val:
                for val in cnt_to_val[cnt]:
                    ans.append(val)
                    k -= 1
                    if k == 0:
                        return ans
        return ans

    def topKFrequent_1(self, nums: List[int], k: int) -> List[int]:
        return [e[0] for e in Counter(nums).most_common(k)]

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash, heap, ans = defaultdict(int), [], []
        for num in nums:
            hash[num] += 1
        for val, cnt in hash.items():
            heapq.heappush(heap, (-cnt, val))
        for i in range(k):
            ans.append(heapq.heappop(heap)[1])
        return ans
