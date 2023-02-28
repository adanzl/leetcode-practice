"""
 * 传送带上的包裹必须在 days 天内从一个港口运送到另一个港口。
 * 传送带上的第 i 个包裹的重量为 weights[i]。每一天，我们都会按给出重量（weights）的顺序往传送带上装载包裹。我们装载的重量不会超过船的最大运载重量。
 * 返回能在 days 天内将传送带上的所有包裹送达的船的最低运载能力。
 * 提示：
 * 1、1 <= days <= weights.length <= 5 * 10^4
 * 2、1 <= weights[i] <= 500
 * 链接：https://leetcode.cn/problems/capacity-to-ship-packages-within-d-days/
"""
from typing import List


class Solution:

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        n = len(weights)
        l, r = 0, 0
        ans = 0
        pre_sum = [0] * (n + 1)
        for i in range(n):
            pre_sum[i + 1] = pre_sum[i] + weights[i]
            l = max(l, weights[i])
            r += weights[i]
        while l <= r:
            mid = (l + r) // 2
            sm, d = 0, 1
            for w in weights:
                if sm + w > mid:
                    d += 1
                    sm = 0
                sm += w
                if d > days:
                    break
            if d <= days:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans


if __name__ == '__main__':
    # 15
    print(Solution().shipWithinDays([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], days=5))
    # 6
    print(Solution().shipWithinDays([3, 2, 2, 4, 1, 4], days=3))
    # 3
    print(Solution().shipWithinDays([1, 2, 3, 1, 1], days=4))
