"""
 * 给你一个下标从 0 开始的正整数数组 nums 。
 * 你可以对数组执行以下两种操作 任意次 ：
 * 1、从数组中选择 两个 值 相等 的元素，并将它们从数组中 删除 。
 * 2、从数组中选择 三个 值 相等 的元素，并将它们从数组中 删除 。
 * 请你返回使数组为空的 最少 操作次数，如果无法达成，请返回 -1 。
 * 提示：
 * 1、2 <= nums.length <= 10^5
 * 2、1 <= nums[i] <= 10^6
 * 链接：https://leetcode.cn/problems/minimum-number-of-operations-to-make-array-empty/
"""
from typing import List


class Solution:

    def minOperations(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        ans = 0
        for v, c in cnt.items():
            if c == 1: return -1
            a, r = divmod(c, 3)
            if r == 2 or r == 1:
                a += 1
            ans += a
        return ans


if __name__ == '__main__':
    # 4
    print(Solution().minOperations([2, 3, 3, 2, 2, 4, 2, 3, 4]))
    # -1
    print(Solution().minOperations([2, 1, 2, 2, 3, 3]))
