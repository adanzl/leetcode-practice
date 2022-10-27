"""
 * 给你一个披萨，它由 3n 块不同大小的部分组成，现在你和你的朋友们需要按照如下规则来分披萨：
 * 你挑选 任意 一块披萨。
 * 1、Alice 将会挑选你所选择的披萨逆时针方向的下一块披萨。
 * 2、Bob 将会挑选你所选择的披萨顺时针方向的下一块披萨。
 * 3、重复上述过程直到没有披萨剩下。
 * 4、每一块披萨的大小按顺时针方向由循环数组 slices 表示。
 * 请你返回你可以获得的披萨大小总和的最大值。
 * 提示：
 * 1、1 <= slices.length <= 500
 * 2、slices.length % 3 == 0
 * 3、1 <= slices[i] <= 1000
 * 链接：https://leetcode.cn/problems/pizza-with-3n-slices/
"""
from functools import cache
from typing import List


class Solution:

    def maxSizeSlices(self, slices: List[int]) -> int:

        n = len(slices)
        k = n // 3

        @cache
        def dfs(idx, cnt, end):
            if cnt == k: return 0
            ret = 0
            for i in range(idx, min(n - (k - cnt - 1) * 2, end)):
                ret = max(ret, slices[i] + dfs(i + 2, cnt + 1, (end - 1) if i == 0 else end))
            return ret

        return dfs(0, 0, n)


if __name__ == '__main__':
    # 30
    print(Solution().maxSizeSlices([9, 5, 1, 7, 8, 4, 4, 5, 5, 8, 7, 7]))
    # 10
    print(Solution().maxSizeSlices([1, 2, 3, 4, 5, 6]))
    # 32
    print(Solution().maxSizeSlices([3, 5, 4, 4, 6, 6, 3, 4, 4, 7, 10, 5, 7, 2, 2]))
    # 30
    print(Solution().maxSizeSlices([10, 9, 1, 10, 8, 5, 10, 2, 2]))
    # 16
    print(Solution().maxSizeSlices([8, 9, 8, 6, 1, 1]))
