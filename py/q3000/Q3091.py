"""
 * 给你一个正整数 k 。最初，你有一个数组 nums = [1] 。
 * 你可以对数组执行以下 任意 操作 任意 次数（可能为零）：
 * 1、选择数组中的任何一个元素，然后将它的值 增加 1 。
 * 2、复制数组中的任何一个元素，然后将它附加到数组的末尾。
 * 返回使得最终数组元素之 和 大于或等于 k 所需的 最少 操作次数。
 * 提示：1 <= k <= 10^5
 * 链接：https://leetcode.cn/problems/apply-operations-to-make-sum-of-array-greater-than-or-equal-to-k/
"""

import math


class Solution:

    def minOperations(self, k: int) -> int:
        ans = k
        for v in range(1, k + 1):
            if v * v > k: break
            ans = min(ans, math.ceil(k / v) + v - 2)
        return ans


if __name__ == '__main__':
    # 4
    print(Solution().minOperations(8))
    # 5
    print(Solution().minOperations(11))
    # 0
    print(Solution().minOperations(1))
