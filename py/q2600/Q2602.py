"""
 * 给你一个正整数数组 nums 。
 * 同时给你一个长度为 m 的整数数组 queries 。第 i 个查询中，你需要将 nums 中所有元素变成 queries[i] 。你可以执行以下操作 任意 次：
 * * 将数组里一个元素 增大 或者 减小 1 。
 * 请你返回一个长度为 m 的数组 answer ，其中 answer[i]是将 nums 中所有元素变成 queries[i] 的 最少 操作次数。
 * 注意，每次查询后，数组变回最开始的值。
 * 提示：
 * 1、n == nums.length
 * 2、m == queries.length
 * 3、1 <= n, m <= 10^5
 * 4、1 <= nums[i], queries[i] <= 10^9
 * 链接：https://leetcode.cn/problems/minimum-operations-to-make-all-array-elements-equal/
"""
import bisect
from itertools import accumulate
from typing import List


class Solution:

    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(queries)
        ans = [0] * n
        nums.sort()
        pre_sum = [0] + list(accumulate(nums)) # type: ignore
        for i in range(n):
            q = queries[i]
            idx = bisect.bisect_left(nums, q)
            ans[i] = idx * q - pre_sum[idx] + pre_sum[-1] - pre_sum[idx] - (len(nums) - idx) * q
        return ans


if __name__ == '__main__':
    # [14,10]
    print(Solution().minOperations([3, 1, 6, 8], queries=[1, 5]))
    # [20]
    print(Solution().minOperations([2, 9, 6, 3], queries=[10]))