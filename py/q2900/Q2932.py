"""
 * 给你一个下标从 0 开始的整数数组 nums 。如果一对整数 x 和 y 满足以下条件，则称其为 强数对 ：
 * |x - y| <= min(x, y)
 * 你需要从 nums 中选出两个整数，且满足：这两个整数可以形成一个强数对，并且它们的按位异或（XOR）值是在该数组所有强数对中的 最大值 。
 * 返回数组 nums 所有可能的强数对中的 最大 异或值。
 * 注意，你可以选择同一个整数两次来形成一个强数对。
 * 提示：
 * 1、1 <= nums.length <= 50
 * 2、1 <= nums[i] <= 100
 * 链接：https://leetcode.cn/problems/maximum-strong-pair-xor-i/
"""
from typing import List


class Solution:

    def maximumStrongPairXor(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            for j in range(i, n):
                if abs(nums[i] - nums[j]) <= min(nums[i], nums[j]):
                    ans = max(ans, nums[i] ^ nums[j])
        return ans


if __name__ == '__main__':
    # 7
    print(Solution().maximumStrongPairXor([1, 2, 3, 4, 5]))
    # 0
    print(Solution().maximumStrongPairXor([10, 100]))
    # 7
    print(Solution().maximumStrongPairXor([5, 6, 25, 30]))
