"""
 * 在一个 8x8 的棋盘上，放置着若干「黑皇后」和一个「白国王」。
 * 给定一个由整数坐标组成的数组 queens ，表示黑皇后的位置；以及一对坐标 king ，表示白国王的位置，返回所有可以攻击国王的皇后的坐标(任意顺序)。
 * 提示：
 * 1、1 <= queens.length <= 63
 * 2、queens[i].length == 2
 * 3、0 <= queens[i][j] < 8
 * 4、king.length == 2
 * 5、0 <= king[0], king[1] < 8
 * 6、一个棋盘格上最多只能放置一枚棋子。
 * 链接：https://leetcode.cn/problems/queens-that-can-attack-the-king
"""

from typing import List

#
# @lc app=leetcode.cn id=1222 lang=python3
#
# [1222] 可以攻击国王的皇后
#


# @lc code=start
class Solution:

    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        ans = {}
        for qx, qy in queens:
            dy, dx = king[0] - qx, king[1] - qy
            dis = abs(qx - king[0]) + abs(qy - king[1])

            if dy == 0:
                k = (dx / abs(dx), 0)
            elif dx == 0:
                k = (0, dy / abs(dy))
            elif abs(dy / dx) == 1:
                k = (dx / abs(dx), dy / abs(dy))
            else:
                continue
            if k not in ans:
                ans[k] = [dis, qx, qy]
            else:
                if dis < ans[k][0]:
                    ans[k] = [dis, qx, qy]

        return [[qx, qy] for d, qx, qy in ans.values()]


# @lc code=end

if __name__ == '__main__':
    # [[0,1],[1,0],[3,3]]
    print(Solution().queensAttacktheKing([[0, 1], [1, 0], [4, 0], [0, 4], [3, 3], [2, 4]], king=[0, 0]))
    # [[2,2],[3,4],[4,4]]
    print(Solution().queensAttacktheKing([[0, 0], [1, 1], [2, 2], [3, 4], [3, 5], [4, 4], [4, 5]], king=[3, 3]))
    # [[2,3],[1,4],[1,6],[3,7],[4,3],[5,4],[4,5]]
    print(Solution().queensAttacktheKing([[5, 6], [7, 7], [2, 1], [0, 7], [1, 6], [5, 1], [3, 7], [0, 3], [4, 0], [1, 2], [6, 3], [5, 0], [0, 4], [2, 2], [1, 1], [6, 4], [5, 4], [0, 0], [2, 6],
                                          [4, 5], [5, 2], [1, 4], [7, 5], [2, 3], [0, 5], [4, 2], [1, 0], [2, 7], [0, 1], [4, 6], [6, 1], [0, 6], [4, 3], [1, 7]],
                                         king=[3, 4]))
