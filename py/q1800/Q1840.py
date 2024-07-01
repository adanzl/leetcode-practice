"""
 * 在一座城市里，你需要建 n 栋新的建筑。这些新的建筑会从 1 到 n 编号排成一列。
 * 这座城市对这些新建筑有一些规定：
 * 1、每栋建筑的高度必须是一个非负整数。
 * 2、第一栋建筑的高度 必须 是 0 。
 * 3、任意两栋相邻建筑的高度差 不能超过  1 。
 * 除此以外，某些建筑还有额外的最高高度限制。
 * 这些限制会以二维整数数组 restrictions 的形式给出，其中 restrictions[i] = [id_i, maxHeight_i] ，
 * 表示建筑 idi 的高度 不能超过 maxHeight_i 。
 * 题目保证每栋建筑在 restrictions 中 至多出现一次 ，同时建筑 1 不会 出现在 restrictions 中。
 * 请你返回 最高 建筑能达到的 最高高度 。
 * 提示：
 * 2 <= n <= 10^9
 * 0 <= restrictions.length <= min(n - 1, 10^5)
 * 2 <= id_i <= n
 * id_i 是 唯一的 。
 * 0 <= maxHeight_i <= 10^9
 * 链接：https://leetcode.cn/problems/maximum-building-height/description/
"""

from typing import List

#
# @lc app=leetcode.cn id=1840 lang=python3
#
# [1840] 最高建筑高度
#


# @lc code=start
class Solution:

    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        rest = [[1, 0]] + sorted(restrictions) + [[n, n - 1]]
        v = 0
        ans = 0
        for i in range(len(rest) - 1):
            r0, r1 = rest[i], rest[i + 1]
            r1[1] = min(r1[1], r0[1] + r1[0] - r0[0])
        for i in range(len(rest) - 1, 0, -1):
            r0, r1 = rest[i - 1], rest[i]
            r0[1] = min(r0[1], r1[1] + (r1[0] - r0[0]))
        for i in range(len(rest) - 1):
            r0, r1 = rest[i], rest[i + 1]
            d = r1[1] - r0[1]
            h = r0[1] + (r1[0] - r0[0] + d) // 2
            ans = max(ans, h)
        return ans


# @lc code=end

if __name__ == '__main__':
    # 1
    print(Solution().maxBuilding(10, [[6, 0], [5, 2], [7, 0], [9, 1], [2, 4], [3, 4], [4, 0], [8, 2], [10, 0]]))
    # 5
    print(Solution().maxBuilding(6, restrictions=[]))
    # 5
    print(Solution().maxBuilding(10, restrictions=[[5, 3], [2, 5], [7, 4], [10, 3]]))
    # 2
    print(Solution().maxBuilding(5, restrictions=[[2, 1], [4, 1]]))
    # 2
    print(Solution().maxBuilding(10, [[8, 5], [9, 0], [6, 2], [4, 0], [3, 2], [10, 0], [5, 3], [7, 3], [2, 4]]))
