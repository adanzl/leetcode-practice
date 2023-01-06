"""
 * 夏日炎炎，小男孩 Tony 想买一些雪糕消消暑。
 * 商店中新到 n 支雪糕，用长度为 n 的数组 costs 表示雪糕的定价，其中 costs[i] 表示第 i 支雪糕的现金价格。
 * Tony 一共有 coins 现金可以用于消费，他想要买尽可能多的雪糕。
 * 给你价格数组 costs 和现金量 coins ，请你计算并返回 Tony 用 coins 现金能够买到的雪糕的 最大数量 。
 * 注意：Tony 可以按任意顺序购买雪糕。
 * 提示：
 * 1、costs.length == n
 * 2、1 <= n <= 10^5
 * 3、1 <= costs[i] <= 10^5
 * 4、1 <= coins <= 10^8
 * 链接：https://leetcode.cn/problems/maximum-ice-cream-bars/
"""
from typing import List


class Solution:

    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        ans = 0
        for c in costs:
            if coins < c: break
            else:
                coins -= c
                ans += 1
        return ans


if __name__ == '__main__':
    # 4
    print(Solution().maxIceCream([1, 3, 2, 4, 1], 7))
    # 0
    print(Solution().maxIceCream([10, 6, 8, 7, 7, 8], 5))
    # 6
    print(Solution().maxIceCream([1, 6, 3, 1, 2, 5], 20))
