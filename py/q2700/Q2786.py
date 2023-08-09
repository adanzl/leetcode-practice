"""
 * 给你一个下标从 0 开始的整数数组 nums 和一个正整数 x 。
 * 你 一开始 在数组的位置 0 处，你可以按照下述规则访问数组中的其他位置：
 * 1、如果你当前在位置 i ，那么你可以移动到满足 i < j 的 任意 位置 j 。
 * 2、对于你访问的位置 i ，你可以获得分数 nums[i] 。
 * 3、如果你从位置 i 移动到位置 j 且 nums[i] 和 nums[j] 的 奇偶性 不同，那么你将失去分数 x 。
 * 请你返回你能得到的 最大 得分之和。
 * 注意 ，你一开始的分数为 nums[0] 。
 * 提示：
 * 1、2 <= nums.length <= 10^5
 * 2、1 <= nums[i], x <= 10^6
 * 链接：https://leetcode.cn/problems/visit-array-positions-to-maximize-score/
"""
from typing import List


class Solution:

    def maxScore(self, nums: List[int], x: int) -> int:
        ans = nums[0]
        LIMIT = 10**6 + 1
        mx = [-LIMIT, -LIMIT]  # odd, even
        if nums[0] % 2:
            mx[0] = nums[0]
        else:
            mx[1] = nums[0]
        for i in range(1, len(nums)):
            f_odd = f_even = -LIMIT
            if nums[i] % 2:  # odd
                if mx[0] != -LIMIT: f_odd = mx[0] + nums[i]
                if mx[1] != -LIMIT: f_even = mx[1] + nums[i] - x
                mx[0] = max(mx[0], f_odd, f_even)
            else:  # even
                if mx[0] != -LIMIT: f_odd = mx[0] + nums[i] - x
                if mx[1] != -LIMIT: f_even = mx[1] + nums[i]
                mx[1] = max(mx[1], f_even, f_odd)
            ans = max(ans, f_odd, f_even)
        return ans


if __name__ == '__main__':
    # 470
    print(Solution().maxScore([8, 50, 65, 85, 8, 73, 55, 50, 29, 95, 5, 68, 52, 79], 74))
    # 1545
    print(Solution().maxScore(
        [38, 92, 23, 30, 25, 96, 6, 71, 78, 77, 33, 23, 71, 48, 87, 77, 53, 28, 6, 20, 90, 83, 42, 21, 64, 95, 84, 29, 22, 21, 33, 36, 53, 51, 85, 25, 80, 56, 71, 69, 5, 21, 4, 84, 28, 16, 65, 7],
        52))
    # 13
    print(Solution().maxScore([2, 3, 6, 1, 9, 2], x=5))
    # 20
    print(Solution().maxScore([2, 4, 6, 8], x=3))
