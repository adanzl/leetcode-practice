"""
 * 给你一个整数数组 nums 和一个整数 x 。每一次操作时，你应当移除数组 nums 最左边或最右边的元素，然后从 x 中减去该元素的值。请注意，需要 修改 数组以供接下来的操作使用。
 * 如果可以将 x 恰好 减到 0 ，返回 最小操作数 ；否则，返回 -1 。
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、1 <= nums[i] <= 10^4
 * 3、1 <= x <= 10^9
 * 链接：https://leetcode.cn/problems/minimum-operations-to-reduce-x-to-zero/
"""
from typing import List


class Solution:

    def minOperations(self, nums: List[int], x: int) -> int:
        n, total = len(nums), sum(nums)
        if total < x: return -1
        if total == x: return n
        ans = n + 5
        l, r = n - 1, n - 1
        l_sum, r_sum = total, 0
        while l >= 0:
            while l_sum + r_sum >= x and l >= 0:
                if l_sum + r_sum == x: ans = min(ans, n - (r - l))
                l_sum -= nums[l]
                l -= 1
            while l_sum + r_sum < x and r >= 0:
                r_sum += nums[r]
                r -= 1
            if l_sum + r_sum == x:
                ans = min(ans, n - (r - l))
        return -1 if ans > n else ans

    def minOperations1(self, nums: List[int], x: int) -> int:
        # 要从 nums 中找最长的子数组，其元素和等于 s-xs−x，这里 ss 为 nums 所有元素之和。
        target = sum(nums) - x
        if target < 0: return -1  # 全部移除也无法满足要求
        ans = -1
        left = s = 0
        for right, x in enumerate(nums):
            s += x
            while s > target:  # 缩小子数组长度
                s -= nums[left]
                left += 1
            if s == target:
                ans = max(ans, right - left + 1)
        return -1 if ans < 0 else len(nums) - ans


if __name__ == '__main__':
    # 1
    print(Solution().minOperations([5, 2, 3, 1, 1], 5))
    # 113
    print(Solution().minOperations([
        5207, 5594, 477, 6938, 8010, 7606, 2356, 6349, 3970, 751, 5997, 6114, 9903, 3859, 6900, 7722, 2378, 1996, 8902, 228, 4461, 90, 7321, 7893, 4879, 9987, 1146, 8177, 1073, 7254, 5088, 402, 4266,
        6443, 3084, 1403, 5357, 2565, 3470, 3639, 9468, 8932, 3119, 5839, 8008, 2712, 2735, 825, 4236, 3703, 2711, 530, 9630, 1521, 2174, 5027, 4833, 3483, 445, 8300, 3194, 8784, 279, 3097, 1491,
        9864, 4992, 6164, 2043, 5364, 9192, 9649, 9944, 7230, 7224, 585, 3722, 5628, 4833, 8379, 3967, 5649, 2554, 5828, 4331, 3547, 7847, 5433, 3394, 4968, 9983, 3540, 9224, 6216, 9665, 8070, 31,
        3555, 4198, 2626, 9553, 9724, 4503, 1951, 9980, 3975, 6025, 8928, 2952, 911, 3674, 6620, 3745, 6548, 4985, 5206, 5777, 1908, 6029, 2322, 2626, 2188, 5639
    ], 565610))
    # 2
    print(Solution().minOperations([1, 1, 4, 2, 3], 5))
    # -1
    print(Solution().minOperations([5, 6, 7, 8, 9], 4))
    # 5
    print(Solution().minOperations([3, 2, 20, 1, 1, 3], 10))
