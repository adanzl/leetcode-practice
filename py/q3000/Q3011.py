"""
 * 给你一个下标从 0 开始且全是 正 整数的数组 nums 。
 * 一次 操作 中，如果两个 相邻 元素在二进制下数位为 1 的数目 相同 ，那么你可以将这两个元素交换。
 * 你可以执行这个操作 任意次 （也可以 0 次）。
 * 如果你可以使数组变有序，请你返回 true ，否则返回 false 。
 * 提示：
 * 1、1 <= nums.length <= 100
 * 2、1 <= nums[i] <= 28
 * 链接：https://leetcode.cn/problems/find-if-array-can-be-sorted/
"""
from typing import List


class Solution:

    def canSortArray(self, nums: List[int]) -> bool:
        pre_size = nums[0].bit_count()
        ii = 0
        pre_mx = 0
        for i in range(1, len(nums)):
            num = nums[i]
            size = num.bit_count()
            if size != pre_size:
                arr = sorted(nums[ii:i])
                mx, mn = max(arr), min(arr)
                if mn < pre_mx:
                    return False
                pre_size = size
                pre_mx = mx
                ii = i
        arr = nums[ii:]
        mx, mn = max(arr), min(arr)
        if mn < pre_mx:
            return False
        return True


if __name__ == '__main__':
    # True
    print(Solution().canSortArray([1, 2, 3, 4, 5]))
    # True
    print(Solution().canSortArray([8, 4, 2, 30, 15]))
    # False
    print(Solution().canSortArray([3, 16, 8, 4, 2]))
