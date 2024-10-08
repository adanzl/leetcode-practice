"""
 * 给你一个整数数组 start 和一个整数 d，代表 n 个区间 [start[i], start[i] + d]。
 * 你需要选择 n 个整数，其中第 i 个整数必须属于第 i 个区间。所选整数的 得分 定义为所选整数两两之间的 最小 绝对差。
 * 返回所选整数的 最大可能得分 。
 * 提示：
 * 1、2 <= start.length <= 10^5
 * 2、0 <= start[i] <= 10^9
 * 3、0 <= d <= 10^9
 * 链接：https://leetcode.cn/problems/maximize-score-of-numbers-in-ranges/
"""
from typing import List

INF = 0x3c3c3c3c3c3c3c3c3c


class Solution:

    def maxPossibleScore(self, start: List[int], d: int) -> int:
        start.sort()
        mn, mx = start[0], start[-1] + d

        def check(v):
            val = mn
            for s in start:
                if val > s + d:
                    return False
                val = max(val, s) + v
            return True

        lo, hi = 0, mx - mn + 1
        ans = 0
        while lo < hi:
            mid = (lo + hi) // 2
            if check(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid
        return ans


if __name__ == '__main__':
    # 2
    print(Solution().maxPossibleScore([0, 9, 2, 9], 2))
    # 2000000000
    print(Solution().maxPossibleScore([1000000000, 0], 1000000000))
    # 5
    print(Solution().maxPossibleScore([2, 6, 13, 13], d=5))
    # 4
    print(Solution().maxPossibleScore([6, 0, 3], d=2))
