"""
 * 给你两个数组 nums 和 andValues，长度分别为 n 和 m。
 * 数组的 值 等于该数组的 最后一个 元素。
 * 你需要将 nums 划分为 m 个 不相交的连续 子数组，对于第 ith 个子数组 [li, ri]，子数组元素的按位AND运算结果等于 andValues[i]，
 * 换句话说，对所有的 1 <= i <= m，nums[li] & nums[li + 1] & ... & nums[ri] == andValues[i] ，其中 & 表示按位AND运算符。
 * 返回将 nums 划分为 m 个子数组所能得到的可能的 最小 子数组 值 之和。如果无法完成这样的划分，则返回 -1 。
 * 提示：
 * 1、1 <= n == nums.length <= 10^4
 * 2、1 <= m == andValues.length <= min(n, 10)
 * 3、1 <= nums[i] < 10^5
 * 4、0 <= andValues[j] < 10^5
 * 链接：https://leetcode.cn/problems/minimum-sum-of-values-by-dividing-array/description/
"""
from functools import cache
from typing import List

INF = (1 << 64) - 1


class Solution:

    def minimumValueSum(self, nums: List[int], andValues: List[int]) -> int:

        n, m = len(nums), len(andValues)

        @cache
        def dfs(i, j, _and):
            # 处理到第i个元素，第j组，当前组的and和为_and
            if j == m: return INF
            val = _and & nums[i]
            if val < andValues[j]:
                return INF
            if i == n - 1:
                return nums[-1] if j == m - 1 and val == andValues[-1] else INF
            # 剩下的不够了
            if n - i < m - j - 1:
                return INF
            # 不换组
            ret = dfs(i + 1, j, val)
            # 换组
            if val == andValues[j]:
                ret = min(ret, dfs(i + 1, j + 1, INF) + nums[i])
            return ret

        ans = dfs(0, 0, INF)
        return ans if ans != INF else -1


if __name__ == '__main__':
    # 4
    print(Solution().minimumValueSum([4, 4], [4]))
    # -1
    print(Solution().minimumValueSum([1, 2, 3, 4], andValues=[2]))
    # 12
    print(Solution().minimumValueSum([1, 4, 3, 3, 2], andValues=[0, 3, 3, 2]))
    # 17
    print(Solution().minimumValueSum([2, 3, 5, 7, 7, 7, 5], andValues=[0, 7, 5]))
