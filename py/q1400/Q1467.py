"""
 * 桌面上有 2n 个颜色不完全相同的球，球上的颜色共有 k 种。给你一个大小为 k 的整数数组 balls ，其中 balls[i] 是颜色为 i 的球的数量。
 * 所有的球都已经 随机打乱顺序 ，前 n 个球放入第一个盒子，后 n 个球放入另一个盒子（请认真阅读示例 2 的解释部分）。
 * 注意：这两个盒子是不同的。例如，两个球颜色分别为 a 和 b，盒子分别为 [] 和 ()，那么 [a] (b) 和 [b] (a) 这两种分配方式是不同的（请认真阅读示例的解释部分）。
 * 请返回「两个盒子中球的颜色数相同」的情况的概率。答案与真实值误差在 10^-5 以内，则被视为正确答案
 * 提示：
 * 1、1 <= balls.length <= 8
 * 2、1 <= balls[i] <= 6
 * 3、sum(balls) 是偶数
 * 链接：https://leetcode.cn/problems/probability-of-a-two-boxes-having-the-same-number-of-distinct-balls/
"""
from functools import cache
from typing import List
from math import comb


class Solution:

    def getProbability(self, balls: List[int]) -> float:
        s, l = sum(balls), len(balls)  # 球总数 颜色总数

        @cache
        def dfs(i, c, t):  # 当前处理的颜色，已选球数量，两组球颜色差值
            if i == l:  # 如果颜色选完了
                return int(t == 0 and c == s // 2)  # 选了1/2的球数量且颜色无变化
            # 不选和全选组合数都为1，直接相加即可，需要更新颜色变化
            res = dfs(i + 1, c, t + 1) + dfs(i + 1, c + balls[i], t - 1)
            for j in range(1, balls[i]):  # 其他情况，颜色无变化
                res += dfs(i + 1, c + j, t) * comb(balls[i], j)
            return res

        return dfs(0, 0, 0) / comb(s, s // 2)


if __name__ == '__main__':
    # 1.0
    print(Solution().getProbability([1, 1]))
    # 0.667
    print(Solution().getProbability([2, 1, 1]))
    # 0.6
    print(Solution().getProbability([1, 2, 1, 2]))
