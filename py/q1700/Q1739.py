"""
 * 有一个立方体房间，其长度、宽度和高度都等于 n 个单位。请你在房间里放置 n 个盒子，每个盒子都是一个单位边长的立方体。放置规则如下：
 * 1、你可以把盒子放在地板上的任何地方。
 * 2、如果盒子 x 需要放置在盒子 y 的顶部，那么盒子 y 竖直的四个侧面都 必须 与另一个盒子或墙相邻。
 * 给你一个整数 n ，返回接触地面的盒子的 最少 可能数量。
 * 提示：1 <= n <= 10^9
 * 链接：https://leetcode.cn/problems/building-boxes/
"""


class Solution:

    def minimumBoxes(self, n: int) -> int:
        sm, layer, nx = 0, 0, 0
        while sm + nx <= n:
            layer += 1
            sm += nx
            nx = layer * (layer + 1) // 2
        r = 0
        for i in range(0, 10**9):
            if i * (i + 1) // 2 >= n - sm:
                r = i
                break
        return layer * (layer - 1) // 2 + r


if __name__ == '__main__':
    # 34
    print(Solution().minimumBoxes(103))
    # 3
    print(Solution().minimumBoxes(3))
    # 1650467
    print(Solution().minimumBoxes(10**9))
    # 6
    print(Solution().minimumBoxes(10))