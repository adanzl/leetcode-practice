"""
 * 现有 n 个机器人，编号从 1 开始，每个机器人包含在路线上的位置、健康度和移动方向。
 * 给你下标从 0 开始的两个整数数组 positions、healths 和一个字符串 directions（directions[i] 为 'L' 表示 向左 或 'R' 表示 向右）。 
 * positions 中的所有整数 互不相同 。
 * 所有机器人以 相同速度 同时 沿给定方向在路线上移动。如果两个机器人移动到相同位置，则会发生 碰撞 。
 * 如果两个机器人发生碰撞，则将 健康度较低 的机器人从路线中 移除 ，并且另一个机器人的健康度 减少 1 。
 * 幸存下来的机器人将会继续沿着与之前 相同 的方向前进。如果两个机器人的健康度相同，则将二者都从路线中移除。
 * 请你确定全部碰撞后幸存下的所有机器人的 健康度 ，并按照原来机器人编号的顺序排列。
 * 即机器人 1 （如果幸存）的最终健康度，机器人 2 （如果幸存）的最终健康度等。 如果不存在幸存的机器人，则返回空数组。
 * 在不再发生任何碰撞后，请你以数组形式，返回所有剩余机器人的健康度（按机器人输入中的编号顺序）。
 * 注意：位置  positions 可能是乱序的。
 * 提示：
 * 1、1 <= positions.length == healths.length == directions.length == n <= 10^5
 * 2、1 <= positions[i], healths[i] <= 10^9
 * 3、directions[i] == 'L' 或 directions[i] == 'R'
 * 4、positions 中的所有值互不相同
 * 链接：https://leetcode.cn/problems/robot-collisions/
"""
from typing import List

#
# @lc app=leetcode.cn id=2751 lang=python3
#


# @lc code=start
class Solution:

    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        ans = []
        s = []  # [health]
        for _, h, d, i in sorted([[p, h, d, i] for i, (p, h, d) in enumerate(zip(positions, healths, directions))]):
            if d == 'L':
                while s and h:
                    lst = s.pop()
                    if lst[1] < h:
                        h -= 1  # type: ignore
                    elif lst[1] == h:
                        h = 0
                    else:
                        h = 0
                        if lst[1] > 0:
                            s.append([lst[0], lst[1] - 1])

                if h:
                    ans.append([i, h])
            else:
                s.append([i, h])
        return [v for _, v in sorted(ans + s)]  # type: ignore


# @lc code=end

if __name__ == '__main__':
    # [2,17,9,15,10]
    print(Solution().survivedRobotsHealths([5, 4, 3, 2, 1], healths=[2, 17, 9, 15, 10], directions="RRRRR"))
    # [14]
    print(Solution().survivedRobotsHealths([3, 5, 2, 6], healths=[10, 10, 15, 12], directions="RLRL"))
    # []
    print(Solution().survivedRobotsHealths([1, 2, 5, 6], healths=[10, 10, 11, 11], directions="RLRL"))
