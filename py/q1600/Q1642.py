"""
 * 给你一个整数数组 heights ，表示建筑物的高度。另有一些砖块 bricks 和梯子 ladders 。
 * 你从建筑物 0 开始旅程，不断向后面的建筑物移动，期间可能会用到砖块或梯子。
 * 当从建筑物 i 移动到建筑物 i+1（下标 从 0 开始 ）时：
 * 1、如果当前建筑物的高度 大于或等于 下一建筑物的高度，则不需要梯子或砖块
 * 2、如果当前建筑的高度 小于 下一个建筑的高度，您可以使用 一架梯子 或 (h[i+1] - h[i]) 个砖块
 * 3、如果以最佳方式使用给定的梯子和砖块，返回你可以到达的最远建筑物的下标（下标 从 0 开始 ）。
 * 提示：
 * 1、1 <= heights.length <= 10^5
 * 2、1 <= heights[i] <= 10^6
 * 3、0 <= bricks <= 10^9
 * 4、0 <= ladders <= heights.length
 * 链接：https://leetcode.cn/problems/furthest-building-you-can-reach
"""
from heapq import heappop, heappush
from typing import List


class Solution:

    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        ans = 0
        h = []
        sm = 0
        cur = heights[0]
        s = 1
        cost = 0

        def f(cost, s):
            nonlocal ans, sm, ladders
            heappush(h, -cost)
            sm += cost
            if sm <= bricks:
                ans += s
                return False
            if ladders == 0:
                return True
            v = -heappop(h)
            sm -= v
            ans += s
            ladders -= 1
            return False

        for i in range(1, len(heights)):
            if heights[i] > cur:
                if (f(cost, s)):
                    break
                cost = heights[i] - cur
                s = 1
            else:
                s += 1
            cur = heights[i]
        f(cost, s)
        return ans - 1


if __name__ == '__main__':
    # 7
    print(Solution().furthestBuilding([4, 12, 2, 7, 3, 18, 20, 3, 19], bricks=10, ladders=2))
    # 4
    print(Solution().furthestBuilding([4, 2, 7, 6, 9, 14, 12], bricks=5, ladders=1))
    # 3
    print(Solution().furthestBuilding([14, 3, 19, 3], bricks=17, ladders=0))
