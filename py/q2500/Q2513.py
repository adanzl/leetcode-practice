"""
 * 给你两个数组 arr1 和 arr2 ，它们一开始都是空的。你需要往它们中添加正整数，使它们满足以下条件：
 * 1、arr1 包含 uniqueCnt1 个 互不相同 的正整数，每个整数都 不能 被 divisor1 整除 。
 * 2、arr2 包含 uniqueCnt2 个 互不相同 的正整数，每个整数都 不能 被 divisor2 整除 。
 * 3、arr1 和 arr2 中的元素 互不相同 。
 * 给你 divisor1 ，divisor2 ，uniqueCnt1 和 uniqueCnt2 ，请你返回两个数组中 最大元素 的 最小值 。
 * 提示：
 * 1、2 <= divisor1, divisor2 <= 10^5
 * 2、1 <= uniqueCnt1, uniqueCnt2 < 10^9
 * 3、2 <= uniqueCnt1 + uniqueCnt2 <= 10^9
 * 链接：https://leetcode.cn/problems/minimize-the-maximum-of-two-arrays
"""
from math import lcm


class Solution:

    def minimizeSet(self, d1: int, d2: int, u1: int, u2: int) -> int:
        mul = lcm(d1, d2)
        tot = u1 + u2
        l, r = 0, 10**15
        ans = -1
        while l <= r:
            mid = (l + r) // 2
            cn = mid - mid // d1 - mid // d2 + mid // mul
            l1 = min(u1, mid // d2 - mid // mul)
            l2 = min(u2, mid // d1 - mid // mul)
            val = cn + l1 + l2

            if val >= tot:
                if val == tot:
                    ans = mid
                r = mid - 1
            else:
                l = mid + 1

        return ans


if __name__ == '__main__':
    # 15
    print(Solution().minimizeSet(2, 4, 8, 2))
    # 1367303863
    print(Solution().minimizeSet(2, 5, 683651932, 161878530))
    # 41373726
    print(Solution().minimizeSet(47911, 14723, 18200983, 23172743))
    # 4
    print(Solution().minimizeSet(2, 7, 1, 3))
    # 3
    print(Solution().minimizeSet(3, 5, 2, 1))
