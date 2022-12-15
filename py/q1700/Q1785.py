"""
 * 给你一个整数数组 nums ，和两个整数 limit 与 goal 。数组 nums 有一条重要属性：abs(nums[i]) <= limit 。
 * 返回使数组元素总和等于 goal 所需要向数组中添加的 最少元素数量 ，添加元素 不应改变 数组中 abs(nums[i]) <= limit 这一属性。
 * 注意，如果 x >= 0 ，那么 abs(x) 等于 x ；否则，等于 -x 。
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、1 <= limit <= 10^6
 * 3、-limit <= nums[i] <= limit
 * 4、-10^9 <= goal <= 10^9
 * 链接：https://leetcode.cn/problems/minimum-elements-to-add-to-form-a-given-sum/
"""
import math
from typing import List


class Solution:

    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        return math.ceil(abs(goal - sum(nums)) / abs(limit))


if __name__ == '__main__':
    # 2
    print(Solution().minElements([1, -1, 1], 3, -4))
    # 1
    print(Solution().minElements([1, -10, 9, 1], 100, 0))
