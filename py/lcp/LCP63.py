"""
 * 欢迎各位来到「力扣嘉年华」，接下来将为各位介绍在活动中广受好评的弹珠游戏。
 * N*M 大小的弹珠盘的初始状态信息记录于一维字符串型数组 plate 中，数组中的每个元素为仅由 "O"、"W"、"E"、"." 组成的字符串。其中：
 * 1、"O" 表示弹珠洞（弹珠到达后会落入洞中，并停止前进）；
 * 2、"W" 表示逆时针转向器（弹珠经过时方向将逆时针旋转 90 度）；
 * 3、"E" 表示顺时针转向器（弹珠经过时方向将顺时针旋转 90 度）；
 * 4、"." 表示空白区域（弹珠可通行）。
 * 游戏规则要求仅能在边缘位置的 空白区域 处（弹珠盘的四角除外）沿 与边缘垂直 的方向打入弹珠，并且打入后的每颗弹珠最多能 前进 num 步。
 * 请返回符合上述要求且可以使弹珠最终入洞的所有打入位置。你可以 按任意顺序 返回答案。
 * 注意：若弹珠已到达弹珠盘边缘并且仍沿着出界方向继续前进，则将直接出界。
 * 提示：
 * 1、1 <= num <= 10^6
 * 2、1 <= plate.length, plate[i].length <= 1000
 * 3、plate[i][j] 仅包含 "O"、"W"、"E"、"."
 * 链接：https://leetcode.cn/problems/EXvqDp/
 * 链接：https://leetcode.cn/contest/season/2022-fall/problems/EXvqDp/
"""

from typing import *


class Solution:

    def ballGame(self, num: int, plate: List[str]) -> List[List[int]]:
        m, n = len(plate), len(plate[0])
        mem = dict()  # (x,y,d)-min
        INF = 0x3c3c3c3c
        # dir u-l-d-r 0-1-2-3 anticlockwise
        dirs = [[-1, 0], [0, -1], [1, 0], [0, 1]]

        def func(x, y, d, vis):
            k = (x, y, d)
            if k in vis: return INF
            if x < 0 or y < 0 or x > m - 1 or y > n - 1: return INF
            if k in mem:
                return mem[k]
            c = plate[x][y]
            vis.add(k)
            if c == 'O':
                mem[k] = 0
            else:
                if c == '.':
                    nd = d
                elif c == 'W':
                    nd = (d + 1) % 4
                elif c == 'E':
                    nd = (d + 3) % 4
                v = func(x + dirs[nd][0], y + dirs[nd][1], nd, vis)
                if v is INF:
                    mem[k] = INF
                else:
                    mem[k] = v + 1
            vis.remove(k)
            return mem[k]

        ans = []
        for i in range(1, m - 1):
            if plate[i][0] == '.' and func(i, 0, 3, set()) <= num:
                ans.append([i, 0])
            if plate[i][n - 1] == '.' and func(i, n - 1, 1, set()) <= num:
                ans.append([i, n - 1])
        for i in range(1, n - 1):
            if plate[0][i] == '.' and func(0, i, 2, set()) <= num:
                ans.append([0, i])
            if plate[m - 1][i] == '.' and func(m - 1, i, 0, set()) <= num:
                ans.append([m - 1, i])

        return ans


if __name__ == '__main__':
    # [[2,1]]
    print(Solution().ballGame(4, ["..E.", ".EOW", "..W."]))
    # [[0,1],[1,0],[2,4],[3,2]]
    print(Solution().ballGame(5, [".....", "..E..", ".WO..", "....."]))
    # []
    print(Solution().ballGame(3, [".....", "....O", "....O", "....."]))
