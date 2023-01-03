"""
 * 有一只跳蚤的家在数轴上的位置 x 处。请你帮助它从位置 0 出发，到达它的家。
 * 跳蚤跳跃的规则如下：
 * 1、它可以 往前 跳恰好 a 个位置（即往右跳）。
 * 2、它可以 往后 跳恰好 b 个位置（即往左跳）。
 * 3、它不能 连续 往后跳 2 次。
 * 4、它不能跳到任何 forbidden 数组中的位置。
 * 跳蚤可以往前跳 超过 它的家的位置，但是它 不能跳到负整数 的位置。
 * 给你一个整数数组 forbidden ，其中 forbidden[i] 是跳蚤不能跳到的位置，同时给你整数 a， b 和 x ，请你返回跳蚤到家的最少跳跃次数。如果没有恰好到达 x 的可行方案，请你返回 -1 。
 * 提示：
 * 1、1 <= forbidden.length <= 1000
 * 2、1 <= a, b, forbidden[i] <= 2000
 * 3、0 <= x <= 2000
 * 4、forbidden 中所有位置互不相同。
 * 5、位置 x 不在 forbidden 中。
 * 链接：https://leetcode.cn/problems/minimum-jumps-to-reach-home/description/
"""
from typing import List

class Solution:

    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        # bfs，用标记为来区分是向右移动还是向左移动，如果是从向左移动过来的节点，则不能再次向左移动
        LIMIT = 10000
        vis = set()
        for f in forbidden:
            vis.add((f, 1))
            vis.add((f, -1))
        q = [(0, 1)]
        ans = 0
        while q:
            nex = []
            for i, f in q:
                if i == x: return ans
                if i + a < LIMIT and (i + a, 1) not in vis:
                    vis.add((i + a, 1))
                    nex.append((i + a, 1))
                if f == 1 and i - b >= 0 and (i - b, -1) not in vis:
                    vis.add((i - b, -1))
                    nex.append((i - b, -1))
            q = nex
            ans += 1
        return -1

if __name__ == '__main__':
    # 121
    print(Solution().minimumJumps([
        162, 118, 178, 152, 167, 100, 40, 74, 199, 186, 26, 73, 200, 127, 30, 124, 193, 84, 184, 36, 103, 149, 153, 9, 54, 154, 133, 95, 45, 198, 79, 157, 64, 122, 59, 71, 48, 177, 82, 35, 14, 176,
        16, 108, 111, 6, 168, 31, 134, 164, 136, 72, 98
    ], 29, 98, 80))
    # 2
    print(Solution().minimumJumps([1, 6, 2, 14, 5, 17, 4], a=16, b=9, x=7))
    # 3
    print(Solution().minimumJumps([14, 4, 18, 1, 15], a=3, b=15, x=9))
    # -1
    print(Solution().minimumJumps([8, 3, 16, 6, 12, 20], a=15, b=13, x=11))
