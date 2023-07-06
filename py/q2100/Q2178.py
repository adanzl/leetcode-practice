"""
 * 给你一个整数 finalSum 。请你将它拆分成若干个 互不相同 的正偶数之和，且拆分出来的正偶数数目 最多 。
 * 比方说，给你 finalSum = 12 ，那么这些拆分是 符合要求 的（互不相同的正偶数且和为 finalSum）：(2 + 10) ，(2 + 4 + 6) 和 (4 + 8) 。
 * 它们中，(2 + 4 + 6) 包含最多数目的整数。注意 finalSum 不能拆分成 (2 + 2 + 4 + 4) ，因为拆分出来的整数必须互不相同。
 * 请你返回一个整数数组，表示将整数拆分成 最多 数目的正偶数数组。
 * 如果没有办法将 finalSum 进行拆分，请你返回一个 空 数组。你可以按 任意 顺序返回这些整数。
 * 提示：1 <= finalSum <= 10^10
 * 链接：https://leetcode.cn/problems/maximum-split-of-positive-even-integers/
"""
from typing import List


class Solution:

    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        ans = []
        if finalSum % 2 == 1:
            return ans
        l, r = 1, finalSum // 2
        v = 0
        while l <= r:
            mid = (l + r) // 2
            if (mid + 1) * mid // 2 > finalSum // 2:
                r = mid - 1
            else:
                v = mid
                l = mid + 1
        ans = [i * 2 for i in range(1, v + 1)]
        if (v + 1) * v < finalSum:
            ans[-1] += (finalSum - (v + 1) * v)
        return ans


if __name__ == '__main__':
    # [2]
    print(Solution().maximumEvenSplit(2))
    # [6,8,2,12]
    print(Solution().maximumEvenSplit(28))
    # [2,4,6]
    print(Solution().maximumEvenSplit(12))
    # []
    print(Solution().maximumEvenSplit(7))