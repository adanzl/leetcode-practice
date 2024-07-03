"""
 * 给你 n 个包裹，你需要把它们装在箱子里，每个箱子装一个包裹。总共有 m 个供应商提供 不同尺寸 的箱子（每个规格都有无数个箱子）。
 * 如果一个包裹的尺寸 小于等于 一个箱子的尺寸，那么这个包裹就可以放入这个箱子之中。
 * 包裹的尺寸用一个整数数组 packages 表示，其中 packages[i] 是第 i 个包裹的尺寸。
 * 供应商用二维数组 boxes 表示，其中 boxes[j] 是第 j 个供应商提供的所有箱子尺寸的数组。
 * 你想要选择 一个供应商 并只使用该供应商提供的箱子，使得 总浪费空间最小 。
 * 对于每个装了包裹的箱子，我们定义 浪费的 空间等于 箱子的尺寸 - 包裹的尺寸 。总浪费空间 为 所有 箱子中浪费空间的总和。
 * 比方说，如果你想要用尺寸数组为 [4,8] 的箱子装下尺寸为 [2,3,5] 的包裹，
 * 你可以将尺寸为 2 和 3 的两个包裹装入两个尺寸为 4 的箱子中，同时把尺寸为 5 的包裹装入尺寸为 8 的箱子中。
 * 总浪费空间为 (4-2) + (4-3) + (8-5) = 6 。
 * 请你选择 最优 箱子供应商，使得 总浪费空间最小 。如果 无法 将所有包裹放入箱子中，请你返回 -1 。
 * 由于答案可能会 很大 ，请返回它对 10^9 + 7 取余 的结果。
 * 提示：
 * 1、n == packages.length
 * 2、m == boxes.length
 * 3、1 <= n <= 10^5
 * 4、1 <= m <= 10^5
 * 5、1 <= packages[i] <= 10^5
 * 6、1 <= boxes[j].length <= 10^5
 * 7、1 <= boxes[j][k] <= 10^5
 * 8、sum(boxes[j].length) <= 10^5
 * 9、boxes[j] 中的元素 互不相同 。
 * 链接：https://leetcode.cn/problems/minimum-space-wasted-from-packaging/
"""

import bisect
from itertools import accumulate
from typing import List

#
# @lc app=leetcode.cn id=1889 lang=python3
#
# [1889] 装包裹的最小浪费空间
#


# @lc code=start
class Solution:

    def minWastedSpace(self, packages: List[int], boxes: List[List[int]]) -> int:
        LIMIT, MOD = 0x3c3c3c3c3c3c, 10**9 + 7
        ans = LIMIT
        packages.sort()
        pre_sum = [0] + list(accumulate(packages))
        for box in boxes:
            ii, vv = 0, 0
            for b in sorted(box):
                idx = bisect.bisect_right(packages, b)
                vv += (idx - ii) * b - (pre_sum[idx] - pre_sum[ii])
                ii = idx
            if ii == len(packages):
                ans = min(ans, vv)
        return (ans % MOD) if ans != LIMIT else -1


# @lc code=end

if __name__ == '__main__':
    # -1
    print(Solution().minWastedSpace([2, 3, 5], boxes=[[1, 4], [2, 3], [3, 4]]))
    # 6
    print(Solution().minWastedSpace([2, 3, 5], boxes=[[4, 8], [2, 8]]))
    # 9
    print(Solution().minWastedSpace([3, 5, 8, 10, 11, 12], boxes=[[12], [11, 9], [10, 5, 14]]))
