"""
 * 给你一个下标从 0 开始的整数数组 nums ，它只包含 正 整数。
 * 你的任务是通过进行以下操作 任意次 （可以是 0 次） 最小化 nums 的长度：
 * 1、在 nums 中选择 两个不同 的下标 i 和 j ，满足 nums[i] > 0 且 nums[j] > 0 。
 * 2、将结果 nums[i] % nums[j] 插入 nums 的结尾。
 * 3、将 nums 中下标为 i 和 j 的元素删除。
 * 请你返回一个整数，它表示进行任意次操作以后 nums 的 最小长度 。
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、1 <= nums[i] <= 10^9
 * 链接：https://leetcode.cn/problems/minimize-length-of-array-using-operations/
"""
from typing import Counter, List


class Solution:

    def minimumArrayLength(self, nums: List[int]) -> int:
        m = min(nums)
        for x in nums:
            if x % m:
                return 1
        return (nums.count(m) + 1) // 2


if __name__ == '__main__':
    #
    print(Solution().minimumArrayLength([2, 7, 2, 4, 2, 9]))
    # 2
    print(Solution().minimumArrayLength([3, 4, 3, 4, 1, 1, 1, 2]))
    # 1
    print(Solution().minimumArrayLength([2, 2, 2, 2, 2, 2, 5]))
    # 1
    print(Solution().minimumArrayLength([5, 2, 2, 2, 9, 10]))
    # 1
    print(Solution().minimumArrayLength([2, 3, 4]))
    # 1
    print(Solution().minimumArrayLength([1, 4, 3, 1]))
    # 2
    print(Solution().minimumArrayLength([5, 5, 5, 10, 5]))
