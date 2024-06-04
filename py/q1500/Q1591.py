"""
 * 给你一个奇怪的打印机，它有如下两个特殊的打印规则：
 * 1、每一次操作时，打印机会用同一种颜色打印一个矩形的形状，每次打印会覆盖矩形对应格子里原本的颜色。
 * 2、一旦矩形根据上面的规则使用了一种颜色，那么 相同的颜色不能再被使用 。
 * 给你一个初始没有颜色的 m x n 的矩形 targetGrid ，其中 targetGrid[row][col] 是位置 (row, col) 的颜色。
 * 如果你能按照上述规则打印出矩形 targetGrid ，请你返回 true ，否则返回 false 。
 * 提示：
 * 1、m == targetGrid.length
 * 2、n == targetGrid[i].length
 * 3、1 <= m, n <= 60
 * 4、1 <= targetGrid[row][col] <= 60
 * 链接：https://leetcode.cn/problems/strange-printer-ii/
"""

from collections import defaultdict
from typing import Counter, Deque, List

#
# @lc app=leetcode.cn id=1591 lang=python3
#
# [1591] 奇怪的打印机 II
#


# @lc code=start
class Solution:

    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        m, n = len(targetGrid), len(targetGrid[0])
        pos = defaultdict(lambda: [n, 0, m, 0])  # l r u d
        for i in range(m):
            for j in range(n):
                nn = targetGrid[i][j]
                pos[nn][0] = min(pos[nn][0], j)
                pos[nn][1] = max(pos[nn][1], j)
                pos[nn][2] = min(pos[nn][2], i)
                pos[nn][3] = max(pos[nn][3], i)
        g_pre = defaultdict(set)
        cnt = Counter()
        for i in range(m):
            for j in range(n):
                nn = targetGrid[i][j]
                for k, v in pos.items():
                    if k == nn: continue
                    if v[0] <= j <= v[1] and v[2] <= i <= v[3]:
                        if k not in g_pre[nn]:
                            cnt[k] += 1
                            g_pre[nn].add(k)
        q = Deque([v for v in pos if cnt[v] == 0])
        tot = len(pos)
        while q:
            v = q.popleft()
            tot -= 1
            for pr in g_pre[v]:
                cnt[pr] -= 1
                if cnt[pr] == 0:
                    q.append(pr)
        return tot == 0


# @lc code=end

if __name__ == '__main__':
    # True
    print(Solution().isPrintable([[1, 1, 1, 1], [1, 1, 3, 3], [1, 1, 3, 4], [5, 5, 1, 4]]))
    # False
    print(Solution().isPrintable([[5, 1, 5, 3, 5], [4, 4, 4, 3, 4], [5, 1, 5, 3, 5], [2, 1, 2, 2, 2], [5, 1, 5, 3, 5]]))
    # True
    print(Solution().isPrintable([[1, 1, 1, 1], [1, 2, 2, 1], [1, 2, 2, 1], [1, 1, 1, 1]]))
    # False
    print(Solution().isPrintable([[1, 2, 1], [2, 1, 2], [1, 2, 1]]))
    # False
    print(Solution().isPrintable([[1, 1, 1], [3, 1, 3]]))
