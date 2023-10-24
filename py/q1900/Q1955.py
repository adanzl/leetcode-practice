"""
 * 特殊序列 是由 正整数 个 0 ，紧接着 正整数 个 1 ，最后 正整数 个 2 组成的序列。
 * 1、比方说，[0,1,2] 和 [0,0,1,1,1,2] 是特殊序列。
 * 2、相反，[2,1,0] ，[1] 和 [0,1,2,0] 就不是特殊序列。
 * 给你一个数组 nums （仅 包含整数 0，1 和 2），请你返回 不同特殊子序列的数目 。由于答案可能很大，请你将它对 10^9 + 7 取余 后返回。
 * 一个数组的 子序列 是从原数组中删除零个或者若干个元素后，剩下元素不改变顺序得到的序列。
 * 如果两个子序列的 下标集合 不同，那么这两个子序列是 不同的 。
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、0 <= nums[i] <= 2
 * 链接：https://leetcode.cn/problems/count-number-of-special-subsequences/
"""
from typing import List


#
# @lc app=leetcode.cn id=2603 lang=python3
# @lc code=start
class Solution:

    def countSpecialSubsequences(self, nums: List[int]) -> int:
        cnt = [0, 0, 0]
        MOD = 10**9 + 7
        for num in nums:
            if num == 0:
                cnt[0] = (cnt[0] + cnt[0] + 1) % MOD
            elif num == 1:
                cnt[1] = (cnt[0] + cnt[1] + cnt[1]) % MOD
            elif num == 2:
                cnt[2] = (cnt[1] + cnt[2] + cnt[2]) % MOD
        return cnt[2]


# @lc code=end

if __name__ == '__main__':
    # 7
    print(Solution().countSpecialSubsequences([0, 1, 2, 0, 1, 2]))
    # 3
    print(Solution().countSpecialSubsequences([0, 1, 2, 2]))
    # 0
    print(Solution().countSpecialSubsequences([2, 2, 0, 0]))
