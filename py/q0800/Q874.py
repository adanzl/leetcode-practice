"""
 * 机器人在一个无限大小的 XY 网格平面上行走，从点 (0, 0) 处开始出发，面向北方。该机器人可以接收以下三种类型的命令 commands ：
 * 1、-2 ：向左转 90 度
 * 2、-1 ：向右转 90 度
 * 3、1 <= x <= 9 ：向前移动 x 个单位长度
 * 在网格上有一些格子被视为障碍物 obstacles 。第 i 个障碍物位于网格点  obstacles[i] = (xi, yi) 。
 * 机器人无法走到障碍物上，它将会停留在障碍物的前一个网格方块上，但仍然可以继续尝试进行该路线的其余部分。
 * 返回从原点到机器人所有经过的路径点（坐标为整数）的最大欧式距离的平方。（即，如果距离为 5 ，则返回 25 ）
 * 注意：
 * 1、北表示 +Y 方向。
 * 2、东表示 +X 方向。
 * 3、南表示 -Y 方向。
 * 4、西表示 -X 方向。
 * 提示：
 * 1、1 <= commands.length <= 10^4
 * 2、commands[i] is one of the values in the list [-2,-1,1,2,3,4,5,6,7,8,9].
 * 3、0 <= obstacles.length <= 10^4
 * 4、-3 * 10^4 <= xi, yi <= 3 * 10^4
 * 5、答案保证小于 2^31
 * 链接：https://leetcode.cn/problems/walking-robot-simulation/
"""
from typing import List


class Solution:

    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        o = set([(x, y) for x, y in obstacles])
        ans = 0
        p, d = (0, 0), 0
        step = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        for c in commands:
            if c == -2:
                d = (d + 3) % 4
            elif c == -1:
                d = (d + 1) % 4
            else:
                while c:
                    np = (p[0] + step[d][0], p[1] + step[d][1])
                    if np in o:
                        break
                    c -= 1
                    p = np
                ans = max(ans, p[0]**2 + p[1]**2)
        return ans


if __name__ == '__main__':
    # 65
    print(Solution().robotSim([4, -1, 4, -2, 4], obstacles=[[2, 4]]))
    # 25
    print(Solution().robotSim([4, -1, 3], obstacles=[]))
    #
    # print(Solution().robotSim())