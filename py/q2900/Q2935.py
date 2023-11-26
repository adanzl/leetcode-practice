"""
 * 给你一个下标从 0 开始的整数数组 nums 。如果一对整数 x 和 y 满足以下条件，则称其为 强数对 ：
 * |x - y| <= min(x, y)
 * 你需要从 nums 中选出两个整数，且满足：这两个整数可以形成一个强数对，并且它们的按位异或（XOR）值是在该数组所有强数对中的 最大值 。
 * 返回数组 nums 所有可能的强数对中的 最大 异或值。
 * 注意，你可以选择同一个整数两次来形成一个强数对。
 * 提示：
 * 1、1 <= nums.length <= 5*10^4
 * 2、1 <= nums[i] <= 2^20-1
 * 链接：https://leetcode.cn/problems/maximum-strong-pair-xor-ii/
"""
from typing import List


class Solution:

    def maximumStrongPairXor(self, nums: List[int]) -> int:
        nums.sort()
        ans = mask = 0
        high_bit = nums[-1].bit_length() - 1
        for i in range(high_bit, -1, -1):  # 从最高位开始枚举
            mask |= 1 << i
            new_ans = ans | (1 << i)  # 这个比特位可以是 1 吗？
            d = {}
            for y in nums:
                mask_y = y & mask  # 低于 i 的比特位置为 0
                if new_ans ^ mask_y in d and d[new_ans ^ mask_y] * 2 >= y:
                    ans = new_ans  # 这个比特位可以是 1
                    break
                d[mask_y] = y
        return ans


if __name__ == '__main__':
    # 7
    print(Solution().maximumStrongPairXor([1, 2, 3, 4, 5]))
    # 0
    print(Solution().maximumStrongPairXor([10, 100]))
    # 1020
    print(Solution().maximumStrongPairXor([500, 520, 2500, 3000]))
