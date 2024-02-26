"""
 * 给你一个下标从 0 开始只包含 正 整数的数组 nums 。
 * 一开始，你可以将数组中 任意数量 元素增加 至多 1 。
 * 修改后，你可以从最终数组中选择 一个或者更多 元素，并确保这些元素升序排序后是 连续 的。
 * 比方说，[3, 4, 5] 是连续的，但是 [3, 4, 6] 和 [1, 1, 2, 3] 不是连续的。
 * 请你返回 最多 可以选出的元素数目。
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、1 <= nums[i] <= 10^6
 * 链接：https://leetcode.cn/problems/maximize-consecutive-elements-in-an-array-after-modification/
"""

from collections import defaultdict
from typing import List


class Solution:

    def maxSelectedElements(self, nums: List[int]) -> int:
        # f[x] 表示子序列的最后一个数是 x 时，子序列的最大长度
        f = defaultdict(int)
        for x in sorted(nums):
            f[x + 1] = f[x] + 1  # 当前 x 若 +1 时，f[x+1] 为 f[x]+1
            f[x] = f[x - 1] + 1  # 当前 x 不 +1 时，f[x] 为 f[x-1]+1
        return max(f.values())


if __name__ == '__main__':
    # 14
    print(Solution().maxSelectedElements([8, 13, 18, 10, 16, 19, 11, 17, 15, 18, 9, 12, 15, 8, 9, 14, 7]))
    # 8
    print(Solution().maxSelectedElements([8, 10, 6, 12, 9, 12, 2, 3, 13, 19, 11, 18, 10, 16]))
    # 1
    print(Solution().maxSelectedElements([1, 4, 7, 10]))
    # 3
    print(Solution().maxSelectedElements([2, 1, 5, 1, 1]))
