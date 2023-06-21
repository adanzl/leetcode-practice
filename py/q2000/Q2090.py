"""
 * 给你一个下标从 0 开始的数组 nums ，数组中有 n 个整数，另给你一个整数 k 。
 * 半径为 k 的子数组平均值 是指：nums 中一个以下标 i 为 中心 且 半径 为 k 的子数组中所有元素的平均值，
 * 即下标在 i - k 和 i + k 范围（含 i - k 和 i + k）内所有元素的平均值。
 * 如果在下标 i 前或后不足 k 个元素，那么 半径为 k 的子数组平均值 是 -1 。
 * 构建并返回一个长度为 n 的数组 avgs ，其中 avgs[i] 是以下标 i 为中心的子数组的 半径为 k 的子数组平均值 。
 * x 个元素的 平均值 是 x 个元素相加之和除以 x ，此时使用截断式 整数除法 ，即需要去掉结果的小数部分。
 * 例如，四个元素 2、3、1 和 5 的平均值是 (2 + 3 + 1 + 5) / 4 = 11 / 4 = 2.75，截断后得到 2 。
 * 提示：
 * 1、n == nums.length
 * 2、1 <= n <= 10^5
 * 3、0 <= nums[i], k <= 10^5
 * 链接：https://leetcode.cn/problems/k-radius-subarray-averages/
"""
from itertools import accumulate
from typing import List


class Solution:

    def getAverages(self, nums: List[int], k: int) -> List[int]:
        pre_sum = [0] + list(accumulate(nums))
        n = len(nums)
        ans = []
        for i in range(n):
            if i < k or i >= n - k:
                ans.append(-1)
            else:
                ans.append((pre_sum[i + k + 1] - pre_sum[i - k]) // (k * 2 + 1))
        return ans


if __name__ == '__main__':
    # [-1,-1,-1,5,4,4,-1,-1,-1]
    print(Solution().getAverages([7, 4, 3, 9, 1, 8, 5, 2, 6], k=3))
    # [100000]
    print(Solution().getAverages([100000], k=0))
    # [-1]
    print(Solution().getAverages([8], k=100000))
