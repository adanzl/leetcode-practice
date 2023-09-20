"""
 * 给你四个整数 sx、sy、fx、fy  以及一个 非负整数 t 。
 * 在一个无限的二维网格中，你从单元格 (sx, sy) 开始出发。每一秒，你 必须 移动到任一与之前所处单元格相邻的单元格中。
 * 如果你能在 恰好 t 秒 后到达单元格 (fx, fy) ，返回 true ；否则，返回  false 。
 * 单元格的 相邻单元格 是指该单元格周围与其至少共享一个角的 8 个单元格。你可以多次访问同一个单元格。
 * 提示：
 * 1、1 <= sx, sy, fx, fy <= 10^9
 * 2、0 <= t <= 10^9
 * 链接：https://leetcode.cn/problems/determine-if-a-cell-is-reachable-at-a-given-time/
"""
#
# @lc app=leetcode.cn id=2849 lang=python3
#

# @lc code=start


class Solution:

    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        d = max(abs(fy - sy), abs(fx - sx))
        return d <= t if d > 0 else (d <= t and t - d > 1 or t == d)


# @lc code=end
if __name__ == '__main__':
    # True
    print(Solution().isReachableAtTime(1, 3, 1, 3, 0))
    # True
    print(Solution().isReachableAtTime(1, 1, 1, 1, 3))
    # False
    print(Solution().isReachableAtTime(1, 2, 1, 2, 1))
    # True
    print(Solution().isReachableAtTime(2, sy=4, fx=7, fy=7, t=6))
    # False
    print(Solution().isReachableAtTime(3, sy=1, fx=7, fy=3, t=3))
