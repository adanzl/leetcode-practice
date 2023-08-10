"""
 * 给你一个下标从 0 开始、由正整数组成的数组 nums 。
 * 你可以在数组上执行下述操作 任意 次：
 * 1、选中一个同时满足 0 <= i < nums.length - 1 和 nums[i] <= nums[i + 1] 的整数 i 。
 *    将元素 nums[i + 1] 替换为 nums[i] + nums[i + 1] ，并从数组中删除元素 nums[i] 。
 * 返回你可以从最终数组中获得的 最大 元素的值。
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、1 <= nums[i] <= 10^6
 * 链接：https://leetcode.cn/problems/largest-element-in-an-array-after-merge-operations/
"""
from typing import List


class Solution:

    def maxArrayValue(self, nums: List[int]) -> int:
        n = len(nums)
        mx = ans = nums[-1]
        for i in range(n - 2, -1, -1):
            if nums[i] <= mx:
                mx += nums[i]
            else:
                mx = nums[i]
            ans = max(ans, mx)
        return ans


if __name__ == '__main__':
    # 21
    print(Solution().maxArrayValue([2, 3, 7, 9, 3]))
    # 11
    print(Solution().maxArrayValue([5, 3, 3]))
