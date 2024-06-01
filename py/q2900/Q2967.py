"""
 * 给你一个长度为 n 下标从 0 开始的整数数组 nums 。
 * 你可以对 nums 执行特殊操作 任意次 （也可以 0 次）。每一次特殊操作中，你需要 按顺序 执行以下步骤：
 * 1、从范围 [0, n - 1] 里选择一个下标 i 和一个 正 整数 x 。
 * 2、将 |nums[i] - x| 添加到总代价里。
 * 3、将 nums[i] 变为 x 。
 * 如果一个正整数正着读和反着读都相同，那么我们称这个数是 回文数 。
 * 比方说，121 ，2552 和 65756 都是回文数，但是 24 ，46 ，235 都不是回文数。
 * 如果一个数组中的所有元素都等于一个整数 y ，且 y 是一个小于 10^9 的 回文数 ，那么我们称这个数组是一个 等数数组 。
 * 请你返回一个整数，表示执行任意次特殊操作后使 nums 成为 等数数组 的 最小 总代价。
 * 提示：
 * 1、1 <= n <= 10^5
 * 2、1 <= nums[i] <= 10^9
 * 链接：https://leetcode.cn/problems/minimum-cost-to-make-array-equalindromic/
"""
import bisect
from itertools import accumulate
from typing import List


def calc(num0, num1):
    ret = num0
    while num1:
        num1, r = divmod(num1, 10)
        ret = ret * 10 + r
    return ret


pal = []
for i in range(1, 6):
    for e in [0, 1]:
        for num in range(10**(i - 1), 10**i):
            if e == 0:  # odd
                pal.append(calc(num, num // 10))
            else:  # even
                pal.append(calc(num, num))


class Solution:

    def minimumCost(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        pre_sm = [0] + list(accumulate(nums))
        ans = pre_sm[-1]
        il = bisect.bisect_left(pal, nums[0])
        ir = bisect.bisect_right(pal, nums[-1])
        for i in range(max(0, il - 1), min(ir + 1, len(pal))):
            ii = bisect.bisect_left(nums, pal[i])
            vl = (ii * pal[i] - pre_sm[ii]) if pal[i] >= nums[0] else 0
            vr = ((pre_sm[-1] - pre_sm[ii]) - (n - ii) * pal[i]) if pal[i] <= nums[-1] else 0
            ans = min(ans, vl + vr)
        return ans


if __name__ == '__main__':
    # 35
    print(Solution().minimumCost([206, 215, 216, 219, 220, 221]))
    # 0
    print(Solution().minimumCost([1]))
    # 11
    print(Solution().minimumCost([10, 12, 13, 14, 15]))
    # 6
    print(Solution().minimumCost([1, 2, 3, 4, 5]))
    # 22
    print(Solution().minimumCost([22, 33, 22, 33, 22]))
