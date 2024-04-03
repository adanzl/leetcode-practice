"""
 * 给你一个 二进制数组 nums 。
 * 如果一个 子数组 中 不存在 两个 相邻 元素的值 相同 的情况，我们称这样的子数组为 交替子数组 。
 * 返回数组 nums 中交替子数组的数量。
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、nums[i] 不是 0 就是 1 。
 * 链接：https://leetcode.cn/problems/count-alternating-subarrays/
"""
from typing import List


class Solution:

    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        ans = 0
        pre = -1
        ln = 0
        for num in nums:
            if num != pre:
                ln += 1
            else:
                ans += (ln + 1) * ln // 2
                ln = 1
            pre = num
        return ans + (ln + 1) * ln // 2


if __name__ == '__main__':
    # 5
    print(Solution().countAlternatingSubarrays([0, 1, 1, 1]))
    # 10
    print(Solution().countAlternatingSubarrays([1, 0, 1, 0]))
