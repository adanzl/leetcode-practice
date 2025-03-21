"""
 * 给你一个下标从 0 开始长度为 n 的整数数组 nums 和一个整数 k 。每一次操作中，你可以选择一个数并将它乘 2 。
 * 你最多可以进行 k 次操作，请你返回 nums[0] | nums[1] | ... | nums[n - 1] 的最大值。
 * a | b 表示两个整数 a 和 b 的 按位或 运算。
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、1 <= nums[i] <= 10^9
 * 3、1 <= k <= 15
 * 链接：https://leetcode.cn/problems/maximum-or/
"""
from typing import List


class Solution:

    def maximumOr(self, nums: List[int], k: int) -> int:
        ans = 0
        or_l, or_r_v = [0], 0
        for num in nums:
            or_l.append(or_l[-1] | num)
        for i in range(len(nums) - 1, -1, -1):
            ans = max(ans, or_l[i] | (nums[i] << k) | or_r_v)
            or_r_v |= nums[i]
        return ans


if __name__ == '__main__':
    # 30
    print(Solution().maximumOr([12, 9], k=1))
    # 511
    print(Solution().maximumOr([98, 54, 6, 34, 66, 63, 52, 39, 62, 46, 75, 28, 65, 18, 37, 18, 97, 13, 80, 33, 69, 91, 78, 19, 40], 2))
    # 35
    print(Solution().maximumOr([8, 1, 2], k=2))
