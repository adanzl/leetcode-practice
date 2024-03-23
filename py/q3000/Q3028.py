"""
 * 边界上有一只蚂蚁，它有时向 左 走，有时向 右 走。
 * 给你一个 非零 整数数组 nums 。蚂蚁会按顺序读取 nums 中的元素，从第一个元素开始直到结束。
 * 每一步，蚂蚁会根据当前元素的值移动：
 * 1、如果 nums[i] < 0 ，向 左 移动 -nums[i]单位。
 * 2、如果 nums[i] > 0 ，向 右 移动 nums[i]单位。
 * 返回蚂蚁 返回 到边界上的次数。
 * 注意：
 * 1、边界两侧有无限的空间。
 * 2、只有在蚂蚁移动了 |nums[i]| 单位后才检查它是否位于边界上。换句话说，如果蚂蚁只是在移动过程中穿过了边界，则不会计算在内。
 * 提示：
 * 1、1 <= nums.length <= 100
 * 2、-10 <= nums[i] <= 10
 * 3、nums[i] != 0
 * 链接：https://leetcode.cn/problems/ant-on-the-boundary/
"""
from typing import List


class Solution:

    def returnToBoundaryCount(self, nums: List[int]) -> int:
        ans = 0
        x = 0
        for num in nums:
            if num < 0:
                nx = x - abs(num)
            else:
                nx = x + abs(num)
            if nx == 0:
                ans += 1
            x = nx
        return ans


if __name__ == '__main__':
    # 0
    print(Solution().returnToBoundaryCount([3, 2, -3, -4]))
    # 1
    print(Solution().returnToBoundaryCount([2, 3, -5]))
