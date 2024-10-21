"""
 * 给你一个长度为 n 的整数数组 nums 和一个整数数组 queries 。
 * gcdPairs 表示数组 nums 中所有满足 0 <= i < j < n 的数对 (nums[i], nums[j]) 的 最大公约数 升序 排列构成的数组。
 * 对于每个查询 queries[i] ，你需要找到 gcdPairs 中下标为 queries[i] 的元素。
 * 请你返回一个整数数组 answer ，其中 answer[i] 是 gcdPairs[queries[i]] 的值。
 * gcd(a, b) 表示 a 和 b 的 最大公约数 。
 * 提示：
 * 1、2 <= n == nums.length <= 10^5
 * 2、1 <= nums[i] <= 5 * 10^4
 * 3、1 <= queries.length <= 10^5
 * 4、0 <= queries[i] < n * (n - 1) / 2
 * 链接：https://leetcode.cn/problems/sorted-gcd-pair-queries
"""

import bisect
from itertools import accumulate
from typing import Counter, List

INF = 0x3c3c3c3c3c3c3c3c3c

#
# @lc app=leetcode.cn id=3312 lang=python3
# @lcpr version=20001
#
# [3312] 查询排序后的最大公约数
#


# @lc code=start
class Solution:

    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        mx = max(nums)
        cnt = [0] * (mx + 1)
        cnt_x = Counter(nums)
        
        for vv in range(mx, 0, -1):
            c = 0
            for n_vv in range(vv, mx + 1, vv):
                c += cnt_x[n_vv]
                cnt[vv] -= cnt[n_vv]  # gcd 是 2i,3i,4i,... 的数对不能统计进来
            cnt[vv] += c * (c - 1) // 2  # c 个数选 2 个，组成 c*(c-1)/2 个数对

        pre_sm = list(accumulate(cnt))
        return [bisect.bisect_right(pre_sm, q) for q in queries]


# @lc code=end

if __name__ == '__main__':
    # [1,2,2]
    print(Solution().gcdValues([2, 3, 4], queries=[0, 2, 2]))
    # [4,2,1,1]
    print(Solution().gcdValues([4, 4, 2, 1], queries=[5, 3, 1, 0]))
    # [2,2]
    print(Solution().gcdValues([2, 2], queries=[0, 0]))
