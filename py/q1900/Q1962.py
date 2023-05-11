"""
 * 给你一个整数数组 piles ，数组 下标从 0 开始 ，其中 piles[i] 表示第 i 堆石子中的石子数量。另给你一个整数 k ，请你执行下述操作 恰好 k 次：
 * 选出任一石子堆 piles[i] ，并从中 移除 floor(piles[i] / 2) 颗石子。
 * 注意：你可以对 同一堆 石子多次执行此操作。
 * 返回执行 k 次操作后，剩下石子的 最小 总数。
 * floor(x) 为 小于 或 等于 x 的 最大 整数。（即，对 x 向下取整）。
 * 提示：
 * 1、1 <= piles.length <= 10^5
 * 2、1 <= piles[i] <= 10^4
 * 3、1 <= k <= 10^5
 * 链接：https://leetcode.cn/problems/remove-stones-to-minimize-the-total/
"""
from heapq import heapify, heappop, heappush
from typing import List


class Solution:

    def minStoneSum(self, piles: List[int], k: int) -> int:
        ans = sum(piles)
        q = [-x for x in piles]
        heapify(q)
        while k:
            c = heappop(q)
            ans -= abs(c) // 2
            heappush(q, c // 2)
            k -= 1
        return ans


if __name__ == '__main__':
    # 12
    print(Solution().minStoneSum([5, 4, 9], 2))
    # 12
    print(Solution().minStoneSum([4, 3, 6, 7], 3))
