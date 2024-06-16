"""
 * 给你一个数组 nums 和一个整数 k 。
 * 你需要找到 nums 的一个 子数组 ，满足子数组中所有元素按位与运算 AND 的值与 k 的 绝对差 尽可能 小 。
 * 换言之，你需要选择一个子数组 nums[l..r] 满足 |k - (nums[l] AND nums[l + 1] ... AND nums[r])| 最小。
 * 请你返回 最小 的绝对差值。
 * 子数组是数组中连续的 非空 元素序列。
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、1 <= nums[i] <= 10^9
 * 3、1 <= k <= 10^9
 * 链接：https://leetcode.cn/problems/find-subarray-with-bitwise-or-closest-to-k/
"""
from typing import List


class Solution:

    def minimumDifference(self, nums: List[int], k: int) -> int:
        ans = 0x3c3c3c3c3c3c
        for i, x in enumerate(nums):
            ans = min(ans, abs(x - k))
            j = i - 1
            while j >= 0 and nums[j] | x != nums[j]:
                nums[j] |= x
                ans = min(ans, abs(nums[j] - k))
                j -= 1
        return ans


if __name__ == '__main__':
    # 1495
    print(Solution().minimumDifference([
        7734, 27946, 47628, 95595, 92840, 3115, 18171, 23688, 71335, 73539, 87965, 38547, 73565, 7195, 18047, 88043,
        78925, 91961, 1399, 70163, 25390, 18566, 99695, 91221, 7885, 68734, 4524, 24708, 5410, 70627, 6886, 14004,
        56305, 90092, 45306, 79429, 70744, 84061, 75601, 54315, 27728, 75860, 34888, 33989, 71632, 80179, 39350, 82046,
        18179, 88586
    ], 9380))
    # 4
    print(Solution().minimumDifference([6], 2))
    # 1
    print(Solution().minimumDifference([1, 2, 4, 5], k=3))
    # 0
    print(Solution().minimumDifference([1, 2, 1, 2], k=2))
    # 9
    print(Solution().minimumDifference([1], k=10))
