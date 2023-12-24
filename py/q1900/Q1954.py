"""
 * 给你一个用无限二维网格表示的花园，每一个 整数坐标处都有一棵苹果树。整数坐标 (i, j) 处的苹果树有 |i| + |j| 个苹果。
 * 你将会买下正中心坐标是 (0, 0) 的一块 正方形土地 ，且每条边都与两条坐标轴之一平行。
 * 给你一个整数 neededApples ，请你返回土地的 最小周长 ，使得 至少 有 neededApples 个苹果在土地 里面或者边缘上。
 * |x| 的值定义为：
 * 1、如果 x >= 0 ，那么值为 x
 * 2、如果 x < 0 ，那么值为 -x
 * 提示：1 <= neededApples <= 10^15
 * 链接：https://leetcode.cn/problems/minimum-garden-perimeter-to-collect-enough-apples
"""


class Solution:

    def minimumPerimeter(self, neededApples: int) -> int:
        n = 1
        while 2 * n * (n + 1) * (2 * n + 1) < neededApples:
            n += 1
        return n * 8


if __name__ == '__main__':
    # 16
    print(Solution().minimumPerimeter(13))
    # 503968
    print(Solution().minimumPerimeter(10**15))
    # 8
    print(Solution().minimumPerimeter(1))
    # 5040
    print(Solution().minimumPerimeter(1000000000))
