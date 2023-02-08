"""
 * 给定一个长度为 n 的 0 索引整数数组 nums。初始位置为 nums[0]。
 * 每个元素 nums[i] 表示从索引 i 向前跳转的最大长度。换句话说，如果你在 nums[i] 处，你可以跳转到任意 nums[i + j] 处:
 * 1、0 <= j <= nums[i] 
 * 2、i + j < n
 * 返回到达 nums[n - 1] 的最小跳跃次数。生成的测试用例可以到达 nums[n - 1]。
 * 提示:
 * 1、1 <= nums.length <= 10^4
 * 2、0 <= nums[i] <= 1000
 * 链接：https://leetcode.cn/problems/jump-game-ii/
"""
from typing import List


class Solution:

    def jump(self, nums: List[int]) -> int:
        l, r, n = 0, nums[0], len(nums)
        if n == 1: return 0
        ans = 1
        while r < n - 1:
            ans += 1
            l, r = r, max(i + nums[i] for i in range(l, r + 1))
        return ans


if __name__ == '__main__':
    # 0
    print(Solution().jump([0]))
    # 1
    print(Solution().jump([1, 3]))
    # 2
    print(Solution().jump([2, 3, 1, 1, 4]))
    # 2
    print(Solution().jump([2, 3, 0, 1, 4]))
