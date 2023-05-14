"""
 * 给你一个下标从 0 开始的数组 nums ，数组长度为 n 。
 * nums 的 不同元素数目差 数组可以用一个长度为 n 的数组 diff 表示，其中 diff[i] 等于前缀 nums[0, ..., i] 中不同元素的数目 减去 后缀 nums[i + 1, ..., n - 1] 中不同元素的数目。
 * 返回 nums 的 不同元素数目差 数组。
 * 注意 nums[i, ..., j] 表示 nums 的一个从下标 i 开始到下标 j 结束的子数组（包含下标 i 和 j 对应元素）。特别需要说明的是，如果 i > j ，则 nums[i, ..., j] 表示一个空子数组。
 * 提示：
 * 1、1 <= n == nums.length <= 50
 * 2、1 <= nums[i] <= 50
 * 链接：https://leetcode.cn/problems/find-the-distinct-difference-array/
"""
from typing import List


class Solution:

    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        ans = []
        for i, v in enumerate(nums):
            ans.append(len(set(nums[:i + 1])) - len(set(nums[i + 1:])))
        return ans


if __name__ == '__main__':
    # [-3,-1,1,3,5]
    print(Solution().distinctDifferenceArray([1, 2, 3, 4, 5]))
    # [-2,-1,0,2,3]
    print(Solution().distinctDifferenceArray([3, 2, 3, 4, 2]))
