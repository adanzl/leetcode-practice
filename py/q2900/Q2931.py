"""
 * 给你一个下标从 0 开始大小为 m * n 的整数矩阵 values ，表示 m 个不同商店里 m * n 件不同的物品。
 * 每个商店有 n 件物品，第 i 个商店的第 j 件物品的价值为 values[i][j] 。
 * 除此以外，第 i 个商店的物品已经按照价值非递增排好序了，也就是说对于所有 0 <= j < n - 1 都有 values[i][j] >= values[i][j + 1] 。
 * 每一天，你可以在一个商店里购买一件物品。具体来说，在第 d 天，你可以：
 * 1、选择商店 i 。
 * 2、购买数组中最右边的物品 j ，开销为 values[i][j] * d 。
 *    换句话说，选择该商店中还没购买过的物品中最大的下标 j ，并且花费 values[i][j] * d 去购买。
 * 注意，所有物品都视为不同的物品。比方说如果你已经从商店 1 购买了物品 0 ，你还可以在别的商店里购买其他商店的物品 0 。
 * 请你返回购买所有 m * n 件物品需要的 最大开销 。
 * 提示：
 * 1、1 <= m == values.length <= 10
 * 2、1 <= n == values[i].length <= 10^4
 * 3、1 <= values[i][j] <= 10^6
 * 4、values[i] 按照非递增顺序排序。
 * 链接：https://leetcode.cn/problems/maximum-spending-after-buying-items/
"""
from heapq import heappop, heappush
from typing import List


class Solution:

    def maxSpending(self, values: List[List[int]]) -> int:
        ans = 0
        h = []
        m, n = len(values), len(values[0])
        for i in range(m):
            heappush(h, [values[i][-1], i, n - 1])
        d = 1
        while h:
            v, i, j = heappop(h)
            ans += v * d
            if j > 0:
                heappush(h, [values[i][j - 1], i, j - 1])
            d += 1
        return ans


if __name__ == '__main__':
    # 285
    print(Solution().maxSpending([[8, 5, 2], [6, 4, 1], [9, 7, 3]]))
    # 386
    print(Solution().maxSpending([[10, 8, 6, 4, 2], [9, 7, 5, 3, 2]]))
