"""
 * 给你一个长度为 n 的整数数组 nums ，n 是 偶数 ，同时给你一个整数 k 。
 * 你可以对数组进行一些操作。每次操作中，你可以将数组中 任一 元素替换为 0 到 k 之间的 任一 整数。
 * 执行完所有操作以后，你需要确保最后得到的数组满足以下条件：
 * 存在一个整数 X ，满足对于所有的 (0 <= i < n) 都有 abs(a[i] - a[n - i - 1]) = X 。
 * 请你返回满足以上条件 最少 修改次数。
 * 提示：
 * 1、2 <= n == nums.length <= 10^5
 * 2、n 是偶数。
 * 3、0 <= nums[i] <= k <= 10^5
 * 链接：https://leetcode.cn/problems/minimum-array-changes-to-make-differences-equal/
"""
from itertools import accumulate
from typing import List


class Solution:

    def minChanges(self, nums: List[int], k: int) -> int:
        n = len(nums)
        diff = [0] * (k + 2)
        for i in range(n // 2):
            mx, mn = max(nums[i], nums[n - i - 1]), min(nums[i], nums[n - i - 1])
            d = mx - mn
            mx_val = max(mx, k - mn)
            # [0, d-1] +1
            diff[0] += 1
            diff[d] -= 1
            # [d+1, mx_val] +1
            diff[d + 1] += 1
            diff[mx_val + 1] -= 1
            # [mx_val+1, k] +2
            diff[mx_val + 1] += 2
            diff[k + 1] -= 2

        return min(accumulate(diff[:-1]))


if __name__ == '__main__':
    # 4
    print(Solution().minChanges([1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0], 1))
    # 2
    print(Solution().minChanges([1, 0, 1, 2, 4, 3], k=4))
    # 5
    print(Solution().minChanges([1, 10, 5, 1, 4, 6, 4, 2, 4, 9, 7, 9, 0, 11], 12))
    # 2
    print(Solution().minChanges([0, 1, 2, 3, 3, 6, 5, 4], k=6))
