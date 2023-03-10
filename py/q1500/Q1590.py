"""
 * 给你一个正整数数组 nums，请你移除 最短 子数组（可以为 空），使得剩余元素的 和 能被 p 整除。 不允许 将整个数组都移除。
 * 请你返回你需要移除的最短子数组的长度，如果无法满足题目要求，返回 -1 。
 * 子数组 定义为原数组中连续的一组元素。
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、1 <= nums[i] <= 10^9
 * 3、1 <= p <= 10^9
 * 链接：https://leetcode.cn/problems/make-sum-divisible-by-p/
"""
from itertools import accumulate
from typing import List


class Solution:

    def minSubarray(self, nums: List[int], p: int) -> int:
        pre_sum = [0] + list(accumulate(nums))
        idx_num = {0: 0}
        n = len(nums)
        ans = n
        for i in range(n + 1):
            rr = (pre_sum[-1] - pre_sum[i]) % p
            lr = pre_sum[i] % p
            if (p - rr) % p in idx_num:
                ans = min(ans, i - idx_num[(p - rr) % p])
            idx_num[lr] = max(idx_num.get(lr, 0), i)
        return ans if ans < n else -1


if __name__ == '__main__':
    # 0
    print(Solution().minSubarray([1, 2, 3], p=3))
    # 2
    print(Solution().minSubarray([6, 3, 5, 2], p=9))
    # 1
    print(Solution().minSubarray([3, 1, 4, 2], p=6))
    # -1
    print(Solution().minSubarray([1, 2, 3], p=7))
    # 0
    print(Solution().minSubarray([1000000000, 1000000000, 1000000000], p=3))
