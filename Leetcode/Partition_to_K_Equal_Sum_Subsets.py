# Solution : Backtracking + dfs.
# Time : O(k * 2^N), Space : O(N)


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        def partition(
            nums: List[int],
            visited: List[bool],
            k: int,
            target: int,
            cur: int,
            index: int,
        ) -> bool:
            if k == 1:
                return True
            if cur == target:
                return partition(nums, visited, k - 1, target, 0, 0)
            for i in range(index, len(nums)):
                if not visited[i] and target >= nums[i] + cur:
                    visited[i] = True
                    if partition(
                        nums, visited, k, target, cur + nums[i], i + 1
                    ):
                        return True
                    visited[i] = False
            return False

        if sum(nums) % k != 0:
            return False
        visited = [False] * len(nums)
        return partition(nums, visited, k, sum(nums) // k, 0, 0)
