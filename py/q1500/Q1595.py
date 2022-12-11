"""
 * 给你两组点，其中第一组中有 size1 个点，第二组中有 size2 个点，且 size1 >= size2 。
 * 任意两点间的连接成本 cost 由大小为 size1 x size2 矩阵给出，其中 cost[i][j] 是第一组中的点 i 和第二组中的点 j 的连接成本。
 * 如果两个组中的每个点都与另一组中的一个或多个点连接，则称这两组点是连通的。换言之，第一组中的每个点必须至少与第二组中的一个点连接，且第二组中的每个点必须至少与第一组中的一个点连接。
 * 返回连通两组点所需的最小成本。
 * 提示：
 * 1、size1 == cost.length
 * 2、size2 == cost[i].length
 * 3、1 <= size1, size2 <= 12
 * 4、size1 >= size2
 * 5、0 <= cost[i][j] <= 100
 * 链接：https://leetcode.cn/problems/minimum-cost-to-connect-two-groups-of-points/
"""
from functools import cache
from typing import List


class Solution:

    def connectTwoGroups(self, cost: List[List[int]]) -> int:
        # 二分图，状态压缩 dp[i][j] 前i行，列的覆盖情况为j时，最小花费
        # 上下限最大流 https://blog.51cto.com/u_15346204/3737363
        s1, s2 = len(cost), len(cost[0])

        @cache
        def f(idx, state):
            if idx < 0: return 0 if state == 0 else 0x3c3c3c3c
            ret = 0x3c3c3c3c
            for i in range(s2):
                if 1 << i & state == 0: continue  # 不在state里
                ret = min(ret, cost[idx][i] + f(idx, state & ~(1 << i)))  # 重复添加，idx处理过state-1，idx的边是额外的
                ret = min(ret, cost[idx][i] + f(idx - 1, state))  # 重复添加，idx-1已经处理过state，idx的边是额外的
                ret = min(ret, cost[idx][i] + f(idx - 1, state & ~(1 << i)))  # 不重复
            return ret

        return f(s1 - 1, (1 << s2) - 1)


if __name__ == '__main__':
    # 33
    print(Solution().connectTwoGroups([[20, 21, 22], [1, 10, 11], [1, 10, 11]]))
    # 17
    print(Solution().connectTwoGroups([[15, 96], [36, 2]]))
    # 4
    print(Solution().connectTwoGroups([[1, 3, 5], [4, 1, 1], [1, 5, 3]]))
    # 10
    print(Solution().connectTwoGroups([[2, 5, 1], [3, 4, 7], [8, 1, 2], [6, 2, 4], [3, 8, 8]]))
    # 242
    print(Solution().connectTwoGroups([[64, 30, 99, 80, 100], [97, 61, 12, 65, 30], [84, 15, 58, 74, 11], [98, 52, 100, 66, 59], [83, 58, 56, 55, 32], [91, 44, 89, 48, 84], [40, 90, 2, 27, 63],
                                       [61, 35, 59, 16, 54], [11, 0, 97, 86, 7], [93, 3, 95, 77, 90], [69, 29, 96, 79, 51]]))
