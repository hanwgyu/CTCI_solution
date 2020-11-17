# 가장 높이가 큰것부터 팔면됨.
# sorting 한후 가장 높은 블록의 갯수 및 그다음 높은 블록의 높이 차이를 업데이트하면서 계산
# Time : O(NlogN), Space : O(1)


class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        ans = 0
        inventory.sort(reverse=True)
        n = 1
        while orders > 0:
            while n < len(inventory) and inventory[0] == inventory[n]:
                n += 1
            diff = inventory[0] - inventory[n] if n < len(inventory) else inventory[0]
            if n * diff > orders:
                d, r = divmod(orders, n)
                ans += n * d * (inventory[0] + inventory[0] - d + 1) // 2 + r * (inventory[0] - d)
                break
            ans += diff * n * (inventory[0] + inventory[0] - diff + 1) // 2
            inventory[0] -= diff
            orders -= n * diff
        return ans % (pow(10, 9) + 7)
