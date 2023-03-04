"""
 * 给你一个整数数组 nums，每次 操作 会从中选择一个元素并 将该元素的值减少 1。
 * 如果符合下列情况之一，则数组 A 就是 锯齿数组：
 * 1、每个偶数索引对应的元素都大于相邻的元素，即 A[0] > A[1] < A[2] > A[3] < A[4] > ...
 * 2、或者，每个奇数索引对应的元素都大于相邻的元素，即 A[0] < A[1] > A[2] < A[3] > A[4] < ...
 * 返回将数组 nums 转换为锯齿数组所需的最小操作次数。
 * 提示：
 * 1、1 <= nums.length <= 1000
 * 2、1 <= nums[i] <= 1000
 * 链接：https://leetcode.cn/problems/decrease-elements-to-make-array-zigzag/
"""
from typing import List


class Solution:

    def movesToMakeZigzag(self, nums):
        s = [0] * 2
        for i, x in enumerate(nums):
            left = nums[i - 1] if i else float('inf')  
            right = nums[i + 1] if i < len(nums) - 1 else float('inf')
            s[i % 2] += max(x - min(left, right) + 1, 0)
        return min(s)


if __name__ == '__main__':
    # 2
    print(Solution().movesToMakeZigzag([1, 2, 3]))
    # 4
    print(Solution().movesToMakeZigzag([9, 6, 1, 6, 2]))
