"""
 * 在一根无限长的数轴上，你站在0的位置。终点在target的位置。
 * 你可以做一些数量的移动 numMoves :
 * 1、每次你可以选择向左或向右移动。
 * 2、第 i 次移动（从 i == 1 开始，到 i == numMoves ），在选择的方向上走 i 步。
 * 给定整数 target ，返回 到达目标所需的 最小 移动次数(即最小 numMoves ) 。
 * 提示:
 * 1、-10^9 <= target <= 10^9
 * 2、target != 0
 * 链接：https://leetcode.cn/problems/reach-a-number/
"""


class Solution:

    def reachNumber(self, target: int) -> int:
        target = abs(target)
        s = n = 0
        # 当总和超过target，切差值为偶数时，一定存在将中间一些数改为负数后使得整体和为target
        while s < target or (s - target) % 2:  # 没有到达（越过）终点，或者相距奇数
            n += 1
            s += n
        return n


if __name__ == '__main__':
    # 44723
    print(Solution().reachNumber(10**9))
    # 3
    print(Solution().reachNumber(2))
    # 2
    print(Solution().reachNumber(3))