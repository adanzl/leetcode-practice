"""
 * 给你一个下标从 0 开始长度为 偶数 的整数数组 nums 。
 * 只要 nums 不是 空数组，你就重复执行以下步骤：
 * 1、找到 nums 中的最小值，并删除它。
 * 2、找到 nums 中的最大值，并删除它。
 * 3、计算删除两数的平均值。
 * 两数 a 和 b 的 平均值 为 (a + b) / 2 。
 * 比方说，2 和 3 的平均值是 (2 + 3) / 2 = 2.5 。
 * 返回上述过程能得到的 不同 平均值的数目。
 * 注意 ，如果最小值或者最大值有重复元素，可以删除任意一个。
 * 提示：
 * 1、2 <= nums.length <= 100
 * 2、nums.length 是偶数。
 * 3、0 <= nums[i] <= 100
 * 链接：https://leetcode.cn/problems/number-of-distinct-averages/
"""
from typing import List


class Solution:

    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        ans = set()
        for i in range(n // 2):
            ans.add((nums[i] + nums[n - i - 1]) / 2)
        return len(ans)


if __name__ == '__main__':
    # 2
    print(Solution().distinctAverages([4, 1, 4, 0, 3, 5]))
    # 1
    print(Solution().distinctAverages([1, 100]))
