"""
 * 有 n 座山排成一列，每座山都有一个高度。给你一个整数数组 height ，其中 height[i] 表示第 i 座山的高度，再给你一个整数 threshold 。
 * 对于下标不为 0 的一座山，如果它左侧相邻的山的高度 严格大于 threshold ，那么我们称它是 稳定 的。我们定义下标为 0 的山 不是 稳定的。
 * 请你返回一个数组，包含所有 稳定 山的下标，你可以以 任意 顺序返回下标数组。
 * 提示：
 * 1、2 <= n == height.length <= 100
 * 2、1 <= height[i] <= 100
 * 3、1 <= threshold <= 100
 * 链接：https://leetcode.cn/problems/find-indices-of-stable-mountains/
"""
from typing import List

INF = 0x3c3c3c3c3c3c3c3c3c


class Solution:

    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        ans = []
        for i in range(1, len(height)):
            if threshold < height[i - 1]:
                 ans.append(i)
        return ans


if __name__ == '__main__':
    # [3,4]
    print(Solution().stableMountains([1, 2, 3, 4, 5], threshold=2))
    # [1,3]
    print(Solution().stableMountains([10, 1, 10, 1, 10], threshold=3))
    # []
    print(Solution().stableMountains([10, 1, 10, 1, 10], threshold=10))
