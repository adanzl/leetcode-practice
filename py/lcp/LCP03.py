"""
 * 力扣团队买了一个可编程机器人，机器人初始位置在原点(0, 0)。
 * 小伙伴事先给机器人输入一串指令command，机器人就会无限循环这条指令的步骤进行移动。
 * 指令有两种：
 * 1、U: 向y轴正方向移动一格
 * 2、R: 向x轴正方向移动一格。
 * 不幸的是，在 xy 平面上还有一些障碍物，他们的坐标用obstacles表示。机器人一旦碰到障碍物就会被损毁。
 * 给定终点坐标(x, y)，返回机器人能否完好地到达终点。如果能，返回true；否则返回false。
 * 限制：
 * 1、2 <= command的长度 <= 1000
 * 2、command由U，R构成，且至少有一个U，至少有一个R
 * 3、0 <= x <= 1e9, 0 <= y <= 1e9
 * 4、0 <= obstacles的长度 <= 1000
 * 5、obstacles[i]不为原点或者终点
 * 链接：https://leetcode.cn/problems/programmable-robot/
"""

from itertools import cycle
from typing import Counter, List

INF = 0x3c3c3c3c3c3c3c3c3c

#
# @lc app=leetcode.cn id=LCP 03 lang=python3
# @lcpr version=20002
#
# [LCP 03] 机器人大冒险
#


# @lc code=start
class Solution:

    def robot(self, command: str, obstacles: List[List[int]], x: int, y: int) -> bool:
        o = set([(x, y) for x, y in obstacles])
        cnt = Counter(command)
        cx, cy = cnt['R'], cnt['U']
        xx, yy = 0, 0
        for c in command:
            if c == 'U':
                yy += 1
            else:
                xx += 1
            if (xx, yy) in o:
                return False
            if (x - xx) == 0 and (y - yy) == 0:
                return True

        xx, yy = 0, 0
        lose_s, win_s = [INF, INF], [INF, INF]
        for i, c in enumerate(command):
            if c == 'U':
                yy += 1
            else:
                xx += 1
            for oo in o:
                if (oo[0] - xx) % cx == 0 and (oo[1] - yy) % cy == 0 and (oo[0] - xx) // cx == (oo[1] - yy) // cy:
                    lose_s = min(lose_s, [max((oo[0] - xx) // cx, (oo[1] - yy) // cy), i])
            if (x - xx) % cx == 0 and (y - yy) % cy == 0 and (x - xx) // cx == (y - yy) // cy:
                win_s = min(win_s, [max((x - xx) // cx, (y - yy) // cy), i])
        return win_s < lose_s


# @lc code=end

if __name__ == '__main__':
    # False
    print(Solution().robot("RU", [[9, 7], [7, 4], [9, 2]], 9527, 679))
    # True
    print(Solution().robot("URRURRR", [[7, 7], [0, 5], [2, 7], [8, 6], [8, 7], [6, 5], [4, 4], [0, 3], [3, 6]],
                           x=4915,
                           y=1966))
    # True
    print(Solution().robot("URR", obstacles=[[4, 2]], x=3, y=2))
    # False
    print(Solution().robot("URR", obstacles=[[2, 2]], x=3, y=2))
    # True
    print(Solution().robot("URR", obstacles=[], x=3, y=2))
