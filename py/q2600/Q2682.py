"""
 * n 个朋友在玩游戏。这些朋友坐成一个圈，按 顺时针方向 从 1 到 n 编号。从第 i 个朋友的位置开始顺时针移动 1 步会到达第 (i + 1) 个朋友的位置（1 <= i < n），而从第 n 个朋友的位置开始顺时针移动 1 步会回到第 1 个朋友的位置。
 * 游戏规则如下：
 * 第 1 个朋友接球。
 * 1、接着，第 1 个朋友将球传给距离他顺时针方向 k 步的朋友。
 * 2、然后，接球的朋友应该把球传给距离他顺时针方向 2 * k 步的朋友。
 * 3、接着，接球的朋友应该把球传给距离他顺时针方向 3 * k 步的朋友，以此类推。
 * 换句话说，在第 i 轮中持有球的那位朋友需要将球传递给距离他顺时针方向 i * k 步的朋友。
 * 当某个朋友第 2 次接到球时，游戏结束。
 * 在整场游戏中没有接到过球的朋友是 输家 。
 * 给你参与游戏的朋友数量 n 和一个整数 k ，请按升序排列返回包含所有输家编号的数组 answer 作为答案。
 * 提示：1 <= k <= n <= 50
 * 链接：https://leetcode.cn/problems/find-the-losers-of-the-circular-game/
"""
from typing import List


class Solution:

    def circularGameLosers(self, n: int, k: int) -> List[int]:
        vis = set()
        nx = 1
        idx = 1
        while nx not in vis:
            vis.add(nx)
            nx = (nx - 1 + k * idx) % n + 1
            idx += 1

        return sorted(list(set([v for v in range(1, n + 1)]) - vis))


if __name__ == '__main__':
    # [2,4,6,8]
    print(Solution().circularGameLosers(8, k=2))
    # [4, 5]
    print(Solution().circularGameLosers(5, k=2))
    # [2, 3, 4]
    print(Solution().circularGameLosers(4, k=4))
