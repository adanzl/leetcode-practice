"""
 * 给你一个长度为 n 下标从 0 开始的数组 nums ，数组中的元素为 互不相同 的正整数。
 * 请你返回让 nums 成为递增数组的 最少右移 次数，如果无法得到递增数组，返回 -1 。
 * 一次 右移 指的是同时对所有下标进行操作，将下标为 i 的元素移动到下标 (i + 1) % n 处。
 * 提示：
 * 1、1 <= nums.length <= 100
 * 2、1 <= nums[i] <= 100
 * 3、nums 中的整数互不相同。
 * 链接：https://leetcode.cn/problems/minimum-right-shifts-to-sort-the-array/
"""
from typing import List


class Solution:

    def minimumRightShifts(self, nums: List[int]) -> int:
        ans = -1
        n = len(nums)
        for i in range(n):
            for j in range(n - 1):
                if nums[(j - i + 1) % n] < nums[(j - i) % n]:
                    break
            else:
                ans = i
                break
        return ans


if __name__ == '__main__':
    # 2
    print(Solution().minimumRightShifts([3, 4, 5, 1, 2]))
    # 0
    print(Solution().minimumRightShifts([1, 3, 5]))
    # -1
    print(Solution().minimumRightShifts([2, 1, 4]))
