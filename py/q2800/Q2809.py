"""
 * 给你两个长度相等下标从 0 开始的整数数组 nums1 和 nums2 。
 * 每一秒，对于所有下标 0 <= i < nums1.length ，nums1[i] 的值都增加 nums2[i] 。操作 完成后 ，你可以进行如下操作：
 * 选择任一满足 0 <= i < nums1.length 的下标 i ，并使 nums1[i] = 0 。
 * 同时给你一个整数 x 。
 * 请你返回使 nums1 中所有元素之和 小于等于 x 所需要的 最少 时间，如果无法实现，那么返回 -1 。
 * 提示：
 * 1、1 <= nums1.length <= 10^3
 * 2、1 <= nums1[i] <= 10^3
 * 3、0 <= nums2[i] <= 10^3
 * 4、nums1.length == nums2.length
 * 5、0 <= x <= 10^6
 * 链接：https://leetcode.cn/problems/minimum-time-to-make-array-sum-at-most-x/
"""
from typing import List


class Solution:

    def minimumTime(self, nums1: List[int], nums2: List[int], x: int) -> int:
        n = len(nums1)
        sm1, sm2 = sum(nums1), sum(nums2)
        # 排序不等式 https://baike.baidu.com/item/%E6%8E%92%E5%BA%8F%E4%B8%8D%E7%AD%89%E5%BC%8F/7775728?fr=ge_ala
        # dp[i][j]: nums2 前i个数，执行j次的最大和, j <= i，对于dp[i][j]，
        #   有两种选择：
        #       1、j次操作选择第i个数   dp[i][j] = dp[i-1][j-1] + (j+1)*nums2[i] + nums1[i]
        #       2、j次操作不选第i个数   dp[i][j] = dp[i-1][j]
        # dp[i][j] = max(dp[i-1][j-1] + nums2[i], dp[i-1][j])
        sorted_range = sorted(range(n), key=lambda x: nums2[x])
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for i, idx in enumerate(sorted_range):
            for j in range(1, n + 1):
                dp[i + 1][j] = max(dp[i][j - 1] + (j) * nums2[idx] + nums1[idx], dp[i][j])
        for i in range(n + 1):  # 次数
            if sm1 + sm2 * (i) - dp[-1][i] <= x:
                return i
        return -1


if __name__ == '__main__':
    # 3
    print(Solution().minimumTime([3, 2, 5, 8, 8], [1, 3, 2, 1, 0], 20))
    # 3
    print(Solution().minimumTime([1, 2, 3], [1, 2, 3], 4))
    # 6
    print(Solution().minimumTime([6, 5, 2, 8, 8, 1, 6, 4], [1, 2, 1, 0, 1, 0, 3, 1], 23))
    # -1
    print(Solution().minimumTime([4, 5, 3, 2, 3, 9, 5, 7, 10, 4], [4, 4, 0, 4, 1, 2, 4, 0, 4, 0], 47))
    # -1
    print(Solution().minimumTime([1, 2, 3], [3, 3, 3], 4))