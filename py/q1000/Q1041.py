"""
 * 在无限的平面上，机器人最初位于 (0, 0) 处，面朝北方。注意:
 * 1、北方向 是y轴的正方向。
 * 2、南方向 是y轴的负方向。
 * 3、东方向 是x轴的正方向。
 * 4、西方向 是x轴的负方向。
 * 机器人可以接受下列三条指令之一：
 * 1、"G"：直走 1 个单位
 * 2、"L"：左转 90 度
 * 3、"R"：右转 90 度
 * 机器人按顺序执行指令 instructions，并一直重复它们。
 * 只有在平面中存在环使得机器人永远无法离开时，返回 true。否则，返回 false。
 * 提示：
 * 1、1 <= instructions.length <= 100
 * 2、instructions[i] 仅包含 'G', 'L', 'R'
 * 链接：https://leetcode.cn/problems/robot-bounded-in-circle/
"""


class Solution:

    def isRobotBounded(self, instructions: str) -> bool:
        vis = set()
        d = 'N'  # 'N', 'E', 'S', 'W'
        p = (0, 0, d, -1)
        dirs = 'NESW'
        n = len(instructions)
        for i in range(n * 100):
            ii = i % n
            a = instructions[ii]
            if p in vis:
                return True
            # print(p)
            vis.add(p)
            if a == 'G':
                if d == 'N':
                    p = (p[0], p[1] + 1, d, ii)
                elif d == 'E':
                    p = (p[0] + 1, p[1], d, ii)
                elif d == 'S':
                    p = (p[0], p[1] - 1, d, ii)
                elif d == 'W':
                    p = (p[0] - 1, p[1], d, ii)
            elif a == 'L':
                d = dirs[(dirs.index(d) - 1 + 4) % 4]
                p = (p[0], p[1], d, ii)
            elif a == 'R':
                d = dirs[(dirs.index(d) + 1 + 4) % 4]
                p = (p[0], p[1], d, ii)
        return False


if __name__ == '__main__':
    # False
    print(Solution().isRobotBounded("GLGLGGLGL"))
    # True
    print(Solution().isRobotBounded("GL"))
    # True
    print(Solution().isRobotBounded("GGLLGG"))
    # False
    print(Solution().isRobotBounded("GG"))