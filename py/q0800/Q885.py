"""
 * 在 rows x cols 的网格上，你从单元格 (rStart, cStart) 面朝东面开始。
 * 网格的西北角位于第一行第一列，网格的东南角位于最后一行最后一列。
 * 你需要以顺时针按螺旋状行走，访问此网格中的每个位置。
 * 每当移动到网格的边界之外时，需要继续在网格之外行走（但稍后可能会返回到网格边界）。
 * 最终，我们到过网格的所有 rows x cols 个空间。
 * 按照访问顺序返回表示网格位置的坐标列表。
 * 提示：
 * 1、1 <= rows, cols <= 100
 * 2、0 <= rStart < rows
 * 3、0 <= cStart < cols
 * 链接：https://leetcode.cn/problems/spiral-matrix-iii
"""

from typing import List

#
# @lc app=leetcode.cn id=885 lang=python3
#
# [885] 螺旋矩阵 III
#


# @lc code=start
class Solution:

    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        ans = []
        vis = [[0 for _ in range(cols)] for _ in range(rows)]
        cnt = rows * cols
        cur = [rStart, cStart]
        d = 0  # r d l u
        limit_l, limit_r = max(0, cStart - 1), min(cols - 1, cStart + 1)
        limit_u, limit_d = max(0, rStart - 1), min(rows - 1, rStart + 1)
        while len(ans) < cnt:
            if vis[cur[0]][cur[1]] == 0:
                ans.append([cur[0], cur[1]])
                vis[cur[0]][cur[1]] = 1
            if d == 0:  # r
                if cur[1] == limit_r:
                    d = (d + 1) % 4
                    limit_r = min(limit_r + 1, cols - 1)
                else:
                    cur[1] += 1
            elif d == 1:  # d
                if cur[0] == limit_d:
                    d = (d + 1) % 4
                    limit_d = min(limit_d + 1, rows - 1)
                else:
                    cur[0] += 1
            elif d == 2:  # l
                if cur[1] == limit_l:
                    d = (d + 1) % 4
                    limit_l = max(limit_l - 1, 0)
                else:
                    cur[1] -= 1
            else:  # u
                if cur[0] == limit_u:
                    d = (d + 1) % 4
                    limit_u = max(limit_u - 1, 0)
                else:
                    cur[0] -= 1
        return ans


# @lc code=end

if __name__ == '__main__':
    # [[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0],[2,0],[1,0],[0,0]]
    print(Solution().spiralMatrixIII(5, cols=6, rStart=1, cStart=4))
    # [[0,0],[0,1],[0,2],[0,3]]
    print(Solution().spiralMatrixIII(1, cols=4, rStart=0, cStart=0))
