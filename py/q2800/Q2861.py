"""
 * 假设你是一家合金制造公司的老板，你的公司使用多种金属来制造合金。现在共有 n 种不同类型的金属可以使用，并且你可以使用 k 台机器来制造合金。
 * 每台机器都需要特定数量的每种金属来创建合金。
 * 对于第 i 台机器而言，创建合金需要 composition[i][j] 份 j 类型金属。
 * 最初，你拥有 stock[i] 份 i 类型金属，而每购入一份 i 类型金属需要花费 cost[i] 的金钱。
 * 给你整数 n、k、budget，下标从 1 开始的二维数组 composition，两个下标从 1 开始的数组 stock 和 cost，
 * 请你在预算不超过 budget 金钱的前提下，最大化 公司制造合金的数量。
 * 所有合金都需要由同一台机器制造。
 * 返回公司可以制造的最大合金数。
 * 提示：
 * 1、1 <= n, k <= 100
 * 2、0 <= budget <= 10^8
 * 3、composition.length == k
 * 4、composition[i].length == n
 * 5、1 <= composition[i][j] <= 100
 * 6、stock.length == cost.length == n
 * 7、0 <= stock[i] <= 10^8
 * 8、1 <= cost[i] <= 100
 * 链接：https://leetcode.cn/problems/maximum-number-of-alloys/
"""
from typing import List


class Solution:

    def maxNumberOfAlloys(self, n: int, k: int, budget: int, composition: List[List[int]], stock: List[int], cost: List[int]) -> int:
        ans = 0
        for ori in composition:
            l, r = 0, 10**10
            vv = 0
            while l <= r:
                mid = (l + r) // 2
                ss = 0
                for i in range(n):  # i type
                    ss += max(0, mid * ori[i] - stock[i]) * cost[i]
                    if ss > budget: break
                if ss <= budget:
                    l = mid + 1
                    vv = mid
                else:
                    r = mid - 1
            ans = max(ans, vv)
        return ans


if __name__ == '__main__':
    # 1
    print(Solution().maxNumberOfAlloys(4, 4, 17, [[10, 10, 1, 5], [9, 7, 7, 1], [6, 3, 5, 9], [2, 10, 2, 7]], [9, 8, 2, 7], [9, 2, 6, 10]))
    # 2
    print(Solution().maxNumberOfAlloys(3, k=2, budget=15, composition=[[1, 1, 1], [1, 1, 10]], stock=[0, 0, 0], cost=[1, 2, 3]))
    # 5
    print(Solution().maxNumberOfAlloys(3, k=2, budget=15, composition=[[1, 1, 1], [1, 1, 10]], stock=[0, 0, 100], cost=[1, 2, 3]))
    # 2
    print(Solution().maxNumberOfAlloys(2, k=3, budget=10, composition=[[2, 1], [1, 2], [1, 1]], stock=[1, 1], cost=[5, 5]))
